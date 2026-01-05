"""Translation data models for the application UI.

This module defines strongly-typed data structures used to store localized
UI strings. The primary goal is to provide IDE-friendly, type-safe access
to translation values instead of relying on unstructured dictionaries.

Each supported language should provide an instance of the ``Translations``
dataclass populated with language-specific strings.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Translations:
    """Container for all UI text used in the application.

    This dataclass represents a complete set of localized strings required
    by the user interface. All fields are mandatory to ensure that every
    language implementation is complete and consistent.

    The class is immutable (``frozen=True``) to guarantee that translation
    data cannot be modified at runtime, preventing accidental UI corruption
    and ensuring predictable behavior.
    """

    main_window_title: str
    """Title of the main window"""
    missions_window_load_missions_button: str
    """Label for the button that triggers loading the missions list"""
    main_window_options_button: str
    """Label for the button that opens the options window"""
    options_window_title: str
    """Title of the options window"""
    options_window_language_label: str
    """Label for the language selection control in the options window"""
    save_button: str
    """Generic label for save button"""
    welcome_label: str
    """Welcome message displayed in the main window"""
    error_label: str
    """Title of an error message box"""
    server_config_title: str
    """Title of the server configuration dialog"""
    server_config_prompt: str
    """Prompt of the server configuration dialog"""
    server_config_empty_error_title: str
    """Title of the error dialog shown when server address is empty"""
    server_config_empty_error_msg: str
    """Message of the error dialog shown when server address is empty"""
    server_address_not_provided_error_message: str
    """Message of the error when server address is not provided and dialog is closed"""
