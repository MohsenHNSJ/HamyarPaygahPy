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

    error_label: str
    """Title of an error message box"""
    error_unexpected_message: str
    """Message to inform user an unexpected error happened"""
    main_window_missions_list_button: str
    """Label for the button that triggers loading the missions list"""
    main_window_options_button: str
    """Label for the button that opens the options window"""
    main_window_title: str
    """Title of the main window"""
    missions_list_address_label: str
    """Address of the mission in missions list table"""
    missions_list_ambulance_code_label: str
    """Ambulance code in missions list table"""
    missions_list_date_label: str
    """Date of the mission in missions list table"""
    missions_list_from_date_is_required_error_message: str
    """Message of the error when (From Date) is not provided"""
    missions_list_hospital_name_label: str
    """Hospital name in missions list table"""
    missions_list_load_missions_button: str
    """Button label to load missions from server"""
    missions_list_mission_id_label: str
    """Missions ID label in missions list table"""
    missions_list_patient_id_label: str
    """Patient ID in missions list table"""
    missions_list_patient_name_label: str
    """Patient name in missions list table"""
    missions_list_persian_date_label: str
    """Persian date of the missions in missions list table"""
    missions_list_region_id_invalid_error_message: str
    """Message of the error when (Region ID) is not valid"""
    missions_list_region_id_is_required_error_message: str
    """Message of the error when (Region ID) is not provided"""
    missions_list_result_label: str
    """Result of the mission in missions list table"""
    missions_list_to_date_is_required_error_message: str
    """Message of the error when (To Date) is not provided"""
    missions_list_window_title: str
    """Title of the missions list window"""
    missions_list_loading_status_message: str
    """Status message shown when missions list is loading"""
    options_window_language_label: str
    """Label for the language selection control in the options window"""
    options_window_title: str
    """Title of the options window"""
    save_button: str
    """Generic label for save button"""
    server_address_not_provided_error_message: str
    """Message of the error when server address is not provided and dialog is closed"""
    server_config_empty_error_msg: str
    """Message of the error dialog shown when server address is empty"""
    server_config_empty_error_title: str
    """Title of the error dialog shown when server address is empty"""
    server_config_prompt: str
    """Prompt of the server configuration dialog"""
    server_config_title: str
    """Title of the server configuration dialog"""
    welcome_label: str
    """Welcome message displayed in the main window"""
