# pylint: disable=I1101
"""XML parsers module for Hamyar Paygah.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

from lxml import etree

from .models import Mission
from .utils import get_int


def get_text(document: etree._Element, tag: str, namespaces: dict[str, str]) -> str | None:
    """Retrieve the text content of a child element by tag.

    Args:
        document (_Element): The parent XML element containing the tag.
        tag (str): The tag name of the child element (without namespace prefix).
        namespaces (dict[str, str]): Namespace mapping for XPath.

    Returns:
        str | None: The text content of the element, or None if not present.
    """
    el: etree._Element | None = document.find(
        path=f"a:{tag}",
        namespaces=namespaces,
    )
    return el.text if el is not None else None


def parse_missions(xml_text: str) -> list[Mission]:
    """Parse EMS mission data from a SOAP XML response.

    This function reads a raw SOAP XML string returned from the EMS server,
    extracts each `<DocumentReport>` element, and converts it into a
    `Mission` dataclass instance. Fields that may be missing or nil are
    safely handled. Numeric fields are converted using `get_int`, and
    missing string fields are defaulted to an empty string.

    Args:
        xml_text (str): Raw XML string returned from the EMS SOAP server.

    Returns:
        list[Mission]: A list of `Mission` dataclass instances representing
        each mission in the XML response.
    """
    root: etree._Element = etree.fromstring(xml_text.encode())

    ns: dict[str, str] = {
        "a": "http://schemas.datacontract.org/2004/07/ClientModel",
    }

    missions: list[Mission] = []

    document_list: list[etree._Element] = root.xpath(
        ".//a:DocumentReport",
        namespaces=ns,
    )

    for document in document_list:
        missions.append(  # noqa: PERF401
            Mission(
                address=get_text(document, "Address", ns) or "",
                ambulance_code=get_int(
                    get_text(document, "AmbulanceCode", ns),
                )
                or 0,
                code=get_int(get_text(document, "MissionCode", ns)) or 0,
                date=get_text(document, "Date", ns) or "",
                hospital_id=get_int(
                    get_text(document, "HospitalId", ns),
                )
                or 0,
                hospital_name=get_text(document, "Hospital", ns),
                id=get_int(get_text(document, "MissionId", ns)) or 0,
                patient_id=get_int(
                    get_text(document, "PatientId", ns),
                )
                or 0,
                patient_name=get_text(document, "Name", ns) or "",
                persian_date=get_text(document, "PersianDate", ns) or "",
                result=get_text(document, "Result", ns) or "",
            ),
        )

    return missions
