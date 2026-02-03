"""Test for qt."""

# pylint: disable=C0114,I1101,E0611
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


@Slot()
def say_hello() -> None:
    """Prints Hello to console."""
    print("Button clicked, Hello!")


# Create the Qt application
app = QApplication([])

# Create a button
button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(say_hello)
# Show the button
button.show()

# Run the main Qt loop
app.exec()
