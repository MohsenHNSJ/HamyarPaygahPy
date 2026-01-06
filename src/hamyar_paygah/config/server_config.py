"""Server configuration.

Handles loading snd saving the EMS server configuration.
"""

from __future__ import annotations

from typing import Final

from hamyar_paygah.config.config_manager import get_config_value, set_config_value
from hamyar_paygah.utils.text_utils import is_valid_server_address

_SERVER_ADDRESS_KEY: Final[str] = "server_address"


def load_server_address() -> str | None:
    """Load the server address from the application configuration file.

    Returns:
        The stored server address if present and valid, otherwise ``None``.
    """
    # Get the server address
    server_address = get_config_value(_SERVER_ADDRESS_KEY)

    # If it's string and valid return it
    if isinstance(server_address, str) and is_valid_server_address(server_address):
        return server_address

    # Else return None
    return None


def save_server_address(server_address: str) -> None:
    """Persist the server address into the application configuration file.

    Args:
        server_address: Server address to store.
    """
    set_config_value(_SERVER_ADDRESS_KEY, server_address)
