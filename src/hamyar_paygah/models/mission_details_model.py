"""Defines the Mission details model used in Hamyar Paygah EMS client."""

from dataclasses import dataclass


@dataclass(slots=True)
class MissionDetails:
    """Represents details of a single EMS mission retrieved from the server."""
