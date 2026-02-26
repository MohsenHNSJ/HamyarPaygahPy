"""Unit tests for math_utils module."""

# ruff: noqa: S101
import datetime

import pytest

from hamyar_paygah.utils.math_utils import calculate_time_delta


@pytest.mark.parametrize(
    ("start_time", "end_time", "expected_seconds"),
    [
        # Normal same-day interval
        (datetime.time(10, 0), datetime.time(12, 0), 2 * 3600),
        # Same time -> zero duration
        (datetime.time(9, 30), datetime.time(9, 30), 0),
        # Midnight crossover
        (datetime.time(23, 30), datetime.time(0, 15), 45 * 60),
        # Large midnight crossover
        (datetime.time(18, 0), datetime.time(6, 0), 12 * 3600),
        # Edge: one minute before midnight to midnight
        (datetime.time(23, 59), datetime.time(0, 0), 60),
        # Edge: midnight to early morning
        (datetime.time(0, 0), datetime.time(1, 0), 3600),
    ],
)
def test_calculate_time_delta_valid_cases(
    start_time: datetime.time,
    end_time: datetime.time,
    expected_seconds: int,
) -> None:
    """Ensure calculate_time_delta returns correct durations."""
    result = calculate_time_delta(start_time, end_time)

    assert isinstance(result, datetime.timedelta)
    assert result.total_seconds() == expected_seconds
    assert result >= datetime.timedelta(0)


@pytest.mark.parametrize(
    ("start_time", "end_time"),
    [
        (None, datetime.time(10, 0)),
        (datetime.time(10, 0), None),
        (None, None),
    ],
)
def test_calculate_time_delta_none_inputs(
    start_time: datetime.time | None,
    end_time: datetime.time | None,
) -> None:
    """Ensure function returns None if either input is None."""
    result = calculate_time_delta(start_time, end_time)
    assert result is None
