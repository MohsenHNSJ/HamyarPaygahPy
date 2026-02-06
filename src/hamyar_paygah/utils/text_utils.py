"""Utility functions related to text."""

import re
from urllib.parse import urlparse


def convert_to_integer(text: str | None) -> int | None:
    """Safely converts an optional string to an integer.

    This function is useful when parsing XML fields that may be empty
    or marked as nil.
    If a field contains both alphabets and numbers, the alphabets will be ignored

    Args:
        text (str | None): A string representing an integer, or None.

    Returns:
        int | None: The integer value if `text` is not None, otherwise None.
    """
    result: int | None = None

    # If input is empty, return None
    if not text:
        return result

    # Try to extract the number regularly
    try:
        result = int(text)
    # If the input is a mix of numbers and alphabets, extract numbers
    except ValueError:
        match = re.search(r"\d+", text)
        result = int(match.group()) if match else None

    return result


def convert_to_bool(text: str | None) -> bool:
    """Safely converts an optional string to a bool.

    This function is useful when parsing XML fields that may be empty
    or marked as nil.

    Args:
        text (str | None): A string representing a bool, or None.

    Returns:
        bool: The bool value if `text` is not None, otherwise `False`.
    """
    return text == "true"


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
    if not address.startswith(("http://", "https://")):
        return False

    # Parse the URL
    parsed = urlparse(address)

    # Ensure scheme and hostname exist
    return not (not parsed.scheme or not parsed.netloc)
