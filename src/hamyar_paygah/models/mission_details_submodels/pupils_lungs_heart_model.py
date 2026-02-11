"""Pupils, Lung and Heart sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass
from enum import Enum


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


class BreathingRhythm(Enum):
    """Breathing rhythm pattern."""

    REGULAR = "regular"
    """Regular breathing rhythm."""

    IRREGULAR = "irregular"
    """Irregular or abnormal breathing rhythm."""


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


class HeartRhythm(Enum):
    """Heart rhythm pattern."""

    REGULAR = "regular"
    """Regular heart rhythm."""

    IRREGULAR = "irregular"
    """Irregular heart rhythm (arrhythmia)."""


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
