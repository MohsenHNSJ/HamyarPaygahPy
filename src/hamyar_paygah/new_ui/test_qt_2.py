"""Test for qt."""

# pylint: disable=C0114,I1101,E0611,R0903
import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout

colors: list[tuple[str, str]] = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
    ("Black", "#000000"),
    ("White", "#FFFFFF"),
    ("Electric Green", "#41CD52"),
    ("Dark Blue", "#222840"),
    ("Yellow", "#F9E56d"),
]


class Form(QDialog):
    """Main window class."""

    def __init__(self) -> None:
        """Window initializer."""
        super().__init__()
        self.setWindowTitle("My Form")

        # Create widgets
        table = QTableWidget()
        table.setRowCount(len(colors))
        table.setColumnCount(len(colors[0]) + 1)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

        # Populate table with color data
        for i, (name, hex_code) in enumerate(colors):
            table.setItem(i, 0, QTableWidgetItem(name))
            table.setItem(i, 1, QTableWidgetItem(hex_code))
            table.setItem(i, 2, QTableWidgetItem(""))
            table.item(i, 2).setBackground(self.get_rgb_from_hex(hex_code))

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(table)

        # Set dialog layout
        self.setLayout(layout)

    def get_rgb_from_hex(self, code: str) -> QColor:
        """Convert hex color code to QColor."""
        code_hex = code.replace("#", "")
        rgb = tuple(int(code_hex[i : i + 2], 16) for i in (0, 2, 4))
        return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
