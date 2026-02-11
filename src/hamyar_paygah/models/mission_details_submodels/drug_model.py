"""Drug sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class Drug:
    """Single administered medication."""

    name: str | None
    """Name of the medication."""

    dose: str | None
    """Administered dose."""

    route: str | None
    """Route of administration (e.g., IV, IM, oral)."""

    time: str | None
    """Time the medication was administered."""
