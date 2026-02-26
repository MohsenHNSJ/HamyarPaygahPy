"""Utilities related to date and time."""

# ruff: noqa: DTZ001
# pylint: disable=E0611
import datetime

import jdatetime  # type: ignore[import-untyped]
from PySide6.QtCore import QDate


def convert_iso_datetime_to_persian_string(string_iso_datetime: str) -> str:
    """Convert an ISO-8601 datetime string to a Persian datetime string.

    The input string must be in a format supported by
    ``datetime.datetime.fromisoformat``. Microseconds are removed
    before conversion.

    Args:
        string_iso_datetime: A datetime string in ISO-8601 format.

    Returns:
        A string representation of the corresponding Persian datetime
        without microseconds.

    Raises:
        ValueError: If the input string is not a valid ISO-8601 datetime.
    """
    gregorian_datetime = datetime.datetime.fromisoformat(string_iso_datetime)

    # Remove redundant milliseconds
    gregorian_datetime = gregorian_datetime.replace(microsecond=0)

    # Convert gregorian datetime to persian datetime
    persian_datetime = jdatetime.datetime.fromgregorian(
        datetime=gregorian_datetime,
    )

    return str(persian_datetime)


def qdate_to_datetime(gregorian_date: QDate) -> datetime.datetime:
    """Convert a QDate to a datetime.datetime object.

    The returned datetime has time set to 00:00:00.

    Args:
        gregorian_date: A valid QDate instance.

    Returns:
        A datetime.datetime representing the same date.
    """
    return datetime.datetime(
        gregorian_date.year(),
        gregorian_date.month(),
        gregorian_date.day(),
    )


def gregorian_to_persian(
    gregorian_date: datetime.datetime | None,
) -> jdatetime.datetime | None:
    """Convert a Gregorian datetime to a Jalali (Persian) datetime.

    Args:
        gregorian_date: A Gregorian ``datetime.datetime`` instance
            or ``None``.

    Returns:
        A ``jdatetime.datetime`` representing the same moment in the
        Jalali calendar, or ``None`` if the input is ``None``.

    Raises:
        TypeError: If the input is not ``None`` and not a
            ``datetime.datetime`` instance.
    """
    if gregorian_date is None:
        return None

    return jdatetime.datetime.fromgregorian(datetime=gregorian_date)
