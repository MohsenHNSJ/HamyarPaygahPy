"""Services to get missions list from server."""

import lzma
from datetime import datetime, timedelta

import aiohttp
from anyio import Path, open_file

from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.services.parsers import parse_to_missions_list

CACHE_DIR = Path("cache/missions_list")


async def _fetch_missions_list(
    server_address: str,
    from_date: datetime,
    to_date: datetime,
    region_id: int,
) -> str:
    """Fetch a list of missions for a specific region from the EMS SOAP service.

    This function sends an asynchronous SOAP request to the EMS reporting
    service and retrieves the raw XML response containing mission data for
    the given date range and region.

    The request uses a legacy SOAP endpoint with strict field names.
    In particular, the XML field named ``passsword`` is intentionally
    misspelled and must not be corrected, as changing it results in a
    ``BAD REQUEST`` response from the server.

    Args:
        server_address: Base address of the EMS server (without trailing slash).
        from_date: Start date of the report range. The time component is
            automatically set to ``00:00:00``.
        to_date: End date of the report range. The time component is
            automatically set to ``23:59:59``.
        region_id: Numeric identifier of the region for which the report
            is requested.

    Returns:
        The raw SOAP response body as a string. The returned value is
        unparsed XML and must be processed by the caller if structured
        data is required.

    Raises:
        aiohttp.ClientError: If the HTTP request fails due to a network
            or connection error.
    """
    url: str = f"{server_address}/Report.svc"
    soap_action: str = "http://tempuri.org/IReport/GetDocumentReportRegion"

    # Convert dates to strings in yyyy-MM-dd format
    from_date_str: str = from_date.strftime(format="%Y-%m-%d")
    to_date_str: str = to_date.strftime(format="%Y-%m-%d")

    # Build SOAP XML body
    # DO NOT TOUCH "passsword"
    # Do not try to correct it, they have misspelled :/
    # Correction results in "BAD REQUEST"
    xml_body: str = f"""
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Body>
            <GetDocumentReportRegion xmlns="http://tempuri.org/">
                <passsword/>
                <fromDate>{from_date_str}T00:00:00</fromDate>
                <toDate>{to_date_str}T23:59:59</toDate>
                <name></name>
                <address></address>
                <ambulanceCode></ambulanceCode>
                <regionId>{region_id}</regionId>
            </GetDocumentReportRegion>
        </s:Body>
    </s:Envelope>
    """
    # Create HTTP headers
    headers: dict[str, str] = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": f'"{soap_action}"',
    }

    # Send async POST request
    async with (
        aiohttp.ClientSession() as session,
        session.post(
            url=url,
            data=xml_body,
            headers=headers,
        ) as response,
    ):
        response_text: str = await response.text()
        return response_text


def _get_cache_file_path(region_id: int, date: datetime) -> Path:
    """Generate a cache file path for a given region and date.

    Args:
        region_id (int): The ID of the region.
        date (datetime.datetime): The date for which to generate the cache path.

    Returns:
        anyio.Path: The path to the cache file.
    """
    date_str = date.strftime(format="%Y-%m-%d")
    return CACHE_DIR / f"region_{region_id}" / f"{date_str}.xml.xz"


async def _save_xml_cache(path: Path, xml_text: str) -> None:
    """Save XML response as compressed LZMA file."""
    await path.parent.mkdir(parents=True, exist_ok=True)

    compressed_data = lzma.compress(xml_text.encode("utf-8"), preset=9)

    async with await open_file(path, "wb") as f:
        await f.write(compressed_data)


async def _load_xml_cache(path: Path) -> str:
    """Load XML response from compressed LZMA cache file."""
    async with await open_file(path, "rb") as f:
        compressed_data = await f.read()

    return lzma.decompress(compressed_data).decode("utf-8")


async def get_missions_list(
    server_address: str,
    from_date: datetime,
    to_date: datetime,
    region_id: int,
) -> list[Mission]:
    """Fetch missions list with caching mechanism.

    This function first checks if a cached response exists for the given
    region and date range. If a valid cache is found, it loads the XML
    data from the cache and parses it into a list of `Mission` objects.
    If no cache is available, it fetches the data from the server, saves
    it to the cache, and then parses it.

    Args:
        server_address (str): The base address of the EMS server.
        from_date (datetime.datetime): The start date of the missions query.
        to_date (datetime.datetime): The end date of the missions query.
        region_id (int): The region ID to filter missions by.

    Returns:
        list[Mission]: A list of `Mission` objects parsed from the server response
            or cache.
    """
    # Get the date of today
    today = datetime.now().date()  # noqa: DTZ005
    # Create an empty list to hold the missions
    missions_list: list[Mission] = []

    # Set the dates for looping
    current_request_date = from_date.date()
    final_request_date = to_date.date()

    while current_request_date <= final_request_date:
        # Create a minimal datetime object for the current date
        request_date_time = datetime.combine(
            current_request_date,
            datetime.min.time(),
        )
        # Generate the cache file path for the current date and region
        cache_file_path = _get_cache_file_path(region_id, request_date_time)

        # Check if the requesting date is older than 2 days and permanent cache can be used
        is_permanent_data = current_request_date <= (today - timedelta(days=2))

        # If it's old, try to load from cache first
        if is_permanent_data:
            # Check if cache exists and load it
            if await cache_file_path.exists():
                raw_data = await _load_xml_cache(cache_file_path)

            # Else, fetch from server and save to cache
            else:
                raw_data = await _fetch_missions_list(
                    server_address,
                    request_date_time,
                    request_date_time,
                    region_id,
                )

                await _save_xml_cache(cache_file_path, raw_data)

        # If it's not old, fetch directly from server without caching
        else:
            raw_data = await _fetch_missions_list(
                server_address,
                request_date_time,
                request_date_time,
                region_id,
            )

        # Parse the raw data into Mission objects and add to the list
        missions = parse_to_missions_list(raw_data)
        missions_list.extend(missions)

        # Move to the next date
        current_request_date += timedelta(days=1)

    return missions_list
