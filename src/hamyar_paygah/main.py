"""Simple Tkinter UI with buttons that do nothing.

This module creates a basic graphical user interface (GUI) using Tkinter.
"""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    """Main function."""
    root = tk.Tk()
    root.title(string="Simple Tkinter UI")

    root.geometry(newGeometry="400x200")
    root.resizable(width=False, height=False)

    frame = ttk.Frame(master=root, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(
        master=frame,
        text="Buttons that do nothing",
        font=("Segoe UI", 12),
    ).pack(pady=(0, 10))

    btn_frame = ttk.Frame(master=frame)
    btn_frame.pack()

    # Buttons intentionally do nothing when clicked (command=lambda: None)
    ttk.Button(master=btn_frame, text="Button 1", command=lambda: None).grid(
        row=0,
        column=0,
        padx=6,
        pady=6,
    )
    ttk.Button(master=btn_frame, text="Button 2", command=lambda: None).grid(
        row=0,
        column=1,
        padx=6,
        pady=6,
    )
    ttk.Button(master=btn_frame, text="Button 3", command=lambda: None).grid(
        row=1,
        column=0,
        padx=6,
        pady=6,
    )
    ttk.Button(master=btn_frame, text="Button 4", command=lambda: None).grid(
        row=1,
        column=1,
        padx=6,
        pady=6,
    )

    ttk.Button(master=frame, text="Exit", command=root.quit).pack(pady=(12, 0))

    root.mainloop()


if __name__ == "__main__":
    main()
