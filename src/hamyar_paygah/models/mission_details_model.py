"""Defines the Mission details model used in Hamyar Paygah EMS client."""

from dataclasses import dataclass

from hamyar_paygah.models.mission_details_submodels.information_model import Information


@dataclass(slots=True)
class MissionDetails:
    """Represents details of a single EMS mission retrieved from the server."""

    information: Information
    """General information of the mission"""
