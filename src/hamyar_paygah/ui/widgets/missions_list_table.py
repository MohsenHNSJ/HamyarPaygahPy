"""Missions List Table Module.

This module defines the `MissionsListTable` widget used in the missions UI.
It encapsulates the table display, sorting, and data population logic.

Responsibilities:
- Display a table of missions with relevant columns
- Support sorting by column
- Populate rows with mission data
- Provide a simple API for clearing and updating the table

Dependencies:
- Tkinter `ttk` widgets
- `reshape_rtl` from text_utils for proper display of RTL text
"""

from __future__ import annotations

from tkinter import ttk
from typing import TYPE_CHECKING

from hamyar_paygah.localization.language_manager import LanguageManager
from hamyar_paygah.utils.text_utils import reshape_rtl

if TYPE_CHECKING:
    import tkinter as tk
    from collections.abc import Callable

    from hamyar_paygah.models.mission_model import Mission


class MissionsListTable(ttk.Frame):
    """Table widget for displaying a list of missions.

    This widget handles:
    - UI creation of the table with headers and scrollbars
    - Sorting by any column
    - Populating the table with `Mission` objects
    - Clearing the table
    """

    def __init__(self, master: tk.Misc) -> None:
        """Initialize the missions list table.

        Args:
            master: Parent Tkinter widget.
        """
        super().__init__(master)

        # Track current sorted column and direction
        self._sort_column: str | None = None
        self._sort_reverse: bool = False

        # Table columns
        self._columns: list[str] = [
            LanguageManager.t(lambda t: t.missions_list_mission_id_label),
            LanguageManager.t(lambda t: t.missions_list_patient_name_label),
            LanguageManager.t(lambda t: t.missions_list_patient_id_label),
            LanguageManager.t(lambda t: t.missions_list_ambulance_code_label),
            LanguageManager.t(lambda t: t.missions_list_hospital_name_label),
            LanguageManager.t(lambda t: t.missions_list_date_label),
            LanguageManager.t(lambda t: t.missions_list_persian_date_label),
            LanguageManager.t(lambda t: t.missions_list_address_label),
            LanguageManager.t(lambda t: t.missions_list_result_label),
        ]
        # Optional custom widths for columns
        self._column_widths: dict[str, int] = {
            LanguageManager.t(lambda t: t.missions_list_mission_id_label): 80,
            LanguageManager.t(lambda t: t.missions_list_patient_name_label): 200,
            LanguageManager.t(lambda t: t.missions_list_patient_id_label): 80,
            LanguageManager.t(lambda t: t.missions_list_ambulance_code_label): 80,
            LanguageManager.t(lambda t: t.missions_list_hospital_name_label): 150,
            LanguageManager.t(lambda t: t.missions_list_date_label): 120,
            LanguageManager.t(lambda t: t.missions_list_persian_date_label): 120,
            LanguageManager.t(lambda t: t.missions_list_address_label): 250,
            LanguageManager.t(lambda t: t.missions_list_result_label): 150,
        }

        self._build_ui()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        """Create and arrange the Treeview and its scrollbars."""
        self.tree = ttk.Treeview(
            self,
            columns=self._columns,
            show="headings",
            style="Missions.Treeview",
        )

        # Configure Treeview style (important for displaying Persian text)
        style = ttk.Style()
        style.configure(
            "Missions.Treeview",
            font=("Tahoma", 11),
            rowheight=25,
        )

        # Set up headings and column widths
        for column in self._columns:
            self.tree.heading(
                column,
                text=column,
                command=self._make_sort_callback(column),  # Enable sorting
            )
            self.tree.column(
                column,
                width=self._column_widths.get(column, 120),
                anchor="center",
            )

        # Alternating row colors for readability
        self.tree.tag_configure("odd", background="white")
        self.tree.tag_configure("even", background="#f0f0ff")

        # Vertical scrollbar
        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview,
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(expand=True, fill="both")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """Remove all rows from the table."""
        for row in self.tree.get_children():
            self.tree.delete(row)

    def populate(self, missions: list[Mission]) -> None:
        """Fill the table with a list of Mission objects.

        Args:
            missions: List of `Mission` instances to display.

        The function alternates row colors and applies `reshape_rtl` to text
        fields to support right-to-left languages like Persian.
        """
        self.clear()

        for index, mission in enumerate(missions):
            tag = "even" if index % 2 == 0 else "odd"

            self.tree.insert(
                "",
                "end",
                values=(
                    mission.id,
                    reshape_rtl(mission.patient_name),
                    mission.patient_id,
                    mission.ambulance_code,
                    reshape_rtl(mission.hospital_name or ""),
                    mission.date,
                    mission.persian_date,
                    reshape_rtl(mission.address),
                    reshape_rtl(mission.result),
                ),
                tags=(tag,),
            )

    # ------------------------------------------------------------------
    # Sorting logic
    # ------------------------------------------------------------------

    def _make_sort_callback(self, column: str) -> Callable[[], None]:
        """Return a callback function that sorts the table by a given column.

        Args:
            column: Name of the column to sort.

        Returns:
            Callable function to be used as Treeview heading command.
        """

        def callback() -> None:
            self._sort_by_column(column)

        return callback

    def _sort_by_column(self, column: str) -> None:
        """Sort the table rows by the specified column.

        Numeric columns are sorted numerically, others alphabetically.

        Args:
            column: Name of the column to sort.
        """
        rows = [(self.tree.set(k, column), k) for k in self.tree.get_children()]

        # Determine sort order: reverse if same column as last click
        reverse = not self._sort_reverse if self._sort_column == column else False

        try:
            # Attempt numeric sort
            rows.sort(
                key=lambda item: float(item[0]) if item[0] else float("-inf"),
                reverse=reverse,
            )
        except ValueError:
            # Fall back to string sort
            rows.sort(key=lambda item: item[0], reverse=reverse)

        # Reorder rows in the Treeview
        for index, (_, row_id) in enumerate(rows):
            self.tree.move(row_id, "", index)

        # Update sort state
        self._sort_column = column
        self._sort_reverse = reverse
