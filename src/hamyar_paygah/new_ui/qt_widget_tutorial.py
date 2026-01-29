"""Simple Qt application that creates and shows a widget."""

# pylint: disable=E0611,R0903
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window.
class MainWindow(QMainWindow):
    """Application main window."""

    def __init__(self) -> None:  # noqa: PLR0915
        """Initialize the main window."""
        super().__init__()

        # Set window title
        self.setWindowTitle("My App")

        # Sample Label
        label = QLabel("Hello, World!")
        # Set label font
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
        )

        # Sample Check box
        checkbox = QCheckBox("This is a checkbox")
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.show_state)

        # Sample Combo box
        combobox = QComboBox()
        combobox.addItems(["One", "Two", "سه"])
        combobox.currentIndexChanged.connect(self.index_changed)
        combobox.currentTextChanged.connect(self.text_changed)
        combobox.setEditable(True)
        combobox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        combobox.setMaxCount(8)

        # Sample List
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        list_widget.currentItemChanged.connect(self.index_changed)
        list_widget.currentTextChanged.connect(self.text_changed)

        # Sample Line Edit
        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(12)
        self.line_edit.setPlaceholderText("Enter up to 12 numbers")
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.setInputMask("000.000.000.000;_")

        # Sample Spin box
        spinbox = QSpinBox()
        spinbox.setMinimum(-10)
        spinbox.setMaximum(3)
        spinbox.setPrefix("$")
        spinbox.setSuffix("c")
        spinbox.setSingleStep(3)  # Or setSingleStep(3.0) for QDoubleSpinBox

        # Sample Slider
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(-10)
        slider.setMaximum(3)
        slider.setSingleStep(3)

        # Sample Dial
        dial = QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(checkbox)
        layout.addWidget(combobox)
        layout.addWidget(list_widget)
        layout.addWidget(self.line_edit)
        layout.addWidget(spinbox)
        layout.addWidget(slider)
        layout.addWidget(dial)
        # Add the widgets to the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def show_state(self, state: Qt.CheckState) -> None:
        """Prints the state of checkbox."""
        print(state == Qt.CheckState.Checked.value)
        print(state)

    def index_changed(self, index: int) -> None:
        """Prints the index."""
        print(f"Current index: {index}")

    def text_changed(self, text: str) -> None:
        """Prints the text."""
        print(f"Current text: {text}")

    def return_pressed(self) -> None:
        """Runs when return key is pressed on line edit widget."""
        print("Return Pressed!")
        self.line_edit.setText("BOOM!")


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
