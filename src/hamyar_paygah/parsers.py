# pylint: disable=I1101
"""XML parsers module for Hamyar Paygah.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

from typing import cast

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

    for doc in root.xpath(".//a:DocumentReport", namespaces=ns):
        # Tell MyPy this is an _Element
        doc_element = cast("etree._Element", doc)  # noqa: SLF001, pylint: disable=W0212

        missions.append(
            Mission(
                address=get_text(doc_element, "Address", ns) or "",
                ambulance_code=get_int(
                    get_text(doc_element, "AmbulanceCode", ns),
                )
                or 0,
                code=get_int(get_text(doc_element, "MissionCode", ns)) or 0,
                date=get_text(doc_element, "Date", ns) or "",
                hospital_id=get_int(
                    get_text(doc_element, "HospitalId", ns),
                )
                or 0,
                hospital_name=get_text(doc_element, "Hospital", ns),
                id=get_int(get_text(doc_element, "MissionId", ns)) or 0,
                patient_id=get_int(
                    get_text(doc_element, "PatientId", ns),
                )
                or 0,
                patient_name=get_text(doc_element, "Name", ns) or "",
                persian_date=get_text(doc_element, "PersianDate", ns) or "",
                result=get_text(doc_element, "Result", ns) or "",
            ),
        )

    return missions
