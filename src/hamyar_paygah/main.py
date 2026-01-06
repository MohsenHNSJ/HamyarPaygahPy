"""Application entry point for Hamyar Paygah.

This module contains the startup routine for the application. It ensures
that the EMS server address is loaded from disk or provided by the user
before launching the main Tkinter window.
"""

import tkinter as tk
from tkinter import messagebox

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.localization.language_manager import LanguageManager
from hamyar_paygah.ui.dialogs.server_config_dialog import ServerConfigDialog
from hamyar_paygah.ui.main_window import MainWindow


def main() -> None:
    """Application startup routine.

    This function handles the following tasks:
    1. Attempt to load the EMS server address from persistent storage.
    2. If no server address exists, open a modal dialog for the user to
       enter one.
    3. If a server address is provided (either loaded or entered by the user),
       launch the main application window.
    4. If no server address is available, show an error message and exit.

    The function uses a hidden Tkinter root window to manage modal dialogs
    without displaying an unnecessary main window during configuration.
    """
    # Attempt to load the server URL from the saved configuration
    server_url: str | None = load_server_address()
    # Create a hidden Tkinter root for modal dialogs
    root = tk.Tk()
    root.withdraw()  # Hide main window while config dialog is active

    if not server_url:
        # Ask the user to input server address via a modal dialog
        dialog = ServerConfigDialog(master=root)  # type: ignore[arg-type]
        root.wait_window(dialog)
        server_url = dialog.server_address  # Retrieve the entered server URL

    if not server_url:
        # No server URL provided, show error and exit
        messagebox.showerror(
            LanguageManager.t(
                lambda t: t.error_label,
            ),
            LanguageManager.t(
                lambda t: t.server_address_not_provided_error_message,
            ),
        )
    else:
        # Close hidden root and launch main application window
        root.destroy()  # close the hidden root
        app = MainWindow(server_url)
        app.mainloop()


if __name__ == "__main__":
    main()
