"""Logic module for managing application options.

This module provides a central handler for application configuration logic.
It decouples the UI from the underlying logic by exposing a clean API to get and set options.

Classes:
    OptionsConfig: Provides methods to query and update application settings.
"""

from hamyar_paygah.localization.language_manager import LANG_MAP, LanguageManager


class OptionsConfig:
    """Logic handler for application options.

    This class manages the application's configurable options.

    Attributes:
        available_languages (list[str]): List of all valid language codes
            supported by the application.
    """

    def __init__(self) -> None:
        """Initialize the options configuration handler.

        Sets up a list of available language codes based on LANG_MAP.
        """
        # Extract all supported language codes from the language map
        self.available_languages: list[str] = list(LANG_MAP.keys())

    @property
    def current_language(self) -> str:
        """Return the currently active language code.

        Returns:
            str: Language code of the current application language
                 (e.g., "en" or "fa").
        """
        return LanguageManager.current_language_code

    def set_language(self, lang_code: str) -> None:
        """Set the application language and persist the preference.

        This method validates the provided language code and then updates
        the LanguageManager accordingly. Raises an error if the code is
        invalid.

        Args:
            lang_code (str): Language code to set (must exist in LANG_MAP).

        Raises:
            ValueError: If `lang_code` is not in the list of available languages.
        """
        # Check that the provided language code is valid
        if lang_code in self.available_languages:
            # Update the application's language through LanguageManager
            LanguageManager.set_language(lang_code)
        else:
            # Raise an error if the code is not supported
            msg: str = f"Invalid language code: {lang_code}"
            raise ValueError(msg)
