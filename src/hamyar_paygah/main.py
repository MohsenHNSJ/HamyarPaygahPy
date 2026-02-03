"""Application entry point for Hamyar Paygah.

This module contains the startup routine for the application. It ensures
that the EMS server address is loaded from disk or provided by the user
before launching the main Qt window.
"""

# pylint: disable=E0611,I1101
from typing import TYPE_CHECKING

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.controllers.dialogs.server_config_dialog_controller import ServerConfigDialog

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


def main() -> None:
    """Application startup routine.

    This function handles the following tasks:
    1. Attempt to load the EMS server address from persistent storage.
    2. If no server address exists, open a dialog for the user to enter one.
    3. If a server address is provided launch the main application window.
    4. If no server address is available, show an error message and exit.
    """
    # Attempt to load the server URL from the saved configuration
    server_url: str | None = load_server_address()

    # Create an instance of QUiLoader
    loader = QUiLoader()
    # Create the QApplication instance
    app = QApplication([])

    # If server URL is not present, ask the user to input it
    if not server_url:
        server_config_dialog = ServerConfigDialog()
        server_config_dialog.open()
        # Else, show the main window directly
    else:
        # Load the UI file
        window: QWidget = loader.load(
            "src/hamyar_paygah/new_ui/main_menu.ui",
            None,
        )

        # Show the main window
        window.show()

    # Start the application's event loop
    app.exec()


if __name__ == "__main__":
    main()
