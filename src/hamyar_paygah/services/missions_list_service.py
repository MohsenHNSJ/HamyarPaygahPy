"""Services to get missions list from server."""

from datetime import datetime

import aiohttp

from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.services.parsers import parse_to_missions_list


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


async def get_missions_list(
    server_address: str,
    from_date: datetime,
    to_date: datetime,
    region_id: int,
) -> list[Mission]:
    """Fetch and parse a list of missions from the server.

    This function handles the complete flow of retrieving missions data
    from the server for a given date range and region, and converting
    it into `Mission` objects suitable for use in the UI or business logic.

    Args:
        server_address (str): The base address of the missions server.
        from_date (datetime): The start date of the missions query.
        to_date (datetime): The end date of the missions query.
        region_id (int): The region ID to filter missions by.

    Returns:
        list[Mission]: A list of `Mission` objects parsed from the server response.

    Raises:
        Any exceptions raised by the underlying `_fetch_missions_list` function
        (e.g., network errors, timeout errors) are propagated to the caller.
    """
    # Fetch raw mission data asynchronously from the server
    raw_data: str = await _fetch_missions_list(server_address, from_date, to_date, region_id)

    # Parse the raw XML/JSON response into a list of Mission objects
    missions_list: list[Mission] = parse_to_missions_list(raw_data)

    return missions_list
