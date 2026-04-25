"""Controller for the personnel analyzer tab."""

# pylint: disable=E0611,I1101,R0903,C0103

import asyncio
from collections import Counter
from collections.abc import Callable
from datetime import timedelta
from typing import TYPE_CHECKING, Any

from aiohttp import ClientError
from PySide6.QtCore import QCalendar, QDate, Qt, Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QLineEdit,
    QPlainTextEdit,
    QProgressDialog,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QWidget,
)

import hamyar_paygah.new_ui.widgets.personnel_analyzer_tab as u_p
import hamyar_paygah.new_ui.widgets.personnel_page as ui_pp
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_details_model import MissionDetails
from hamyar_paygah.models.mission_details_submodels.trauma_types_model import PatientExtrication
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.models.region_model import Region
from hamyar_paygah.services.mission_details_service import get_mission_details
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.utils.date_utils import qdate_to_datetime
from hamyar_paygah.utils.qt_utils import show_error_dialog, typed_async_slot

if TYPE_CHECKING:
    from datetime import datetime

    from hamyar_paygah.models.mission_details_model import MissionDetails

COUNT_PERSIAN_TEXT: str = "تعداد"
"""Persian text for the word (count)"""


class PersonnelAnalyzerTab(QWidget):
    """Tab that analyzes the personnel and shows its details."""

    def __init__(self) -> None:
        """Initialize the personnel analyzer tab UI."""
        super().__init__()

        # Set up the UI
        self.ui = u_p.Ui_personnel_analyzer_tab()  # type: ignore[attr-defined]
        self.ui.setupUi(self)

        # Set up date picker calendar types
        persian_calendar: QCalendar = QCalendar(QCalendar.System.Jalali)
        self.ui.from_date_picker.setCalendar(persian_calendar)
        self.ui.to_date_picker.setCalendar(persian_calendar)

        # Set initial dates to today
        self.ui.from_date_picker.setDate(QDate.currentDate())
        self.ui.to_date_picker.setDate(QDate.currentDate())

        # Populate the region picker
        self._populate_region_picker()

    def _populate_region_picker(self) -> None:
        """Populates the region picker with regions dictionary."""
        # Define available regions
        available_regions: list[Region] = [
            Region("ساری", 1),
            Region("چالوس", 2),
            Region("رامسر", 3),
            Region("تنکابن", 4),
            Region("عباس آباد", 5),
            Region("6", 6),
            Region("7", 7),
            Region("8", 8),
            Region("9", 9),
            Region("نوشهر", 10),
            Region("11", 11),
            Region("جویبار", 12),
            Region("13", 13),
            Region("14", 14),
            Region("15", 15),
            Region("گلوگاه", 16),
            Region("17", 17),
            Region("18", 18),
            Region("19", 19),
            Region("20", 20),
            Region("21", 21),
            Region("کلاردشت", 22),
            Region("23", 23),
        ]

        # Populate the region picker
        for region in available_regions:
            self.ui.region_picker.addItem(region.region_name, region.region_id)

        # Set initial selected item to first item
        self.ui.region_picker.setCurrentIndex(0)

    @Slot(QDate)
    def on_from_date_picker_userDateChanged(self, new_date: QDate) -> None:  # noqa: N802
        """Ensure from date is always equal or less than the to date.

        Args:
            new_date (PySide6.QtCore.QDate): User input date when from date picker is changed.
        """
        # Check if the new date is greater than to date
        if new_date.toJulianDay() > self.ui.to_date_picker.date().toJulianDay():
            # If so, set the to date the same as from date
            self.ui.to_date_picker.setDate(new_date)

    @Slot(QDate)
    def on_to_date_picker_userDateChanged(self, new_date: QDate) -> None:  # noqa: N802
        """Ensure to date is always equal or more that the from date.

        Args:
            new_date (PySide6.QtCore.QDate): User input date when to date picker is changed.
        """
        # Check if the new date is lower than from date
        if new_date.toJulianDay() < self.ui.from_date_picker.date().toJulianDay():
            # If so, set the from date the same as to date
            self.ui.from_date_picker.setDate(new_date)

    @typed_async_slot()
    async def on_load_button_clicked(self) -> None:
        """Dynamically load the missions list from the server and build the tabs based on it."""
        # Clear the current data
        self._clear_data()

        # Convert from date and to date to normal pythonic dates
        pythonic_from_date: datetime = qdate_to_datetime(
            self.ui.from_date_picker.date(),
        )
        pythonic_to_date: datetime = qdate_to_datetime(
            self.ui.to_date_picker.date(),
        )

        # Create and show a progress bar
        total_days = (pythonic_to_date.date() - pythonic_from_date.date()).days + 1
        progress_bar = QProgressDialog(
            "در حال دریافت اطلاعات از سرور ...",
            "لغو",
            0,
            total_days,
            self,
        )
        progress_bar.setWindowModality(Qt.WindowModality.ApplicationModal)
        progress_bar.setMinimumDuration(0)  # Show immediately
        progress_bar.setValue(0)
        progress_bar.show()

        # Define the progress bar update function
        def progress_callback(processed: int, total: int) -> None:
            progress_bar.setMaximum(total)
            progress_bar.setValue(processed)

        # Create task to get the list of missions
        task_get_missions_list = asyncio.create_task(
            get_missions_list(
                str(load_server_address()),
                pythonic_from_date,
                pythonic_to_date,
                self.ui.region_picker.currentData(),
                progress_callback=progress_callback,
            ),
        )

        # Connect cancel button to task.cancel()
        progress_bar.canceled.connect(task_get_missions_list.cancel)

        try:
            # Get missions list from server
            missions_list: list[Mission] = await task_get_missions_list
        except asyncio.CancelledError:
            progress_bar.close()
            return  # User cancelled, silent exit
        except ClientError as e:
            progress_bar.close()
            show_error_dialog(
                self,
                "خطای اینترنت",
                f"مشکل در دریافت اطلاعات از سرور:\n{e}\nType: {type(e)}",
            )
            return
        except Exception as e:  # noqa: BLE001
            progress_bar.close()
            show_error_dialog(
                self,
                "خطای ناشناخته",
                f"جهت رفع مشکل، اطلاعات زیر را به توسعه دهنده بفرستید:\n{e}\nType: {type(e)}",
            )
            return
        finally:
            progress_bar.close()
        # Build the tabs with the retrieved missions list
        await self._build_tabs(missions_list)

    def _clear_data(self) -> None:
        """Clears all the fields and checkboxes in the UI."""
        # Clear widgets used for data showing
        for line_edits in self.ui.scrollAreaWidgetContents.findChildren(QLineEdit):
            line_edits.clear()
            line_edits.setEnabled(True)

        for plain_text_edits in self.ui.scrollAreaWidgetContents.findChildren(QPlainTextEdit):
            plain_text_edits.clear()
            plain_text_edits.setEnabled(True)

        for text_edits in self.ui.scrollAreaWidgetContents.findChildren(QTextEdit):
            text_edits.clear()
            text_edits.setEnabled(True)

        for checkbox in self.ui.scrollAreaWidgetContents.findChildren(QCheckBox):
            checkbox.setChecked(False)
            # Set checkboxes to not react to mouse events
            checkbox.setAttribute(
                Qt.WA_TransparentForMouseEvents,  # type: ignore[attr-defined]
            )
            checkbox.setEnabled(True)

        for table_widget in self.ui.scrollAreaWidgetContents.findChildren(QTableWidget):
            table_widget.clearContents()
            table_widget.clear()
            table_widget.setEnabled(True)

        for tab_widget in self.ui.scrollAreaWidgetContents.findChildren(QTabWidget):
            tab_widget.clear()

    async def _build_tabs(self, missions_list: list[Mission]) -> None:
        """Build dynamic tabs per personnel and one overall tab."""
        # Create overall summary tab
        overall_summary_widget: QWidget | None = await self._create_summary_widget(
            missions_list,
        )
        # Check if data is available
        if overall_summary_widget is None:
            # If not, do nothing
            return
        self.ui.analysis_tab_container.addTab(
            overall_summary_widget,
            "کل پرسنل",
        )

        # Create per personnel tabs
        grouped_missions: dict[
            int,
            list[Mission],
        ] = await self._group_missions_by_personnel_code(missions_list)

        for personnel_code in sorted(grouped_missions.keys()):
            personnel_missions: list[Mission] = grouped_missions[personnel_code]
            personnel_summary_widget: QWidget | None = await self._create_summary_widget(
                personnel_missions,
            )
            # Check if data is available
            if personnel_summary_widget is None:
                # if not, do nothing
                continue
            self.ui.analysis_tab_container.addTab(
                personnel_summary_widget,
                f"{personnel_code}",
            )

    async def _group_missions_by_personnel_code(
        self,
        missions_list: list[Mission],
    ) -> dict[int, list[Mission]]:
        """Groups the missions by personnel code.

        Args:
            missions_list (list[Mission]): List of missions to be grouped.

        Returns:
            dict[int, list[Mission]]: A dictionary where the keys are personnel codes
            and the values are lists of missions.
        """
        grouped_missions: dict[int, list[Mission]] = {}

        # Loop through all the missions
        for mission in missions_list:
            # Retrieve the details of the mission
            mission_data: MissionDetails = await get_mission_details(
                str(load_server_address()),
                mission.id,  # type: ignore[arg-type]
                mission.patient_id,  # type: ignore[arg-type]
            )
            # Check staff codes
            staff_codes: list[int | None] = [
                mission_data.times_and_distances.senior_staff_code,
                mission_data.times_and_distances.first_staff_code,
                mission_data.times_and_distances.second_staff_code,
            ]
            for staff_code in staff_codes:
                # Check if staff code is available
                if staff_code is not None and staff_code != 0:
                    # If it's available and not yet added
                    if staff_code not in grouped_missions:
                        # Create the sub group in the list of groups
                        grouped_missions[staff_code] = []
                    # Add the mission to the sub group
                    grouped_missions[staff_code].append(mission)

        return grouped_missions

    def _sorted_counter(self, counter: Counter[Any]) -> list[tuple[str, int]]:
        return counter.most_common()

    async def _create_summary_widget(self, missions_list: list[Mission]) -> QWidget | None:
        """Create a simple summary display widget for a mission list."""
        # Get summary stats from the missions list
        stats = await self._summarize_missions(missions_list)

        # Check if data is available
        if stats is None:
            # If not, do nothing
            return None

        # Setup UI
        widget = QWidget()
        ui = ui_pp.Ui_personnel_page()  # type: ignore[attr-defined]
        ui.setupUi(widget)

        # Set patients count field
        ui.patients_count_field.setText(str(stats["total_patients"]))

        # Set missions count field
        ui.missions_count_field.setText(str(stats["total_missions"]))

        # Set average time to arrive field
        temp_seconds = float(
            stats["average_time_to_arrive"],  # type: ignore[arg-type]
        )
        ui.average_arriving_time_field.setText(
            str(
                timedelta(
                    0,
                    temp_seconds,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
            ),
        )
        # Set average time to depart field
        temp_seconds = float(
            stats["average_time_to_depart"],  # type: ignore[arg-type]
        )
        ui.average_reaction_time_field.setText(
            str(
                timedelta(
                    0,
                    temp_seconds,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
            ),
        )
        # Set average presence at emergency location field
        temp_seconds = float(
            stats["average_presence_time"],  # type: ignore[arg-type]
        )
        ui.average_emergency_location_presence_time_field.setText(
            str(
                timedelta(
                    0,
                    temp_seconds,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
            ),
        )
        # Set average deliver to hospital field
        temp_seconds = float(
            stats["average_deliver_to_hospital"],  # type: ignore[arg-type]
        )
        ui.average_deliver_to_hospital_field.setText(
            str(
                timedelta(
                    0,
                    temp_seconds,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
            ),
        )
        # Set average mission end time field
        temp_seconds = float(
            stats["average_mission_end_time"],  # type: ignore[arg-type]
        )
        ui.average_mission_end_time_field.setText(
            str(
                timedelta(
                    0,
                    temp_seconds,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
            ),
        )

        # Set total vehicle accidents field
        ui.total_vehicle_accident_field.setText(
            str(stats["total_vehicle_accident"]),
        )

        # Set total missions over 60KM field
        ui.missions_over_60km_field.setText(
            str(stats["total_missions_over_60km"]),
        )

        # Set total vehicle refuel field
        ui.refueling_count_field.setText(
            str(stats["total_vehicle_refuel"]),
        )

        # Set total patient extraction field
        ui.patient_extraction_count_field.setText(
            str(stats["total_patient_extraction"]),
        )

        # Set overall distance driven field
        ui.overall_distance_driven_field.setText(
            str(stats["overall_distance_driven"]),
        )

        # Populate the missions per code table
        self._populate_missions_per_code_table(
            stats["missions_per_code"],  # type: ignore[arg-type]
            ui,
        )

        return widget

    async def _summarize_missions(
        self,
        missions_list: list[Mission],
    ) -> dict[str, int | list[tuple[str, int]] | Counter[Any]] | None:
        """Compute basic statistics from the missions list."""
        # Create and show a progress bar
        total_missions = len(missions_list)
        progress_bar = QProgressDialog(
            "در حال دریافت اطلاعات ماموریت ها از سرور ...",  # noqa: RUF001
            "لغو",
            0,
            total_missions,
            self,
        )
        progress_bar.setWindowModality(Qt.WindowModality.ApplicationModal)
        progress_bar.setMinimumDuration(0)  # Show immediately
        progress_bar.setValue(0)
        progress_bar.show()

        # Define the progress bar update function
        def progress_callback(processed: int) -> None:
            progress_bar.setValue(processed)

        # Create task to get the details of missions
        task_process_missions = asyncio.create_task(
            self._process_missions(
                missions_list,
                progress_callback,
            ),
        )

        # Connect cancel button to task.cancel()
        progress_bar.canceled.connect(task_process_missions.cancel)

        try:
            # Get processed missions with details
            processed_missions = await task_process_missions
        except asyncio.CancelledError:
            progress_bar.close()
            return None  # User cancelled, silent exit
        except ClientError as e:
            progress_bar.close()
            show_error_dialog(
                self,
                "خطای اینترنت",
                f"مشکل در دریافت اطلاعات ماموریت‌ها از سرور:\n{e}\nType: {type(e)}",  # noqa: RUF001
            )
            return None
        except Exception as e:  # noqa: BLE001
            progress_bar.close()
            show_error_dialog(
                self,
                "خطای ناشناخته",
                f"جهت رفع مشکل، اطلاعات زیر را به توسعه دهنده بفرستید:\n{e}\nType: {type(e)}",
            )
            return None
        finally:
            progress_bar.close()

        return processed_missions

    async def _process_missions(  # noqa: C901, PLR0912, PLR0915
        self,
        missions_list: list[Mission],
        progress_callback: Callable[[int], None],
    ) -> dict[str, int | list[tuple[Any, int]] | Counter[Any]]:
        """Process missions asynchronously with progress reporting."""
        # Get total patients
        total_patients: int = len(missions_list)

        # Get total missions (with unique IDs to avoid counting duplicates)
        total_missions: int = len(
            {mission.id for mission in missions_list if mission.id is not None},
        )

        # Get missions count per ambulance code
        missions_per_code: list[tuple[int, int]] = Counter(
            mission.ambulance_code
            for mission in missions_list
            if mission.ambulance_code is not None
        ).most_common()

        # Mission details variables
        total_vehicle_accident: int = 0
        total_missions_over_60km: int = 0
        total_vehicle_refuel: int = 0
        total_patient_extraction: int = 0
        total_time_to_arrive: timedelta = timedelta(0, 0, 0, 0, 0, 0, 0)
        total_time_to_depart: timedelta = timedelta(0, 0, 0, 0, 0, 0, 0)
        total_emergency_location_presence_time: timedelta = timedelta(
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )
        total_deliver_to_hospital_time: timedelta = timedelta(
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )
        total_mission_end_time: timedelta = timedelta(0, 0, 0, 0, 0, 0, 0)
        overall_distance_driven: int = 0

        # Control variables
        empty_time_to_arrives: int = 0
        empty_time_to_depart: int = 0
        empty_emergency_presence_time: int = 0
        empty_deliver_to_hospital_time: int = 0
        empty_mission_end_time: int = 0

        # Iterate through each mission in the list and get mission details
        # for processing deeper statistics
        for i, mission in enumerate(missions_list, start=1):
            # Allow cancellation to be raised here
            await asyncio.sleep(0)

            # Get mission details
            mission_details: MissionDetails = await get_mission_details(
                str(load_server_address()),
                mission.id,  # type: ignore[arg-type]
                mission.patient_id,  # type: ignore[arg-type]
            )

            # Get total vehicle accidents
            if mission_details.location_and_emergency.is_vehicle_accident:
                total_vehicle_accident += 1

            # Check if mission has arrival time
            if mission_details.times_and_distances.time_to_arrive is not None:
                # Add time to arrive to total time to arrive
                total_time_to_arrive += mission_details.times_and_distances.time_to_arrive
            # Else, omit this from average calculations
            else:
                empty_time_to_arrives += 1

            # Check if mission has departure time
            if mission_details.times_and_distances.time_to_depart is not None:
                # Add time to depart to total time to depart
                total_time_to_depart += mission_details.times_and_distances.time_to_depart
            # Else, omit this from average calculations
            else:
                empty_time_to_depart += 1

            # Check if mission has emergency location presence time
            if mission_details.times_and_distances.time_at_emergency_location is not None:
                # Add emergency location presence time to total time
                total_emergency_location_presence_time += (
                    mission_details.times_and_distances.time_at_emergency_location
                )
            # Else, omit this from average calculations
            else:
                empty_emergency_presence_time += 1

            # Check if mission has deliver to hospital time
            if mission_details.times_and_distances.time_to_deliver is not None:
                # Add deliver to hospital time to total time
                total_deliver_to_hospital_time += (
                    mission_details.times_and_distances.time_to_deliver
                )
            # Else, omit this from average calculations
            else:
                empty_deliver_to_hospital_time += 1

            # Check if mission has mission end time
            if mission_details.times_and_distances.time_to_complete is not None:
                # Add time to complete to mission end time
                total_mission_end_time += mission_details.times_and_distances.time_to_complete
            # Else, omit this from average calculations
            else:
                empty_mission_end_time += 1

            # Get total missions over 60KM
            if mission_details.times_and_distances.overall_mission_distance > 60:  # noqa: PLR2004
                total_missions_over_60km += 1

            # Get total vehicle refuel
            if (
                mission_details.times_and_distances.vehicle_refuel_odometer is not None
                and mission_details.times_and_distances.vehicle_refuel_odometer != 0
            ):
                total_vehicle_refuel += 1

            # Get total patient extraction
            if (
                mission_details.trauma_types.patient_extraction is not None
                and mission_details.trauma_types.patient_extraction == PatientExtrication.BY_EMS
            ):
                total_patient_extraction += 1

            # Get overall distance driven
            overall_distance_driven += mission_details.times_and_distances.overall_mission_distance

            # ---- Update progress ----
            progress_callback(i)

        # Calculate average time to arrive
        average_time_to_arrive: int
        try:
            average_time_to_arrive = (
                total_time_to_arrive / (total_missions - empty_time_to_arrives)
            ).seconds
            # If for some reason, either total missions are the same as empty time to arrive
            # or any other unknown reason, the total time to arrive is being divided by zero
            # catch the exception and set the average time to zero.
        except ZeroDivisionError:
            average_time_to_arrive = 0

        # Calculate average time to depart
        average_time_to_depart: int
        try:
            average_time_to_depart = (
                total_time_to_depart / (total_missions - empty_time_to_depart)
            ).seconds
        except ZeroDivisionError:
            average_time_to_depart = 0

        # Calculate average presence at emergency location
        average_presence_at_emergency_location_time: int
        try:
            average_presence_at_emergency_location_time = (
                total_emergency_location_presence_time
                / (total_missions - empty_emergency_presence_time)
            ).seconds
        except ZeroDivisionError:
            average_presence_at_emergency_location_time = 0

        # Calculate average deliver to hospital time
        average_deliver_to_hospital_time: int
        try:
            average_deliver_to_hospital_time = (
                total_deliver_to_hospital_time / (total_missions - empty_deliver_to_hospital_time)
            ).seconds
        except ZeroDivisionError:
            average_deliver_to_hospital_time = 0

        # Calculate average mission end time
        average_mission_end_time: int
        try:
            average_mission_end_time = (
                total_mission_end_time / (total_missions - empty_mission_end_time)
            ).seconds
        except ZeroDivisionError:
            average_mission_end_time = 0

        return {
            "total_patients": total_patients,
            "total_missions": total_missions,
            "total_vehicle_accident": total_vehicle_accident,
            "average_time_to_arrive": average_time_to_arrive,
            "average_time_to_depart": average_time_to_depart,
            "average_presence_time": average_presence_at_emergency_location_time,
            "average_deliver_to_hospital": average_deliver_to_hospital_time,
            "missions_per_code": missions_per_code,
            "total_missions_over_60km": total_missions_over_60km,
            "total_vehicle_refuel": total_vehicle_refuel,
            "total_patient_extraction": total_patient_extraction,
            "overall_distance_driven": overall_distance_driven,
            "average_mission_end_time": average_mission_end_time,
        }

    def _populate_missions_per_code_table(
        self,
        missions_per_code: list[tuple[int, int]],
        ui: ui_pp.Ui_personnel_page,  # type: ignore[name-defined]
    ) -> None:
        """Populate the missions per code table with the given data."""
        # Get the table widget
        table_widget: QTableWidget = ui.missions_per_code_tableWidget

        # Clear the table contents
        table_widget.clearContents()

        # Set row and column count based on the data
        table_widget.setRowCount(len(missions_per_code))
        table_widget.setColumnCount(2)

        # Set horizontal header labels
        table_widget.setHorizontalHeaderLabels(
            ["کد آمبولانس", COUNT_PERSIAN_TEXT],
        )

        # Populate the table rows
        for row_index, (ambulance_code, mission_count) in enumerate(missions_per_code):
            # Create and set result item
            code = QTableWidgetItem(str(ambulance_code))
            code.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            # Create and set mission count item
            count_item = QTableWidgetItem()
            count_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                mission_count,
            )
            count_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table_widget.setItem(row_index, 0, code)
            table_widget.setItem(row_index, 1, count_item)

        # Resize columns to fit contents
        table_widget.resizeColumnsToContents()
