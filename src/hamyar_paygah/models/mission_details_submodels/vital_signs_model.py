"""Vital signs sub-model for Mission details model."""
# pylint: disable=R0902

import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class VitalSigns:
    """Single snapshot of patient vital signs recorded at a specific time."""

    record_time: datetime.time | None
    """Time when vital signs were recorded"""
    respiratory_rate: int | None
    """Respiratory rate in breaths per minute."""
    pulse_rate: int | None
    """Pulse rate in beats per minute."""
    blood_pressure: str | None
    """Blood pressure measurement in systolic/diastolic format (e.g., '120/80')."""
    blood_sugar: int | None
    """Blood sugar level (mg/dL), if measured."""
    oxygen_saturation: int | None
    """Blood oxygen saturation percentage (SpO₂)."""
    gcs_eye: int | None
    """Glasgow Coma Scale - eye response score."""
    gcs_verbal: int | None
    """Glasgow Coma Scale - verbal response score."""
    gcs_motor: int | None
    """Glasgow Coma Scale - motor response score."""
    gcs_total: int | None
    """Total GCS score as reported by the server"""
