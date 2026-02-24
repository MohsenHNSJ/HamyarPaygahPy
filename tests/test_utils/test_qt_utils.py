"""Unit tests for qt_utils module."""

# ruff: noqa: S101
# pylint: disable=E0611
import os

import pytest
import pytestqt
import pytestqt.qtbot
from PySide6.QtWidgets import QCheckBox

from hamyar_paygah.utils.qt_utils import set_checkbox

# In headless CI or remote Linux, you need to tell Qt to use a dummy platform
os.environ["QT_QPA_PLATFORM"] = "offscreen"


@pytest.mark.parametrize(
    ("value", "expected_checked", "expected_enabled"),
    [
        (True, True, True),
        (False, False, False),
    ],
)
def test_set_checkbox(
    qtbot: pytestqt.qtbot.QtBot,
    *,
    value: bool,
    expected_checked: bool,
    expected_enabled: bool,
) -> None:
    """Test that set_checkbox sets the checkbox's checked and enabled states correctly."""
    # Create a checkbox widget and add it to qtbot for safe GUI testing
    checkbox = QCheckBox()
    qtbot.addWidget(checkbox)

    # Set initial opposite state to ensure function actually changes it
    checkbox.setChecked(not expected_checked)
    checkbox.setEnabled(not expected_enabled)

    # Call the function under test
    set_checkbox(checkbox, value=value)

    # Assertions
    assert checkbox.isChecked() == expected_checked
    assert checkbox.isEnabled() == expected_enabled
