"""XML parsers module.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

# pylint: disable=I1101
import datetime
from typing import cast

import jdatetime  # type: ignore[import-untyped]
from lxml import etree

from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.utils.text_utils import convert_to_bool, convert_to_integer
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


def parse_to_mission_details(xml_text: str) -> MissionDetails:
    """Parse EMS mission details from a SOAP XML response.

    Args:
        xml_text (str): Raw XML string returned from the EMS SOAP server.

    Returns:
        MissionDetails: Details of a mission in an object.
    """
    # Configure root element and namespaces
    root_element: etree._Element = etree.fromstring(xml_text.encode())
    namespaces: dict[str, str] = {
        "a": "http://schemas.datacontract.org/2004/07/ClientModel",
        "t": "http://tempuri.org/",
    }

    # Convert the input date to a xml element
    document: etree._Element = cast(
        "etree._Element",  # noqa: SLF001
        root_element.find(
            ".//t:GetMissionReportFormDataResult",
            namespaces=namespaces,
        ),
    )

    # NOTICE! in the upcoming lines, you will see some funny field names or
    # some actual crimes in the world of programming, These are server side
    # responses and not controlled by me, i tried my best to store them
    # in a better and more meaningful way. x-x

    # Create sub-models
    # Create information sub-model
    information: Information = Information(
        patient_name=get_text(document, "BimarName", namespaces) or "",
        years_of_age=convert_to_integer(
            get_text(document, "Age", namespaces),
        )
        or 0,
        months_of_age=convert_to_integer(
            get_text(document, "AgeMonth", namespaces),
        )
        or 0,
        iranian_nationality=convert_to_bool(
            get_text(document, "IsIrani", namespaces),
        )
        or False,
        foreign_nationality=convert_to_bool(
            get_text(document, "IsGheirIrani", namespaces),
        )
        or False,
        is_male_gender=convert_to_bool(
            get_text(document, "IsMozakar", namespaces),
        )
        or False,
        is_female_gender=convert_to_bool(
            get_text(document, "IsMoanas", namespaces),
        )
        or False,
        is_unknown_gender=convert_to_bool(
            get_text(document, "IsNamoshakhas", namespaces),
        )
        or False,
        national_code=convert_to_integer(
            get_text(document, "CodeMelli", namespaces),
        )
        or 0,
        document_serial_number=get_text(
            document,
            "ShomareSerialParvade",
            namespaces,
        )
        or "",  # Parvade?? :/
        caller_number=get_text(
            document,
            "TelAsli",
            namespaces,
        )
        or "",
        backup_number=get_text(
            document,
            "TelPoshtibani",
            namespaces,
        )
        or "",
        ambulance_code=convert_to_integer(
            get_text(document, "AmbulanceCode", namespaces),
        )
        or 0,
        document_request_time=_parse_print_date_clock_to_datetime(
            str(
                get_text(
                    document,
                    "PrintDate",
                    namespaces,
                ),
            ),
            str(get_text(document, "PrintClock", namespaces)),
        ),
        province=get_text(
            document,
            "Province",
            namespaces,
        )
        or "",
        summary=get_text(
            document,
            "Tozihat",
            namespaces,
        )
        or "",
    )

    # Create final model
    mission_details: MissionDetails = MissionDetails(information=information)

    return mission_details


def _parse_print_date_clock_to_datetime(print_date: str, print_clock: str) -> datetime.datetime:
    """Converts jalali date and clock strings into a gregorian datetime.

    Args:
        print_date (str): Jalali date
        print_clock (str): Jalali time

    Returns:
        datetime: gregorian datetime object.
    """
    # Split the input values
    year, month, day = map(int, print_date.split("/"))
    hour, minute = map(int, print_clock.split(":"))

    # Create a jalali date time using split values
    jalali_datetime: jdatetime.datetime = jdatetime.datetime(
        year,
        month,
        day,
        hour,
        minute,
    )

    # Return the gregorian date
    return jalali_datetime.togregorian()  # type: ignore[no-any-return]
