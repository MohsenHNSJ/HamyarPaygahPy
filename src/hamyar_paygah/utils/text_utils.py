"""Utility functions related to text."""

import datetime
from urllib.parse import urlparse

import jdatetime  # type: ignore[import-untyped]


def convert_date_to_datetime(date_string: str | None) -> datetime.datetime | None:
    """Convert a Jalali date string to a Gregorian datetime object.

    The input must be in the format ``YYYY/MM/DD``. If ``None`` or an
    empty string is provided, ``None`` is returned.

    Args:
        date_string: Jalali date string in ``YYYY/MM/DD`` format.

    Returns:
        A ``datetime.datetime`` object representing the corresponding
        Gregorian date at midnight, or ``None`` if the input is ``None``
        or empty.
    """
    # If input is `None`, return `None`
    if date_string is None or not date_string.strip():
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
    """Convert Jalali date and time strings to a Gregorian datetime.

    The date must be in ``YYYY/MM/DD`` format and the time must be in
    ``HH:MM`` format. If either value is ``None`` or equals ``"-"``,
    ``None`` is returned.

    Args:
        date_string: Jalali date string in ``YYYY/MM/DD`` format.
        time_string: Jalali time string in ``HH:MM`` format.

    Returns:
        A ``datetime.datetime`` object representing the corresponding
        Gregorian date and time, or ``None`` if inputs are missing or
        marked as invalid.
    """
    # If inputs are `None` or invalid, return `None`
    # Sometimes the server may respond in "-" instead of `None`
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
    gregorian: datetime.datetime = jalali_datetime.togregorian()
    return gregorian


def is_valid_server_address(server_address: str | None) -> bool:
    """Check whether a server address has a valid HTTP/HTTPS URL structure.

    The address must:
    - Be a non-empty string
    - Use the ``http`` or ``https`` scheme
    - Contain a network location component (host)

    This function validates only the structural format of the URL.
    It does not verify DNS resolution or server reachability.

    Args:
        server_address: Server address entered by the user.

    Returns:
        ``True`` if the address appears structurally valid,
        otherwise ``False``.
    """
    # If server address is empty return False
    if not server_address:
        return False

    # Strip empty spaces
    address: str = server_address.strip()
    if not address:
        return False

    # Must explicitly specify scheme
    if not address.startswith(("http://", "https://")):
        return False

    # Parse the URL
    parsed = urlparse(address)

    # Ensure scheme and hostname exist
    return bool(parsed.scheme and parsed.netloc)
