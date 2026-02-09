"""Services to get mission details from server."""

# pylint: disable=R0912
from dataclasses import fields

import aiohttp

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.services.parsers import parse_to_mission_details


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


async def get_mission_details(
    server_address: str,
    mission_id: int,
    patient_id: int,
) -> MissionDetails:
    """Fetch and parse details of a mission from server.

    This function handles the complete flow of retrieving mission data
    from the server based on mission ID and patient ID, and converting
    it into `MissionDetails` object suitable for use in teh UI or business logic.

    Args:
        server_address (str): The base address of the missions server.
        mission_id (int): ID of the mission.
        patient_id (int): ID of the patient.

    Returns:
        MissionDetails: An object holding the details of a mission.
    """
    # Fetch raw mission data asynchronously from the server
    raw_data: str = await _fetch_mission_details(server_address, mission_id, patient_id)

    # Parse the raw XML/JSON response into a MissionDetails object
    mission_details: MissionDetails = parse_to_mission_details(raw_data)

    return mission_details


async def test() -> None:  # noqa: C901, PLR0912
    """Temporary test function."""
    test_m: MissionDetails = await get_mission_details(
        str(load_server_address()),
        6330344,
        1182628,
    )

    print("---Information---")
    for field in fields(test_m.information):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.information, field.name)}",
        )
    print(f"{'Full Age':<30} {test_m.information.full_age}")

    print("---Times and Distances---")
    for field in fields(test_m.times_and_distances):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.times_and_distances, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )
    print(
        f"{'Overall mission distance':<30} {test_m.times_and_distances.overall_mission_distance}",
    )

    print("---Location and Emergency---")
    for field in fields(test_m.location_and_emergency):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.location_and_emergency, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )

    print("---Symptoms---")
    for field in fields(test_m.symptoms):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.symptoms, field.name)}",
        )

    for vital_sign in test_m.vital_signs:
        print("---Vital Signs---")
        for field in fields(vital_sign):
            print(
                f"{field.name.replace('_', ' ').title():<30} {getattr(vital_sign, field.name)}",
            )

    print("---Medical History---")
    for field in fields(test_m.medical_history):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.medical_history, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )

    print("Pupils Lungs Heart---")
    for field in fields(test_m.pupils_lungs_heart.pupils):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.pupils_lungs_heart.pupils, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )
    for field in fields(test_m.pupils_lungs_heart.lungs):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.pupils_lungs_heart.lungs, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )
    for field in fields(test_m.pupils_lungs_heart.heart):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.pupils_lungs_heart.heart, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )

    print("---Trauma Types---")
    for field in fields(test_m.trauma_types):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.trauma_types, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )

    for drug in test_m.drugs:
        print("---Drugs---")
        for field in fields(drug):
            print(
                f"{field.name.replace('_', ' ').title():<30} {getattr(drug, field.name)}",
            )

    print("---Mission Result---")
    for field in fields(test_m.result):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.result, field.name)}",
        )

    print("---Medical Center---")
    for field in fields(test_m.medical_center):
        print(
            f"{field.name.replace('_', ' ').title():<30} {getattr(test_m.medical_center, field.name)}",  # noqa: E501 # pylint: disable=C0301
        )
    print("---Consumables---")
    print(test_m.consumables.items.items())


if __name__ == "__main__":
    import asyncio

    asyncio.run(test())
