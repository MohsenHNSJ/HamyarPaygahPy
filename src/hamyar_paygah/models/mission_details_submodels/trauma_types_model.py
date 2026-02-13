"""Trauma types sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass
from enum import Enum


class PatientExtrication(Enum):
    """Who extricated or moved the patient from the incident scene."""

    BEFORE_EMS = "TromaBefore"
    """Patient was moved before EMS technicians arrived."""
    BY_EMS = "TromaHozoor"
    """Patient was moved by EMS technicians."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set patient extraction type."""
        return {
            PatientExtrication.BEFORE_EMS: "قبل از رسیدن تکنسین",
            PatientExtrication.BY_EMS: "در حضور تکنسین",
        }[self]


class FractureType(Enum):
    """Type of bone fracture."""

    OPEN = "ShekastegiBaz"
    """Open fracture with skin penetration (compound fracture)."""
    CLOSED = "ShekastegiBaste"
    """Closed fracture without skin penetration."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set fracture type."""
        return {
            FractureType.OPEN: "باز",
            FractureType.CLOSED: "بسته",
        }[self]


class DistalPulseStatus(Enum):
    """Status of distal pulse in the affected extremity."""

    PRESENT = "DistalDard"
    """Distal pulse is palpable."""
    ABSENT = "DistalNadard"
    """Distal pulse is not palpable."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set fracture type."""
        return {
            DistalPulseStatus.PRESENT: "دارد",
            DistalPulseStatus.ABSENT: "ندارد",
        }[self]


@dataclass(slots=True)
class TraumaTypes:
    """Tracks trauma types of the patient."""

    has_deformity: bool
    """Visible change in shape or structure (deformity)."""
    has_abrasion: bool
    """Superficial skin scraping or abrasion."""
    has_tenderness: bool
    """Localized pain or tenderness on palpation."""
    has_crush_injury: bool
    """Crush injury caused by compression or heavy force."""
    has_swelling: bool
    """Swelling or edema at the injury site."""
    has_dislocation: bool
    """Joint dislocation or abnormal joint positioning."""
    has_contusion: bool
    """Bruising or blunt force injury (contusion)."""
    has_puncture_wound: bool
    """Puncture wound caused by a sharp object."""
    has_laceration: bool
    """Cut or laceration of the skin."""
    has_tear: bool
    """Torn tissue or rupture."""
    has_amputation: bool
    """Partial or complete traumatic amputation."""
    has_external_bleeding: bool
    """Visible external bleeding."""
    has_sensory_deficit: bool
    """Loss or impairment of sensation."""
    has_motor_deficit: bool
    """Loss or impairment of motor function."""
    has_penetrating_trauma: bool
    """Penetrating injury reaching internal tissues."""
    has_blunt_trauma: bool
    """Blunt force trauma without penetration."""

    patient_extraction: PatientExtrication | None
    """Who extricated or moved the patient from the incident scene."""
    fracture_type: FractureType | None
    """Type of bone fracture."""
    distal_pulse_status: DistalPulseStatus | None
    """Status of distal pulse in the affected extremity."""

    burn_type: str | None
    """Type of burn the patient has"""
    burn_percentage: str | None
    """Percentage of burn"""
    front_trauma_locations: str | None
    """Trauma locations in frontal of body"""
    rear_trauma_locations: str | None
    """Trauma locations in the rear of body"""
