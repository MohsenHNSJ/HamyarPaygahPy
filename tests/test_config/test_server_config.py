"""Units tests for server_config module."""

# ruff: noqa: S101, ANN401
from typing import Any
from unittest.mock import patch

import pytest

from hamyar_paygah.config.server_config import (
    _SERVER_ADDRESS_KEY,
    load_server_address,
    save_server_address,
)


@pytest.mark.parametrize(
    ("config_value", "is_valid_return", "expected_result"),
    [
        # Valid string address
        ("127.0.0.1", True, "127.0.0.1"),
        # Missing address (None)
        (None, True, None),
        # Invalid string address
        ("invalid-address", False, None),
        # Address is not a string
        (12345, True, None),
        # Empty string
        ("", False, None),
    ],
)
def test_load_server_address(
    *,
    config_value: Any,
    is_valid_return: bool,
    expected_result: Any,
) -> None:
    """Test that `load_server_address` works correctly.

    Retrieves the server address from the configuration,
    validating it with `is_valid_server_address`.

    Scenarios:
    1. Valid string -> returns address
    2. Missing -> returns None
    3. Invalid string -> returns None
    4. Non-string -> returns None
    5. Empty string -> returns None
    """
    # Patch get_config_value to return controlled test value
    with (
        patch(
            "hamyar_paygah.config.server_config.get_config_value",
            return_value=config_value,
        ) as get_mock,
        patch(
            "hamyar_paygah.config.server_config.is_valid_server_address",
            return_value=is_valid_return,
        ) as valid_mock,
    ):
        # Call the function under test
        result = load_server_address()

        # Ensure get_config_value is called exactly once with the correct key
        get_mock.assert_called_once_with(_SERVER_ADDRESS_KEY)

        # Ensure is_valid_server_address is called if input is a string
        if isinstance(config_value, str):
            valid_mock.assert_called_once_with(config_value)
        else:
            valid_mock.assert_not_called()

        # Verify the returned result matches expected
        assert result == expected_result


@pytest.mark.parametrize(
    "server_address",
    [
        pytest.param("127.0.0.1", id="ipv4 address"),
        pytest.param("::1", id="ipv6 address"),
        pytest.param("example.com", id="hostname"),
        pytest.param("", id="empty string"),
        pytest.param("server-123_✓", id="unicode / special chars"),
    ],
)
def test_save_server_address(server_address: str) -> None:
    """Test that `save_server_address` works correctly.

    Calls `set_config_value` with the server address under the correct key.

    Args:
        server_address (str): Server address to save.
    """
    # Patch set_config_value to prevent touching actual configuration
    with patch("hamyar_paygah.config.server_config.set_config_value") as set_mock:
        # Call the function under test
        save_server_address(server_address)

        # Ensure set_config_value is called exactly once
        set_mock.assert_called_once_with(_SERVER_ADDRESS_KEY, server_address)
