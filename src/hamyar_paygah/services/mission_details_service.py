"""Services to get mission details from server."""

# pylint: disable=R0912
import datetime
import lzma

import aiohttp
from anyio import Path

from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.services.parsers import parse_to_mission_details

CACHE_DIR = Path("cache/mission_details")


async def _fetch_mission_details(
    server_address: str,
    mission_id: int,
    patient_id: int,
) -> str:
    """Fetch details of a mission from the EMS SOAP service.

    This function send an asynchronous SOAP request to the EMS reporting
    service and retrieves the raw XML response containing mission details for
    the given mission ID and patient ID.

    The request uses a legacy SOAP endpoint with strict field names.

    Args:
        server_address (str): Base address of the EMS server (without trailing slash).
        mission_id (int): ID of the mission.
        patient_id (int): ID of the patient.

    Returns:
        The raw SOAP response body as a string. The returned value is
        unparsed XML and must be processed by the caller if structured
        data is required.
    """
    url: str = f"{server_address}/Report.svc"
    soap_action: str = "http://tempuri.org/IReport/GetMissionReportFormData"

    # Build SOAP XML body
    # DO NOT TOUCH "passsword"
    # Do not try to correct it, they have misspelled :/
    # Correction results in "BAD REQUEST"
    xml_body: str = f"""
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Body>
            <GetMissionReportFormData xmlns="http://tempuri.org/">
                <password/>
                <missionId>{mission_id}</missionId>
                <patientId>{patient_id}</patientId>
            </GetMissionReportFormData>
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

        # if server response is empty, raise an error
        if response_text == "":
            raise aiohttp.ServerConnectionError
        return response_text


def _get_cache_file_path(mission_id: int, patient_id: int) -> Path:
    """Generate a cache file path for a given mission and patient ID.

    This function constructs a unique file path within the `CACHE_DIR`
    directory based on the provided mission ID and patient ID. The resulting
    file name follows the format `mission_{mission_id}_patient_{patient_id}.xml.xz`,
    ensuring that cached data for different missions and patients are stored
    separately.

    Args:
        mission_id (int): The ID of the mission.
        patient_id (int): The ID of the patient.

    Returns:
        anyio.Path: The path to the cache file.
    """
    return CACHE_DIR / f"mission_{mission_id}_patient_{patient_id}.xml.xz"


def _save_xml_cache(mission_id: int, patient_id: int, xml_text: str) -> None:
    """Save XML response as compressed LZMA file."""
    path = CACHE_DIR / f"mission_{mission_id}_patient_{patient_id}.xml.xz"
    with lzma.open(path, "wb", preset=9) as f:
        f.write(xml_text.encode("utf-8"))


def _load_xml_cache(mission_id: int, patient_id: int) -> str:
    """Load compressed XML response from cache."""
    path = CACHE_DIR / f"mission_{mission_id}_patient_{patient_id}.xml.xz"
    with lzma.open(path, "rb") as f:
        return f.read().decode("utf-8")


async def get_mission_details(
    server_address: str,
    mission_id: int,
    patient_id: int,
) -> MissionDetails:
    """Get mission details with caching mechanism.

    This function first checks if the mission details for the given mission ID
    and patient ID are available in the cache. If a cached file exists, it
    reads the data from the cache and parses it into a `MissionDetails`
    object. If no cache is found, it fetches the details from the server,
    parses it, and saves the raw response to the cache for future use
    if mission is older than 2 days.

    Args:
        server_address (str): The base address of the EMS server.
        mission_id (int): The ID of the mission.
        patient_id (int): The ID of the patient.

    Returns:
        MissionDetails: An object containing the details of the mission.
    """
    # Check if cache directory exists, if not create it.
    # This is a safety check in case the directory was deleted after the initial creation.
    if not await CACHE_DIR.exists():
        await CACHE_DIR.mkdir(parents=True)

    # Generate the cache file path for the given mission and patient IDs
    cached_mission_details: Path = _get_cache_file_path(mission_id, patient_id)

    raw_data: str = ""

    if await cached_mission_details.exists():
        # If cache exists, read from it
        raw_data = _load_xml_cache(mission_id, patient_id)
    else:
        # If no cache, fetch from server
        raw_data = await _fetch_mission_details(server_address, mission_id, patient_id)

    # Parse the raw data into MissionDetails object
    mission_details: MissionDetails = parse_to_mission_details(raw_data)

    # If the date of the mission is older than 2 day,
    # we can consider it as a mission that will not change anymore, so we can cache it safely.
    if (
        mission_details.times_and_distances.mission_date is not None
        and mission_details.times_and_distances.mission_date
        < (datetime.datetime.now() - datetime.timedelta(days=2))  # noqa: DTZ005
    ):
        _save_xml_cache(mission_id, patient_id, raw_data)

    return mission_details
