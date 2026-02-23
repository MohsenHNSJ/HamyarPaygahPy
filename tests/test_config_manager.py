"""Unit tests for config_manager module."""

# ruff: noqa: S101, ANN401
import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from hamyar_paygah.config.config_manager import (
    get_config_value,
    load_config,
    save_config,
    set_config_value,
)


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


@pytest.mark.parametrize(
    "config_to_save",
    [
        pytest.param({}, id="empty dict"),  # Edge case: empty dictionary
        # Simple key-value
        pytest.param({"simple": "value"}, id="simple dict"),
        pytest.param(
            {"number": 123, "bool": True},
            id="primitive types",
        ),  # Primitive types
        # Nested structure
        pytest.param({"nested": {"a": 1, "b": [1, 2]}}, id="nested dict"),
        pytest.param(
            {"unicode": "✓ Привет 🌍"},
            id="unicode characters",
        ),  # Unicode support
    ],
)
def test_save_config_parametrized(config_to_save: dict[str, Any]) -> None:
    """Parametrized test for `save_config`.

    Ensures any dictionary is correctly serialized to JSON and written to disk
    with UTF-8 encoding and pretty-printing.

    Args:
        config_to_save (dict): The configuration dictionary to save.
    """
    # Patch the write_text method on Path class to avoid AttributeError
    with patch.object(Path, "write_text") as write_text_mock:
        # Call the function under test
        save_config(config_to_save)

        # Ensure write_text was called exactly once
        write_text_mock.assert_called_once()

        # Capture the arguments passed to write_text
        args, kwargs = write_text_mock.call_args

        # The first positional argument should be the serialized JSON string
        json_arg = args[0]
        # The encoding keyword argument should be "utf-8"
        encoding_arg = kwargs.get("encoding")

        # Verify UTF-8 encoding
        assert encoding_arg == "utf-8", f"Expected UTF-8 encoding, got {encoding_arg}"

        # Verify the JSON string deserializes back to the original dictionary
        deserialized = json.loads(json_arg)
        assert deserialized == config_to_save, "Serialized JSON does not match input dictionary"


@pytest.mark.parametrize(
    ("existing_config", "key_to_set", "value_to_set", "expected_config"),
    [
        # Empty existing config, add one key
        ({}, "new_key", "new_value", {"new_key": "new_value"}),
        # Existing config with different keys, add a new key
        ({"a": 1}, "b", 2, {"a": 1, "b": 2}),
        # Existing config with same key, update value
        ({"key": "old"}, "key", "updated", {"key": "updated"}),
        # Nested value update
        ({"nested": {"a": 1}}, "nested", {"a": 2}, {"nested": {"a": 2}}),
        # Unicode value
        ({}, "emoji", "✓ 🌍", {"emoji": "✓ 🌍"}),
    ],
)
def test_set_config_value(
    existing_config: dict[str, Any],
    key_to_set: str,
    value_to_set: Any,
    expected_config: dict[str, Any],
) -> None:
    """Test that `set_config_value` works properly.

    Loads the existing configuration, sets the specified key to the new value,
    and saves the updated configuration.

    This test patches `load_config` to return a controlled dictionary
    and `save_config` to capture what would be written to disk.

    Args:
        existing_config: Dictionary returned by patched load_config.
        key_to_set: Key to update in the configuration.
        value_to_set: Value to set for the key.
        expected_config: Expected dictionary passed to save_config.
    """
    # Patch load_config to return a predefined dictionary
    with (
        patch(
            "hamyar_paygah.config.config_manager.load_config",
            return_value=existing_config,
        ) as load_mock,
        patch("hamyar_paygah.config.config_manager.save_config") as save_mock,
    ):
        # Call the function under test
        set_config_value(key_to_set, value_to_set)

        # Ensure load_config was called exactly once
        load_mock.assert_called_once()

        # Ensure save_config was called exactly once with the updated dictionary
        save_mock.assert_called_once_with(expected_config)


@pytest.mark.parametrize(
    ("config_dict", "key_to_get", "default_value", "expected_value"),
    [
        # Key exists in config
        ({"a": 1, "b": 2}, "a", None, 1),
        # Key does not exist, default provided
        ({"a": 1}, "b", 99, 99),
        # Key does not exist, default is None
        ({"a": 1}, "b", None, None),
        # Nested value returned as-is
        ({"nested": {"x": 10}}, "nested", None, {"x": 10}),
        # Unicode value
        ({"emoji": "✓ 🌍"}, "emoji", None, "✓ 🌍"),
        # Key exists, default ignored
        ({"key": "value"}, "key", "default", "value"),
    ],
)
def test_get_config_value(
    config_dict: dict[str, Any],
    key_to_get: str,
    default_value: Any,
    expected_value: Any,
) -> None:
    """Test that `get_config_value` works correctly.

    Retrieves values from the configuration dictionary,
    and returns the default value when the key is not present.

    This test patches `load_config` to return a controlled dictionary
    to avoid reading actual files.

    Args:
        config_dict: Dictionary returned by patched load_config.
        key_to_get: Configuration key to retrieve.
        default_value: Default value to return if key does not exist.
        expected_value: Expected value returned by get_config_value.
    """
    # Patch load_config to return the controlled dictionary
    with patch(
        "hamyar_paygah.config.config_manager.load_config",
        return_value=config_dict,
    ) as load_mock:
        # Call the function under test
        result = get_config_value(key_to_get, default_value)

        # Ensure load_config was called exactly once
        load_mock.assert_called_once()

        # Verify that the returned value matches expected
        assert result == expected_value
