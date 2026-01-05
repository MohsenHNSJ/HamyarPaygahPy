"""Language management system.

This module provides the `LanguageManager` class, which handles loading,
storing, and retrieving translations for the application's user interface.
It supports multiple languages (currently English and Persian/Farsi) and
ensures proper handling of right-to-left (RTL) languages.
Translations are defined in dedicated modules (`en.py` and `fa.py`) as
immutable `Translations` dataclass instances, enabling IDE type checking
and autocompletion.
The current language setting is persisted in a JSON configuration file
(`language_config.json`) so that user preferences are retained across
application restarts.
"""

from collections.abc import Callable
from typing import Final

from hamyar_paygah.config.config_manager import get_config_value, set_config_value
from hamyar_paygah.localization.base import Translations
from hamyar_paygah.localization.en import EN
from hamyar_paygah.localization.fa import FA
from hamyar_paygah.utils.text_utils import reshape_rtl

LANG_MAP: dict[str, Translations] = {
    "English": EN,
    "Persian": FA,
}
"""Map of all available languages and their name presentation in options window"""

RTL_LANGS: set[str] = {"Persian"}
"""Set of language codes that use Right-to-Left text"""

_APP_LANGUAGE_KEY: Final[str] = "app_language"
"""Key for saving app language in JSON file"""

_DEFAULT_LANGUAGE_CODE: str = "Persian"
"""Language code of default language"""


class LanguageManager:
    """Manages the application's UI translations and language settings."""

    current_language_code: str = _DEFAULT_LANGUAGE_CODE
    """Currently active language code"""
    current_translations: Translations = FA
    """Translations corresponding to the current language"""

    @classmethod
    def load_language(cls) -> None:
        """Load the user's preferred language from the configuration file.

        If the configuration file is missing or invalid, defaults to Persian/Farsi.
        Updates the `current_translations` attribute to match the loaded language.
        """
        cls.current_language_code = get_config_value(
            _APP_LANGUAGE_KEY,
            _DEFAULT_LANGUAGE_CODE,
        )

        # Set translations to language code, on error set to Persian
        cls.current_translations = (
            LANG_MAP.get(
                cls.current_language_code,
                FA,
            )
            or FA
        )

    @classmethod
    def t(cls, getter: Callable[[Translations], str]) -> str:
        """Translate a UI string using a lambda or attribute reference.

        This method retrieves the string corresponding to the current language,
        and reshapes it for right-to-left languages if needed.

        Args:
            getter (Callable[[Translations], str]): A function or lambda that
                accepts a `Translations` instance and returns the desired string.

        Returns:
            str: The translated and reshaped string ready for display.

        Example:
            LanguageManager.t(lambda t: t.main_window_title)
        """
        # Get the current translation of the requested text
        text: str = getter(cls.current_translations)

        # If it's Right-to-Left, reshape it
        if cls.current_language_code in RTL_LANGS:
            return reshape_rtl(text)

        # Return the translated text
        return text

    @classmethod
    def set_language(cls, lang_code: str) -> None:
        """Set the application's language and save the preference to disk.

        Updates the `current_language_code` and `current_translations` attributes, and writes
        the selected language code to the configuration file (`language_config.json`).

        Args:
            lang_code (str): The language code to set (e.g., "en" or "fa").
                             Defaults to Persian/Farsi if the code is invalid.
        """
        # If new language code is not in language map, ignore and set to Persian
        if lang_code not in LANG_MAP:
            lang_code = _DEFAULT_LANGUAGE_CODE

        # Set language code
        cls.current_language_code = lang_code
        # Set translations
        cls.current_translations = LANG_MAP[lang_code]

        # Write selected language into config file
        set_config_value(_APP_LANGUAGE_KEY, lang_code)
