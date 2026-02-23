"""Unit tests for config_manager module."""

# ruff: noqa: S101
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from hamyar_paygah.config.config_manager import load_config


@pytest.mark.parametrize(
    ("exists", "read_text", "expected"),
    [
        # Each tuple represents a test case
        pytest.param(False, None, {}, id="File does not exist"),
        pytest.param(True, OSError, {}, id="File unreadable"),
        pytest.param(True, "invalid json", {}, id="Invalid JSON"),
        pytest.param(True, json.dumps([1, 2, 3]), {}, id="JSON not dict"),
        pytest.param(
            True,
            json.dumps({"key": "value"}),
            {
                "key": "value",
            },
            id="Valid JSON dict",
        ),
    ],
)
def test_load_config_cases(
    *,
    exists: bool,
    read_text: None | type[OSError] | str,
    expected: dict[str, str],
) -> None:
    """Test `load_config` under various scenarios to ensure it always returns a dictionary.

    Scenarios tested:
    1. File does not exist.
    2. File exists but raises an OSError when reading.
    3. File exists but contains invalid JSON.
    4. File exists with valid JSON that is not a dictionary (e.g., a list).
    5. File exists with valid JSON dictionary.

    Args:
        exists (bool): Whether the configuration file should be treated as existing.
        read_text (str | Exception | None): Content returned by read_text or exception to raise.
        expected (dict): The expected dictionary that load_config should return.
    """
    # Patch Path.exists and Path.read_text methods for all Path objects
    # so we can simulate file system behavior without touching real files.
    with (
        patch.object(Path, "exists", return_value=exists) as _,
        patch.object(Path, "read_text") as read_text_mock,
    ):
        # Configure the behavior of read_text depending on the test case
        if isinstance(read_text, type) and issubclass(read_text, Exception):
            # If read_text is an Exception class, calling read_text will raise it
            read_text_mock.side_effect = read_text
        elif read_text is not None:
            # If read_text is a string, calling read_text will return that string
            read_text_mock.return_value = read_text

        # Call the function under test
        result = load_config()

    # Verify that the result matches the expected dictionary
    assert result == expected
