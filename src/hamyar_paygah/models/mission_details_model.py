"""Defines the Mission details model used in Hamyar Paygah EMS client."""

from dataclasses import dataclass

from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
    LocationAndEmergency,
)
from hamyar_paygah.models.mission_details_submodels.medical_history_model import MedicalHistory
from hamyar_paygah.models.mission_details_submodels.symptoms_model import Symptoms
from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
    TimesAndDistances,
)
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
