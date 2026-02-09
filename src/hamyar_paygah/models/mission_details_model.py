"""Defines the Mission details model used in Hamyar Paygah EMS client."""
# pylint: disable=R0902

from dataclasses import dataclass

from hamyar_paygah.models.mission_details_submodels.drug_model import Drug
from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
    LocationAndEmergency,
)
from hamyar_paygah.models.mission_details_submodels.medical_actions_model import MedicalActions
from hamyar_paygah.models.mission_details_submodels.medical_center_model import MedicalCenter
from hamyar_paygah.models.mission_details_submodels.medical_history_model import MedicalHistory
from hamyar_paygah.models.mission_details_submodels.mission_result_model import MissionResult
from hamyar_paygah.models.mission_details_submodels.pupils_lungs_heart_model import PupilsLungsHeart
from hamyar_paygah.models.mission_details_submodels.symptoms_model import Symptoms
from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
    TimesAndDistances,
)
from hamyar_paygah.models.mission_details_submodels.trauma_types_model import TraumaTypes
from hamyar_paygah.models.mission_details_submodels.vital_signs_model import VitalSigns


@dataclass(slots=True)
class MissionDetails:
    """Represents details of a single EMS mission retrieved from the server."""

    information: Information
    """General information of the mission"""
    times_and_distances: TimesAndDistances
    """Times and distances information of the mission"""
    location_and_emergency: LocationAndEmergency
    """Location and emergency information of the mission"""
    symptoms: Symptoms
    """Symptoms of the patient"""
    vital_signs: list[VitalSigns]
    """Vital signs of the patient"""
    medical_history: MedicalHistory
    """Medical history of the patient"""
    pupils_lungs_heart: PupilsLungsHeart
    """Status of pupils, lungs and heart of the patient."""
    trauma_types: TraumaTypes
    """Trauma types of the patient."""
    medical_actions: MedicalActions
    """Medical actions performed for the patient"""
    drugs: list[Drug]
    """List of drugs administered to the patient"""
    result: MissionResult
    """Result of the mission"""
    medical_center: MedicalCenter
    """Medical center information"""
