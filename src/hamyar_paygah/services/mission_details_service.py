"""Services to get mission details from server."""

import aiohttp


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
        return response_text
