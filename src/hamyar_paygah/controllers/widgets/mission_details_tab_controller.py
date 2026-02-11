"""Controller for mission details tab."""

# pylint: disable=E0611,I1101,R0903
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QCheckBox, QLineEdit, QPlainTextEdit, QTextEdit, QWidget
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.widgets.mission_details_tab as ui_mdt
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.services.mission_details_service import get_mission_details
from hamyar_paygah.utils.date_utils import convert_gregorian_date_to_persian_date

if TYPE_CHECKING:
    import jdatetime  # type: ignore[import-untyped]


class MissionsDetailsTab(QWidget):
    """Tab that enables user to retrieve details of a mission."""

    def __init__(self) -> None:
        """Initialize the mission details tab UI."""
        super().__init__()

        # Set up the UI
        self.ui = ui_mdt.Ui_mission_details_tab()  # type: ignore[attr-defined]
        self.ui.setupUi(self)

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
            self.ui.national_code_field.setText("ارائه نشده")

        # Set document serial number field
        self.ui.document_serial_number_field.setText(
            mission_details.information.document_serial_number,
        )

        # Set caller number field
        self.ui.caller_number_field.setText(
            mission_details.information.caller_number,
        )

        # Set backup number field
        self.ui.backup_number_field.setText(
            mission_details.information.backup_number,
        )

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

    def _populate_times_and_distances_tab(self, mission_details: MissionDetails) -> None:
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
        self.ui.arrive_at_hospital_time_field.setText(
            str(mission_details.times_and_distances.arrive_at_hospital_time),
        )

        # Set time to hospital
        self.ui.time_to_hospital_field.setText(
            str(mission_details.times_and_distances.time_to_hospital),
        )

        # Set deliver to hospital time
        self.ui.deliver_to_hospital_time_field.setText(
            str(mission_details.times_and_distances.deliver_to_hospital_time),
        )

        # Set time to deliver
        self.ui.time_to_deliver_field.setText(
            str(mission_details.times_and_distances.time_to_deliver),
        )

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
            self.ui.arrive_at_emergency_odo_field.setText("ثبت نشده")

        # Set arrive at hospital ODO
        if mission_details.times_and_distances.arrive_at_hospital_odometer != 0:
            self.ui.arrive_at_hospital_odo_field.setText(
                str(mission_details.times_and_distances.arrive_at_hospital_odometer),
            )
        else:
            self.ui.arrive_at_hospital_odo_field.setText("ثبت نشده")

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
