"""Controller for mission details tab."""

# pylint: disable=E0611,I1101,R0903,R0912,R0915,C0301,C0302,R0911
# region imports
from typing import TYPE_CHECKING

from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QLineEdit,
    QPlainTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QWidget,
)
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.widgets.mission_details_tab as ui_mdt
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.models.mission_details_submodels.pupils_lungs_heart_model import (
    BreathingRhythm,
    HeartRhythm,
    HeartSound,
    LungSound,
    PupilStatus,
)
from hamyar_paygah.services.mission_details_service import get_mission_details
from hamyar_paygah.utils.date_utils import convert_gregorian_date_to_persian_date
from hamyar_paygah.utils.qt_utils import set_checkbox, set_enum_textfield, set_textfield
from hamyar_paygah.view_models.consumables_table_model import ConsumablesTableModel

if TYPE_CHECKING:
    import jdatetime  # type: ignore[import-untyped]

    from hamyar_paygah.models.mission_details_submodels.information_model import Information
    from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
        LocationAndEmergency,
    )
    from hamyar_paygah.models.mission_details_submodels.mission_result_model import MissionResult
    from hamyar_paygah.models.mission_details_submodels.times_and_distances_model import (
        TimesAndDistances,
    )
# endregion imports

# region constants
NOT_REGISTERED_PERSIAN_TEXT: str = "ثبت نشده"
"""Text to show when an information is not yet registered by EMS"""
IRREGULAR_PERSIAN_TEXT: str = "نامنظم"
"""Text to show when status is irregular"""
NORMAL_PERSIAN_TEXT: str = "طبیعی"
"""Text to show when status is normal"""
COLOR_WARNING = QColor("#FFF59D")  # soft yellow
"""Color to use for warning values that are approaching critical thresholds."""
COLOR_CRITICAL = QColor("#EF9A9A")  # soft red
"""Color to use for critical values that have exceeded safe thresholds."""

# ==============================
# Respiratory Rate (breaths/min)
# ==============================
RR_CRITICAL_LOW = 8
"""Respiratory rate less than or equal to this value is considered critical (adult baseline)."""
RR_WARNING_LOW = 11
"""Lower bound of warning range for respiratory rate (inclusive).
Values between RR_CRITICAL_LOW+1 and this value are considered warning."""
RR_NORMAL_HIGH = 20
"""Upper bound of normal range for respiratory rate (inclusive)."""
RR_WARNING_HIGH = 24
"""Upper bound of warning range for respiratory rate (inclusive)."""
RR_CRITICAL_HIGH = 25
"""Respiratory rate greater than or equal to this value is considered critical (adult baseline)."""
# ==============================
# Pulse Rate (beats per minute)
# ==============================
PULSE_CRITICAL_LOW = 50
"""Pulse rate strictly less than this value is considered critical (adult baseline)."""
PULSE_WARNING_LOW = 59
"""Lower bound of warning range for pulse rate (inclusive)."""
PULSE_NORMAL_HIGH = 100
"""Upper bound of normal range for pulse rate (inclusive)."""
PULSE_CRITICAL_HIGH = 120
"""Pulse rate strictly greater than this value is considered critical (adult baseline)."""
# ==============================
# Oxygen Saturation (SpO₂ %)
# ==============================
SPO2_CRITICAL = 90
"""Oxygen saturation strictly less than this value is considered critical."""
SPO2_WARNING_HIGH = 94
"""Upper bound of warning oxygen saturation range (inclusive)."""
# ==============================
# Blood Sugar (mg/dL)
# ==============================
BS_CRITICAL_LOW = 54
"""Blood sugar strictly less than this value is considered critical hypoglycemia."""
BS_WARNING_LOW = 69
"""Lower bound of warning hypoglycemia range (inclusive)."""
BS_NORMAL_HIGH = 140
"""Upper bound of normal glucose in blood"""
BS_CRITICAL_HIGH = 250
"""Blood sugar strictly greater than this value is considered critical hyperglycemia."""
# ==============================
# Blood Pressure (mmHg)
# ==============================
BP_WARNING_SYS = 140
"""Systolic blood pressure greater than or equal to this value enters warning range."""
BP_CRITICAL_SYS = 180
"""Systolic blood pressure greater than or equal to this value is considered critical."""
BP_WARNING_DIA = 90
"""Diastolic blood pressure greater than or equal to this value enters warning range."""
BP_CRITICAL_DIA = 120
"""Diastolic blood pressure greater than or equal to this value is considered critical."""
# ==============================
# Eye GCS
# ==============================
EYE_GCS_CRITICAL = 2
"""Eye GCS score less than or equal to this value is considered critical."""
EYE_GCS_WARNING = 3
"""Eye GCS score equal to this value is considered warning."""
EYE_GCS_NORMAL = 4
"""Eye GCS score equal to this value is considered normal."""
# ==============================
# Verbal GCS
# ==============================
VERBAL_GCS_CRITICAL = 3
"""Verbal GCS score less than or equal to this value is considered critical."""
VERBAL_GCS_WARNING = 4
"""Verbal GCS score equal to this value is considered warning."""
VERBAL_GCS_NORMAL = 5
"""Verbal GCS score equal to this value is considered normal."""
# ==============================
# Motor GCS
# ==============================
MOTOR_GCS_CRITICAL = 4
"""Motor GCS score less than or equal to this value is considered critical."""
MOTOR_GCS_WARNING = 5
"""Motor GCS score equal to this value is considered warning."""
MOTOR_GCS_NORMAL = 6
"""Motor GCS score equal to this value is considered normal."""
# ==============================
# Glasgow Coma Scale (GCS Total)
# ==============================
GCS_CRITICAL = 8
"""Total GCS less than or equal to this value is considered critical (severe impairment)."""
GCS_WARNING_LOW = 9
"""Lower bound of warning GCS range (inclusive)."""
GCS_WARNING_HIGH = 14
"""Upper bound of warning GCS range (inclusive). A score of 15 is considered normal."""
# endregion constants


class MissionsDetailsTab(QWidget):
    """Tab that enables user to retrieve details of a mission."""

    def __init__(self) -> None:
        """Initialize the mission details tab UI."""
        super().__init__()

        # Set up the UI
        self.ui = ui_mdt.Ui_mission_details_tab()  # type: ignore[attr-defined]
        self.ui.setupUi(self)

        # Set up vital signs table
        self._setup_vital_signs_table()
        # Set up drugs list table
        self._setup_drugs_list_table()

    @asyncSlot()  # type: ignore[misc]
    async def on_search_button_clicked(self) -> None:
        """Loads the mission details from server and populates the fields."""
        # Clear the current data
        self._clear_data()
        # Get mission details from server
        mission_details: MissionDetails = await get_mission_details(
            str(load_server_address()),
            int(self.ui.mission_id_line_edit.text()),
            int(self.ui.patient_id_line_edit.text()),
        )

        # Define a list of functions that populate tabs
        tab_populators = [
            self._populate_information_tab,
            self._populate_times_and_distances_tab,
            self._populate_location_and_emergency_tab,
            self._populate_symptoms_tab,
            self._populate_vital_signs_table,
            self._populate_medical_history_section,
            self._populate_pupils_lungs_heart_section,
            self._populate_trauma_types_section,
            self._populate_medical_actions_section,
            self._populate_drugs_list_table,
            self._populate_consumables_list_table,
            self._populate_medical_center_section,
        ]

        # Iterate through all of them
        for populator in tab_populators:
            populator(mission_details)

    def _clear_data(self) -> None:
        """Clears all the fields and checkboxes in the UI."""
        # Clear widgets used for data showing
        for line_edits in self.ui.mission_data_tab_widget.findChildren(QLineEdit):
            line_edits.clear()
            line_edits.setEnabled(True)

        for plain_text_edits in self.ui.mission_data_tab_widget.findChildren(QPlainTextEdit):
            plain_text_edits.clear()
            plain_text_edits.setEnabled(True)

        for text_edits in self.ui.mission_data_tab_widget.findChildren(QTextEdit):
            text_edits.clear()
            text_edits.setEnabled(True)

        for checkbox in self.ui.mission_data_tab_widget.findChildren(QCheckBox):
            checkbox.setChecked(False)
            # Set checkboxes to not react to mouse events
            checkbox.setAttribute(
                Qt.WA_TransparentForMouseEvents,  # type: ignore[attr-defined]
            )
            checkbox.setEnabled(True)

        for table_widget in self.ui.mission_data_tab_widget.findChildren(QTableWidget):
            table_widget.clearContents()
            table_widget.setEnabled(True)

    def _populate_information_tab(self, mission_details: MissionDetails) -> None:
        """Populates the information tab with data of the mission details model."""
        info: Information = mission_details.information
        result: MissionResult = mission_details.result

        # Text fields
        text_fields = [
            (self.ui.patient_name_field, info.patient_name),
            (self.ui.age_field, info.full_age),
            (self.ui.national_code_field, info.national_code),
            (self.ui.document_serial_number_field, info.document_serial_number),
            (self.ui.caller_number_field, info.caller_number),
            (self.ui.backup_number_field, info.backup_number),
            (self.ui.ambulance_code_field, info.ambulance_code),
            (self.ui.base_station_field, info.province),
            (self.ui.hospital_name_field, result.hospital_name),
            (self.ui.refusal_form_code_field, result.refusal_form_code),
            (self.ui.mission_summary_field, info.summary),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)

        # Checkboxes
        checkbox_fields = [
            (self.ui.iranian_nationality_checkBox, info.iranian_nationality),
            (self.ui.foreign_nationality_checkBox, info.foreign_nationality),
            (self.ui.is_male_checkBox, info.is_male_gender),
            (self.ui.is_female_checkBox, info.is_female_gender),
            (self.ui.is_gender_unknown_checkbox, info.is_unknown_gender),
        ]
        # Set all checkboxes
        for checkbox, value in checkbox_fields:
            set_checkbox(checkbox, value=value)

        # Special cases
        set_textfield(
            self.ui.last_update_field,
            str(
                convert_gregorian_date_to_persian_date(
                    info.document_request_time,
                ),
            ),
        )
        set_enum_textfield(self.ui.mission_result_field, result.result)

    def _populate_times_and_distances_tab(self, mission_details: MissionDetails) -> None:
        """Populates the times and distances tab with data from mission details model."""
        times: TimesAndDistances = mission_details.times_and_distances

        # Text fields
        text_fields = [
            (self.ui.first_staff_field, times.first_staff_code),
            (self.ui.second_staff_field, times.second_staff_code),
            (self.ui.senior_staff_field, times.senior_staff_code),
            (
                self.ui.depart_from_station_odo_field,
                times.depart_from_station_odometer,
            ),
            (
                self.ui.mission_received_field,
                times.mission_received_time,
            ),
            (
                self.ui.overall_mission_distance_field,
                times.overall_mission_distance,
            ),
            (
                self.ui.depart_from_station_time_field,
                times.depart_from_station_time,
            ),
            (self.ui.time_to_depart_field, times.time_to_depart),
            (
                self.ui.arrive_at_emergency_time_field,
                times.arrive_at_emergency_time,
            ),
            (self.ui.time_to_arrive_field, times.time_to_arrive),
            (
                self.ui.depart_from_emergency_time_field,
                times.depart_from_emergency_time,
            ),
            (
                self.ui.time_at_emergency_field,
                times.time_at_emergency_location,
            ),
            (
                self.ui.arrive_at_hospital_time_field,
                times.arrive_at_hospital_time,
            ),
            (self.ui.time_to_hospital_field, times.time_to_hospital),
            (
                self.ui.deliver_to_hospital_time_field,
                times.deliver_to_hospital_time,
            ),
            (self.ui.time_to_deliver_field, times.time_to_deliver),
            (
                self.ui.arrive_at_station_time_field,
                times.arrive_at_station_time,
            ),
            (
                self.ui.mission_complete_time_field,
                times.mission_complete_time,
            ),
            (self.ui.time_to_complete_field, times.time_to_complete),
            (
                self.ui.arrive_at_emergency_odo_field,
                times.arrive_at_emergency_odometer,
            ),
            (
                self.ui.arrive_at_hospital_odo_field,
                times.arrive_at_hospital_odometer,
            ),
            (
                self.ui.overall_mission_time_field,
                times.overall_mission_time,
            ),
            (
                self.ui.arrive_at_station_odo_field,
                times.arrive_at_station_odometer,
            ),
            (
                self.ui.mission_complete_odo_field,
                times.mission_complete_odometer,
            ),
            (self.ui.refuel_odo_field, times.vehicle_refuel_odometer),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)

        # Special cases
        jalali_mission_date: jdatetime.datetime | None = convert_gregorian_date_to_persian_date(
            mission_details.times_and_distances.mission_date,
        )
        if jalali_mission_date is not None:
            set_textfield(
                self.ui.mission_date_field,
                jalali_mission_date.date(),
            )

    def _populate_location_and_emergency_tab(self, mission_details: MissionDetails) -> None:
        """Populates the location and emergency tab with data from mission details model."""
        location: LocationAndEmergency = mission_details.location_and_emergency

        # Text fields
        text_fields = [
            (self.ui.address_plain_text_edit, location.address),
            (self.ui.chief_complaint_field, location.chief_complaint),
            (
                self.ui.type_of_location_other_info_field,
                location.location_other_info,
            ),
            (
                self.ui.emergency_other_info_field,
                location.emergency_type_other_info,
            ),
            (
                self.ui.role_in_accident_other_info_field,
                location.role_in_accident_other_info,
            ),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)

        # Checkboxes
        checkbox_fields = [
            (self.ui.is_vehicle_accident_checkBox, location.is_vehicle_accident),
        ]
        # Set all checkboxes
        for checkbox, check_value in checkbox_fields:
            set_checkbox(checkbox, value=check_value)

        # Enum text fields
        enum_text_fields = [
            (self.ui.type_of_location_field, location.location_type),
            (self.ui.accident_type_field, location.accident_type),
            (self.ui.illness_type_field, location.illness_type),
            (self.ui.role_in_accident_field, location.role_in_accident),
            (self.ui.vehicle_type_field, location.vehicle_type),
        ]
        # Set all enum text fields
        for enum_field, enum_value in enum_text_fields:
            set_enum_textfield(enum_field, enum_value)

    def _populate_symptoms_tab(self, mission_details: MissionDetails) -> None:
        """Populates the symptoms tab from mission details data."""
        symptoms = mission_details.symptoms

        # Checkboxes
        checkbox_fields = [
            (self.ui.has_abdominal_pain_checkbox, symptoms.has_abdominal_pain),
            (
                self.ui.has_altered_consciousness_checkbox,
                symptoms.has_altered_consciousness,
            ),
            (self.ui.has_bleeding_checkbox, symptoms.has_bleeding),
            (self.ui.has_blurred_vision_checkbox, symptoms.has_blurred_vision),
            (self.ui.has_chest_pain_checkbox, symptoms.has_chest_pain),
            (self.ui.has_diarrhea_checkbox, symptoms.has_diarrhea),
            (self.ui.has_dizziness_checkbox, symptoms.has_dizziness),
            (self.ui.has_double_vision_checkbox, symptoms.has_double_vision),
            (self.ui.has_fainting_checkbox, symptoms.has_fainting),
            (self.ui.has_fever_chills_checkbox, symptoms.has_fever_chills),
            (self.ui.has_headache_checkbox, symptoms.has_headache),
            (
                self.ui.has_memory_loss_post_trauma_checkbox,
                symptoms.has_memory_loss_post_trauma,
            ),
            (
                self.ui.has_sensory_motor_disturbance_checkbox,
                symptoms.has_sensory_motor_disturbance,
            ),
            (
                self.ui.has_shortness_of_breath_checkbox,
                symptoms.has_shortness_of_breath,
            ),
            (self.ui.has_sweating_checkbox, symptoms.has_sweating),
            (self.ui.has_vomiting_checkbox, symptoms.has_vomiting),
            (self.ui.has_weakness_checkBox, symptoms.has_weakness),
        ]
        # Set all checkboxes
        for checkbox, check_value in checkbox_fields:
            set_checkbox(checkbox, value=check_value)

        # Set text field
        set_textfield(self.ui.other_symptoms_field, symptoms.other_symptoms)

    def _setup_vital_signs_table(self) -> None:
        # Get the vital signs table widget
        vital_signs_table = self.ui.vital_signs_table_Widget

        # Set row labels
        row_labels = [
            "زمان ثبت",
            "تعداد تنفس (در دقیقه)",
            "تعداد ضربان قلب (در دقیقه)",
            "فشار خون (دیاستولیک/سیستولیک)",
            "قند خون (میلی‌گرم بر دسی‌لیتر)",
            "اشباع اکسیژن خون (%)",
            "GCS چشمی",
            "GCS کلامی",
            "GCS حرکتی",
            "GCS کل",
        ]
        # Set the number of rows based on the number of vital sign attributes
        vital_signs_table.setRowCount(len(row_labels))
        # Set the vertical header labels to the attribute names
        vital_signs_table.setVerticalHeaderLabels(row_labels)

    def _classify_vital_sign(self, row: int, value: int | str | None) -> str:  # noqa: C901, PLR0911, PLR0912
        """Classifies a vital sign value into normal, warning, or critical state.

        The classification is based on predefined adult physiological thresholds.
        The `row` parameter determines which vital sign is being evaluated,
        following the fixed row index mapping of the vital signs table.

        Row index mapping:
            1: Respiratory rate
            2: Pulse rate
            3: Blood pressure (systolic/diastolic string format, e.g. "120/80")
            4: Blood sugar
            5: Oxygen saturation (SpO₂)
            6: Eye GCS
            7: Verbal GCS
            8: Motor GCS
            9: Total Glasgow Coma Scale (GCS)

        All other rows default to "normal".

        Thresholds are heuristic adult baseline values and may not apply to
        pediatric patients or specific clinical contexts.

        Args:
            row (int):
                The row index corresponding to the vital sign type.
            value (int | str | None):
                The measured value. Blood pressure must be provided as a
                "systolic/diastolic" string. Other numeric values may be
                provided as int or numeric string. If None, the value is
                treated as normal.

        Returns:
            str:
                One of:
                    - "normal": Value within acceptable physiological range.
                    - "warning": Value moderately outside normal range.
                    - "critical": Value significantly outside normal range.
        """
        # If input is empty, return normal (we only classify registered values,
        # unregistered values are not classified)
        if value is None:
            return "normal"

        try:
            if row == 1:  # Respiratory rate
                # Get respiratory rate
                respiratory_rate = int(value)
                # Check critical range
                if respiratory_rate <= RR_CRITICAL_LOW or respiratory_rate >= RR_CRITICAL_HIGH:
                    return "critical"
                if (
                    RR_CRITICAL_LOW < respiratory_rate <= RR_WARNING_LOW
                    or RR_NORMAL_HIGH < respiratory_rate <= RR_WARNING_HIGH
                ):
                    return "warning"

            elif row == 2:  # Pulse  # noqa: PLR2004
                pulse = int(value)
                if pulse <= PULSE_CRITICAL_LOW or pulse > PULSE_CRITICAL_HIGH:
                    return "critical"
                if (
                    PULSE_CRITICAL_LOW < pulse <= PULSE_WARNING_LOW
                    or PULSE_NORMAL_HIGH < pulse <= PULSE_CRITICAL_HIGH
                ):
                    return "warning"

            elif row == 3:  # Blood pressure  # noqa: PLR2004
                systolic, diastolic = map(
                    int,
                    value.split("/"),  # type: ignore[union-attr]
                )
                if systolic >= BP_CRITICAL_SYS or diastolic >= BP_CRITICAL_DIA:
                    return "critical"
                if systolic >= BP_WARNING_SYS or diastolic >= BP_WARNING_DIA:
                    return "warning"

            elif row == 4:  # Blood sugar  # noqa: PLR2004
                blood_sugar = int(value)
                if blood_sugar < BS_CRITICAL_LOW or blood_sugar > BS_CRITICAL_HIGH:
                    return "critical"
                if (
                    BS_CRITICAL_LOW <= blood_sugar <= BS_WARNING_LOW
                    or BS_NORMAL_HIGH < blood_sugar <= BS_CRITICAL_HIGH
                ):
                    return "warning"

            elif row == 5:  # SpO2  # noqa: PLR2004
                spo2 = int(value)
                if spo2 < SPO2_CRITICAL:
                    return "critical"
                if SPO2_CRITICAL <= spo2 <= SPO2_WARNING_HIGH:
                    return "warning"

            elif row == 6:  # Eye GCS # noqa: PLR2004
                eye_gcs = int(value)
                if eye_gcs <= EYE_GCS_CRITICAL:
                    return "critical"
                if EYE_GCS_CRITICAL < eye_gcs <= EYE_GCS_WARNING:
                    return "warning"

            elif row == 7:  # Verbal GCS  # noqa: PLR2004
                verbal_gcs = int(value)
                if verbal_gcs <= VERBAL_GCS_CRITICAL:
                    return "critical"
                if VERBAL_GCS_CRITICAL < verbal_gcs <= VERBAL_GCS_WARNING:
                    return "warning"

            elif row == 8:  # Motor GCS  # noqa: PLR2004
                motor_gcs = int(value)
                if motor_gcs <= MOTOR_GCS_CRITICAL:
                    return "critical"
                if MOTOR_GCS_CRITICAL < motor_gcs <= MOTOR_GCS_WARNING:
                    return "warning"

            elif row == 9:  # GCS total  # noqa: PLR2004
                gcs_total = int(value)
                if gcs_total <= GCS_CRITICAL:
                    return "critical"
                if GCS_WARNING_LOW <= gcs_total <= GCS_WARNING_HIGH:
                    return "warning"

        except Exception:  # noqa: BLE001 # pylint: disable=broad-except
            return "normal"

        return "normal"

    def _populate_vital_signs_table(self, mission_details: MissionDetails) -> None:
        """Populates the vital signs table from mission details data."""
        # If the list of vital signs is empty, we do not populate the table
        if not mission_details.vital_signs:
            return

        # Get the table
        vital_signs_table = self.ui.vital_signs_table_Widget

        # Set the number of columns based on the number of vital signs records
        vital_signs_table.setColumnCount(len(mission_details.vital_signs))

        # Iterate through columns and set the data for each vital sign record
        for column, vital_sign in enumerate(mission_details.vital_signs):
            # Get the vital signs attribute values in the order of the row labels
            values = [
                vital_sign.record_time or NOT_REGISTERED_PERSIAN_TEXT,
                vital_sign.respiratory_rate,
                vital_sign.pulse_rate,
                vital_sign.blood_pressure,
                vital_sign.blood_sugar,
                vital_sign.oxygen_saturation,
                vital_sign.gcs_eye,
                vital_sign.gcs_verbal,
                vital_sign.gcs_motor,
                vital_sign.gcs_total,
            ]

            # Iterate through rows and set the value for each vital sign attribute
            for row, value in enumerate(values):
                item = QTableWidgetItem(
                    NOT_REGISTERED_PERSIAN_TEXT
                    if value is None
                    else str(
                        value,
                    ),
                )
                # Set background color
                state = self._classify_vital_sign(
                    row,
                    value,  # type: ignore[arg-type]
                )
                if state == "warning":
                    item.setBackground(COLOR_WARNING)
                elif state == "critical":
                    item.setBackground(COLOR_CRITICAL)

                # Set center align
                item.setTextAlignment(
                    Qt.AlignCenter,  # type: ignore[attr-defined]
                )
                # Add item to table
                vital_signs_table.setItem(row, column, item)

        # Resize to content
        vital_signs_table.resizeColumnsToContents()

    def _populate_medical_history_section(self, mission_details: MissionDetails) -> None:
        """Populates the medical history section by data of mission details."""
        history = mission_details.medical_history

        # Text fields
        text_fields = [
            (self.ui.drug_allergies_field, history.drug_allergies),
            (
                self.ui.current_medications_field,
                history.current_medications,
            ),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)

        # Checkboxes
        checkbox_fields = [
            (
                self.ui.has_cardiac_disease_checkBox,
                history.has_cardiac_disease,
            ),
            (self.ui.has_hypertension_checkBox, history.has_hypertension),
            (
                self.ui.has_substance_abuse_checkBox,
                history.has_substance_abuse,
            ),
            (self.ui.has_disability_checkBox, history.has_disability),
            (self.ui.has_asthma_checkBox, history.has_asthma),
            (
                self.ui.has_stroke_history_checkBox,
                history.has_stroke_history,
            ),
            (
                self.ui.has_psychiatric_disorder_checkBox,
                history.has_psychiatric_disorder,
            ),
            (self.ui.has_prior_trauma_checkBox, history.has_prior_trauma),
            (
                self.ui.has_surgical_history_checkBox,
                history.has_surgical_history,
            ),
            (
                self.ui.has_gastrointestinal_disease_checkBox,
                history.has_gastrointestinal_disease,
            ),
            (
                self.ui.has_renal_disease_checkBox,
                history.has_renal_disease,
            ),
            (
                self.ui.has_seizure_disorder_checkBox,
                history.has_seizure_disorder,
            ),
            (
                self.ui.has_infectious_disease_checkBox,
                history.has_infectious_disease,
            ),
            (self.ui.has_diabetes_checkBox, history.has_diabetes),
            (
                self.ui.has_malignancy_history_checkBox,
                history.has_malignancy_history,
            ),
            (
                self.ui.has_special_conditions_checkBox,
                history.has_special_conditions,
            ),
            (
                self.ui.has_pulmonary_disease_checkBox,
                history.has_pulmonary_disease,
            ),
            (
                self.ui.other_medical_history_checkBox,
                history.has_other_medical_history,
            ),
        ]
        # Set all checkboxes
        for checkbox, check_value in checkbox_fields:
            set_checkbox(checkbox, value=check_value)

    def _populate_pupils_lungs_heart_section(self, mission_details: MissionDetails) -> None:  # noqa: C901, PLR0912, PLR0915
        """Populates the pupils, lungs and heart section by data of mission details."""
        # Set right pupil status
        if mission_details.pupils_lungs_heart.pupils.right is not None:
            right_pupil_status = mission_details.pupils_lungs_heart.pupils.right
            if right_pupil_status == PupilStatus.NORMAL:
                self.ui.right_eye_examine_field.setText(NORMAL_PERSIAN_TEXT)
            elif right_pupil_status == PupilStatus.DILATED:
                self.ui.right_eye_examine_field.setText("گشاد شده")
            elif right_pupil_status == PupilStatus.MIOTIC:
                self.ui.right_eye_examine_field.setText("منقبض شده")
            elif right_pupil_status == PupilStatus.NO_RESPONSE:
                self.ui.right_eye_examine_field.setText("بدون پاسخ به نور")
        else:
            self.ui.right_eye_examine_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )
            self.ui.right_eye_examine_field.setEnabled(False)

        # Set left pupil status
        if mission_details.pupils_lungs_heart.pupils.left is not None:
            left_pupil_status = mission_details.pupils_lungs_heart.pupils.left
            if left_pupil_status == PupilStatus.NORMAL:
                self.ui.left_eye_examine_field.setText(NORMAL_PERSIAN_TEXT)
            elif left_pupil_status == PupilStatus.DILATED:
                self.ui.left_eye_examine_field.setText("گشاد شده")
            elif left_pupil_status == PupilStatus.MIOTIC:
                self.ui.left_eye_examine_field.setText("منقبض شده")
            elif left_pupil_status == PupilStatus.NO_RESPONSE:
                self.ui.left_eye_examine_field.setText("بدون پاسخ به نور")
        else:
            self.ui.left_eye_examine_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.left_eye_examine_field.setEnabled(False)

        # Set lung sounds
        # Right Lung
        if mission_details.pupils_lungs_heart.lungs.right.sound is not None:
            right_lung_sound = mission_details.pupils_lungs_heart.lungs.right.sound
            if right_lung_sound == LungSound.NORMAL:
                self.ui.right_lung_sound_field.setText(NORMAL_PERSIAN_TEXT)
            elif right_lung_sound == LungSound.RALES:
                self.ui.right_lung_sound_field.setText("رال")
            elif right_lung_sound == LungSound.WHEEZE:
                self.ui.right_lung_sound_field.setText("ویز")
        else:
            self.ui.right_lung_sound_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.right_lung_sound_field.setEnabled(False)
        # Left Lung
        if mission_details.pupils_lungs_heart.lungs.left.sound is not None:
            left_lung_sound = mission_details.pupils_lungs_heart.lungs.left.sound
            if left_lung_sound == LungSound.NORMAL:
                self.ui.left_lung_sound_field.setText(NORMAL_PERSIAN_TEXT)
            elif left_lung_sound == LungSound.RALES:
                self.ui.left_lung_sound_field.setText("رال")
            elif left_lung_sound == LungSound.WHEEZE:
                self.ui.left_lung_sound_field.setText("ویز")
        else:
            self.ui.left_lung_sound_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.left_lung_sound_field.setEnabled(False)

        # Set breathing rhythm
        # Right Lung
        if mission_details.pupils_lungs_heart.lungs.right.rhythm is not None:
            breathing_rhythm = mission_details.pupils_lungs_heart.lungs.right.rhythm
            if breathing_rhythm == BreathingRhythm.REGULAR:
                self.ui.right_lung_rhythm_field.setText("منظم")
            elif breathing_rhythm == BreathingRhythm.IRREGULAR:
                self.ui.right_lung_rhythm_field.setText(IRREGULAR_PERSIAN_TEXT)
        else:
            self.ui.right_lung_rhythm_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )
            self.ui.right_lung_rhythm_field.setEnabled(False)
        # Left Lung
        if mission_details.pupils_lungs_heart.lungs.left.rhythm is not None:
            breathing_rhythm = mission_details.pupils_lungs_heart.lungs.left.rhythm
            if breathing_rhythm == BreathingRhythm.REGULAR:
                self.ui.left_lung_rhythm_field.setText("منظم")
            elif breathing_rhythm == BreathingRhythm.IRREGULAR:
                self.ui.left_lung_rhythm_field.setText(IRREGULAR_PERSIAN_TEXT)
        else:
            self.ui.left_lung_rhythm_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.left_lung_rhythm_field.setEnabled(False)

        # Set heart sound
        if mission_details.pupils_lungs_heart.heart.sound is not None:
            heart_sound = mission_details.pupils_lungs_heart.heart.sound
            if heart_sound == HeartSound.NORMAL:
                self.ui.heart_sound_field.setText(NORMAL_PERSIAN_TEXT)
            elif heart_sound == HeartSound.ABNORMAL:
                self.ui.heart_sound_field.setText("صدای اضافی")
        else:
            self.ui.heart_sound_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.heart_sound_field.setEnabled(False)

        # Set heart rhythm
        if mission_details.pupils_lungs_heart.heart.rhythm is not None:
            heart_rhythm = mission_details.pupils_lungs_heart.heart.rhythm
            if heart_rhythm == HeartRhythm.REGULAR:
                self.ui.heart_rhythm_field.setText("منظم")
            elif heart_rhythm == HeartRhythm.IRREGULAR:
                self.ui.heart_rhythm_field.setText(IRREGULAR_PERSIAN_TEXT)
        else:
            self.ui.heart_rhythm_field.setText(NOT_REGISTERED_PERSIAN_TEXT)
            self.ui.heart_rhythm_field.setEnabled(False)

    def _populate_trauma_types_section(self, mission_details: MissionDetails) -> None:
        """Populates the trauma types section by data of mission details."""
        trauma = mission_details.trauma_types

        # Text fields
        text_fields = [
            (self.ui.burn_type_field, trauma.burn_type),
            (self.ui.burn_percentage_field, trauma.burn_percentage),
            (self.ui.front_trauma_locations_field, trauma.front_trauma_locations),
            (self.ui.rear_trauma_locations_field, trauma.rear_trauma_locations),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)

        # Checkboxes
        checkbox_fields = [
            (self.ui.has_deformity_checkBox, trauma.has_deformity),
            (self.ui.has_abrasion_checkBox, trauma.has_abrasion),
            (self.ui.has_tenderness_checkBox, trauma.has_tenderness),
            (self.ui.has_crush_injury_checkBox, trauma.has_crush_injury),
            (self.ui.has_swelling_checkBox, trauma.has_swelling),
            (self.ui.has_dislocation_checkBox, trauma.has_dislocation),
            (self.ui.has_contusion_checkBox, trauma.has_contusion),
            (self.ui.has_puncture_wound_checkBox, trauma.has_puncture_wound),
            (self.ui.has_laceration_checkBox, trauma.has_laceration),
            (self.ui.has_tear_checkBox, trauma.has_tear),
            (self.ui.has_amputation_checkBox, trauma.has_amputation),
            (self.ui.has_external_bleeding_checkBox, trauma.has_external_bleeding),
            (self.ui.has_sensory_deficit_checkBox, trauma.has_sensory_deficit),
            (self.ui.has_motor_deficit_checkBox, trauma.has_motor_deficit),
            (self.ui.penetrating_trauma_checkBox, trauma.has_penetrating_trauma),
            (self.ui.blunt_trauma_checkBox, trauma.has_blunt_trauma),
        ]
        # Set all checkboxes
        for checkbox, check_value in checkbox_fields:
            set_checkbox(checkbox, value=check_value)

        # Enum text fields
        enum_text_fields = [
            (self.ui.patient_extraction_field, trauma.patient_extraction),
            (self.ui.type_of_fracture_field, trauma.fracture_type),
            (self.ui.distal_pulse_field, trauma.distal_pulse_status),
        ]
        # Set all enum text fields
        for enum_field, enum_value in enum_text_fields:
            set_enum_textfield(enum_field, enum_value)

    def _populate_medical_actions_section(self, mission_details: MissionDetails) -> None:
        """Populates the medical actions section by data of mission details."""
        actions = mission_details.medical_actions

        # Checkboxes
        checkbox_fields = [
            (self.ui.suction_action_before_checkBox, actions.suction.before_ems),
            (self.ui.cpr_action_before_checkBox, actions.cpr.before_ems),
            (self.ui.dressing_action_before_checkBox, actions.dressing.before_ems),
            (
                self.ui.airway_tube_action_before_checkBox,
                actions.airway_tube.before_ems,
            ),
            (
                self.ui.cardiac_massage_action_before_checkBox,
                actions.cardiac_massage.before_ems,
            ),
            (
                self.ui.assisted_ventilation_action_before_checkBox,
                actions.assisted_ventilation.before_ems,
            ),
            (
                self.ui.vital_sign_action_before_checkBox,
                actions.vital_signs.before_ems,
            ),
            (
                self.ui.consultation_action_before_checkBox,
                actions.consultation.before_ems,
            ),
            (self.ui.biography_action_before_checkBox, actions.biography.before_ems),
            (
                self.ui.monitoring_action_before_checkBox,
                actions.monitoring.before_ems,
            ),
            (self.ui.iv_action_before_checkBox, actions.iv_access.before_ems),
            (
                self.ui.oxygen_action_before_checkBox,
                actions.oxygen_therapy.before_ems,
            ),
            (self.ui.cbr_action_before_checkBox, actions.cbr.before_ems),
            (
                self.ui.head_fix_action_before_checkBox,
                actions.head_immobilization.before_ems,
            ),
            (
                self.ui.limb_fix_action_before_checkBox,
                actions.limb_immobilization.before_ems,
            ),
            (
                self.ui.spinal_fix_action_before_checkBox,
                actions.spinal_immobilization.before_ems,
            ),
        ]
        # Set all checkboxes
        for checkbox, check_value in checkbox_fields:
            set_checkbox(checkbox, value=check_value)

    def _setup_drugs_list_table(self) -> None:
        """Setups the drugs list table with appropriate row labels and initial configuration."""
        # Get the drugs list table widget
        drugs_list_table = self.ui.drugs_list_table_widget

        # Set row labels
        row_labels = [
            "نام",
            "دوز",
            "روش تجویز",
            "زمان تجویز",
        ]
        # Set the number of rows based on the number of drugs list attributes
        drugs_list_table.setRowCount(len(row_labels))
        # Set the vertical header labels to the attribute names
        drugs_list_table.setVerticalHeaderLabels(row_labels)

    def _populate_drugs_list_table(self, mission_details: MissionDetails) -> None:
        """Populates the drugs list table from mission details data."""
        # If the list of drugs list is empty, we do not populate the table
        if not mission_details.drugs:
            return

        # Get the table
        drugs_table = self.ui.drugs_list_table_widget

        # Set the number of columns based on the number of drugs records
        drugs_table.setColumnCount(len(mission_details.drugs))

        # Iterate through the columns and set the date for each drug record
        for column, drug in enumerate(mission_details.drugs):
            # Get the drug attribute values in the order of the row labels
            values = [
                drug.name or NOT_REGISTERED_PERSIAN_TEXT,
                drug.dose or NOT_REGISTERED_PERSIAN_TEXT,
                drug.route or NOT_REGISTERED_PERSIAN_TEXT,
                drug.time or NOT_REGISTERED_PERSIAN_TEXT,
            ]

            # Iterate through rows and set the value for each drug attribute
            for row, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                # Set center align
                item.setTextAlignment(
                    Qt.AlignCenter,  # type: ignore[attr-defined]
                )
                # Add item to table
                drugs_table.setItem(row, column, item)

        # Resize to content
        drugs_table.resizeColumnsToContents()

    def _populate_consumables_list_table(self, mission_details: MissionDetails) -> None:
        """Populates the consumables list table from mission details data."""
        # If the list of consumables list is empty, we do not populate the table
        if not mission_details.consumables:
            return

        # Create the model for table view
        source_model = ConsumablesTableModel(mission_details.consumables.items)

        # Proxy the model to enable sorting and filtering
        proxy_model = QSortFilterProxyModel(self)
        proxy_model.setSourceModel(source_model)
        # Set proxy model to be case insensitive
        proxy_model.setSortCaseSensitivity(
            Qt.CaseInsensitive,  # type: ignore[attr-defined]
        )
        # Set proxy model to be local aware for sorting
        proxy_model.setSortLocaleAware(True)

        # Set the model to table
        self.ui.consumable_list_table_view.setModel(proxy_model)

        # Resize columns to content
        self.ui.consumable_list_table_view.resizeColumnsToContents()

    def _populate_medical_center_section(self, mission_details: MissionDetails) -> None:
        """Populates the medical center section by data of mission details."""
        center = mission_details.medical_center

        # Text fields
        text_fields = [
            (
                self.ui.receiving_physician_code_field,
                center.receiving_physician_code,
            ),
            (self.ui.physician_code_field, center.physician_code),
            (
                self.ui.physician_code_1050_field,
                center.physician_1050_code,
            ),
            (self.ui.physician_order_field, center.physician_order),
            (
                self.ui.physician_order_secondary_field,
                center.physician_order_secondary,
            ),
            (
                self.ui.receiving_physician_name_field,
                center.receiving_physician_name,
            ),
            (self.ui.handover_time_field, center.handover_datetime),
        ]
        # Set all text fields
        for field, value in text_fields:
            set_textfield(field, value)
