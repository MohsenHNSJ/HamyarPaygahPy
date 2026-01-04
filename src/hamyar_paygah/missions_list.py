"""EMS Missions List Application.

This module provides a Tkinter-based GUI application for Emergency Medical
Services (EMS) mission management. It allows users to fetch mission data
from a remote server asynchronously, parse the XML responses, and display
them in a sortable and user-friendly table.

Key Features:
    - Date range selection using calendar widgets.
    - Region ID input with integer-only validation.
    - Asynchronous data fetching using asyncio and aiohttp.
    - Parsing of XML mission data into structured Mission objects.
    - Tabular display of missions with sortable columns.
    - Alternate row colors for readability.
    - Loading indicator to show fetch progress.
    - Error handling for network and data issues.

Classes:
    MissionsListApp (tk.Tk): Main application window. Handles UI initialization,
        user interactions, async data fetching, table population, and
        column sorting.

Example:
    To run the application, execute the module directly:

        python -m src.hamyar_paygah.main

Notes:
    - Requires Python 3.13+, Tkinter 8.6, tkcalendar, aiohttp, and lxml.
    - Uses asyncio to avoid blocking the GUI while fetching data.
    - The EMSApp class encapsulates all UI components and helper methods.

"""

# ruff: noqa: DTZ007
import asyncio
import threading
import tkinter as tk
from collections.abc import Callable
from datetime import datetime
from tkinter import messagebox, ttk

import arabic_reshaper  # type: ignore[import-untyped]
from aiohttp import ClientError
from bidi import get_display  # type: ignore[import-untyped]
from lxml import etree
from tkcalendar import DateEntry  # type: ignore[import-untyped]

from hamyar_paygah.models import Mission
from hamyar_paygah.parsers import parse_missions
from hamyar_paygah.services import get_missions_list


class MissionsListApp(tk.Toplevel):
    """Main Missions List application window with async fetching and sortable table."""

    def __init__(self, server_url: str, master: tk.Misc | None = None) -> None:
        """Initialize the main EMS Missions List application window.

        This constructor sets up the entire user interface and initial state
        of the application. It creates a large main window containing:

        - An input section with date pickers for selecting a date range,
        an integer-only field for region ID, and a search button.
        - A loading indicator used to display fetch progress or status messages.
        - A tabular view (Treeview) for displaying mission records, with
        sortable columns and alternating row colors for readability.
        - A vertical scrollbar linked to the mission table.

        The window is configured to support column sorting, non-blocking
        asynchronous data loading, and dynamic clearing and repopulation
        of mission data when new searches are performed.

        UI State Initialized:
            - sort_column: The currently sorted column name, or None if no
            sorting has been applied.
            - sort_reverse: Whether the current sort order is descending.
            - from_date: Date picker widget for the start date.
            - to_date: Date picker widget for the end date.
            - region_id_var: StringVar bound to the region ID entry field.
            - search_btn: Button that triggers the search operation.
            - loading_label: Label used to display loading or status messages.
            - tree: Treeview widget used to display mission data.
            - columns: Ordered list of column headers shown in the table.

        Notes:
            - The region ID entry field enforces integer-only input via
            validation.
            - Column headers are clickable and toggle sorting behavior.
            - Alternate row coloring is applied using Treeview tags.
            - The scrollbar is correctly wired using the ``yscrollcommand``
            option to ensure smooth scrolling.

        """
        super().__init__(master=master)
        self.title("Missions List")
        self.geometry("1200x700")  # large window
        self.sort_column: str | None = None
        self.sort_reverse = False
        self.server_url: str = server_url

        # --- Input Frame ---
        input_frame = ttk.Frame(self)
        input_frame.pack(side="top", fill="x", padx=10, pady=10)

        ttk.Label(input_frame, text="From Date:").grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )
        self.from_date = DateEntry(input_frame, date_pattern="yyyy-mm-dd")
        self.from_date.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="To Date:").grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
        )
        self.to_date = DateEntry(input_frame, date_pattern="yyyy-mm-dd")
        self.to_date.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Region ID:").grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
        )
        self.region_id_var = tk.StringVar()
        region_entry = ttk.Entry(input_frame, textvariable=self.region_id_var)
        region_entry.grid(row=0, column=5, padx=5, pady=5)
        region_entry.config(
            validate="key",
            validatecommand=(
                self.register(self.validate_int),
                "%P",
            ),
        )

        self.search_btn = ttk.Button(
            input_frame,
            text="Search",
            command=self.on_search_click,
        )
        self.search_btn.grid(row=0, column=6, padx=10, pady=5)

        # --- Loading Indicator ---
        self.loading_label = ttk.Label(input_frame, text="", foreground="blue")
        self.loading_label.grid(row=1, column=0, columnspan=7, pady=5)

        # --- Table Frame ---
        table_frame = ttk.Frame(self)
        table_frame.pack(
            side="top",
            fill="both",
            expand=True,
            padx=10,
            pady=10,
        )

        self.columns: list[str] = [
            "Mission ID",
            "Patient Name",
            "Patient ID",
            "Ambulance Code",
            "Hospital Name",
            "Date",
            "Persian Date",
            "Address",
            "Result",
        ]

        # Column widths: smaller for ID/code fields, bigger for names/addresses
        column_widths = {
            "Mission ID": 80,
            "Patient Name": 200,
            "Patient ID": 80,
            "Ambulance Code": 80,
            "Hospital Name": 150,
            "Date": 120,
            "Persian Date": 120,
            "Address": 250,
            "Result": 150,
        }

        self.tree = ttk.Treeview(
            table_frame,
            columns=self.columns,
            show="headings",
            style="Custom.Treeview",  # Custom style for showing Persian text correctly
        )

        # Set Treeview font to one that supports Persian
        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            font=("Tahoma", 11),  # change to 'Vazir' if you have it installed
            rowheight=25,
        )

        for col in self.columns:
            self.tree.heading(
                col,
                text=col,
                command=self._make_sort_callback(col),
            )
            # Fallback to 120 if not specified
            current_column_width = column_widths.get(col, 120)
            self.tree.column(col, width=current_column_width, anchor="center")

        # --- Define row tags for alternating colors ---
        self.tree.tag_configure("oddrow", background="white")
        self.tree.tag_configure("evenrow", background="#f0f0ff")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview,
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(expand=True, fill="both")

    # ----------------- Helper Methods -----------------

    def validate_int(self, value: str) -> bool:
        """Allow only digits in region ID entry."""
        return value.isdigit() or value == ""

    def clear_table(self) -> None:
        """Remove all rows from the table."""
        for row in self.tree.get_children():
            self.tree.delete(row)

    def populate_table(self, missions: list[Mission]) -> None:
        """Fill the table with a list of Mission objects with alternating row colors."""
        self.clear_table()
        for index, m in enumerate(missions):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            self.tree.insert(
                "",
                "end",
                values=(
                    m.id,
                    self.reshape_rtl(m.patient_name),
                    m.patient_id,
                    m.ambulance_code,
                    self.reshape_rtl(m.hospital_name or ""),
                    m.date,
                    m.persian_date,
                    self.reshape_rtl(m.address),
                    self.reshape_rtl(m.result),
                ),
                tags=(tag,),
            )

    def sort_by_column(self, col: str) -> None:
        """Sort the Treeview by a given column."""
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children()]
        reverse = not self.sort_reverse if self.sort_column == col else False
        try:
            # try numeric sort
            data.sort(
                key=lambda t: float(
                    t[0],
                )
                if t[0]
                else float("-inf"),
                reverse=reverse,
            )
        except ValueError:
            # fallback to string sort
            data.sort(key=lambda t: t[0], reverse=reverse)
        for index, (_, k) in enumerate(data):
            self.tree.move(k, "", index)
        self.sort_column = col
        self.sort_reverse = reverse

    def on_search_click(self) -> None:
        """Handle Search button click, validate input, and start async fetch in a thread."""
        if not self.from_date.get() or not self.to_date.get() or not self.region_id_var.get():
            messagebox.showwarning(
                "Input Error",
                "Please fill all input fields!",
            )
            return

        try:
            region_id = int(self.region_id_var.get())
        except ValueError:
            messagebox.showwarning(
                "Input Error",
                "Region ID must be an integer!",
            )
            return

        from_dt = datetime.strptime(self.from_date.get(), "%Y-%m-%d")
        to_dt = datetime.strptime(self.to_date.get(), "%Y-%m-%d")

        # Show loading indicator
        self.loading_label.config(text="Loading...")
        self.search_btn.config(state="disabled")

        # Run async fetch in background thread
        threading.Thread(
            target=self._run_async_fetch,
            args=(
                from_dt,
                to_dt,
                region_id,
            ),
            daemon=True,
        ).start()

    def _run_async_fetch(self, from_dt: datetime, to_dt: datetime, region_id: int) -> None:
        """Run the async fetch safely in a background thread."""
        loop: asyncio.AbstractEventLoop | None = None
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                self.fetch_and_display(from_dt, to_dt, region_id),
            )
        except Exception as exc:  # noqa: BLE001 , # pylint: disable=broad-exception-caught
            # Unexpected crash: notify user safely in main thread
            self._show_error(
                "Crash",
                f"The program encountered an unexpected error:\n{exc}",
            )
        finally:
            if loop is not None:
                loop.close()

    async def fetch_and_display(self, from_dt: datetime, to_dt: datetime, region_id: int) -> None:
        """Fetch missions data and populate the table asynchronously."""
        try:
            xml_response = await get_missions_list(
                self.server_url,
                from_dt,
                to_dt,
                region_id,
            )
            missions = parse_missions(xml_response)
            # UI updates must happen in main thread
            self.after(0, lambda: self.populate_table(missions))

        except (TimeoutError, ClientError) as exc:
            self._show_error(
                "Network Error",
                f"Failed to contact server:\n{exc}",
            )

        except (etree.XMLSyntaxError, ValueError) as exc:  # pylint: disable=I1101
            self._show_error(
                "Data Error",
                f"Received invalid data from server:\n{exc}",
            )
        finally:
            # Clear loading label and re-enable button
            self.after(0, lambda: self.loading_label.config(text=""))
            self.after(0, lambda: self.search_btn.config(state="normal"))

    def _make_sort_callback(self, column: str) -> Callable[[], None]:
        def callback() -> None:
            self.sort_by_column(column)

        return callback

    def _show_error(self, title: str, message: str) -> None:
        """Show an error message safely on the main thread."""
        messagebox.showerror(title, message)

    def _reset_ui(self) -> None:
        """Reset loading indicator and enable the search button."""
        self.loading_label.config(text="")
        self.search_btn.config(state="normal")

    def reshape_rtl(self, text: str | None) -> str:
        """Reshape Persian/Arabic text for correct display in Tkinter Treeview."""
        if not text:
            return ""
        reshaped = arabic_reshaper.reshape(text)  # correct letter connections
        return str(get_display(reshaped))  # apply RTL bidi reordering
