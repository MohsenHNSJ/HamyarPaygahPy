"""Tkinter dialogs for server configuration.

This module provides UI components for viewing, editing, and persisting
the EMS server address used by the application. The configuration dialog
is implemented as a modal Tkinter window and integrates with the
application's localization system and configuration storage layer.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from hamyar_paygah.config.server_config import load_server_address, save_server_address
from hamyar_paygah.localization.language_manager import LanguageManager
from hamyar_paygah.utils.text_utils import is_valid_server_address


class ServerConfigDialog(tk.Toplevel):
    """Modal dialog for configuring the EMS server address.

    This dialog allows the user to view and modify the server base address
    used by the application. The address is validated before being saved
    to persistent configuration storage.

    The dialog is modal, blocking interaction with the parent window until
    it is closed. On successful submission, the selected server address
    is stored and made available via the ``server_address`` attribute.
    """

    def __init__(self, master: tk.Tk | None = None) -> None:
        """Initialize the server configuration dialog.

        Args:
            master: Optional parent Tkinter window. If provided, the dialog
                will be centered relative to the parent and behave modally.
        """
        super().__init__(master=master)

        # Configure window appearance
        self.title(LanguageManager.t(lambda t: t.server_config_title))
        self.geometry("400x150")
        self.resizable(width=False, height=False)

        # Holds the confirmed server URL after dialog closes
        self.server_address: str | None = None

        # Prompt label
        ttk.Label(
            self,
            text=LanguageManager.t(lambda t: t.server_config_prompt),
        ).pack(pady=10)

        # Pre-fill entry with previously saved server address (if any)
        self.entry_var = tk.StringVar(value=load_server_address() or "")
        entry = ttk.Entry(self, textvariable=self.entry_var, width=40)
        entry.pack(pady=5)
        entry.focus()

        # Save button
        ttk.Button(
            self,
            text=LanguageManager.t(lambda t: t.save_button),
            command=self._on_ok,
        ).pack(pady=10)

        # Center dialog relative to parent window
        self._center(master)

        # Make dialog modal
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_ok(self) -> None:
        """Validate input, persist server address, and close the dialog.

        If the entered server address is invalid, a warning message is
        displayed and the dialog remains open. On success, the address is
        saved to configuration storage and the dialog closes.
        """
        input_address = self.entry_var.get()

        # Validate server address format before saving
        if not is_valid_server_address(input_address):
            messagebox.showwarning(
                title=LanguageManager.t(
                    lambda t: t.server_config_empty_error_title,
                ),
                message=LanguageManager.t(
                    lambda t: t.server_config_empty_error_msg,
                ),
            )
            return

        # Persist valid server address
        save_server_address(input_address)
        self.server_address = input_address.strip()
        self.destroy()

    def _on_close(self) -> None:
        """Close the dialog without saving changes.

        Destroys the dialog window.
        """
        self.destroy()

    def _center(self, master: tk.Tk | None) -> None:
        """Center the dialog relative to its parent window.

        Args:
            master: Parent Tkinter window to center against. If ``None``,
                no centering is performed.
        """
        # Ensure window size is calculated
        self.update_idletasks()
        if not master:
            return

        # Calculate centered position relative to parent
        x = master.winfo_rootx() + (master.winfo_width() - self.winfo_width()) // 2
        y = master.winfo_rooty() + (master.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
