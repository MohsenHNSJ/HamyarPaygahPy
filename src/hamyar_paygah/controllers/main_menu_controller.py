"""Controller for main menu UI."""

# ruff: noqa: DTZ001
# pylint: disable=E0611,I1101,R0903,C0103
from datetime import datetime
from typing import TYPE_CHECKING

from PySide6.QtCore import QCalendar, QDate, QSortFilterProxyModel, Qt, Slot
from PySide6.QtWidgets import QMainWindow
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.main_menu as main_menu_ui
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.models.region_model import Region
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.view_models.mission_table_model import MissionTableModel

if TYPE_CHECKING:
    from hamyar_paygah.models.mission_model import Mission


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
        self.populate_region_picker()

        # TODO@MohsenHNSJ: Set a default space for table columns and rows  # noqa: TD003

    @Slot(QDate)
    def on_from_date_picker_userDateChanged(self, new_date: QDate) -> None:  # noqa: N802
        """Ensure from date is always equal or less than the to date.

        Args:
            new_date (QDate): User input date when from date picker is changed.
        """
        # Check if the new date is greater than to date
        if new_date > self.ui.to_date_picker.date():  # type: ignore[]
            # If so, set the to date the same as from date
            self.ui.to_date_picker.setDate(new_date)

    @asyncSlot()  # type: ignore[misc]
    async def on_load_button_clicked(self) -> None:
        """Loads the list of missions from server and populates the table."""
        # Convert Persian dates to gregorian dates
        gregorian_from_date: QDate = self.ui.from_date_picker.date()
        gregorian_to_date: QDate = self.ui.to_date_picker.date()

        # Convert from date and to date to normal pythonic dates
        pythonic_from_date: datetime = datetime(
            gregorian_from_date.year(),
            gregorian_from_date.month(),
            gregorian_from_date.day(),
        )
        pythonic_to_date: datetime = datetime(
            gregorian_to_date.year(),
            gregorian_to_date.month(),
            gregorian_to_date.day(),
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

        # Create the model for table view
        source_model = MissionTableModel(missions_list)

        # Proxy the model to enable sorting and filtering
        proxy_model = QSortFilterProxyModel(self)
        proxy_model.setSourceModel(source_model)
        # Set proxy model to be case insensitive
        proxy_model.setSortCaseSensitivity(
            Qt.CaseInsensitive,
        )  # type: ignore[attr-defined]

        # Set the model to table
        self.ui.missions_list_table.setModel(proxy_model)

    def populate_region_picker(self) -> None:
        """Populates the region picker with regions dictionary."""
        # Define available regions
        available_regions: list[Region] = [
            Region("1", 1),
            Region("2", 2),
            Region("3", 3),
            Region("4", 4),
            Region("عباس آباد", 5),
        ]

        # Populate the region picker
        for region in available_regions:
            self.ui.region_picker.addItem(region.region_name, region.region_id)

        # Set initial selected item to first item
        self.ui.region_picker.setCurrentIndex(0)
