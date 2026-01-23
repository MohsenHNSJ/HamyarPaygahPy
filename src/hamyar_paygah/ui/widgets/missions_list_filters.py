"""Missions List Filters UI Module.

This module provides the `MissionsListFilters` widget, a reusable
Tkinter panel for collecting and validating mission search filters.

Responsibilities:
    - Rendering filter input fields for querying missions:
    - Performing live input validation (numeric check for Region ID)
    - Converting user input into strongly-typed Python values
    - Displaying error dialogs for invalid or missing input
    - Integrating seamlessly with other UI components without performing any data fetching

Typical Usage:
    from hamyar_paygah.ui.widgets.missions_list_filters import MissionsListFilters

    root = tk.Tk()
    filters_panel = MissionsListFilters(root)
    filters_panel.pack()

    # Later, retrieve validated filter values
    result = filters_panel.get_filters()
    if result is not None:
        from_date, to_date, region_id = result

Notes:
    - This widget is UI-only and does not handle networking.
    - Error messages are localized via LanguageManager.
"""

from __future__ import annotations

import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING

import jdatetime  # type: ignore[import-untyped]
from tkcalendar import DateEntry  # type: ignore[import-untyped]

from hamyar_paygah.localization.language_manager import (
    LanguageManager,  # type: ignore[import-untyped]
)

if TYPE_CHECKING:
    from collections.abc import Callable


class MissionsListFilters(ttk.Frame):
    """UI panel for collecting mission search filters.

    This widget encapsulates all filter-related UI elements used to
    query missions. It is responsible only for:

    - Rendering filter input fields
    - Validating user input
    - Returning parsed filter values
    """

    def __init__(self, master: tk.Misc, on_load_clicked: Callable[[], None]) -> None:
        """Initialize the filters panel.

        Args:
            master: Parent Tkinter widget.
            on_load_clicked: Callable to call when load button is clicked.
        """
        super().__init__(master)
        # Set up the connection for load button function
        self._on_load_clicked = on_load_clicked
        # Build and lay out all UI elements
        self._build_ui()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        """Create and arrange filter input widgets.

        This method constructs:
        - From date picker
        - To date picker
        - Region ID entry with numeric validation
        """
        # From date label and date picker
        ttk.Label(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_list_from_date_label,
            )
            + ":",
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )
        self.from_date = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.from_date.grid(row=0, column=1, padx=5, pady=5)

        # To date label and date picker
        ttk.Label(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_list_to_date_label,
            )
            + ":",
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
        )
        self.to_date = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.to_date.grid(row=0, column=3, padx=5, pady=5)

        # Region ID label and entry field
        ttk.Label(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_list_region_id_label,
            )
            + ":",
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
        )
        self.region_id_var = tk.StringVar()

        region_entry = ttk.Entry(self, textvariable=self.region_id_var)
        region_entry.grid(row=0, column=5, padx=5, pady=5)

        # Validate input on each keystroke to allow only digits
        region_entry.config(
            validate="key",
            validatecommand=(self.register(self._validate_int), "%P"),
        )

        # Load button
        self.load_button = ttk.Button(
            self,
            text=LanguageManager.t(
                lambda t: t.missions_list_load_missions_button,
            ),
            command=self._on_load_clicked,
        )
        self.load_button.grid(row=0, column=6, padx=10, pady=5)

        # --- Jalali date labels (only for Persian language) ---
        self._show_jalali = LanguageManager.current_language_code == ("Persian")

        # Show only when Persian language is selected
        if self._show_jalali:
            # From date label
            self.from_jalali_label = ttk.Label(self, text="")
            self.from_jalali_label.grid(
                row=1,
                column=1,
                padx=5,
                pady=(0, 5),
                sticky="w",
            )
            # To date label
            self.to_jalali_label = ttk.Label(self, text="")
            self.to_jalali_label.grid(
                row=1,
                column=3,
                padx=5,
                pady=(0, 5),
                sticky="w",
            )

            # Initial update
            self._update_jalali_labels()

            # Update when date changes
            self.from_date.bind(
                "<<DateEntrySelected>>",
                self._on_date_changed,
            )
            self.to_date.bind(
                "<<DateEntrySelected>>",
                self._on_date_changed,
            )

        # Align nicely
        self.grid_columnconfigure(6, weight=1)

    # ------------------------------------------------------------------
    # Validation & data extraction
    # ------------------------------------------------------------------

    def _validate_int(self, value: str) -> bool:
        """Validate that a string contains only digits.

        Args:
            value: Current contents of the entry field.

        Returns:
            True if the value is empty or numeric, False otherwise.
        """
        return value.isdigit() or value == ""

    def get_filters(self) -> tuple[datetime, datetime, int] | None:
        """Return validated filter values entered by the user.

        This method performs final validation and converts UI input
        into strongly-typed Python values suitable for business logic.

        Displays error dialogs for invalid or missing fields.

        Returns: tuple: A tuple containing: from_date (datetime) to_date (datetime) region_id (int)
        """
        # Ensure required fields are present
        if not self.from_date.get():
            messagebox.showerror(
                LanguageManager.t(
                    lambda t: t.error_label,
                ),
                LanguageManager.t(
                    lambda t: t.missions_list_from_date_is_required_error_message,
                ),
            )
            return None

        if not self.to_date.get():
            messagebox.showerror(
                LanguageManager.t(
                    lambda t: t.error_label,
                ),
                LanguageManager.t(
                    lambda t: t.missions_list_to_date_is_required_error_message,
                ),
            )
            return None

        if not self.region_id_var.get():
            messagebox.showerror(
                LanguageManager.t(
                    lambda t: t.error_label,
                ),
                LanguageManager.t(
                    lambda t: t.missions_list_region_id_is_required_error_message,
                ),
            )
            return None

        # Convert region ID to integer
        try:
            region_id = int(self.region_id_var.get())
        except ValueError:
            messagebox.showerror(
                LanguageManager.t(
                    lambda t: t.error_label,
                ),
                LanguageManager.t(
                    lambda t: t.missions_list_region_id_invalid_error_message,
                ),
            )
            return None

        # Parse dates from string input
        from_date = datetime.strptime(self.from_date.get(), "%Y-%m-%d")  # noqa: DTZ007
        to_date = datetime.strptime(self.to_date.get(), "%Y-%m-%d")  # noqa: DTZ007

        return from_date, to_date, region_id

    # ------------------------------------------------------------------
    # Jalali calendar
    # ------------------------------------------------------------------
    # pylint: disable=W0613
    def _on_date_changed(self, _: DateEntry) -> None:
        # Release dangling grab First
        self._release_any_grab()

        # Restore focus to the main window, not the DateEntry
        self.focus_set()

        if self._show_jalali:
            self._update_jalali_labels()

    def _update_jalali_labels(self) -> None:
        """Update Jalali date labels based on selected Gregorian dates."""
        try:
            from_dt = datetime.strptime(self.from_date.get(), "%Y-%m-%d")  # noqa: DTZ007
            to_dt = datetime.strptime(self.to_date.get(), "%Y-%m-%d")  # noqa: DTZ007
        except ValueError:
            # Date not fully selected yet
            return

        from_jalali = jdatetime.date.fromgregorian(date=from_dt.date())
        to_jalali = jdatetime.date.fromgregorian(date=to_dt.date())

        self.from_jalali_label.config(
            text=from_jalali.strftime("%Y/%m/%d"),
        )

        self.to_jalali_label.config(
            text=to_jalali.strftime("%Y/%m/%d"),
        )

    def _release_any_grab(self) -> None:
        try:
            current = self.grab_current()  # type: ignore[no-untyped-call]
            if current is not None:
                current.grab_release()
        except tk.TclError:
            pass
