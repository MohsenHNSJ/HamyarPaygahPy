"""Simple Qt application that creates and shows a widget."""
# pylint: disable=E0611,R0903

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window.
class MainWindow(QMainWindow):
    """Application main window."""

    def __init__(self) -> None:
        """Main window constructor."""
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our main window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event loop has stopped.
