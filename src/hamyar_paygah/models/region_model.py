"""Defines the Region data model."""

from dataclasses import dataclass


@dataclass(slots=True)
class Region:
    """Represents an EMS Region."""

    region_name: str
    """Name of the EMS Region."""
    region_id: int
    """ID of the EMS Region."""
