"""Main application window for Hamyar Paygah.

This module defines the primary Tkinter window of the application. It
handles launching the Missions List window and the Options window.

Classes:
    MainWindow: The main application window that serves as the entry point
                for user interactions.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from hamyar_paygah.localization.language_manager import LanguageManager
from hamyar_paygah.ui.missions_list_window import MissionsListWindow
from hamyar_paygah.ui.options_window import OptionsWindow


class MainWindow(tk.Tk):
    """Main Tkinter window of the Hamyar Paygah application.

    This window displays a welcome message and provides buttons to:
        - Open the Missions List window.
        - Open the Options window for changing settings such as language.
    """

    def __init__(self, input_server_address: str) -> None:
        """Initialize the main application window.

        Args:
            input_server_address: The EMS server address to use for Missions List.
        """
        super().__init__()

        # Load saved or default language
        LanguageManager.load_language()  # Load the chosen language

        # Set window title and size
        self.title(LanguageManager.t(lambda t: t.main_window_title))
        self.geometry("400x200")

        # Store server URL for Missions List window
        self.input_server_address: str = input_server_address

        # Welcome label
        ttk.Label(
            self,
            text=LanguageManager.t(
                lambda t: t.welcome_label,
            ),
        ).pack(pady=20)

        # Reference to windows window (None if not open)
        self._missions_window: MissionsListWindow | None = None
        self._options_window: OptionsWindow | None = None

        # Button to open Missions List window
        open_btn = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.main_window_missions_list_button,
            ),
            command=self.open_missions_list_window,
        )
        open_btn.pack(pady=10)

        # Button to open Options window
        options_btn = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.main_window_options_button,
            ),
            command=self.open_options_window,
        )
        options_btn.pack(pady=10)

    def open_missions_list_window(self) -> None:
        """Open the Missions List window.

        If the window is already open, it does nothing.
        If opening the window fails (e.g., Tkinter error), shows an error dialog.
        """
        if self._missions_window and self._missions_window.winfo_exists():
            # Window already exists; do not open a duplicate
            return

        # Create a new Missions List window
        try:
            self._missions_window = MissionsListWindow(
                server_address=self.input_server_address,
                master=self,
            )
        except tk.TclError as e:
            # Show error if the window cannot be created
            messagebox.showerror(
                LanguageManager.t(lambda t: t.error_label),
                f"Could not open Missions List window:\n{e}",
            )
            self._missions_window = None

    def open_options_window(self) -> None:
        """Open the Options window for changing application settings.

        If the window is already open, it does nothing.
        If opening the window fails (e.g., Tkinter error), shows an error dialog.
        """
        if self._options_window and self._options_window.winfo_exists():
            # Window already exists; do not open a duplicate
            return

        # Create a new Options window
        try:
            self._options_window = OptionsWindow(self)
        except tk.TclError as e:
            # Show error if the window cannot be created
            messagebox.showerror(
                LanguageManager.t(lambda t: t.error_label),
                f"Could not open options list window:\n{e}",
            )
            self._options_window = None
