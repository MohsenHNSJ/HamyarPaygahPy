"""Sample QT widget for testing purposes."""

import random
import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    """Initial sample class for testing Qt functionality."""

    def __init__(self) -> None:
        """Initialize the sample widget."""
        super().__init__()

        self.hello: list[str] = [
            "Hallo Welt",
            "Hei maailma",
            "Hola Mundo",
            "Bonjour le monde",
            "Ciao mondo",
        ]

        self.button = QtWidgets.QPushButton("Click Me")
        self.text = QtWidgets.QLabel(
            "Hello World",
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter,
        )

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self) -> None:
        """Randomly change the label text to a different language."""
        self.text.setText(random.choice(self.hello))  # noqa: S311


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
