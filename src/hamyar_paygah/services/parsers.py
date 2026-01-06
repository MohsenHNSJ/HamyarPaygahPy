"""XML parsers module.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

# pylint: disable=I1101
from typing import cast

from lxml import etree

from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.utils.text_utils import convert_to_integer
from hamyar_paygah.utils.xml_utils import get_text


def parse_to_missions_list(xml_text: str) -> list[Mission]:
    """Parse EMS mission data from a SOAP XML response.

    This function reads a raw SOAP XML string returned from the EMS server,
    extracts each `<DocumentReport>` element, and converts it into a
    `Mission` dataclass instance. Fields that may be missing or nil are
    safely handled. Numeric fields are converted using `convert_to_integer`, and
    missing string fields are defaulted to an empty string.

    Args:
        xml_text (str): Raw XML string returned from the EMS SOAP server.

    Returns:
        list[Mission]: A list of `Mission` dataclass instances representing
        each mission in the XML response.
    """
    # Configure root element and namespaces
    root_element: etree._Element = etree.fromstring(xml_text.encode())
    namespaces: dict[str, str] = {
        "a": "http://schemas.datacontract.org/2004/07/ClientModel",
    }
    # Create an empty missions list
    missions_list: list[Mission] = []
    # Convert the input data to a list of xml elements
    document_list: list[etree._Element] = cast(
        "list[etree._Element]",  # noqa: SLF001
        root_element.xpath(
            ".//a:DocumentReport",
            namespaces=namespaces,
        ),
    )
    # Iterate documents list and convert each to a mission and add it to the list of missions.
    for document in document_list:
        missions_list.append(  # noqa: PERF401
            Mission(
                address=get_text(document, "Address", namespaces) or "",
                ambulance_code=convert_to_integer(
                    get_text(document, "AmbulanceCode", namespaces),
                )
                or 0,
                code=convert_to_integer(
                    get_text(document, "MissionCode", namespaces),
                )
                or 0,
                date=get_text(document, "Date", namespaces) or "",
                hospital_id=convert_to_integer(
                    get_text(document, "HospitalId", namespaces),
                )
                or 0,
                hospital_name=get_text(document, "Hospital", namespaces),
                id=convert_to_integer(
                    get_text(document, "MissionId", namespaces),
                )
                or 0,
                patient_id=convert_to_integer(
                    get_text(document, "PatientId", namespaces),
                )
                or 0,
                patient_name=get_text(document, "Name", namespaces) or "",
                persian_date=get_text(
                    document,
                    "PersianDate",
                    namespaces,
                )
                or "",
                result=get_text(document, "Result", namespaces) or "",
            ),
        )

    return missions_list
