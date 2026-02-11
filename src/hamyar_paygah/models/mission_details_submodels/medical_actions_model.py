"""Medical actions sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class ActionTiming:
    """Timing information for a medical action."""

    before_ems: bool = False
    """Action was performed before EMS technicians arrived."""
    after_ems: bool = False
    """Action was performed after EMS technicians arrived."""


@dataclass(slots=True)
class MedicalActions:
    """Medical actions performed for the patient."""

    suction: ActionTiming
    """Airway suctioning."""
    cpr: ActionTiming
    """Cardiopulmonary resuscitation."""
    dressing: ActionTiming
    """Wound dressing or bandaging."""
    airway_tube: ActionTiming
    """Airway tube insertion."""
    cardiac_massage: ActionTiming
    """Cardiac massage."""
    assisted_ventilation: ActionTiming
    """Assisted ventilation or breathing support."""
    vital_signs: ActionTiming
    """Vital signs assessment."""
    consultation: ActionTiming
    """Medical consultation."""
    defibrillation: ActionTiming
    """Electrical shock / defibrillation."""
    monitoring: ActionTiming
    """Patient monitoring."""
    iv_access: ActionTiming
    """Intravenous access."""
    oxygen_therapy: ActionTiming
    """Oxygen administration."""
    cbr: ActionTiming
    """Complete bed rest (patient kept immobile in bed)."""
    head_immobilization: ActionTiming
    """Head immobilization."""
    limb_immobilization: ActionTiming
    """Limb immobilization or splinting."""
    spinal_immobilization: ActionTiming
    """Spinal immobilization."""
