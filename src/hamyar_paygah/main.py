"""Application entry point for Hamyar Paygah.

This module contains the startup routine for the application. It ensures
that the EMS server address is loaded from disk or provided by the user
before launching the main Qt window.
"""

# pylint: disable=E0611,I1101
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QApplication

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.controllers.dialogs.server_config_dialog_controller import ServerConfigDialog
from hamyar_paygah.controllers.main_menu_controller import MainMenu

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow


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

    # Create the QApplication instance
    app = QApplication([])

    # Create initial UI elements
    server_config_dialog = ServerConfigDialog()
    main_menu: QMainWindow = MainMenu()

    # If server URL is not present, ask the user to input it
    if not server_url:
        # Connect the dialog's accepted signal to load and show the main window
        server_config_dialog.accepted.connect(main_menu.show)

        # Show the prompt dialog to get server address from user
        server_config_dialog.open()
    else:
        # Else, show the main window directly
        main_menu.show()

    # Start the application's event loop
    app.exec()


if __name__ == "__main__":
    main()
