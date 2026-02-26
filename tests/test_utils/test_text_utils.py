"""Unit tests for text_utils functions."""
# ruff: noqa: S101, DTZ001

import datetime

import pytest

from hamyar_paygah.utils.text_utils import (
    convert_date_and_time_to_datetime,
    convert_date_to_datetime,
    is_valid_server_address,
)


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        # None / empty cases
        (None, None),
        ("", None),
        ("   ", None),
        # Valid Jalali date: 1402/01/01 == 2023-03-21
        ("1402/01/01", datetime.datetime(2023, 3, 21)),
    ],
)
def test_convert_date_to_datetime(
    input_value: str | None,
    expected: datetime.datetime | None,
) -> None:
    """Tests the convert_date_to_datetime function."""
    result = convert_date_to_datetime(input_value)
    assert result == expected

    if result is not None:
        # Ensure midnight normalization
        assert result.time() == datetime.time.min


@pytest.mark.parametrize(
    ("date_input", "time_input", "expected"),
    [
        # None handling
        (None, "10:30", None),
        ("1402/01/01", None, None),
        # Sentinel "-" handling
        ("-", "10:30", None),
        ("1402/01/01", "-", None),
        # Valid conversion
        # 1402/01/01 10:30 (Jalali) == 2023-03-21 10:30 (Gregorian)
        (
            "1402/01/01",
            "10:30",
            datetime.datetime(2023, 3, 21, 10, 30),
        ),
    ],
)
def test_convert_date_and_time_to_datetime(
    date_input: str | None,
    time_input: str | None,
    expected: datetime.datetime | None,
) -> None:
    """Tests convert_date_and_time_to_datetime function."""
    result = convert_date_and_time_to_datetime(date_input, time_input)
    assert result == expected


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        # None and empty cases
        (None, False),
        ("", False),
        ("   ", False),
        # Missing scheme
        ("example.com", False),
        ("www.example.com", False),
        # Wrong scheme
        ("ftp://example.com", False),
        ("file://localhost", False),
        # Missing host
        ("http://", False),
        ("https://", False),
        # Valid HTTP/HTTPS
        ("http://example.com", True),
        ("https://example.com", True),
        # Valid with port
        ("http://example.com:8080", True),
        # Valid with path
        ("https://example.com/api/v1", True),
        # Leading/trailing whitespace
        ("  https://example.com  ", True),
    ],
)
def test_is_valid_server_address(
    input_value: str | None,
    *,
    expected: bool,
) -> None:
    """Tests the is_valid_server_address function."""
    assert is_valid_server_address(input_value) is expected
