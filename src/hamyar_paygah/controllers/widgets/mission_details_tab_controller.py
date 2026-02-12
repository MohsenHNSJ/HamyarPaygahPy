"""Controller for mission details tab."""

# pylint: disable=E0611,I1101,R0903,R0912,R0915
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt
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
from hamyar_paygah.services.mission_details_service import get_mission_details
from hamyar_paygah.utils.date_utils import convert_gregorian_date_to_persian_date

if TYPE_CHECKING:
    import jdatetime  # type: ignore[import-untyped]

NOT_PROVIDED_PERSIAN_TEXT: str = "ارائه نشده"
"""Text to show when an information is not provided to EMS"""
NOT_REGISTERED_PERSIAN_TEXT: str = "ثبت نشده"
"""Text to show when an information is not yet registered by EMS"""


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

    @asyncSlot()  # type: ignore[untyped-decorator,misc]
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

        # Populate information tab
        self._populate_information_tab(mission_details)

        # Populate times and distances tab
        self._populate_times_and_distances_tab(mission_details)

        # Populate location and emergency type tab
        self._populate_location_and_emergency_tab(mission_details)

        # Populate symptoms tab
        self._populate_symptoms_tab(mission_details)

        # Populate vital sings table
        self._populate_vital_signs_table(mission_details)

    def _clear_data(self) -> None:
        """Clears all the fields and checkboxes in the UI."""
        # Clear widgets used for data showing
        for line_edits in self.ui.mission_data_tab_widget.findChildren(QLineEdit):
            line_edits.clear()

        for plain_text_edits in self.ui.mission_data_tab_widget.findChildren(QPlainTextEdit):
            plain_text_edits.clear()

        for text_edits in self.ui.mission_data_tab_widget.findChildren(QTextEdit):
            text_edits.clear()

        for checkbox in self.ui.mission_data_tab_widget.findChildren(QCheckBox):
            checkbox.setChecked(False)
            # Set checkboxes to not react to mouse events
            checkbox.setAttribute(
                Qt.WA_TransparentForMouseEvents,  # type: ignore[attr-defined]
            )

        for table_widget in self.ui.mission_data_tab_widget.findChildren(QTableWidget):
            table_widget.clearContents()

    def _populate_information_tab(self, mission_details: MissionDetails) -> None:
        """Populates the information tab with data of the mission details model."""
        # Populate the name field
        self.ui.patient_name_field.setText(
            mission_details.information.patient_name,
        )

        # Populate age field
        self.ui.age_field.setText(mission_details.information.full_age)

        # Set nationality checkbox
        if mission_details.information.iranian_nationality:
            self.ui.iranian_nationality_checkBox.setChecked(True)
        else:
            self.ui.foreign_nationality_checkBox.setChecked(True)

        # Set gender checkbox
        if mission_details.information.is_male_gender:
            self.ui.is_male_checkBox.setChecked(True)
        elif mission_details.information.is_female_gender:
            self.ui.is_female_checkBox.setChecked(True)
        elif mission_details.information.is_unknown_gender:
            self.ui.is_gender_unknown_checkbox.setChecked(True)

        # Set national code field
        if mission_details.information.national_code != 0:
            self.ui.national_code_field.setText(
                str(mission_details.information.national_code),
            )
        else:
            self.ui.national_code_field.setText(NOT_PROVIDED_PERSIAN_TEXT)

        # Set document serial number field
        self.ui.document_serial_number_field.setText(
            mission_details.information.document_serial_number,
        )

        # Set caller number field
        if mission_details.information.caller_number is not None:
            self.ui.caller_number_field.setText(
                mission_details.information.caller_number,
            )
        else:
            self.ui.caller_number_field.setText(NOT_PROVIDED_PERSIAN_TEXT)

        # Set backup number field
        if mission_details.information.backup_number is not None:
            self.ui.backup_number_field.setText(
                mission_details.information.backup_number,
            )
        else:
            self.ui.backup_number_field.setText(NOT_PROVIDED_PERSIAN_TEXT)

        # Set ambulance code field
        self.ui.ambulance_code_field.setText(
            str(mission_details.information.ambulance_code),
        )

        # Set document request time field
        self.ui.last_update_field.setText(
            str(
                convert_gregorian_date_to_persian_date(
                    mission_details.information.document_request_time,
                ),
            ),
        )

        # Set province field
        self.ui.base_station_field.setText(
            mission_details.information.province,
        )

        # Set summary field
        self.ui.mission_summary_field.setPlainText(
            str(mission_details.information.summary),
        )

    def _populate_times_and_distances_tab(self, mission_details: MissionDetails) -> None:  # noqa: PLR0912, PLR0915
        """Populates the times and distances tab with data from mission details model."""
        # Set first staff field
        self.ui.first_staff_field.setText(
            str(mission_details.times_and_distances.first_staff_code),
        )

        # Set mission date field
        jalali_mission_date: jdatetime.datetime | None = convert_gregorian_date_to_persian_date(
            mission_details.times_and_distances.mission_date,
        )
        if jalali_mission_date is not None:
            self.ui.mission_date_field.setText(
                str(jalali_mission_date.date()),
            )

        # Set second staff field
        if mission_details.times_and_distances.second_staff_code != 0:
            self.ui.second_staff_field.setText(
                str(mission_details.times_and_distances.second_staff_code),
            )
        else:
            self.ui.second_staff_field.setText("بدون پرسنل دوم")

        # Set senior staff field
        self.ui.senior_staff_field.setText(
            str(mission_details.times_and_distances.senior_staff_code),
        )

        # Set depart from station ODO
        self.ui.depart_from_station_odo_field.setText(
            str(mission_details.times_and_distances.depart_from_station_odometer),
        )

        # Set mission received time
        self.ui.mission_received_field.setText(
            str(mission_details.times_and_distances.mission_received_time),
        )

        # Set overall mission distance
        self.ui.overall_mission_distance_field.setText(
            str(mission_details.times_and_distances.overall_mission_distance),
        )

        # Set depart from station time
        self.ui.depart_from_station_time_field.setText(
            str(mission_details.times_and_distances.depart_from_station_time),
        )

        # Set time to depart
        self.ui.time_to_depart_field.setText(
            str(mission_details.times_and_distances.time_to_depart),
        )

        # Set arrive at emergency time
        self.ui.arrive_at_emergency_time_field.setText(
            str(mission_details.times_and_distances.arrive_at_emergency_time),
        )

        # Set time to arrive
        self.ui.time_to_arrive_field.setText(
            str(mission_details.times_and_distances.time_to_arrive),
        )

        # Set depart from emergency time
        self.ui.depart_from_emergency_time_field.setText(
            str(mission_details.times_and_distances.depart_from_emergency_time),
        )

        # Set time at emergency
        self.ui.time_at_emergency_field.setText(
            str(mission_details.times_and_distances.time_at_emergency_location),
        )

        # Set arrive at hospital time
        if mission_details.times_and_distances.arrive_at_hospital_time is not None:
            self.ui.arrive_at_hospital_time_field.setText(
                str(mission_details.times_and_distances.arrive_at_hospital_time),
            )
        else:
            self.ui.arrive_at_hospital_time_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )

        # Set time to hospital
        if mission_details.times_and_distances.time_to_hospital is not None:
            self.ui.time_to_hospital_field.setText(
                str(mission_details.times_and_distances.time_to_hospital),
            )
        else:
            self.ui.time_to_hospital_field.setText(NOT_REGISTERED_PERSIAN_TEXT)

        # Set deliver to hospital time
        if mission_details.times_and_distances.deliver_to_hospital_time is not None:
            self.ui.deliver_to_hospital_time_field.setText(
                str(mission_details.times_and_distances.deliver_to_hospital_time),
            )
        else:
            self.ui.deliver_to_hospital_time_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )

        # Set time to deliver
        if mission_details.times_and_distances.time_to_deliver is not None:
            self.ui.time_to_deliver_field.setText(
                str(mission_details.times_and_distances.time_to_deliver),
            )
        else:
            self.ui.time_to_deliver_field.setText(NOT_REGISTERED_PERSIAN_TEXT)

        # Set arrive at station time
        self.ui.arrive_at_station_time_field.setText(
            str(mission_details.times_and_distances.arrive_at_station_time),
        )

        # Set mission complete time
        self.ui.mission_complete_time_field.setText(
            str(mission_details.times_and_distances.mission_complete_time),
        )

        # Set time to complete
        self.ui.time_to_complete_field.setText(
            str(mission_details.times_and_distances.time_to_complete),
        )

        # Set arrive at emergency ODO
        if mission_details.times_and_distances.arrive_at_emergency_odometer != 0:
            self.ui.arrive_at_emergency_odo_field.setText(
                str(mission_details.times_and_distances.arrive_at_emergency_odometer),
            )
        else:
            self.ui.arrive_at_emergency_odo_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )

        # Set arrive at hospital ODO
        if mission_details.times_and_distances.arrive_at_hospital_odometer != 0:
            self.ui.arrive_at_hospital_odo_field.setText(
                str(mission_details.times_and_distances.arrive_at_hospital_odometer),
            )
        else:
            self.ui.arrive_at_hospital_odo_field.setText(
                NOT_REGISTERED_PERSIAN_TEXT,
            )

        # Set overall mission time
        self.ui.overall_mission_time_field.setText(
            str(mission_details.times_and_distances.overall_mission_time),
        )

        # Set arrive at station ODO
        self.ui.arrive_at_station_odo_field.setText(
            str(mission_details.times_and_distances.arrive_at_station_odometer),
        )

        # Set mission complete ODO
        self.ui.mission_complete_odo_field.setText(
            str(mission_details.times_and_distances.mission_complete_odometer),
        )

        # Set refuel ODO
        if mission_details.times_and_distances.vehicle_refuel_odometer != 0:
            self.ui.refuel_odo_field.setText(
                str(mission_details.times_and_distances.vehicle_refuel_odometer),
            )
        else:
            self.ui.refuel_odo_field.setText("سوختگیری انجام نشده")

    def _populate_location_and_emergency_tab(self, mission_details: MissionDetails) -> None:
        """Populates the location and emergency tab with data from mission details model."""
        # Set address field
        self.ui.address_plain_text_edit.setPlainText(
            str(mission_details.location_and_emergency.address),
        )

        # Set chief complaint
        self.ui.chief_complaint_field.setText(
            str(mission_details.location_and_emergency.chief_complaint),
        )

        # Set type of location
        if mission_details.location_and_emergency.location_type is not None:
            self.ui.type_of_location_field.setText(
                mission_details.location_and_emergency.location_type.persian_label,
            )

        # Set type of location other info
        self.ui.type_of_location_other_info_field.setText(
            mission_details.location_and_emergency.location_other_info,
        )

        # Set accident type
        if mission_details.location_and_emergency.accident_type is not None:
            self.ui.accident_type_field.setText(
                mission_details.location_and_emergency.accident_type.persian_label,
            )

        # Set illness type
        if mission_details.location_and_emergency.illness_type is not None:
            self.ui.illness_type_field.setText(
                mission_details.location_and_emergency.illness_type.persian_label,
            )

        # Set emergency type other info
        self.ui.emergency_other_info_field.setText(
            mission_details.location_and_emergency.emergency_type_other_info,
        )

        # Set vehicle accident
        self.ui.is_vehicle_accident_checkBox.setChecked(
            mission_details.location_and_emergency.is_vehicle_accident,
        )

        # Set role in accident
        if mission_details.location_and_emergency.role_in_accident is not None:
            self.ui.role_in_accident_field.setText(
                mission_details.location_and_emergency.role_in_accident.persian_label,
            )

        # Set role in accident other info
        self.ui.role_in_accident_other_info_field.setText(
            mission_details.location_and_emergency.role_in_accident_other_info,
        )

        # Set vehicle type
        if mission_details.location_and_emergency.vehicle_type is not None:
            self.ui.vehicle_type_field.setText(
                mission_details.location_and_emergency.vehicle_type.persian_label,
            )

    def _populate_symptoms_tab(self, mission_details: MissionDetails) -> None:
        """Populates the symptoms tab from mission details data."""
        # Set abdominal pain
        self.ui.has_abdominal_pain_checkbox.setChecked(
            mission_details.symptoms.has_abdominal_pain,
        )

        # Set altered consciousness
        self.ui.has_altered_consciousness_checkbox.setChecked(
            mission_details.symptoms.has_altered_consciousness,
        )

        # Set bleeding
        self.ui.has_bleeding_checkbox.setChecked(
            mission_details.symptoms.has_bleeding,
        )

        # Set blurred vision
        self.ui.has_blurred_vision_checkbox.setChecked(
            mission_details.symptoms.has_blurred_vision,
        )

        # Set chest pain
        self.ui.has_chest_pain_checkbox.setChecked(
            mission_details.symptoms.has_chest_pain,
        )

        # Set diarrhea
        self.ui.has_diarrhea_checkbox.setChecked(
            mission_details.symptoms.has_diarrhea,
        )

        # Set dizziness
        self.ui.has_dizziness_checkbox.setChecked(
            mission_details.symptoms.has_dizziness,
        )

        # Set double vision
        self.ui.has_double_vision_checkbox.setChecked(
            mission_details.symptoms.has_double_vision,
        )

        # Set fainting
        self.ui.has_fainting_checkbox.setChecked(
            mission_details.symptoms.has_fainting,
        )

        # Set fever chills
        self.ui.has_fever_chills_checkbox.setChecked(
            mission_details.symptoms.has_fever_chills,
        )

        # Set headache
        self.ui.has_headache_checkbox.setChecked(
            mission_details.symptoms.has_headache,
        )

        # Set memory loss
        self.ui.has_memory_loss_post_trauma_checkbox.setChecked(
            mission_details.symptoms.has_memory_loss_post_trauma,
        )

        # Set sensory motor disturbance
        self.ui.has_sensory_motor_disturbance_checkbox.setChecked(
            mission_details.symptoms.has_sensory_motor_disturbance,
        )

        # Set shortness of breath
        self.ui.has_shortness_of_breath_checkbox.setChecked(
            mission_details.symptoms.has_shortness_of_breath,
        )

        # Set sweating
        self.ui.has_sweating_checkbox.setChecked(
            mission_details.symptoms.has_sweating,
        )

        # Set vomiting
        self.ui.has_vomiting_checkbox.setChecked(
            mission_details.symptoms.has_vomiting,
        )

        # Set weakness
        self.ui.has_weakness_checkBox.setChecked(
            mission_details.symptoms.has_weakness,
        )

        # Set other symptoms
        if mission_details.symptoms.other_symptoms is not None:
            self.ui.other_symptoms_field.setPlainText(
                mission_details.symptoms.other_symptoms,
            )

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

    def _populate_vital_signs_table(self, mission_details: MissionDetails) -> None:
        """Populates the vital signs table from mission details data."""
        # If the list of vital signs is empty, we do not populate the table
        if not mission_details.vital_signs:
            return

        # Get the table
        vital_signs_table = self.ui.vital_signs_table_Widget

        # Set the number of columns based on the number of vital signs records
        vital_signs_table.setColumnCount(len(mission_details.vital_signs))

        # Set headers to record time
        headers = []
        for vital_sign in mission_details.vital_signs:
            if vital_sign.record_time:
                headers.append(str(vital_sign.record_time))
            else:
                headers.append(NOT_REGISTERED_PERSIAN_TEXT)

        vital_signs_table.setHorizontalHeaderLabels(headers)

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
                item.setTextAlignment(
                    Qt.AlignCenter,  # type: ignore[attr-defined]
                )
                vital_signs_table.setItem(row, column, item)

        # Resize to content
        vital_signs_table.resizeColumnsToContents()
