"""Controller for mission details tab."""

# pylint: disable=E0611,I1101,R0903
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget
from qasync import asyncSlot  # type: ignore[import-untyped]

import hamyar_paygah.new_ui.widgets.mission_details_tab as ui_mdt
from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.services.mission_details_service import get_mission_details

if TYPE_CHECKING:
    from hamyar_paygah.models.mission_details_model import MissionDetails


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
        # Get mission details from server
        mission_details: MissionDetails = await get_mission_details(
            str(load_server_address()),
            int(self.ui.mission_id_line_edit.text()),
            int(self.ui.patient_id_line_edit.text()),
        )

        # Populate the name field
        self.ui.patient_name_field.setText(
            mission_details.information.patient_name,
        )
        # Populate age field
        self.ui.age_field.setText(mission_details.information.full_age)
        # Set nationality
        if mission_details.information.iranian_nationality:
            self.ui.iranian_nationality_checkBox.setChecked(True)
        else:
            self.ui.foreign_nationality_checkBox.setChecked(True)
