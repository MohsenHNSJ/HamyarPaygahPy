"""Controller for the region analyzer tab."""

# pylint: disable=E0611,I1101,R0903,C0103

from typing import TYPE_CHECKING

from PySide6.QtCore import QCalendar, QDate, Qt, Slot
from PySide6.QtWidgets import (
    QCheckBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QTableWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.widgets.region_analyzer_tab as ui_rat
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.models.region_model import Region
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.utils.date_utils import convert_persian_q_date_to_gregorian_pythonic_date

if TYPE_CHECKING:
    from datetime import datetime


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
        if new_date > self.ui.to_date_picker.date():  # type: ignore[]
            # If so, set the to date the same as from date
            self.ui.to_date_picker.setDate(new_date)

    @Slot(QDate)
    def on_to_date_picker_userDateChanged(self, new_date: QDate) -> None:  # noqa: N802
        """Ensure to date is always equal or more that the from date.

        Args:
            new_date (PySide6.QtCore.QDate): User input date when to date picker is changed.
        """
        # Check if the new date is lower than from date
        if new_date < self.ui.from_date_picker.date():  # type: ignore[]
            # If so, set the from date the same as to date
            self.ui.from_date_picker.setDate(new_date)

    @asyncSlot()  # type: ignore[untyped-decorator,misc]
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
        self._build_tabs(missions_list)

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
            table_widget.setEnabled(True)

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

    def _summarize_missions(self, missions_list: list[Mission]) -> dict[str, int]:
        """Compute basic statistics from the missions list."""
        total_missions: int = len(missions_list)

        return {
            "total_missions": total_missions,
        }

    def _build_tabs(self, missions_list: list[Mission]) -> None:
        """Build dynamic tabs per ambulance and one overall tab."""
        self.ui.analysis_tab_container.clear()  # Clear existing tabs

        # Create overall summary tab
        overall_summary_widget: QWidget = self._create_summary_widget(
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
            ambulance_summary_widget: QWidget = self._create_summary_widget(
                ambulance_missions,
            )
            self.ui.analysis_tab_container.addTab(
                ambulance_summary_widget,
                f"{ambulance_code}",
            )

    def _create_summary_widget(self, missions_list: list[Mission]) -> QWidget:
        """Create a simple summary display widget for a mission list."""
        stats = self._summarize_missions(missions_list)

        widget = QWidget()

        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel(f"Total Missions: {stats['total_missions']}"))

        layout.addStretch()  # Add stretch to push content to the top

        return widget
