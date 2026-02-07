"""Utility functions related to text."""

import datetime
import re
from urllib.parse import urlparse

import jdatetime  # type: ignore[import-untyped]


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


def convert_to_time(text: str | None) -> datetime.time | None:
    """Converts the input text into a datetime.time object.

    Args:
        text (str): Time as string

    Returns:
        datetime.time | None: Time object or None if input is invalid
    """
    # If time is not provided by server, return None
    if text == "-" or text is None:
        return None
    # Else, convert the string to time
    return datetime.datetime.strptime(text, "%H:%M:%S").time()  # noqa: DTZ007


def convert_date_to_datetime(date_string: str | None) -> datetime.datetime | None:
    """Converts a Jalali date string (YYYY/MM/DD) to gregorian datetime.

    Args:
        date_string (str): Jalali date string

    Returns:
        datetime.datetime: Gregorian datetime object
    """
    # If input is `None`, return `None`
    if not date_string:
        return None

    # Split the input to values
    year, month, day = map(int, date_string.split("/"))

    # Create a jalali date object
    jalali_date = jdatetime.date(year, month, day)

    # Convert to gregorian date
    gregorian_date: datetime.date = jalali_date.togregorian()

    # Create a datetime object and return it
    return datetime.datetime.combine(gregorian_date, datetime.time.min)


def convert_date_and_time_to_datetime(date: str, time: str) -> datetime.datetime:
    """Converts jalali date and time strings into a gregorian datetime.

    Args:
        date (str): Jalali date
        time (str): Jalali time

    Returns:
        datetime.datetime: gregorian datetime object.
    """
    # Split the input values
    year, month, day = map(int, date.split("/"))
    hour, minute = map(int, time.split(":"))

    # Create a jalali date time using split values
    jalali_datetime: jdatetime.datetime = jdatetime.datetime(
        year,
        month,
        day,
        hour,
        minute,
    )

    # Return the gregorian date
    return jalali_datetime.togregorian()  # type: ignore[no-any-return]


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
