"""Utilities related to date and time."""

# ruff: noqa: DTZ001
# pylint: disable=E0611
import datetime

import jdatetime  # type: ignore[import-untyped]
from PySide6.QtCore import QDate


def convert_string_iso_date_to_string_persian_date(string_iso_datetime: str) -> str:
    """Converts the input ISO-8601 datetime string to Persian datetime string and returns it.

    This function also removed milliseconds.
    """
    # Convert string input to datetime
    gregorian_datetime = datetime.datetime.fromisoformat(string_iso_datetime)

    # Remove redundant milliseconds
    gregorian_datetime = gregorian_datetime.replace(microsecond=0)

    # Convert gregorian datetime to persian datetime
    persian_datetime = jdatetime.datetime.fromgregorian(
        datetime=gregorian_datetime,
    )

    return str(persian_datetime)


def convert_persian_q_date_to_gregorian_pythonic_date(persian_q_date: QDate) -> datetime.datetime:
    """Converts Persian date in QDate format to Pythonic gregorian datetime object.

    Args:
        persian_q_date (PySide6.QtCore.QDate): Persian date in QDate format.

    Returns:
        datetime.datetime: Pythonic datetime object in gregorian format.
    """
    # Convert Persian QDate to gregorian QDate
    gregorian_date: QDate = persian_q_date

    # Convert QDate to normal pythonic datetime object
    pythonic_datetime: datetime.datetime = datetime.datetime(
        gregorian_date.year(),
        gregorian_date.month(),
        gregorian_date.day(),
    )

    # Return pythonic datetime
    return pythonic_datetime


def convert_gregorian_date_to_persian_date(
    gregorian_date: datetime.datetime | None,
) -> jdatetime.datetime | None:
    """Converts gregorian date to jalali date.

    Args:
        gregorian_date (datetime.datetime | None): Gregorian date

    Returns:
        jdatetime.datetime | None: Jalali date or None if the input is also None.
    """
    if gregorian_date is not None:
        # Convert to jalali and return
        return jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    # Else, return None
    return None
