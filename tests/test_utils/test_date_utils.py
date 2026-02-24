"""Unit tests for date_utils module."""

# ruff: noqa: S101, DTZ001
# pylint: disable=E0611
import datetime

import jdatetime  # type: ignore[import-untyped]
import pytest
from PySide6.QtCore import QDate

from hamyar_paygah.utils.date_utils import (
    convert_iso_datetime_to_persian_string,
    gregorian_to_persian,
    qdate_to_datetime,
)


@pytest.mark.parametrize(
    "iso_string",
    [
        "2026-02-23T12:30:45",
        "2026-02-23T12:30:45.123456",
        "2026-02-23T12:30:45+00:00",
    ],
)
def test_valid_iso_inputs(iso_string: str) -> None:
    """Test valid ISO inputs convert correctly."""
    result = convert_iso_datetime_to_persian_string(iso_string)

    gregorian = datetime.datetime.fromisoformat(iso_string)
    expected = str(
        jdatetime.datetime.fromgregorian(
            datetime=gregorian.replace(microsecond=0),
        ),
    )

    assert result == expected


@pytest.mark.parametrize(
    ("year", "month", "day"),
    [
        (2026, 2, 23),
        (2000, 1, 1),
        (1999, 12, 31),
        (2024, 2, 29),  # leap year
    ],
)
def test_qdate_to_datetime_valid_dates(year: int, month: int, day: int) -> None:
    """Ensure valid QDate objects convert correctly to datetime."""
    q_date = QDate(year, month, day)

    result = qdate_to_datetime(q_date)

    assert result == datetime.datetime(year, month, day)
    assert result.hour == 0
    assert result.minute == 0
    assert result.second == 0
    assert result.microsecond == 0


@pytest.mark.parametrize(
    "gregorian_input",
    [
        None,
        datetime.datetime(2026, 2, 23),
        datetime.datetime(2000, 1, 1, 12, 30, 45),
        datetime.datetime(2024, 2, 29),  # leap year
        datetime.datetime(1999, 12, 31, 23, 59, 59),
    ],
)
def test_gregorian_to_persian(gregorian_input: None | datetime.datetime) -> None:
    """Ensure Gregorian datetimes convert correctly to Jalali."""
    result = gregorian_to_persian(gregorian_input)

    if gregorian_input is None:
        assert result is None
    else:
        expected = jdatetime.datetime.fromgregorian(
            datetime=gregorian_input,
        )

        assert isinstance(result, jdatetime.datetime)
        assert result == expected

        # Ensure time components are preserved
        assert result.hour == gregorian_input.hour
        assert result.minute == gregorian_input.minute
        assert result.second == gregorian_input.second
        assert result.microsecond == gregorian_input.microsecond
