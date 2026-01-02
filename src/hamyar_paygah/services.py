"""Application core to communicate with server."""

from datetime import datetime

import aiohttp


async def get_missions_list(
    server_url: str,
    from_date: datetime,
    to_date: datetime,
    region_id: int,
) -> str:
    """Returns the list of missions in the defined time frame.

    :param server_url: URL of the server to send requests.
    :type server_url: str
    :param from_date: Starting date of the time frame in Gregorian calendar. Don't use persian.
    :type from_date: datetime
    :param to_date: Ending date of the time frame in Gregorian calendar. Don't use persian.
    :type to_date: datetime
    :param region_id: ID of the requested region.
    :type region_id: int
    :return: Raw string response from server.
    :rtype: str
    """
    url: str = f"{server_url}/Report.svc"
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
