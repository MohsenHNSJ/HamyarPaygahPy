"""Controller for the region analyzer tab."""

# pylint: disable=E0611,I1101,R0903,C0103

from collections import Counter
from typing import TYPE_CHECKING, Any

from PySide6.QtCore import QCalendar, QDate, Qt, Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QLineEdit,
    QPlainTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QWidget,
)
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.widgets.analysis_page as ui_ap
import hamyar_paygah.new_ui.widgets.region_analyzer_tab as ui_rat
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.models.region_model import Region
from hamyar_paygah.services.mission_details_service import get_mission_details
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.utils.date_utils import convert_persian_q_date_to_gregorian_pythonic_date

if TYPE_CHECKING:
    from datetime import datetime

    from hamyar_paygah.models.mission_details_model import MissionDetails


class RegionAnalyzerTab(QWidget):
    """Tab that analyzes a region and shows its details."""

    def __init__(self) -> None:
        """Initialize the region analyzer tab UI."""
        super().__init__()

        # Set up the UI
        self.ui = ui_rat.Ui_region_analyzer_tab()  # type: ignore[attr-defined]
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

    @asyncSlot()  # type: ignore[misc]
    async def on_load_button_clicked(self) -> None:
        """Dynamically load the missions list from the server and build the tabs based on it."""
        # Clear the current data
        self._clear_data()

        # Convert from date and to date to normal pythonic dates
        pythonic_from_date: datetime = convert_persian_q_date_to_gregorian_pythonic_date(
            self.ui.from_date_picker.date(),
        )
        pythonic_to_date: datetime = convert_persian_q_date_to_gregorian_pythonic_date(
            self.ui.to_date_picker.date(),
        )

        # TODO@MohsenHNSJ: Show a loading progress or something  # noqa: TD003
        # TODO@MohsenHNSJ: Use try, catch and except the common errors # noqa: TD003

        # Get missions list from server
        missions_list: list[Mission] = await get_missions_list(
            str(load_server_address()),
            pythonic_from_date,
            pythonic_to_date,
            self.ui.region_picker.currentData(),
        )

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

    def _group_missions_by_ambulance_code(
        self,
        missions_list: list[Mission],
    ) -> dict[int, list[Mission]]:
        """Groups the missions by ambulance code.

        Args:
            missions_list (list[Mission]): List of missions to be grouped.

        Returns:
            dict[int, list[Mission]]: A dictionary where the keys are ambulance codes
            and the values are lists of missions.
        """
        grouped_missions: dict[int, list[Mission]] = {}

        for mission in missions_list:
            if mission.ambulance_code is not None:
                if mission.ambulance_code not in grouped_missions:
                    grouped_missions[mission.ambulance_code] = []
                grouped_missions[mission.ambulance_code].append(mission)

        return grouped_missions

    async def _summarize_missions(  # noqa: C901, PLR0912, PLR0915
        self,
        missions_list: list[Mission],
    ) -> dict[str, int | list[tuple[str, int]] | Counter[Any]]:
        """Compute basic statistics from the missions list."""
        # Get total patients
        total_patients: int = len(missions_list)

        # Get total missions (with unique IDs to avoid counting duplicates)
        total_missions: int = len(
            {mission.id for mission in missions_list if mission.id is not None},
        )

        # Get missions count per hospital (only for transported patients)
        missions_per_hospital: list[tuple[str, int]] = Counter(
            mission.hospital_name for mission in missions_list if mission.hospital_name is not None
        ).most_common()

        # Get missions count per result
        missions_per_result: list[tuple[str, int]] = Counter(
            mission.result for mission in missions_list if mission.result is not None
        ).most_common()

        # Mission details variables
        total_iranian_patients: int = 0
        total_foreign_patients: int = 0
        total_male_patients: int = 0
        total_female_patients: int = 0
        total_unknown_gender: int = 0
        total_consumables: Counter[Any] = Counter()
        total_drugs: Counter[Any] = Counter()
        total_vehicle_accident: int = 0
        total_caller_numbers: Counter[Any] = Counter()
        total_location_types: Counter[Any] = Counter()
        total_accident_types: Counter[Any] = Counter()
        total_illness_types: Counter[Any] = Counter()
        total_vehicle_types: Counter[Any] = Counter()
        total_injury_types: Counter[Any] = Counter()
        total_chief_complaints: Counter[Any] = Counter()
        # Iterate through each mission in the list and get mission details
        # for processing deeper statistics
        for mission in missions_list:
            mission_details: MissionDetails = await get_mission_details(
                str(load_server_address()),
                mission.id,  # type: ignore[arg-type]
                mission.patient_id,  # type: ignore[arg-type]
            )

            # Get iranian and foreign patients count
            if mission_details.information.iranian_nationality:
                total_iranian_patients += 1
            if mission_details.information.foreign_nationality:
                total_foreign_patients += 1

            # Get genders count
            if mission_details.information.is_male_gender:
                total_male_patients += 1
            if mission_details.information.is_female_gender:
                total_female_patients += 1
            if mission_details.information.is_unknown_gender:
                total_unknown_gender += 1

            # Get total consumables
            total_consumables += mission_details.consumables.items

            # Get total drugs
            total_drugs += Counter(
                drug.name
                for drug in mission_details.drugs
                if drug.name  # ignore None
            )

            # Get total vehicle accidents
            if mission_details.location_and_emergency.is_vehicle_accident:
                total_vehicle_accident += 1

            # Get total caller numbers
            total_caller_numbers += Counter(
                number
                for number in (
                    mission_details.information.caller_number,
                    mission_details.information.backup_number,
                )
                if number is not None and number != "Anonymous"
            )

            # Get total location types
            location_type = mission_details.location_and_emergency.location_type
            if location_type is not None:
                total_location_types[location_type.persian_label] += 1

            # Get total accident types
            accident_type = mission_details.location_and_emergency.accident_type
            if accident_type is not None:
                total_accident_types[accident_type.persian_label] += 1

            # Get total illness types
            illness_type = mission_details.location_and_emergency.illness_type
            if illness_type is not None:
                total_illness_types[illness_type.persian_label] += 1

            # Get total vehicle types
            vehicle_type = mission_details.location_and_emergency.vehicle_type
            if vehicle_type is not None:
                total_vehicle_types[vehicle_type.persian_label] += 1

            # Get total injury types
            injury_type = mission_details.location_and_emergency.role_in_accident
            if injury_type is not None:
                total_injury_types[injury_type.persian_label] += 1

            # Get total chief complaints
            if mission_details.location_and_emergency.chief_complaint is not None:
                total_chief_complaints[mission_details.location_and_emergency.chief_complaint] += 1

        # Sort the consumables list
        sorted_total_consumables = sorted(
            total_consumables.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sort the drugs list
        sorted_total_drugs = sorted(
            total_drugs.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sort caller numbers list
        sorted_caller_numbers = sorted(
            total_caller_numbers.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sort location types
        sorted_location_types = sorted(
            total_location_types.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sorted accident types
        sorted_accident_types = sorted(
            total_accident_types.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sorted illness types
        sorted_illness_types = sorted(
            total_illness_types.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sorted vehicle types
        sorted_vehicle_types = sorted(
            total_vehicle_types.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sorted injury types
        sorted_injury_types = sorted(
            total_injury_types.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # Sorted chief complaints
        sorted_chief_complaints = sorted(
            total_chief_complaints.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return {
            "total_patients": total_patients,
            "total_missions": total_missions,
            "missions_per_hospital": missions_per_hospital,
            "missions_per_result": missions_per_result,
            "total_iranian_patients": total_iranian_patients,
            "total_foreign_patients": total_foreign_patients,
            "total_male_patients": total_male_patients,
            "total_female_patients": total_female_patients,
            "total_unknown_gender": total_unknown_gender,
            "total_consumables": sorted_total_consumables,
            "total_drugs": sorted_total_drugs,
            "total_vehicle_accident": total_vehicle_accident,
            "total_caller_numbers": sorted_caller_numbers,
            "total_location_types": sorted_location_types,
            "total_accident_types": sorted_accident_types,
            "total_illness_types": sorted_illness_types,
            "total_vehicle_types": sorted_vehicle_types,
            "total_injury_types": sorted_injury_types,
            "total_chief_complaints": sorted_chief_complaints,
        }

    async def _build_tabs(self, missions_list: list[Mission]) -> None:
        """Build dynamic tabs per ambulance and one overall tab."""
        # Create overall summary tab
        overall_summary_widget: QWidget = await self._create_summary_widget(
            missions_list,
        )
        self.ui.analysis_tab_container.addTab(
            overall_summary_widget,
            "کل منطقه",
        )

        # Create per ambulance tabs
        grouped_missions: dict[
            int,
            list[Mission],
        ] = self._group_missions_by_ambulance_code(missions_list)

        for ambulance_code in sorted(grouped_missions.keys()):
            ambulance_missions: list[Mission] = grouped_missions[ambulance_code]
            ambulance_summary_widget: QWidget = await self._create_summary_widget(
                ambulance_missions,
            )
            self.ui.analysis_tab_container.addTab(
                ambulance_summary_widget,
                f"{ambulance_code}",
            )

    async def _create_summary_widget(self, missions_list: list[Mission]) -> QWidget:
        """Create a simple summary display widget for a mission list."""
        # Get summary stats from the missions list
        stats = await self._summarize_missions(missions_list)

        # Setup UI
        widget = QWidget()
        ui = ui_ap.Ui_analysis_page()  # type: ignore[attr-defined]
        ui.setupUi(widget)

        # Set patients count field
        ui.patients_count_field.setText(str(stats["total_patients"]))

        # Set missions count field
        ui.missions_count_field.setText(str(stats["total_missions"]))

        # Populate the missions per hospital table
        self._populate_mission_per_hospital_table(
            stats["missions_per_hospital"],  # type: ignore[arg-type]
            ui,
        )

        # Populate the missions per result table
        self._populate_mission_per_result_table(
            stats["missions_per_result"],  # type: ignore[arg-type]
            ui,
        )

        # Populate total iranian patients
        ui.total_iranian_patient_field.setText(
            str(stats["total_iranian_patients"]),
        )

        # Populate total foreign patients
        ui.total_foreign_patient_field.setText(
            str(stats["total_foreign_patients"]),
        )

        # Populate genders section
        ui.total_male_patients_field.setText(str(stats["total_male_patients"]))
        ui.total_female_patients_field.setText(
            str(stats["total_female_patients"]),
        )
        ui.total_unknown_gender_field.setText(
            str(stats["total_unknown_gender"]),
        )

        # Populate consumables table
        self._populate_consumables_table(
            ui.consumables_list_tableWidget,
            stats["total_consumables"],  # type: ignore[arg-type]
        )

        # Populate drugs table
        self._populate_drugs_table(
            ui.drugs_list_tableWidget,
            stats["total_drugs"],  # type: ignore[arg-type]
        )

        # Set total vehicle accidents field
        ui.total_vehicle_accident_field.setText(
            str(stats["total_vehicle_accident"]),
        )

        # Populate caller numbers table
        self._populate_caller_numbers_table(
            ui.caller_numbers_tableWidget,
            stats["total_caller_numbers"],  # type: ignore[arg-type]
        )

        # Populate location types table
        self._populate_location_types_table(
            ui.missions_per_type_of_location_tableWidget,
            stats["total_location_types"],  # type: ignore[arg-type]
        )

        # Populate accident types table
        self._populate_accident_types_table(
            ui.missions_per_accident_type_tableWidget,
            stats["total_accident_types"],  # type: ignore[arg-type]
        )

        # Populate illness types table
        self._populate_illness_types_table(
            ui.missions_per_illness_type_tableWidget,
            stats["total_illness_types"],  # type: ignore[arg-type]
        )

        # Populate vehicle types table
        self._populate_vehicle_types_table(
            ui.missions_per_vehicle_type_tableWidget,
            stats["total_vehicle_types"],  # type: ignore[arg-type]
        )

        # Populate injury types table
        self._populate_injury_types_table(
            ui.missions_per_injured_type_tableWidget,
            stats["total_injury_types"],  # type: ignore[arg-type]
        )

        # Populate chief complaints table
        self._populate_chief_complaints_table(
            ui.missions_per_chief_complain_tableWidget,
            stats["total_chief_complaints"],  # type: ignore[arg-type]
        )

        return widget

    def _populate_mission_per_hospital_table(
        self,
        missions_per_hospital: list[tuple[str, int]],
        ui: ui_ap.Ui_analysis_page,  # type: ignore[name-defined]
    ) -> None:
        """Populate the missions per hospital table with the given data."""
        # Get the table widget
        table_widget: QTableWidget = ui.missions_per_hospital_tableWidget

        # Clear the table contents
        table_widget.clearContents()

        # Set row count based on the data
        table_widget.setRowCount(len(missions_per_hospital))

        # Set horizontal header labels
        table_widget.setHorizontalHeaderLabels(
            ["نام بیمارستان", "تعداد ماموریت"],
        )

        # Populate the table rows
        for row_index, (hospital_name, mission_count) in enumerate(missions_per_hospital):
            # Create and set hospital name item
            hospital_item = QTableWidgetItem(hospital_name)
            hospital_item.setTextAlignment(
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

            table_widget.setItem(row_index, 0, hospital_item)
            table_widget.setItem(row_index, 1, count_item)

        # Resize columns to fit contents
        table_widget.resizeColumnsToContents()

    def _populate_mission_per_result_table(
        self,
        missions_per_result: list[tuple[str, int]],
        ui: ui_ap.Ui_analysis_page,  # type: ignore[name-defined]
    ) -> None:
        """Populate the missions per result table with the given data."""
        # Get the table widget
        table_widget: QTableWidget = ui.missions_per_result_tableWidget

        # Set row count based on the data
        table_widget.setRowCount(len(missions_per_result))

        # Set horizontal header labels
        table_widget.setHorizontalHeaderLabels(["نتیجه", "تعداد ماموریت"])

        # Populate the table rows
        for row_index, (result, mission_count) in enumerate(missions_per_result):
            # Create and set result item
            result_item = QTableWidgetItem(result)
            result_item.setTextAlignment(
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

            table_widget.setItem(row_index, 0, result_item)
            table_widget.setItem(row_index, 1, count_item)

        # Resize columns to fit contents
        table_widget.resizeColumnsToContents()

    def _populate_consumables_table(
        self,
        table: QTableWidget,
        consumables_list: list[tuple[Any, int]],
    ) -> None:

        table.setRowCount(len(consumables_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع", "تعداد"])

        for row, (name, quantity) in enumerate(consumables_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )
            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_drugs_table(self, table: QTableWidget, drugs_list: list[tuple[Any, int]]) -> None:

        table.setRowCount(len(drugs_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع", "تعداد"])

        for row, (name, quantity) in enumerate(drugs_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_caller_numbers_table(
        self,
        table: QTableWidget,
        numbers_list: list[tuple[Any, int]],
    ) -> None:

        table.setRowCount(len(numbers_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["شماره", "تعداد"])

        for row, (name, quantity) in enumerate(numbers_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_location_types_table(
        self,
        table: QTableWidget,
        location_types_list: list[tuple[Any, int]],
    ) -> None:

        table.setRowCount(len(location_types_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع محل فوریت", "تعداد"])

        for row, (name, quantity) in enumerate(location_types_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_accident_types_table(
        self,
        table: QTableWidget,
        accident_types_list: list[tuple[Any, int]],
    ) -> None:
        table.setRowCount(len(accident_types_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع حادثه", "تعداد"])

        for row, (name, quantity) in enumerate(accident_types_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_illness_types_table(
        self,
        table: QTableWidget,
        illness_types_list: list[tuple[Any, int]],
    ) -> None:
        table.setRowCount(len(illness_types_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع بیماری", "تعداد"])

        for row, (name, quantity) in enumerate(illness_types_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_vehicle_types_table(
        self,
        table: QTableWidget,
        vehicle_types_list: list[tuple[Any, int]],
    ) -> None:
        table.setRowCount(len(vehicle_types_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نوع خودرو", "تعداد"])

        for row, (name, quantity) in enumerate(vehicle_types_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_injury_types_table(
        self,
        table: QTableWidget,
        injury_types_list: list[tuple[Any, int]],
    ) -> None:
        table.setRowCount(len(injury_types_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["نقش مصدوم", "تعداد"])

        for row, (name, quantity) in enumerate(injury_types_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()

    def _populate_chief_complaints_table(
        self,
        table: QTableWidget,
        chief_complaints_list: list[tuple[Any, int]],
    ) -> None:
        table.setRowCount(len(chief_complaints_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["شکایت اصلی", "تعداد"])

        for row, (name, quantity) in enumerate(chief_complaints_list):
            name_item = QTableWidgetItem(name)
            name_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            quantity_item = QTableWidgetItem()
            quantity_item.setData(
                Qt.DisplayRole,  # type: ignore[attr-defined]
                quantity,
            )

            quantity_item.setTextAlignment(
                Qt.AlignCenter,  # type: ignore[attr-defined]
            )

            table.setItem(row, 0, name_item)
            table.setItem(row, 1, quantity_item)

        table.resizeColumnsToContents()
