"""Mission result sub-model for Mission details model."""
# pylint: disable=R0902

from dataclasses import dataclass
from enum import Enum


class MissionOutcome(Enum):
    """Final outcome of an EMS mission.

    Exactly zero or one outcome may apply to a mission.
    These values describe how the mission concluded,
    not the patient's clinical condition.
    """

    PATROL = "Esteghrar"
    """Patrol or standby mission.

    The ambulance was deployed for presence, crowd coverage,
    or rapid-response readiness. No patient was present,
    and no medical intervention was required.
    """
    BASIC_CARE_ONLY = "EghdamatAvaliye"
    """Basic medical care provided without patient transport.

    Minor treatment was performed (e.g., small wound care),
    and the situation did not warrant hospital transfer.
    """
    PRIVATE_TRANSPORT = "EnteghalBaKhodroShakhsi"
    """Patient transported using a private or non-EMS vehicle.

    EMS personnel did not perform the transport.
    """
    TRANSFERRED_TO_MEDICAL_CENTER = "EzamBeDarmani"
    """Patient transferred to a hospital or medical facility.

    Transport was performed as part of the EMS mission.
    """
    OTHER_AMBULANCE = "AmbulanceDigar"
    """Mission handled or completed by another ambulance unit.

    This unit did not complete the patient care or transport.
    """
    NO_SHOW = "AdamHozoor"
    """Patient was not present at the scene.

    EMS arrived but could not locate the patient.
    """
    NO_COOPERATION_ANY = "AdamHamkariHarNoe"
    """Complete refusal of cooperation.

    The patient refused all assessment, treatment,
    and transport under any circumstances.
    """
    NO_COOPERATION = "AdamHamkari"
    """Partial refusal of cooperation.

    The patient refused certain aspects of care
    but may have accepted others.
    """
    CANCELED_BY_DISPATCH = "LaghvAzHedayat"
    """Mission canceled by dispatch or command center.

    Cancellation occurred before meaningful patient contact.
    """
    FALSE_CALL = "Kazeb"
    """False or incorrect emergency call.

    The mission was triggered by incorrect information,
    prank calls, or deliberate misinformation.
    """
    DECEASED_BEFORE_ARRIVAL = "FotGhabl"
    """Patient was already deceased upon EMS arrival.

    No resuscitation or treatment was initiated.
    """

    @property
    def persian_label(self) -> str:
        """Returns the persian label of the set location type."""
        return {
            MissionOutcome.PATROL: "استقرار",
            MissionOutcome.BASIC_CARE_ONLY: "اقدامات اولیه و توصیه مراجعه به مرکز درمانی",
            MissionOutcome.PRIVATE_TRANSPORT: "انتقال با خودروی شخصی",
            MissionOutcome.TRANSFERRED_TO_MEDICAL_CENTER: "انتقال به مرکز درمانی",
            MissionOutcome.OTHER_AMBULANCE: "تحویل به آمبولانس دیگر",
            MissionOutcome.NO_SHOW: "عدم حضور بیمار",
            MissionOutcome.NO_COOPERATION_ANY: "انصراف کامل از همکاری",
            MissionOutcome.NO_COOPERATION: "عدم همکاری و اخذ امضا",
            MissionOutcome.CANCELED_BY_DISPATCH: "لغو از طرف مرکز  ",
            MissionOutcome.FALSE_CALL: "کاذب / اشتباه",
            MissionOutcome.DECEASED_BEFORE_ARRIVAL: "فوت قبل از رسیدن تکنسین",
        }[self]


@dataclass(slots=True)
class MissionResult:
    """Results information of the mission."""

    result: MissionOutcome | None
    """Final result of the mission."""
    hospital_name: str | None
    """Name of the hospital if the patient is transferred"""
    refusal_form_code: str | None
    """Reference code of the signed informed refusal form."""
