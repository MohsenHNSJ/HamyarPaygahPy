"""Medical history sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass


@dataclass(slots=True)
class MedicalHistory:
    """Represents the patient's known medical history conditions."""

    # History
    drug_allergies: str | None
    """Known drug allergies reported for the patient."""
    current_medications: str | None
    """Medications currently being taken by the patient."""

    # Diseases
    has_cardiac_disease: bool
    """History of heart or cardiac disease."""
    has_hypertension: bool
    """History of high blood pressure (hypertension)."""
    has_substance_abuse: bool
    """History of substance or drug abuse."""
    has_disability: bool
    """History of physical or mental disability."""
    has_asthma: bool
    """History of asthma or chronic reactive airway disease."""
    has_stroke_history: bool
    """History of cerebrovascular accident (stroke)."""
    has_psychiatric_disorder: bool
    """History of psychiatric or mental health disorders."""
    has_prior_trauma: bool
    """History of previous traumatic injuries."""
    has_surgical_history: bool
    """History of prior surgical procedures."""
    has_gastrointestinal_disease: bool
    """History of gastrointestinal disorders."""
    has_renal_disease: bool
    """History of kidney or renal disorders."""
    has_seizure_disorder: bool
    """History of seizures or epilepsy."""
    has_infectious_disease: bool
    """History of infectious diseases."""
    has_diabetes: bool
    """History of diabetes mellitus."""
    has_malignancy_history: bool
    """History of cancer or malignant disease."""
    has_special_conditions: bool
    """History of special or unspecified medical conditions."""
    has_pulmonary_disease: bool
    """History of lung or chronic pulmonary disease."""
    has_other_medical_history: bool
    """Patient has other medical history not specified here"""
