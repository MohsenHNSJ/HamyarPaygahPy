"""Missions List Window Module.

This module defines a Tkinter-based UI window for displaying and
interacting with a list of EMS missions. It separates UI concerns
from networking and data parsing, delegating fetching and parsing
to service functions.

Classes:
    MissionsListWindow: Main UI window for displaying missions with
        filter panel, data table, and asynchronous loading.
"""

import asyncio
import threading
import tkinter as tk
from tkinter import messagebox, ttk

from aiohttp import ClientError

# pylint: disable=I1101
from lxml import etree

from hamyar_paygah.localization.language_manager import LanguageManager
from hamyar_paygah.services.missions_list_service import get_missions_list
from hamyar_paygah.ui.widgets.missions_list_filters import MissionsListFilters
from hamyar_paygah.ui.widgets.missions_list_table import MissionsListTable

_MISSIONS_LIST_STARTING_WINDOW_SIZE: str = "1200x700"


class MissionsListWindow(tk.Toplevel):
    """Tkinter window for displaying missions with filters and table.

    This window encapsulates all UI elements, user interactions,
    and orchestrates async data fetching while keeping the UI responsive.

    Attributes:
        server_address (str): Base URL of the EMS server to fetch missions from.
        filters_panel (MissionsListFilters): Widget panel for inputting query filters.
        table (MissionsListTable): Widget for displaying mission data.
        status_label (ttk.Label): Label showing status messages.
        load_button (ttk.Button): Button to trigger mission loading.
    """

    _MISSIONS_LIST_STARTING_WINDOW_SIZE: str = "1200x700"

    def __init__(self, master: tk.Misc, server_address: str) -> None:
        """Initialize the missions list window and layout UI components.

        Args:
            master (tk.Misc): Parent Tkinter widget.
            server_address (str): URL of the server to fetch mission data from.
        """
        super().__init__(master)
        self.title(LanguageManager.t(lambda t: t.missions_list_window_title))
        self.geometry(_MISSIONS_LIST_STARTING_WINDOW_SIZE)
        self.server_address = server_address

        # --- UI components ---
        # Filter panel for inputting date range and region
        self.filters_panel = MissionsListFilters(self)
        self.filters_panel.pack(fill="x", padx=10, pady=5)

        # Table for displaying missions
        self.table = MissionsListTable(self)
        self.table.pack(fill="both", expand=True, padx=10, pady=5)

        # Status label for showing messages like "Loading..."
        self.status_label = ttk.Label(self, text="")
        self.status_label.pack(anchor="w", padx=10, pady=5)

        # Load button to trigger fetching missions
        self.load_button = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_list_load_missions_button,
            ),
            command=self.on_load_clicked,
        )
        self.load_button.pack(pady=5)

    # ------------------------------------------------------------------
    # Button callback
    # ------------------------------------------------------------------

    def on_load_clicked(self) -> None:
        """Handle the Load Missions button click safely in a background thread.

        Since Tkinter does not support async directly in button callbacks,
        this method runs the async `_load_missions` in a separate thread
        using `asyncio.run`.
        """

        def runner() -> None:
            asyncio.run(self._load_missions())

        threading.Thread(target=runner, daemon=True).start()

    # ------------------------------------------------------------------
    # Async data fetching
    # ------------------------------------------------------------------

    async def _load_missions(self) -> None:
        """Fetch missions asynchronously and update the UI.

        Performs the following steps:
        1. Show loading state in UI.
        2. Retrieve filters from the filter panel.
        3. Fetch missions from the server asynchronously.
        4. Populate the table with fetched missions.
        5. Handle errors and finalize UI state.
        """
        try:
            # Show loading UI
            self.after(0, self._on_loading_start)

            # Get user-selected filters
            filters = self.filters_panel.get_filters()

            if filters is None:
                # Validation failed, reset UI
                self.after(0, lambda: self._on_loading_done)
                return  # User error already shown

            from_date, to_date, region_id = filters

            # Fetch missions list asynchronously
            missions_list = await get_missions_list(
                self.server_address,
                from_date,
                to_date,
                region_id,
            )
            # Update table in main thread
            self.after(0, lambda: self.table.populate(missions_list))

        except (ClientError, TimeoutError) as network_exc:
            # Network-related error
            self._on_error(network_exc)

        except (ValueError, etree.XMLSyntaxError) as data_exc:
            # Data parsing/validation errors
            self._on_error(data_exc)
        finally:
            # Reset UI state regardless of success or failure
            self.after(0, self._on_loading_done)

    # ------------------------------------------------------------------
    # UI helpers
    # ------------------------------------------------------------------

    def _on_loading_start(self) -> None:
        """Set UI state to loading mode."""
        self.status_label.config(
            text=LanguageManager.t(
                lambda t: t.missions_list_loading_status_message,
            ),
        )
        self.load_button.config(state="disabled")
        self.table.clear()

    def _on_loading_done(self) -> None:
        """Reset UI state after loading is complete."""
        self.status_label.config(text="")
        self.load_button.config(state="normal")

    def _on_error(self, exception: Exception) -> None:
        """Handle errors by showing a message box.

        Args:
            exception (Exception): The exception that occurred.
        """
        messagebox.showerror(
            title=LanguageManager.t(lambda t: t.error_label),
            message=LanguageManager.t(
                lambda t: t.error_unexpected_message,
            )
            + f"\n{exception}",
        )
