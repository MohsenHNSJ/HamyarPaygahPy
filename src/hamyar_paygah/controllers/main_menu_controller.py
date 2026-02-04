"""Controller for main menu UI."""

# pylint: disable=E0611,I1101,R0903
from PySide6.QtWidgets import QMainWindow

import hamyar_paygah.new_ui.main_menu as main_menu_ui


class MainMenu(QMainWindow):
    """Main menu of the application."""

    def __init__(self) -> None:
        """Initialize the main menu UI."""
        super().__init__()

        # Set up the UI
        self.ui = main_menu_ui.Ui_main_window()  # type: ignore[attr-defined]
        self.ui.setupUi(self)
