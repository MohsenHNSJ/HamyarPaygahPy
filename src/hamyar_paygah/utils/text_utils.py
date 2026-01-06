"""Utility functions related to text."""

from urllib.parse import urlparse

import arabic_reshaper  # type: ignore[import-untyped]
from bidi import get_display  # type: ignore[import-untyped]


def convert_to_integer(text: str | None) -> int | None:
    """Safely converts an optional string to an integer.

    This function is useful when parsing XML fields that may be empty
    or marked as nil.

    Args:
        text (str | None): A string representing an integer, or None.

    Returns:
        int | None: The integer value if `text` is not None, otherwise None.
    """
    return int(text) if text is not None else None


def reshape_rtl(text: str | None) -> str:
    """Prepare Persian or Arabic text for correct display in Tkinter.

    Tkinter does not natively support right-to-left (RTL) scripts or proper
    Arabic letter shaping. This function reshapes the input text so that
    characters are joined correctly and then applies bidirectional (bidi)
    reordering to ensure the text is rendered properly in the UI.

    Args:
        text: The input string containing Persian or Arabic text.
            If None or an empty string is provided, an empty string is returned.

    Returns:
        A reshaped and RTL-corrected string suitable for display in Tkinter.
    """
    # Handle None or empty input
    if not text:
        return ""
    # Correct letter connections
    reshaped_text = arabic_reshaper.reshape(text)
    # Apply RTL bidi reordering
    return str(get_display(reshaped_text))


def is_valid_server_address(server_address: str | None) -> bool:
    """Validate the server address format.

    The address must:
    - Be a non-empty string
    - Start with ``http://`` or ``https://``
    - Contain a valid network location (host)

    Args:
        server_address: Server address entered by the user.

    Returns:
        ``True`` if the address appears valid, otherwise ``False``.
    """
    # If server address is empty return False
    if not server_address:
        return False

    # Strip empty spaces
    address: str = server_address.strip()

    # Must explicitly specify scheme
    if not (address.startswith(("http://", "https://"))):
        return False

    # Parse the URL
    parsed = urlparse(address)

    # Ensure scheme and hostname exist
    return not (not parsed.scheme or not parsed.netloc)
