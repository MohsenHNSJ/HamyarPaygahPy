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

CONFIG_FILE = Path("server_config.json")


class ServerConfigDialog(tk.Toplevel):
    """Dialog to request the EMS server address from the user."""

    def __init__(self, master: tk.Tk | None = None) -> None:
        """Initialize the server configuration dialog."""
        super().__init__(master)
        self.title("Server Configuration")
        self.geometry("400x150")
        self.resizable(width=False, height=False)
        self.server_url: str | None = None

        ttk.Label(self, text="Please enter server address:").pack(pady=10)
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=self.entry_var, width=40)
        entry.pack(pady=5)
        entry.focus()

        ok_btn = ttk.Button(self, text="OK", command=self.on_ok)
        ok_btn.pack(pady=10)

        # Center window relative to master
        self.update_idletasks()
        if master:
            x = master.winfo_rootx() + (master.winfo_width() - self.winfo_width()) // 2
            y = master.winfo_rooty() + (master.winfo_height() - self.winfo_height()) // 2
            self.geometry(f"+{x}+{y}")

        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_ok(self) -> None:
        """Handle OK button click."""
        url = self.entry_var.get().strip()
        if not url:
            messagebox.showwarning(
                "Input Error",
                "Server address cannot be empty!",
            )
            return

        self.server_url = url
        self.save_to_disk(url)
        self.destroy()

    def on_close(self) -> None:
        """Handle user closing the dialog without entering a URL."""
        self.server_url = None
        self.destroy()

    @staticmethod
    def save_to_disk(url: str) -> None:
        """Save server address to local disk."""
        with CONFIG_FILE.open("w", encoding="utf-8") as f:
            json.dump({"server_url": url}, f)

    @staticmethod
    def load_from_disk() -> str | None:
        """Load server address from local disk if it exists."""
        if CONFIG_FILE.exists():
            try:
                with CONFIG_FILE.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                    url = data.get("server_url")
                    return url if isinstance(url, str) else None
            except (OSError, json.JSONDecodeError):
                return None
        return None
