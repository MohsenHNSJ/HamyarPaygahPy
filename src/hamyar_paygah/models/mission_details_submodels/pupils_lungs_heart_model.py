"""Pupils, Lung and Heart sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass
from enum import Enum

REGULAR_PERSIAN_TEXT: str = "منظم"
"""Text to show when status is regular"""
IRREGULAR_PERSIAN_TEXT: str = "نامنظم"
"""Text to show when status is irregular"""
NORMAL_PERSIAN_TEXT: str = "طبیعی"
"""Text to show when status is normal"""


class PupilStatus(Enum):
    """Clinical status of the pupil."""

    NORMAL = "normal"
    """Normal pupil size and response."""
    DILATED = "dilated"
    """Abnormally dilated pupil (mydriasis)."""
    MIOTIC = "miotic"
    """Abnormally constricted pupil (miosis)."""
    NO_RESPONSE = "no_response"
    """No pupillary response to light."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set pupil status."""
        return {
            PupilStatus.NORMAL: NORMAL_PERSIAN_TEXT,
            PupilStatus.DILATED: "گشاد شده",
            PupilStatus.MIOTIC: "منقبض شده",
            PupilStatus.NO_RESPONSE: "بدون پاسخ به نور",
        }[self]


@dataclass(slots=True)
class Pupils:
    """Pupillary examination findings."""

    right: PupilStatus | None
    """Right eye pupil status."""

    left: PupilStatus | None
    """Left eye pupil status."""


class LungSound(Enum):
    """Auscultation sound of the lung."""

    NORMAL = "normal"
    """Normal breath sounds."""
    RALES = "rales"
    """Crackles (rales) heard on auscultation."""
    WHEEZE = "wheeze"
    """Wheezing breath sounds."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set lung sound."""
        return {
            LungSound.NORMAL: NORMAL_PERSIAN_TEXT,
            LungSound.RALES: "رال",
            LungSound.WHEEZE: "ویز",
        }[self]


class BreathingRhythm(Enum):
    """Breathing rhythm pattern."""

    REGULAR = "regular"
    """Regular breathing rhythm."""
    IRREGULAR = "irregular"
    """Irregular or abnormal breathing rhythm."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set breathing rhythm."""
        return {
            BreathingRhythm.REGULAR: REGULAR_PERSIAN_TEXT,
            BreathingRhythm.IRREGULAR: IRREGULAR_PERSIAN_TEXT,
        }[self]


@dataclass(slots=True)
class LungSide:
    """Clinical findings for one lung."""

    sound: LungSound | None
    """Breath sound assessment."""

    rhythm: BreathingRhythm | None
    """Breathing rhythm assessment."""


@dataclass(slots=True)
class Lungs:
    """Pulmonary examination findings."""

    right: LungSide
    """Right lung findings."""

    left: LungSide
    """Left lung findings."""


class HeartSound(Enum):
    """Heart auscultation sound."""

    NORMAL = "normal"
    """Normal heart sounds."""
    ABNORMAL = "abnormal"
    """Abnormal or muffled heart sounds."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set heart sound."""
        return {
            HeartSound.NORMAL: NORMAL_PERSIAN_TEXT,
            HeartSound.ABNORMAL: "صدای اضافی",
        }[self]


class HeartRhythm(Enum):
    """Heart rhythm pattern."""

    REGULAR = "regular"
    """Regular heart rhythm."""
    IRREGULAR = "irregular"
    """Irregular heart rhythm (arrhythmia)."""

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set heart rhythm."""
        return {
            HeartRhythm.REGULAR: REGULAR_PERSIAN_TEXT,
            HeartRhythm.IRREGULAR: IRREGULAR_PERSIAN_TEXT,
        }[self]


@dataclass(slots=True)
class Heart:
    """Cardiac examination findings."""

    sound: HeartSound | None
    """Heart sound assessment."""

    rhythm: HeartRhythm | None
    """Heart rhythm assessment."""


@dataclass(slots=True)
class PupilsLungsHeart:
    """Status of pupils, lungs and heart of the patient."""

    pupils: Pupils
    """Status of pupils"""
    lungs: Lungs
    """Status of lungs"""
    heart: Heart
    """Status of heart"""
