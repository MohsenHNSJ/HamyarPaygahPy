"""Symptoms sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class Symptoms:
    """Tracks the presence of various patient symptoms."""

    has_abdominal_pain: bool
    """Acute abdominal pain."""
    has_weakness: bool
    """General weakness or fatigue."""
    has_bleeding: bool
    """Presence of bleeding."""
    has_diarrhea: bool
    """Diarrhea."""
    has_vomiting: bool
    """Vomiting."""
    has_altered_consciousness: bool
    """Altered level of consciousness."""
    has_headache: bool
    """Headache."""
    has_fever_chills: bool
    """Fever with chills or shivering."""
    has_fainting: bool
    """Fainting or syncope."""
    has_blurred_vision: bool
    """Blurred vision."""
    has_double_vision: bool
    """Double vision."""
    has_sensory_motor_disturbance: bool
    """Disturbance in sensory or motor function."""
    has_memory_loss_post_trauma: bool
    """Memory loss following trauma."""
    has_dizziness: bool
    """Dizziness or vertigo."""
    has_sweating: bool
    """Excess sweating"""
    has_chest_pain: bool
    """Chest pain."""
    has_shortness_of_breath: bool
    """Shortness of breath or difficulty breathing."""
    other_symptoms: str | None
    """Other symptoms the patient has"""
