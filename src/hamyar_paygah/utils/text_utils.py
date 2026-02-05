"""Utility functions related to text."""

from urllib.parse import urlparse


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
