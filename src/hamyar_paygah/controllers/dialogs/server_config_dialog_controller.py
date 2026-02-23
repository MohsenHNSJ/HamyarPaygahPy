"""Controller for the server configuration dialog."""

# pylint: disable=E0611,I1101,R0903
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from hamyar_paygah.config.server_config import (  # type: ignore[attr-defined]
    is_valid_server_address,
    save_server_address,
)
from hamyar_paygah.new_ui.dialogs.server_config_dialog import (  # type: ignore[attr-defined]
    Ui_ServerConfigDialog,
)


class ServerConfigDialog(QDialog):
    """Controller for server address configuration dialog."""

    @Slot()
    def on_save_button_clicked(self) -> None:
        """Handle save button click event."""
        # Strip the input from whitespace and save it
        server_address: str = self.ui.server_address_input.text().strip()

        # Check if the input server address is valid and not empty
        if not is_valid_server_address(server_address) or not server_address:
            # Show a warning if the address is invalid
            self._show_invalid_input()
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
        self.ui: Ui_ServerConfigDialog = Ui_ServerConfigDialog()
        self.ui.setupUi(self)

        # Set button actions
        self.ui.abort_button.clicked.connect(self.reject)

        # Hide invalid input label initially
        self.ui.invalid_input_label.hide()

        # Connect input text changed signal to hide invalid input label on text change
        self.ui.server_address_input.textChanged.connect(
            self._hide_invalid_input,
        )

    def _show_invalid_input(self) -> None:
        """Display the 'invalid input' warning label in the dialog.

        This method makes the label visible to inform the user
        that the server address entered is invalid. Typically called
        after validation fails.
        """
        self.ui.invalid_input_label.show()

    def _hide_invalid_input(self) -> None:
        """Hide the 'invalid input' warning label in the dialog.

        This method hides the label, typically used when the user
        starts editing the input field or when the dialog is initialized,
        indicating that the previous input is no longer considered invalid.
        """
        self.ui.invalid_input_label.hide()
