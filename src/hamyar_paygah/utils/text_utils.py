"""Utility functions related to text."""

import datetime
from urllib.parse import urlparse

import jdatetime  # type: ignore[import-untyped]


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


def convert_date_and_time_to_datetime(
    date_string: str | None,
    time_string: str | None,
) -> datetime.datetime | None:
    """Converts jalali date and time strings into a gregorian datetime.

    Args:
        date_string (str): Jalali date
        time_string (str): Jalali time

    Returns:
        datetime.datetime: gregorian datetime object.
    """
    # If inputs are `None` or invalid, return `None`
    if date_string is None or time_string is None or date_string == "-" or time_string == "-":
        return None
    # Split the input values
    year, month, day = map(int, date_string.split("/"))
    hour, minute = map(int, time_string.split(":"))

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
