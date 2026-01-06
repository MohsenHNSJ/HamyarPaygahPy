"""Tkinter window for configuring application options.

This module provides a GUI for users to view and modify application settings.
It separates the UI (OptionsWindow) from the logic (OptionsConfig) so that
the logic can be reused or tested independently of the GUI.

Classes:
    OptionsWindow: A modal window allowing users to change the application options.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from hamyar_paygah.config.options_config import OptionsConfig
from hamyar_paygah.localization.language_manager import LanguageManager


class OptionsWindow(tk.Toplevel):
    """Window for changing application settings.

    This window provides a dropdown to select the interface language and a
    button to save the change. It uses OptionsConfig as the controller to
    handle logic separate from the UI.
    """

    def __init__(self, parent: tk.Tk) -> None:
        """Initialize the options window.

        Args:
            parent (tk.Tk): The parent Tkinter window to attach this window to.
        """
        # Instantiate the logic controller
        super().__init__(parent)
        self.controller: OptionsConfig = OptionsConfig()
        """The logic handler for application options."""

        # Window configuration
        self.title(string=LanguageManager.t(lambda t: t.options_window_title))
        self.resizable(width=False, height=False)

        # Label for language selection
        tk.Label(
            self,
            text=LanguageManager.t(lambda t: t.options_window_language_label),
        ).grid(row=0, column=0, padx=10, pady=10)

        # Dropdown for selecting language
        self.lang_var = tk.StringVar(value=self.controller.current_language)
        """Holds the currently selected language code in the dropdown."""
        lang_dropdown = ttk.Combobox(
            self,
            textvariable=self.lang_var,
            values=self.controller.available_languages,
            state="readonly",
        )
        lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Save button to apply selected language
        save_button = tk.Button(
            self,
            text=LanguageManager.t(lambda t: t.save_button),
            command=self._on_save,
        )
        save_button.grid(row=1, column=0, columnspan=2, pady=10)

    def _on_save(self) -> None:
        """Save the selected language using the controller.

        Attempts to update the application language using OptionsConfig. If
        the language code is invalid, shows an error message to the user.

        Raises:
            ValueError: If the selected language code is invalid. This is
                caught and shown in a messagebox instead of propagating.
        """
        try:
            self.controller.set_language(self.lang_var.get())
            self.destroy()
        except ValueError as e:
            messagebox.showerror(title="Error", message=str(e))
