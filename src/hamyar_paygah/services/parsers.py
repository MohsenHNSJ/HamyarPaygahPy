"""XML parsers module.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

# pylint: disable=I1101
import datetime
from typing import cast

from lxml import etree

from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
    TimesAndDistances,
)
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.utils.math_utils import calculate_time_delta
from hamyar_paygah.utils.text_utils import (
    convert_date_and_time_to_datetime,
    convert_date_to_datetime,
    convert_to_bool,
    convert_to_integer,
    convert_to_time,
)
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
    information: Information = _parse_information_sub_model(
        document,
        namespaces,
    )
    # Create times and distances sub-model
    times_and_distances: TimesAndDistances = _parse_times_and_distances_sub_model(
        document,
        namespaces,
    )

    # Create final model
    mission_details: MissionDetails = MissionDetails(
        information=information,
        times_and_distances=times_and_distances,
    )

    return mission_details


def _parse_information_sub_model(
    document: etree._Element,
    namespaces: dict[str, str],
) -> Information:
    """Parses the information sub model and returns it.

    Args:
        document (etree._Element): XML SOAP document
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        Information: Information sub model
    """
    information_sub_model: Information = Information(
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
        document_request_time=convert_date_and_time_to_datetime(
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

    return information_sub_model


def _parse_times_and_distances_sub_model(
    document: etree._Element,
    namespaces: dict[str, str],
) -> TimesAndDistances:

    # Create the sub-model, we temporary set the time delta properties to 0
    zero_time_delta: datetime.timedelta = datetime.timedelta.min
    tad_sub_model: TimesAndDistances = TimesAndDistances(
        mission_date=convert_date_to_datetime(
            get_text(document, "MamooriatDate", namespaces),
        ),
        mission_received_time=convert_to_time(
            get_text(document, "DaryaftMamooriat", namespaces),
        ),
        depart_from_station_odometer=convert_to_integer(
            get_text(document, "KMHarkat", namespaces),
        ),
        arrive_at_emergency_odometer=convert_to_integer(
            get_text(document, "KMResidanBeForiat", namespaces),
        ),
        arrive_at_hospital_odometer=convert_to_integer(
            get_text(document, "KMResidanBeDarmani", namespaces),
        ),
        mission_complete_odometer=convert_to_integer(
            get_text(document, "KMPayanMamooriat", namespaces),
        ),
        arrive_at_station_odometer=convert_to_integer(
            get_text(document, "KMesidanBePaygah", namespaces),
        ),
        vehicle_refuel_odometer=convert_to_integer(
            get_text(document, "KMSookhtgiri", namespaces),
        ),
        senior_staff_code=convert_to_integer(
            get_text(document, "StaffArshad", namespaces),
        ),
        first_staff_code=convert_to_integer(
            get_text(document, "Staff1", namespaces),
        ),
        second_staff_code=convert_to_integer(
            get_text(document, "Staff2", namespaces),
        ),
        depart_from_station_time=convert_to_time(
            get_text(document, "HarkatAzPaygah", namespaces),
        ),
        arrive_at_emergency_time=convert_to_time(
            get_text(document, "ResidanBeForiat", namespaces),
        ),
        depart_from_emergency_time=convert_to_time(
            get_text(document, "HarkatAzForiat", namespaces),
        ),
        arrive_at_hospital_time=convert_to_time(
            get_text(document, "ResidanBeDarmani", namespaces),
        ),
        deliver_to_hospital_time=convert_to_time(
            get_text(document, "TahvilBedarmani", namespaces),
        ),
        mission_complete_time=convert_to_time(
            get_text(document, "PayanMamooriat", namespaces),
        ),
        arrive_at_station_time=convert_to_time(
            get_text(document, "ResidanBePaygah", namespaces),
        ),
        time_to_depart=zero_time_delta,
        time_to_arrive=zero_time_delta,
        time_at_emergency_location=zero_time_delta,
        time_to_hospital=zero_time_delta,
        time_to_deliver=zero_time_delta,
        time_to_complete=zero_time_delta,
        overall_mission_time=zero_time_delta,
    )

    # Calculate and assign the delta properties
    tad_sub_model.time_to_depart = calculate_time_delta(
        tad_sub_model.mission_received_time,
        tad_sub_model.depart_from_station_time,
    )
    tad_sub_model.time_to_arrive = calculate_time_delta(
        tad_sub_model.depart_from_station_time,
        tad_sub_model.arrive_at_emergency_time,
    )
    tad_sub_model.time_at_emergency_location = calculate_time_delta(
        tad_sub_model.arrive_at_emergency_time,
        tad_sub_model.depart_from_emergency_time,
    )
    tad_sub_model.time_to_hospital = calculate_time_delta(
        tad_sub_model.depart_from_emergency_time,
        tad_sub_model.arrive_at_hospital_time,
    )
    tad_sub_model.time_to_deliver = calculate_time_delta(
        tad_sub_model.arrive_at_hospital_time,
        tad_sub_model.deliver_to_hospital_time,
    )
    tad_sub_model.time_to_complete = calculate_time_delta(
        tad_sub_model.mission_complete_time,
        tad_sub_model.arrive_at_station_time,
    )
    tad_sub_model.overall_mission_time = calculate_time_delta(
        tad_sub_model.mission_received_time,
        tad_sub_model.arrive_at_station_time,
    )

    return tad_sub_model
