"""Tests for core module."""

import datetime

from private_info import SERVER_URL

from src.hamyar_paygah.core import get_missions_list

from_date: datetime.datetime = datetime.datetime(2025, 12, 28)  # noqa: DTZ001
to_date: datetime.datetime = datetime.datetime(2025, 12, 30)  # noqa: DTZ001

test_response: str = get_missions_list(SERVER_URL, from_date, to_date, 5)
