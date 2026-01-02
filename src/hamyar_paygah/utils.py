"""Utility functions for Hamyar Paygah."""


def get_int(text: str | None) -> int | None:
    """Safely convert an optional string to an integer.

    This function is useful when parsing XML fields that may be empty
    or marked as nil.

    Args:
        text (str | None): A string representing an integer, or None.

    Returns:
        int | None: The integer value if `text` is not None, otherwise None.
    """
    return int(text) if text is not None else None
