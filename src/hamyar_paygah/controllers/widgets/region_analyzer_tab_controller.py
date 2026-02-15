"""Controller for the region analyzer tab."""

# pylint: disable=E0611,I1101,R0903,C0103

from PySide6.QtCore import QCalendar, QDate
from PySide6.QtWidgets import QWidget

import hamyar_paygah.new_ui.widgets.region_analyzer_tab as ui_rat
from hamyar_paygah.models.region_model import Region


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
