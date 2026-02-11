"""Medical center sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class MedicalCenter:
    """Information related to patient handover to a medical facility."""

    receiving_physician_code: str | None
    """Identifier code of the physician who received the patient."""
    physician_code: str | None
    """Primary physician identifier code."""
    physician_1050_code: str | None
    """Physician code of EMS center."""
    physician_order: str | None
    """Medical instructions or orders given by the physician."""
    physician_order_secondary: str | None
    """Additional or secondary physician instructions."""
    receiving_physician_name: str | None
    """Full name of the physician who received the patient."""
    handover_datetime: str | None
    """Date and time when the patient was handed over to the medical facility."""
