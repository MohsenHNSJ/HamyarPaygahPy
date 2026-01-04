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

Classes:
    LanguageManager: Centralized manager for loading, setting, and
        retrieving UI translations.

Constants:
    CONFIG_FILE (Path): Path to the JSON file storing language configuration.
    LANG_MAP (dict[str, Translations]): Maps language codes to
        corresponding translation sets.
    RTL_LANGS (set[str]): Set of language codes that use right-to-left text.
"""

import json
from collections.abc import Callable
from pathlib import Path

from hamyar_paygah.localization.base import Translations
from hamyar_paygah.localization.en import EN
from hamyar_paygah.localization.fa import FA
from hamyar_paygah.utils.text_utils import reshape_rtl

CONFIG_FILE = Path("language_config.json")
"""Path to UI language config file"""

LANG_MAP: dict[str, Translations] = {
    "English": EN,
    "Persian": FA,
}
"""Map of all available languages and their name presentation in options window"""

RTL_LANGS: set[str] = {"Persian"}


class LanguageManager:
    """Manages the application's UI translations and language settings.

    Attributes:
        _lang_code (str): The currently active language code.
        _translations (Translations): The translations corresponding
            to the current language.
    """

    _lang_code: str = "Persian"
    _translations: Translations = FA

    @classmethod
    def load_language(cls) -> None:
        """Load the user's preferred language from the configuration file.

        If the configuration file is missing or invalid, defaults to Persian/Farsi.
        Updates the internal `_translations` attribute to match the loaded language.
        """
        if CONFIG_FILE.exists():
            try:
                data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
                cls._lang_code = data.get("language", "Persian")
            except (OSError, json.JSONDecodeError):
                cls._lang_code = "Persian"

        cls._translations = (
            LANG_MAP.get(
                cls._lang_code,
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
        text = getter(cls._translations)
        if cls._lang_code in RTL_LANGS:
            return reshape_rtl(text)
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
        if lang_code not in LANG_MAP:
            lang_code = "Persian"

        cls._lang_code = lang_code
        cls._translations = LANG_MAP[lang_code]

        CONFIG_FILE.write_text(
            json.dumps({"language": lang_code}, ensure_ascii=False),
            encoding="utf-8",
        )
