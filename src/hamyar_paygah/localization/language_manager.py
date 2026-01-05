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

import json
from collections.abc import Callable

from hamyar_paygah.app.paths import CONFIG_FILE_PATH
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


class LanguageManager:
    """Manages the application's UI translations and language settings."""

    language_code: str = "Persian"
    """Currently active language code"""
    _translations: Translations = FA
    """Translations corresponding to the current language"""

    @classmethod
    def load_language(cls) -> None:
        """Load the user's preferred language from the configuration file.

        If the configuration file is missing or invalid, defaults to Persian/Farsi.
        Updates the internal `_translations` attribute to match the loaded language.
        """
        # If there is a config file, try to read the language code from it, on error load Persian
        if CONFIG_FILE_PATH.exists():
            try:
                data = json.loads(CONFIG_FILE_PATH.read_text(encoding="utf-8"))
                cls.language_code = data.get("language", "Persian")
            except (OSError, json.JSONDecodeError):
                cls.language_code = "Persian"

        # Set translations to language code, on error set to Persian
        cls._translations = (
            LANG_MAP.get(
                cls.language_code,
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
        text: str = getter(cls._translations)

        # If it's Right-to-Left, reshape it
        if cls.language_code in RTL_LANGS:
            return reshape_rtl(text)

        # Return the translated text
        return text

    @classmethod
    def set_language(cls, lang_code: str) -> None:
        """Set the application's language and save the preference to disk.

        Updates the `_lang_code` and `_translations` attributes, and writes
        the selected language code to the configuration file (`language_config.json`).

        Args:
            lang_code (str): The language code to set (e.g., "en" or "fa").
                             Defaults to Persian/Farsi if the code is invalid.
        """
        # If new language code is not in language map, ignore and set to Persian
        if lang_code not in LANG_MAP:
            lang_code = "Persian"

        # Set language code
        cls.language_code = lang_code
        # Set translations
        cls._translations = LANG_MAP[lang_code]

        # Write selected language into config file
        CONFIG_FILE_PATH.write_text(
            json.dumps({"language": lang_code}, ensure_ascii=False),
            encoding="utf-8",
        )
