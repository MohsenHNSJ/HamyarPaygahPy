"""Utility functions related to Qt UI."""

# pylint: disable=E0611
from datetime import time, timedelta
from enum import Enum

import jdatetime  # type: ignore[import-untyped]
from PySide6.QtWidgets import QCheckBox, QLineEdit, QPlainTextEdit

NOT_REGISTERED_PERSIAN_TEXT: str = "ثبت نشده"
"""Text to show when an information is not yet registered by EMS"""


def set_checkbox(checkbox: QCheckBox, *, value: bool) -> None:
    """Sets the checkbox state and enables it if value is True, otherwise disables it."""
    checkbox.setChecked(value)
    checkbox.setEnabled(value)


def set_textfield(
    textfield: QLineEdit | QPlainTextEdit,
    value: int | str | timedelta | time | jdatetime.date | None,
) -> None:
    """Sets the text field with value, if None or zero, disables it."""
    if value is not None and (not isinstance(value, int) or value != 0):
        if isinstance(textfield, QLineEdit):
            textfield.setText(str(value))
        else:
            textfield.setPlainText(str(value))
    else:
        if isinstance(textfield, QLineEdit):
            textfield.setText(NOT_REGISTERED_PERSIAN_TEXT)
        else:
            textfield.setPlainText(NOT_REGISTERED_PERSIAN_TEXT)
        textfield.setEnabled(False)


def set_enum_textfield(textfield: QLineEdit, enum_value: Enum | None) -> None:
    """Sets the text field with the value of an enum, if None or zero, disables it."""
    if enum_value is not None:
        textfield.setText(
            enum_value.persian_label,  # type: ignore[attr-defined]
        )
    else:
        textfield.setText(NOT_REGISTERED_PERSIAN_TEXT)
        textfield.setEnabled(False)
