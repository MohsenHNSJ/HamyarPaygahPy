"""Manages the EMS server address configuration.

This module provides functionality to:

- Prompt the user for a server address (if none is stored locally).
- Save the server address to a local file for future application runs.
- Load a previously saved server address from disk.
- Ensure type safety and proper validation of stored data.

The server address is stored in a JSON file (`server_config.json`) in the
current working directory. If the file does not exist or contains invalid
data, the application will prompt the user to enter a server address.
"""

import json
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from hamyar_paygah.localization.language_manager import LanguageManager

# Path to the server configuration file
CONFIG_FILE = Path("server_config.json")


class ServerConfigDialog(tk.Toplevel):
    """Modal dialog for configuring and persisting the server address.

    This dialog allows the user to enter the base URL of the EMS server.
    The value is validated, saved to disk, and made available to the
    calling code after the dialog is closed.

    The dialog is modal (grabs focus) and centered relative to its master
    window when provided.
    """

    def __init__(self, master: tk.Tk | None = None) -> None:
        """Initialize the server configuration dialog.

        Args:
            master: Optional parent Tkinter window. If provided, the dialog
                will be centered relative to it and behave modally.
        """
        super().__init__(master=master)
        # Configure the dialog window
        self.title(string=LanguageManager.t(lambda t: t.server_config_title))
        self.geometry(newGeometry="400x150")
        self.resizable(width=False, height=False)

        # Initialize server_url attribute
        self.server_url: str | None = None

        # UI Elements
        # Prompt label
        ttk.Label(
            master=self,
            text=LanguageManager.t(
                lambda t: t.server_config_prompt,
            ),
        ).pack(pady=10)
        # Entry field for server address
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(master=self, textvariable=self.entry_var, width=40)
        entry.pack(pady=5)
        entry.focus()

        # OK button
        ok_btn = ttk.Button(
            master=self,
            text=LanguageManager.t(
                lambda t: t.save_button,
            ),
            command=self.on_ok,
        )
        ok_btn.pack(pady=10)

        # Center window relative to master
        self.update_idletasks()
        if master:
            x: int = master.winfo_rootx() + (master.winfo_width() - self.winfo_width()) // 2
            y: int = master.winfo_rooty() + (master.winfo_height() - self.winfo_height()) // 2
            self.geometry(newGeometry=f"+{x}+{y}")

        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_ok(self) -> None:
        """Validate the input, persist it, and close the dialog.

        If the server URL field is empty, a warning message is shown and
        the dialog remains open. On success, the URL is saved to disk and
        the dialog is closed.
        """
        url: str = self.entry_var.get().strip()
        if not url:
            messagebox.showwarning(
                title=LanguageManager.t(
                    lambda t: t.server_config_empty_error_title,
                ),
                message=LanguageManager.t(
                    lambda t: t.server_config_empty_error_msg,
                ),
            )
            return

        self.server_url = url
        self.save_to_disk(url)
        self.destroy()

    def on_close(self) -> None:
        """Handle dialog close without saving.

        This method is invoked when the user closes the window using the
        window manager controls. The stored server URL is cleared and the
        dialog is destroyed.
        """
        self.server_url = None
        self.destroy()

    @staticmethod
    def save_to_disk(url: str) -> None:
        """Persist the server URL to the configuration file.

        Args:
            url: Server base URL to store on disk.
        """
        with CONFIG_FILE.open("w", encoding="utf-8") as f:
            json.dump({"server_url": url}, f)

    @staticmethod
    def load_from_disk() -> str | None:
        """Load the server URL from the configuration file.

        Returns:
            The stored server URL if present and valid, otherwise ``None``.
            Returns ``None`` if the file does not exist or cannot be read.
        """
        if CONFIG_FILE.exists():
            try:
                with CONFIG_FILE.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                    url = data.get("server_url")
                    return url if isinstance(url, str) else None
            except (OSError, json.JSONDecodeError):
                return None
        return None
