"""Test for qt."""

# pylint: disable=C0114,I1101,E0611,R0903
import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):
    """Main window class."""

    def __init__(self) -> None:
        """Window initializer."""
        super().__init__()
        self.setWindowTitle("My Form")

        # Create widgets
        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show Greetings")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    def greetings(self) -> None:
        """Shows a greeting message."""
        print("Hello " + self.edit.text())


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
