"""Main application window for the Hamyar Paygah project.

This module defines a simple Tkinter main window that serves as the
entry point of the application.

Classes:
    MainWindow: The primary Tkinter window of the application.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from hamyar_paygah.config.server_config import load_server_address
from hamyar_paygah.localization.language_manager import LANG_MAP, LanguageManager
from hamyar_paygah.missions_list_ui import MissionsListApp
from hamyar_paygah.ui.dialogs.server_config_dialog import ServerConfigDialog


class MainWindow(tk.Tk):
    """Main Tkinter window of the application."""

    def __init__(self, input_server_url: str) -> None:
        """Initialize the main window."""
        super().__init__()
        LanguageManager.load_language()  # Load the chosen language
        self.title(LanguageManager.t(lambda t: t.main_window_title))
        self.geometry("400x200")
        self.input_server_url: str = input_server_url

        ttk.Label(
            self,
            text=LanguageManager.t(
                lambda t: t.welcome_label,
            ),
        ).pack(pady=20)

        self._missions_window: MissionsListApp | None = None

        open_btn = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_window_load_missions_button,
            ),
            command=self.open_missions_list_window,
        )
        open_btn.pack(pady=10)

        # Options button for changing UI language
        options_btn = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.main_window_options_button,
            ),
            command=self.open_options_window,
        )
        options_btn.pack(pady=10)

    def open_missions_list_window(self) -> None:
        """Opens the Missions List window if it is not already open.

        If the window already exists, brings it to the front.
        """
        if self._missions_window and self._missions_window.winfo_exists():
            # Window already exists
            return

        # Create a new Missions List window
        try:
            self._missions_window = MissionsListApp(
                server_url=self.input_server_url,
                master=self,
            )
        except tk.TclError as e:
            messagebox.showerror(
                "Error",
                f"Could not open Missions List window:\n{e}",
            )
            self._missions_window = None

    def open_options_window(self) -> None:
        """Open the Options window."""
        OptionsWindow(self)


class OptionsWindow(tk.Toplevel):
    """Window for changing application settings (currently only language)."""

    def __init__(self, parent: tk.Tk) -> None:
        """Initializer."""
        super().__init__(parent)
        self.title(LanguageManager.t(lambda t: t.options_window_title))
        self.resizable(width=False, height=False)

        tk.Label(self, text=LanguageManager.t(lambda t: t.options_window_language_label)).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.lang_var = tk.StringVar(
            value=LanguageManager.current_language_code,
        )
        lang_dropdown = ttk.Combobox(
            self,
            textvariable=self.lang_var,
            values=list(LANG_MAP.keys()),
            state="readonly",
        )
        lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

        save_button = tk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.save_button,
            ),
            command=self.save_and_restart,
        )
        save_button.grid(row=1, column=0, columnspan=2, pady=10)

    def save_and_restart(self) -> None:
        """Shows a message box."""
        LanguageManager.set_language(self.lang_var.get())
        messagebox.showinfo(
            "Info",
            "Language saved. Please restart the application.",
        )
        self.destroy()


if __name__ == "__main__":
    # Load server URL from disk or ask user
    server_url: str | None = load_server_address()
    root = tk.Tk()
    root.withdraw()  # hide main window while config dialog opens

    if not server_url:
        dialog = ServerConfigDialog(master=root)  # type: ignore[arg-type]
        root.wait_window(dialog)
        server_url = dialog.server_address

    if not server_url:
        messagebox.showerror("Error", "No server address provided. Exiting.")
    else:
        root.destroy()  # close the hidden root
        app = MainWindow(server_url)
        app.mainloop()
