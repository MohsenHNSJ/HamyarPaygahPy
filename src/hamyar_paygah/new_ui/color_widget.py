"""Custom Qt widget to display a color."""

# pylint: disable=E0611,R0903
from PySide6.QtGui import QColor, QPalette, QRgba64
from PySide6.QtWidgets import QWidget


class Color(QWidget):
    """Widget that displays a color."""

    def __init__(self, color: QColor | str | QRgba64 | int) -> None:
        """Initialize color widget."""
        super().__init__()
        self.setAutoFillBackground(True)

        palette: QPalette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
