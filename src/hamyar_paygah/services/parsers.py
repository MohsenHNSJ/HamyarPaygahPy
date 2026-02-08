"""XML parsers module.

This module provides functions to parse SOAP XML responses from the EMS server
and convert them into Python data models.
"""

# pylint: disable=I1101,R0914
import datetime
from typing import cast

from lxml import etree

from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
    AccidentType,
    IllnessType,
    InjuryRole,
    LocationAndEmergency,
    LocationType,
    VehicleType,
)
from hamyar_paygah.models.mission_details_submodels.medical_actions_model import (
    ActionTiming,
    MedicalActions,
)
from hamyar_paygah.models.mission_details_submodels.medical_history_model import MedicalHistory
from hamyar_paygah.models.mission_details_submodels.pupils_lungs_heart_model import (
    BreathingRhythm,
    Heart,
    HeartRhythm,
    HeartSound,
    Lungs,
    LungSide,
    LungSound,
    Pupils,
    PupilsLungsHeart,
    PupilStatus,
)
from hamyar_paygah.models.mission_details_submodels.symptoms_model import Symptoms
from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
    TimesAndDistances,
)
from hamyar_paygah.models.mission_details_submodels.trauma_types_model import (
    DistalPulseStatus,
    FractureType,
    PatientExtrication,
    TraumaTypes,
)
from hamyar_paygah.models.mission_details_submodels.vital_signs_model import VitalSigns
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.utils.math_utils import calculate_time_delta
from hamyar_paygah.utils.text_utils import (
    convert_date_and_time_to_datetime,
    convert_date_to_datetime,
)
from hamyar_paygah.utils.xml_utils import (
    get_bool,
    get_enum_from_boolean_flags,
    get_integer,
    get_text,
    get_time,
)


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
                address=get_text(document, "Address", namespaces),
                ambulance_code=get_integer(
                    document,
                    "AmbulanceCode",
                    namespaces,
                ),
                code=get_integer(document, "MissionCode", namespaces),
                date=get_text(document, "Date", namespaces),
                hospital_id=get_integer(document, "HospitalId", namespaces),
                hospital_name=get_text(document, "Hospital", namespaces),
                id=get_integer(document, "MissionId", namespaces),
                patient_id=get_integer(document, "PatientId", namespaces),
                patient_name=get_text(document, "Name", namespaces),
                persian_date=get_text(
                    document,
                    "PersianDate",
                    namespaces,
                ),
                result=get_text(document, "Result", namespaces),
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
    information: Information = _parse_information(
        document,
        namespaces,
    )
    # Create times and distances sub-model
    times_and_distances: TimesAndDistances = _parse_times_and_distances(
        document,
        namespaces,
    )
    # Create location and emergency sub-model
    location_and_emergency: LocationAndEmergency = _parse_location_and_emergency(
        document,
        namespaces,
    )
    # Create symptoms sub-model
    symptoms: Symptoms = _parse_symptoms(document, namespaces)
    # Create vital signs sub-model
    vital_signs: list[VitalSigns] = _parse_vital_signs(document, namespaces)
    # Create medical history sub-model
    medical_history: MedicalHistory = _parse_medical_history(
        document,
        namespaces,
    )
    # Create pupils, lungs and heart sub-model
    pupils_lungs_heart: PupilsLungsHeart = _parse_pupils_lungs_heart(
        document,
        namespaces,
    )
    # Create trauma types sub-model
    trauma_types: TraumaTypes = _parse_trauma_types(document, namespaces)
    # Create medical actions sub-model
    medical_actions: MedicalActions = _parse_medical_actions(
        document,
        namespaces,
    )

    # Create final model
    mission_details: MissionDetails = MissionDetails(
        information=information,
        times_and_distances=times_and_distances,
        location_and_emergency=location_and_emergency,
        symptoms=symptoms,
        vital_signs=vital_signs,
        medical_history=medical_history,
        pupils_lungs_heart=pupils_lungs_heart,
        trauma_types=trauma_types,
        medical_actions=medical_actions,
    )

    return mission_details


def _parse_information(
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
    return Information(
        patient_name=get_text(document, "BimarName", namespaces),
        years_of_age=get_integer(document, "Age", namespaces),
        months_of_age=get_integer(document, "AgeMonth", namespaces),
        iranian_nationality=get_bool(document, "IsIrani", namespaces),
        foreign_nationality=get_bool(document, "IsGheirIrani", namespaces),
        is_male_gender=get_bool(document, "IsMozakar", namespaces),
        is_female_gender=get_bool(document, "IsMoanas", namespaces),
        is_unknown_gender=get_bool(document, "IsNamoshakhas", namespaces),
        national_code=get_integer(document, "CodeMelli", namespaces),
        document_serial_number=get_text(
            document,
            "ShomareSerialParvade",
            namespaces,
        ),  # Parvade?? :/
        caller_number=get_text(
            document,
            "TelAsli",
            namespaces,
        ),
        backup_number=get_text(
            document,
            "TelPoshtibani",
            namespaces,
        ),
        ambulance_code=get_integer(document, "AmbulanceCode", namespaces),
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
        ),
        summary=get_text(
            document,
            "Tozihat",
            namespaces,
        ),
    )


def _parse_times_and_distances(
    document: etree._Element,
    namespaces: dict[str, str],
) -> TimesAndDistances:

    # Create the sub-model, we temporary set the time delta properties to 0
    zero_time_delta: datetime.timedelta = datetime.timedelta.min
    tad_sub_model: TimesAndDistances = TimesAndDistances(
        mission_date=convert_date_to_datetime(
            get_text(document, "MamooriatDate", namespaces),
        ),
        mission_received_time=get_time(
            document,
            "DaryaftMamooriat",
            namespaces,
        ),
        depart_from_station_odometer=get_integer(
            document,
            "KMHarkat",
            namespaces,
        ),
        arrive_at_emergency_odometer=get_integer(
            document,
            "KMResidanBeForiat",
            namespaces,
        ),
        arrive_at_hospital_odometer=get_integer(
            document,
            "KMResidanBeDarmani",
            namespaces,
        ),
        mission_complete_odometer=get_integer(
            document,
            "KMPayanMamooriat",
            namespaces,
        ),
        arrive_at_station_odometer=get_integer(
            document,
            "KMesidanBePaygah",
            namespaces,
        ),
        vehicle_refuel_odometer=get_integer(
            document,
            "KMSookhtgiri",
            namespaces,
        ),
        senior_staff_code=get_integer(document, "StaffArshad", namespaces),
        first_staff_code=get_integer(document, "Staff1", namespaces),
        second_staff_code=get_integer(document, "Staff2", namespaces),
        depart_from_station_time=get_time(
            document,
            "HarkatAzPaygah",
            namespaces,
        ),
        arrive_at_emergency_time=get_time(
            document,
            "ResidanBeForiat",
            namespaces,
        ),
        depart_from_emergency_time=get_time(
            document,
            "HarkatAzForiat",
            namespaces,
        ),
        arrive_at_hospital_time=get_time(
            document,
            "ResidanBeDarmani",
            namespaces,
        ),
        deliver_to_hospital_time=get_time(
            document,
            "TahvilBedarmani",
            namespaces,
        ),
        mission_complete_time=get_time(document, "PayanMamooriat", namespaces),
        arrive_at_station_time=get_time(
            document,
            "ResidanBePaygah",
            namespaces,
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


def _parse_location_and_emergency(
    document: etree._Element,
    namespaces: dict[str, str],
) -> LocationAndEmergency:
    """Parses the location and emergency sub model and returns it.

    Args:
        document (etree._Element): XML SOAP document
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        LocationAndEmergency: Location and emergency sub model
    """
    return LocationAndEmergency(
        address=get_text(document, "Address", namespaces),
        chief_complaint=get_text(document, "CC", namespaces),
        location_type=get_enum_from_boolean_flags(
            document,
            namespaces,
            LocationType,
        ),
        location_other_info=get_text(
            document,
            "MahalForiatSayer",
            namespaces,
        ),
        accident_type=get_enum_from_boolean_flags(
            document,
            namespaces,
            AccidentType,
        ),
        illness_type=get_enum_from_boolean_flags(
            document,
            namespaces,
            IllnessType,
        ),
        is_vehicle_accident=get_bool(document, "Tasadofat", namespaces),
        emergency_type_other_info=get_text(
            document,
            "TashkhisAvaliyeSayer",
            namespaces,
        ),
        role_in_accident=get_enum_from_boolean_flags(
            document,
            namespaces,
            InjuryRole,
        ),
        role_in_accident_other_info=get_text(
            document,
            "VaziatMasdoomSayer",
            namespaces,
        ),
        vehicle_type=get_enum_from_boolean_flags(
            document,
            namespaces,
            VehicleType,
        ),
    )


def _parse_symptoms(document: etree._Element, namespaces: dict[str, str]) -> Symptoms:
    """Parses the symptoms sub model and returns it.

    Args:
         document (etree._Element): XML SOAP document
         namespaces (dict[str, str]): SOAP namespaces

    Returns:
         Symptoms: Symptoms sub model
    """
    return Symptoms(
        has_abdominal_pain=get_bool(document, "DShekami", namespaces),
        has_weakness=get_bool(document, "ZafBihali", namespaces),
        has_bleeding=get_bool(document, "Khoonizi", namespaces),
        has_diarrhea=get_bool(document, "Eshal", namespaces),
        has_vomiting=get_bool(document, "Tahavoestefragh", namespaces),
        has_altered_consciousness=get_bool(
            document,
            "EkhtelalHooshyari",
            namespaces,
        ),
        has_headache=get_bool(document, "Sardard", namespaces),
        has_fever_chills=get_bool(document, "TaboLarz", namespaces),
        has_fainting=get_bool(document, "BihooshiGozara", namespaces),
        has_blurred_vision=get_bool(document, "TariDid", namespaces),
        has_double_vision=get_bool(document, "Dobini", namespaces),
        has_sensory_motor_disturbance=get_bool(
            document,
            "EkhtelaHesiHarkati",
            namespaces,
        ),
        has_memory_loss_post_trauma=get_bool(
            document,
            "FaramooshiBadAzZarbe",
            namespaces,
        ),
        has_dizziness=get_bool(document, "Sargije", namespaces),
        has_sweating=get_bool(document, "Tarigh", namespaces),
        has_chest_pain=get_bool(document, "dardGhafaseSadra", namespaces),
        has_shortness_of_breath=get_bool(document, "TangiNafas", namespaces),
        other_symptoms=get_text(document, "AlaemHamrahSayer", namespaces),
    )


def _parse_vital_signs(document: etree._Element, namespaces: dict[str, str]) -> list[VitalSigns]:
    """Extracts patient vital sign records from SOAP XML response.

    Args:
        document (etree._Element): XML SOAP document
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        list[VitalSigns]: List of vita signs
    """
    # Create and empty list
    vital_signs: list[VitalSigns] = []

    # Iterate through all four available records
    for i in range(1, 5):
        record = VitalSigns(
            record_time=get_time(document, f"Time{i}", namespaces),
            respiratory_rate=get_integer(document, f"Rr{i}", namespaces),
            pulse_rate=get_integer(document, f"PR{i}", namespaces),
            blood_pressure=get_text(document, f"BP{i}", namespaces),
            blood_sugar=get_integer(document, f"BS{i}", namespaces),
            oxygen_saturation=get_integer(document, f"SPO2{i}", namespaces),
            gcs_eye=get_integer(document, f"E4{i}", namespaces),
            gcs_verbal=get_integer(document, f"v5{i}", namespaces),
            gcs_motor=get_integer(document, f"m6{i}", namespaces),
            gcs_total=get_integer(document, f"T15{i}", namespaces),
        )

        # If the vital sign has a valid record time
        if record.record_time is not None:
            # Add it to the list
            vital_signs.append(record)

    return vital_signs


def _parse_medical_history(document: etree._Element, namespaces: dict[str, str]) -> MedicalHistory:
    """Extracts patient medical history from SOAP XML response.

    Args:
        document (etree._Element): XML SOAP document
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        MedicalHistory: Medical history of patient
    """
    return MedicalHistory(
        drug_allergies=get_text(document, "Hasasiatdarooei", namespaces),
        current_medications=get_text(document, "DarooMasrafi", namespaces),
        has_cardiac_disease=get_bool(document, "TGhalbi", namespaces),
        has_hypertension=get_bool(document, "TFesharKhoon", namespaces),
        has_substance_abuse=get_bool(document, "SooMasrafMavad", namespaces),
        has_disability=get_bool(document, "TMalooliat", namespaces),
        has_asthma=get_bool(document, "TAsm", namespaces),
        has_stroke_history=get_bool(document, "TSakteMaghzi", namespaces),
        has_psychiatric_disorder=get_bool(document, "TRavani", namespaces),
        has_prior_trauma=get_bool(document, "TSabegheTroma", namespaces),
        has_surgical_history=get_bool(document, "TJarahi", namespaces),
        has_gastrointestinal_disease=get_bool(
            document,
            "TMoshkelatGovareshi",
            namespaces,
        ),
        has_renal_disease=get_bool(document, "TMoshkeatKolyavi", namespaces),
        has_seizure_disorder=get_bool(document, "TSar", namespaces),
        has_infectious_disease=get_bool(document, "TOfooni", namespaces),
        has_diabetes=get_bool(document, "TDiabet", namespaces),
        has_malignancy_history=get_bool(
            document,
            "TSabegheBadkhimi",
            namespaces,
        ),
        has_special_conditions=get_bool(document, "TKhas", namespaces),
        has_pulmonary_disease=get_bool(document, "TRiavi", namespaces),
        has_other_medical_history=get_bool(document, "TSayer", namespaces),
    )


def _parse_pupils_lungs_heart(
    document: etree._Element,
    namespaces: dict[str, str],
) -> PupilsLungsHeart:
    """Parses the pupils, lungs and heart sub model and returns it.

    Args:
        document (etree._Element): XML SOAP document
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        PupilsLungsHeart: Pupils, lungs and heart model
    """
    # Create pupils model
    pupils: Pupils = Pupils(
        right=_parse_pupil_status(document, namespaces, "R"),
        left=_parse_pupil_status(document, namespaces, "L"),
    )
    # Create lungs model
    lungs: Lungs = Lungs(
        right=_parse_lung_status(document, namespaces, "R"),
        left=_parse_lung_status(document, namespaces, "L"),
    )
    # Create heart model
    heart: Heart = _parse_heart_status(document, namespaces)

    # Return the final model
    return PupilsLungsHeart(pupils=pupils, lungs=lungs, heart=heart)


def _parse_pupil_status(
    document: etree._Element,
    namespaces: dict[str, str],
    pupil_side: str,
) -> PupilStatus | None:
    """Parses the status of pupil from server into Pupil status object.

    Args:
        document (etree._Element): XML SOAP response
        namespaces (dict[str, str]): SOAP namespaces
        pupil_side (str): "R" for right side and "L" for left side

    Returns:
        PupilStatus | None: PupilStatus object or none.
    """
    # Return pupils status
    if get_bool(document, f"MardommakNo{pupil_side}", namespaces):
        return PupilStatus.NORMAL
    if get_bool(document, f"MardommakDi{pupil_side}", namespaces):
        return PupilStatus.DILATED
    if get_bool(document, f"MardommakMi{pupil_side}", namespaces):
        return PupilStatus.MIOTIC
    if get_bool(document, f"MardommakBe{pupil_side}", namespaces):
        return PupilStatus.NO_RESPONSE
    # Return None if all false
    return None


def _parse_lung_status(
    document: etree._Element,
    namespaces: dict[str, str],
    lung_side: str,
) -> LungSide:
    """Parses the status of lung from server into Lung side object.

    Args:
        document (etree._Element): XML SOAP response
        namespaces (dict[str, str]): SOAP namespaces
        lung_side (str): "R" for right side and "L" for left side.

    Returns:
        LungSide: LungSide object.
    """
    # Get lung sound
    lung_sound: LungSound | None = None
    if get_bool(document, f"RieNo{lung_side}", namespaces):
        lung_sound = LungSound.NORMAL
    if get_bool(document, f"RieRa{lung_side}", namespaces):
        lung_sound = LungSound.RALES
    if get_bool(document, f"RieBa{lung_side}", namespaces):
        lung_sound = LungSound.WHEEZE

    # Get lung rhythm
    lung_rhythm: BreathingRhythm | None = None
    if get_bool(document, f"RieMo{lung_side}", namespaces):
        lung_rhythm = BreathingRhythm.REGULAR
    if get_bool(document, f"RieNa{lung_side}", namespaces):
        lung_rhythm = BreathingRhythm.IRREGULAR

    # Return lung status
    return LungSide(sound=lung_sound, rhythm=lung_rhythm)


def _parse_heart_status(document: etree._Element, namespaces: dict[str, str]) -> Heart:
    """Parses the status of heart from server into heart object.

    Args:
        document (etree._Element): XML SOAP response
        namespaces (dict[str, str]): SOAP namespaces

    Returns:
        Heart: Heart object.
    """
    # Get heart sound
    heart_sound: HeartSound | None = None
    if get_bool(document, "GhalbNormal", namespaces):
        heart_sound = HeartSound.NORMAL
    if get_bool(document, "GhalbSafi", namespaces):
        heart_sound = HeartSound.ABNORMAL

    # Get heart rhythm
    heart_rhythm: HeartRhythm | None = None
    if get_bool(document, "GhalbMonazam", namespaces):
        heart_rhythm = HeartRhythm.REGULAR
    if get_bool(document, "GhalbNamonazam", namespaces):
        heart_rhythm = HeartRhythm.IRREGULAR

    # Return heart
    return Heart(sound=heart_sound, rhythm=heart_rhythm)


def _parse_trauma_types(document: etree._Element, namespaces: dict[str, str]) -> TraumaTypes:
    """Parses the trauma types sub model and returns it.

    Args:
         document (etree._Element): XML SOAP document
         namespaces (dict[str, str]): SOAP namespaces

    Returns:
         TraumaTypes: trauma types sub model
    """
    return TraumaTypes(
        has_deformity=get_bool(document, "TaghirShekl", namespaces),
        has_abrasion=get_bool(document, "Kharashidegi", namespaces),
        has_tenderness=get_bool(document, "Tenderes", namespaces),
        has_crush_injury=get_bool(document, "LehShodegi", namespaces),
        has_swelling=get_bool(document, "Tavarom", namespaces),
        has_dislocation=get_bool(document, "DarRaftegi", namespaces),
        has_contusion=get_bool(document, "Kooftegi", namespaces),
        has_puncture_wound=get_bool(document, "SoorakhShodegi", namespaces),
        has_laceration=get_bool(document, "Boridegi", namespaces),
        has_tear=get_bool(document, "PareShodegi", namespaces),
        has_amputation=get_bool(document, "GhateOzv", namespaces),
        has_external_bleeding=get_bool(document, "ZKhoonRizi", namespaces),
        has_sensory_deficit=get_bool(document, "ZayeHesi", namespaces),
        has_motor_deficit=get_bool(document, "ZayeHarkati", namespaces),
        has_penetrating_trauma=get_bool(document, "Nafez", namespaces),
        has_blunt_trauma=get_bool(document, "Blant", namespaces),
        patient_extraction=get_enum_from_boolean_flags(
            document,
            namespaces,
            PatientExtrication,
        ),
        fracture_type=get_enum_from_boolean_flags(
            document,
            namespaces,
            FractureType,
        ),
        distal_pulse_status=get_enum_from_boolean_flags(
            document,
            namespaces,
            DistalPulseStatus,
        ),
        burn_type=get_text(document, "Sookhtegi", namespaces),
        burn_percentage=get_text(document, "DarsadSookhtegi", namespaces),
        front_trauma_locations=get_text(document, "Jolo", namespaces),
        rear_trauma_locations=get_text(document, "Aghab", namespaces),
    )


def _parse_medical_actions(document: etree._Element, namespaces: dict[str, str]) -> MedicalActions:
    """Parses the medical actions sub model and returns it.

    Args:
         document (etree._Element): XML SOAP document
         namespaces (dict[str, str]): SOAP namespaces

    Returns:
         MedicalActions: Medical actions sub model
    """
    # Get suction
    suction: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "SucktionGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "SucktionBad", namespaces),
    )
    # Get cpr
    cpr: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "CPRGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "CPRBad", namespaces),
    )
    # Get dressing
    dressing: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "PansemanGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "PansemanBad", namespaces),
    )
    # Get airway tube
    airway_tube: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "LooleGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "LooleBad", namespaces),
    )
    # Get cardiac massage
    cardiac_massage: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "MasajGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "MasajBad", namespaces),
    )
    # Get assisted ventilation
    assisted_ventilation: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "TnafosGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "TanafosBad", namespaces),
    )
    # Get vital signs
    vital_signs: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "VSGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "VSBad", namespaces),
    )
    # Get consultation
    consultation: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "MoshavereGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "MoshavereBad", namespaces),
    )
    # Get defibrillation
    defibrillation: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "ShockGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "ShockBad", namespaces),
    )
    # Get monitoring
    monitoring: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "MonitoringGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "MonitoringBad", namespaces),
    )
    # Get iv access
    iv_access: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "RagGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "RagBad", namespaces),
    )
    # Get oxygen therapy
    oxygen_therapy: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "OxygenGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "OxygenBad", namespaces),
    )
    # Get cbr
    cbr: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "CbrGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "CbrBad", namespaces),
    )
    # Get head immobilization
    head_immobilization: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "SarGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "SarBad", namespaces),
    )
    # Get limb immobilization
    limb_immobilization: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "AndamGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "AndamBad", namespaces),
    )
    # Get spinal immobilization
    spinal_immobilization: ActionTiming = ActionTiming(
        before_ems=get_bool(
            document,
            "SotoonGhabl",
            namespaces,
        ),
        after_ems=get_bool(document, "StoonBad", namespaces),
    )

    return MedicalActions(
        suction=suction,
        cpr=cpr,
        dressing=dressing,
        airway_tube=airway_tube,
        cardiac_massage=cardiac_massage,
        assisted_ventilation=assisted_ventilation,
        vital_signs=vital_signs,
        consultation=consultation,
        defibrillation=defibrillation,
        monitoring=monitoring,
        iv_access=iv_access,
        oxygen_therapy=oxygen_therapy,
        cbr=cbr,
        head_immobilization=head_immobilization,
        limb_immobilization=limb_immobilization,
        spinal_immobilization=spinal_immobilization,
    )
