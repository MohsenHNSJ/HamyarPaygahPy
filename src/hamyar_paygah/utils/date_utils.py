"""Utilities related to date and time."""

from datetime import datetime

import jdatetime  # type: ignore[import-untyped]


def convert_string_iso_date_to_string_persian_date(string_iso_datetime: str) -> str:
    """Converts the input ISO-8601 datetime string to Persian datetime string and returns it.

    This function also removed milliseconds.
    """
    # Convert string input to datetime
    gregorian_datetime = datetime.fromisoformat(string_iso_datetime)

    # Remove redundant milliseconds
    gregorian_datetime = gregorian_datetime.replace(microsecond=0)

    # Convert gregorian datetime to persian datetime
    persian_datetime = jdatetime.datetime.fromgregorian(
        datetime=gregorian_datetime,
    )

    return str(persian_datetime)
