"""This module defines the core data models for Hamyar Paygah.

This module is designed to be IDE-friendly: all fields are documented
so hovering over them shows explanations.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Mission:
    """Represents a single EMS mission retrieved from the server."""

    address: str
    """Full address of the mission location."""
    ambulance_code: int
    """Code/ID of the ambulance handling the mission."""
    code: int
    """Mission code (unique identifier from server)."""
    date: str
    """Mission timestamp in ISO format (yyyy-mm-ddThh:mm:ss)."""
    hospital_id: int | None
    """Optional hospital ID (None if patient is not transported)."""
    hospital_name: str | None
    """Optional hospital name (None if patient is not transported)."""
    id: int
    """Mission ID (Identical to Code, redundant)."""
    patient_id: int
    """Patient ID involved in the mission."""
    patient_name: str
    """Name of the patient."""
    persian_date: str
    """Persian calendar date of the mission."""
    result: str
    """Mission result or status description."""
