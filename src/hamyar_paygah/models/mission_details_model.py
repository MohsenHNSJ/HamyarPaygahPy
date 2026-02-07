"""Defines the Mission details model used in Hamyar Paygah EMS client."""

from dataclasses import dataclass

from hamyar_paygah.models.mission_details_submodels.information_model import Information
from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
    LocationAndEmergency,
)
from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
    TimesAndDistances,
)


@dataclass(slots=True)
class MissionDetails:
    """Represents details of a single EMS mission retrieved from the server."""

    information: Information
    """General information of the mission"""
    times_and_distances: TimesAndDistances
    """Times and distances information of the mission"""
    location_and_emergency: LocationAndEmergency
