"""Defines the Mission data model used in the Hamyar Paygah EMS client."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class Mission:
    """Represents a single EMS mission retrieved from the server."""

    address: str | None
    """Full address of the mission location."""
    ambulance_code: int | None
    """Code/ID of the ambulance handling the mission."""
    code: int | None
    """Mission code (unique identifier from server)."""
    date: str | None
    """Mission timestamp in ISO format (``yyyy-mm-ddThh:mm:ss``)."""
    hospital_id: int | None
    """Optional hospital ID (None if patient is not transported)."""
    hospital_name: str | None
    """Optional hospital name (None if patient is not transported)."""
    id: int | None
    """Mission ID (Identical to Code, redundant)."""
    patient_id: int | None
    """Patient ID involved in the mission."""
    patient_name: str | None
    """Name of the patient."""
    persian_date: str | None
    """Persian calendar date of the mission."""
    result: str | None
    """Mission result or status description."""
