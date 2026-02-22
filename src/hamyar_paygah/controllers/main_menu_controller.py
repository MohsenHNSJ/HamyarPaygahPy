"""Controller for main menu UI."""

# pylint: disable=E0611,I1101,R0903,C0103
from typing import TYPE_CHECKING

from PySide6.QtCore import QCalendar, QDate, QSortFilterProxyModel, Qt, Slot
from PySide6.QtWidgets import QMainWindow

import hamyar_paygah.new_ui.main_menu as main_menu_ui
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.controllers.widgets.mission_details_tab_controller import MissionsDetailsTab
from hamyar_paygah.controllers.widgets.region_analyzer_tab_controller import RegionAnalyzerTab
from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.models.region_model import Region
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.utils.date_utils import convert_persian_q_date_to_gregorian_pythonic_date
from hamyar_paygah.utils.qt_utils import typed_async_slot
from hamyar_paygah.view_models.mission_table_model import MissionTableModel

if TYPE_CHECKING:
    from datetime import datetime

    from PySide6.QtWidgets import QWidget


class MainMenu(QMainWindow):
    """Main menu of the application."""

    def __init__(self) -> None:
        """Initialize the main menu UI."""
        super().__init__()

        # Set up the UI
        self.ui = main_menu_ui.Ui_main_window()  # type: ignore[attr-defined]
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

        # Add the mission details tab
        mission_details_tab: QWidget = MissionsDetailsTab()
        self.ui.tab_widget.addTab(mission_details_tab, "گزارش ماموریت")

        # Add the region analyzer tab
        region_analyzer_tab: QWidget = RegionAnalyzerTab()
        self.ui.tab_widget.addTab(region_analyzer_tab, "تحلیل منطقه")

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
        """Loads the list of missions from server and populates the table."""
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

        # Populate and setup the table
        self._populate_and_setup_table_view(missions_list)

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

    def _populate_and_setup_table_view(self, missions_list: list[Mission]) -> None:
        """Populates the missions list table with data and configures the columns width.

        Args:
            missions_list (list[Mission]): List of missions received from the server.
        """
        # Create the model for table view
        source_model = MissionTableModel(missions_list)

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
        self.ui.missions_list_table.setModel(proxy_model)

        # Set default column width
        minimum_section_size: int = (
            self.ui.missions_list_table.horizontalHeader().minimumSectionSize()
        )
        # Missions ID
        self.ui.missions_list_table.setColumnWidth(
            0,
            int(
                minimum_section_size * 1.25,
            ),
        )
        # Patient Name
        self.ui.missions_list_table.setColumnWidth(
            1,
            int(minimum_section_size * 1.5),
        )
        # Hospital Name
        self.ui.missions_list_table.setColumnWidth(
            4,
            int(minimum_section_size * 1.5),
        )
        # Date
        self.ui.missions_list_table.setColumnWidth(
            5,
            int(minimum_section_size * 2),
        )
        # Address
        self.ui.missions_list_table.setColumnWidth(
            6,
            int(minimum_section_size * 5),
        )
        # Result
        self.ui.missions_list_table.setColumnWidth(
            7,
            int(minimum_section_size * 3),
        )
