"""Unit tests for qt_utils module."""

# ruff: noqa: S101
# pylint: disable=E0611
import os
from datetime import time, timedelta
from enum import Enum
from unittest.mock import Mock, patch

import jdatetime  # type: ignore[import-untyped]
import pytest
import pytestqt
import pytestqt.qtbot
from PySide6.QtWidgets import QCheckBox, QLineEdit, QPlainTextEdit

from hamyar_paygah.utils.qt_utils import (
    NOT_REGISTERED_PERSIAN_TEXT,
    set_checkbox,
    set_enum_textfield,
    set_textfield,
    typed_async_slot,
)

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


@pytest.mark.parametrize(
    ("widget_type", "value", "expected_text", "expected_enabled"),
    [
        (QLineEdit, "hello", "hello", True),
        (QPlainTextEdit, "world", "world", True),
        (QLineEdit, 42, "42", True),
        (QLineEdit, 0, NOT_REGISTERED_PERSIAN_TEXT, False),
        (QLineEdit, None, NOT_REGISTERED_PERSIAN_TEXT, False),
        (QPlainTextEdit, timedelta(hours=2), str(timedelta(hours=2)), True),
        (QLineEdit, time(13, 45), str(time(13, 45)), True),
        (
            QPlainTextEdit,
            jdatetime.date(1402, 1, 1),
            str(jdatetime.date(1402, 1, 1)),
            True,
        ),
    ],
)
def test_set_textfield(
    qtbot: pytestqt.qtbot.QtBot,
    widget_type: QLineEdit | QPlainTextEdit,
    value: str | int | None | timedelta | time | jdatetime.date,
    expected_text: str | int | None | timedelta | time | jdatetime.date,
    *,
    expected_enabled: bool,
) -> None:
    """Test that set_textfield sets text and enabled state correctly for various types."""
    # Create widget instance and add to qtbot
    widget = widget_type()  # type: ignore[operator]
    qtbot.addWidget(widget)

    # Pre-fill with opposite values to ensure function changes them
    if isinstance(widget, QLineEdit):
        widget.setText("dummy")
    else:
        widget.setPlainText("dummy")
    widget.setEnabled(not expected_enabled)

    # Call the function under test
    set_textfield(widget, value=value)

    # Assertions
    if isinstance(widget, QLineEdit):
        assert widget.text() == expected_text
    else:
        assert widget.toPlainText() == expected_text
    assert widget.isEnabled() == expected_enabled


class FakeEnum(Enum):
    """Fake enum for testing set_enum_textfield function."""

    SUCCESS = "success"
    FAILURE = "failure"

    @property
    def persian_label(self) -> str:
        """Fake property."""
        return f"persian_{self.value}"


@pytest.mark.parametrize(
    ("enum_value", "expected_text", "expected_enabled"),
    [
        (None, NOT_REGISTERED_PERSIAN_TEXT, False),
        (FakeEnum.SUCCESS, "persian_success", True),
        (FakeEnum.FAILURE, "persian_failure", True),
    ],
)
def test_set_enum_textfield(
    qtbot: pytestqt.qtbot.QtBot,
    enum_value: Enum,
    expected_text: str,
    *,
    expected_enabled: bool,
) -> None:
    """Test that set_enum_textfield sets text and enabled state correctly."""
    widget = QLineEdit()
    qtbot.addWidget(widget)

    # Force opposite state to ensure function controls state deterministically
    widget.setText("dummy")
    widget.setEnabled(not expected_enabled)

    set_enum_textfield(
        widget,
        enum_value,  # type: ignore[arg-type]
    )

    assert widget.text() == expected_text
    assert widget.isEnabled() is expected_enabled


async def test_typed_async_slot_wraps_asyncslot() -> None:
    """Unit test for typed_async_slot decorator."""
    mock_decorator = Mock()

    async def sample_function() -> None:
        return None

    mock_decorator.return_value = sample_function

    with patch(
        "hamyar_paygah.utils.qt_utils.asyncSlot",
        return_value=mock_decorator,
    ) as mock_asyncslot:
        decorator = typed_async_slot(int, name="test")

        # Ensure asyncSlot was called with correct args
        mock_asyncslot.assert_called_once_with(int, name="test")

        decorated = decorator(sample_function)

        # Ensure decorator was applied
        mock_decorator.assert_called_once_with(sample_function)

        assert decorated is sample_function
