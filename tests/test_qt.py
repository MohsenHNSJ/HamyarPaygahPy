"""Test for qt."""

# pylint: disable=C0114,I1101,E0611
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
# This HTML approach will be valid too!
label = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
app.exec()
