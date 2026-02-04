"""Controller for the server configuration dialog."""

# pylint: disable=E0611,I1101,R0903
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

import hamyar_paygah.new_ui.dialogs.server_config_dialog as ui_scd
from hamyar_paygah.config.server_config import is_valid_server_address, save_server_address


class ServerConfigDialog(QDialog):
    """Dialog that asks user to input server address."""

    @Slot()
    def on_save_button_clicked(self) -> None:
        """Handle save button click event."""
        # Strip the input from whitespace and save it
        server_address: str = self.ui.server_address_input.text().strip()

        # Check if the input server address is valid
        if not is_valid_server_address(server_address):
            # Show a warning if the address is invalid
            self.ui.invalid_input_label.show()
            # Do not close the dialog
            return

        # Save the server address from the input field
        save_server_address(server_address)

        # Close the dialog with acceptance
        self.accept()

    def __init__(self) -> None:
        """Initialize the server configuration dialog UI."""
        super().__init__()

        # Set up the UI
        self.ui = ui_scd.Ui_ServerConfigDialog()  # type: ignore[attr-defined]
        self.ui.setupUi(self)

        # Set button actions
        self.ui.abort_button.clicked.connect(self.reject)

        # Hide invalid input label initially
        self.ui.invalid_input_label.hide()

        # Connect input text changed signal to hide invalid input label on text change
        self.ui.server_address_input.textChanged.connect(
            self.ui.invalid_input_label.hide,
        )
