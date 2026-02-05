"""Application entry point for Hamyar Paygah.

This module contains the startup routine for the application. It ensures
that the EMS server address is loaded from disk or provided by the user
before launching the main Qt window.
"""

# pylint: disable=E0611,I1101
import asyncio
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop  # type: ignore[import-untyped]

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.controllers.dialogs.server_config_dialog_controller import ServerConfigDialog
from hamyar_paygah.controllers.main_menu_controller import MainMenu

if TYPE_CHECKING:
    from PySide6.QtWidgets import QMainWindow


async def main(app: QApplication) -> None:
    """Asynchronous entry point for the Qt application.

    This function integrates Qt's application lifecycle with Python's
    asyncio event loop. It establishes a synchronization mechanism that
    allows asynchronous tasks to detect when the Qt application is
    about to shut down and perform a graceful cleanup.

    The function is designed to run inside an asyncio-compatible
    event loop (e.g., ``qasync.QEventLoop``), enabling seamless
    cooperation between Qt's event-driven architecture and asyncio's
    coroutine-based concurrency model.

    Args:
        app (QApplication): The active Qt application instance whose
            lifecycle is monitored for shutdown events.
    """
    # Signal application shutdown.
    app_close_event = asyncio.Event()
    # Connect Qt's shutdown signal to the asyncio shutdown event.
    app.aboutToQuit.connect(app_close_event.set)

    # Attempt to load the server URL from the saved configuration
    server_url: str | None = load_server_address()

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

    # Start the application's shared event loop and wait until closed
    await app_close_event.wait()


if __name__ == "__main__":
    # Create the QApplication instance
    main_app = QApplication([])

    # Call the main function to start the application event loop
    asyncio.run(main(main_app), loop_factory=QEventLoop)
