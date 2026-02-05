"""Controller for mission details tab."""

# pylint: disable=E0611,I1101,R0903
from PySide6.QtWidgets import QWidget

import hamyar_paygah.new_ui.widgets.mission_details_tab as ui_mdt


class MissionsDetailsTab(QWidget):
    """Tab that enables user to retrieve details of a mission."""

    def __init__(self) -> None:
        """Initialize the mission details tab UI."""
        super().__init__()

        # Set up the UI
        self.ui = ui_mdt.Ui_mission_details_tab()  # type: ignore[attr-defined]
        self.ui.setupUi(self)
