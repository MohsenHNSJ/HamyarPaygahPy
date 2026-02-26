"""Utility functions related to Qt UI."""

# pylint: disable=E0611
from collections.abc import Awaitable, Callable
from datetime import time, timedelta
from typing import Any, TypeVar, cast

import jdatetime  # type: ignore[import-untyped]
from PySide6.QtWidgets import QCheckBox, QLineEdit, QMessageBox, QPlainTextEdit, QWidget
from qasync import asyncSlot  # type: ignore[import-untyped]

from hamyar_paygah.models.mission_details_submodels.location_and_emergency_model import (
    AccidentType,
    IllnessType,
    InjuryRole,
    LocationType,
    VehicleType,
)
from hamyar_paygah.models.mission_details_submodels.mission_result_model import (
    MissionOutcome,
)
from hamyar_paygah.models.mission_details_submodels.pupils_lungs_heart_model import (
    BreathingRhythm,
    HeartRhythm,
    HeartSound,
    LungSound,
    PupilStatus,
)
from hamyar_paygah.models.mission_details_submodels.trauma_types_model import (
    DistalPulseStatus,
    FractureType,
    PatientExtrication,
)

NOT_REGISTERED_PERSIAN_TEXT: str = "ثبت نشده"
"""Text to show when an information is not yet registered by EMS"""


def set_checkbox(checkbox: QCheckBox, *, value: bool) -> None:
    """Set a checkbox state and enabled status.

    The checkbox is checked and enabled if ``value`` is ``True``.
    If ``value`` is ``False``, the checkbox is unchecked and disabled.

    Args:
        checkbox: The QCheckBox instance to modify.
        value: Determines both the checked state and whether the checkbox is enabled.
    """
    checkbox.setEnabled(value)
    checkbox.setChecked(value)


def set_textfield(
    textfield: QLineEdit | QPlainTextEdit,
    value: int | str | timedelta | time | jdatetime.date | None,
) -> None:
    """Set a text field with a value or disable it if empty/zero.

    This function updates the text of a QLineEdit or QPlainTextEdit widget.
    - If `value` is None or zero (for integers), the field is disabled and
    filled with a placeholder text (`NOT_REGISTERED_PERSIAN_TEXT`).
    - Otherwise, the field is updated with `str(value)` and will be enabled.

    Args:
        textfield: A QLineEdit or QPlainTextEdit widget to update.
        value: The value to set. Can be int, str, timedelta, time, jdatetime.date,
            or None. Integers equal to zero are treated as empty.

    Returns:
        None

    Notes:
        - This function is designed to handle various types safely.
        - `NOT_REGISTERED_PERSIAN_TEXT` is used as a placeholder for missing values.
    """
    # Determine if the value is valid (not None and not integer zero)
    is_valid = value is not None and not (isinstance(value, int) and value == 0)

    # Convert value to string or use placeholder text
    text_to_set = str(value) if is_valid else NOT_REGISTERED_PERSIAN_TEXT

    # Set the text based on widget type
    if isinstance(textfield, QLineEdit):
        textfield.setText(text_to_set)
    else:  # QPlainTextEdit
        textfield.setPlainText(text_to_set)

    # Disable the field if value is invalid, Enable if valid.
    textfield.setEnabled(is_valid)


def set_enum_textfield(
    textfield: QLineEdit,
    enum_value: MissionOutcome
    | LocationType
    | AccidentType
    | IllnessType
    | InjuryRole
    | VehicleType
    | PupilStatus
    | LungSound
    | BreathingRhythm
    | HeartSound
    | HeartRhythm
    | PatientExtrication
    | FractureType
    | DistalPulseStatus
    | None,
) -> None:
    """Set a QLineEdit with the Persian label of a domain enum.

    If `enum_value` is None, the text field is populated with
    `NOT_REGISTERED_PERSIAN_TEXT` and disabled.

    If a valid enum value is provided, its `persian_label`
    attribute is displayed and the field is enabled.

    Args:
        textfield: The QLineEdit widget to update.
        enum_value: A supported domain enum instance or None.

    Returns:
        None
    """
    if enum_value is None:
        textfield.setText(NOT_REGISTERED_PERSIAN_TEXT)
        textfield.setEnabled(False)
        return

    textfield.setText(
        enum_value.persian_label,
    )
    textfield.setEnabled(True)


F = TypeVar("F", bound=Callable[..., Awaitable[Any]])


def typed_async_slot(*args: Any, **kwargs: Any) -> Callable[[F], F]:  # noqa: ANN401
    """Typed wrapper around qasync.asyncSlot.

    Provides proper type hints for the untyped ``asyncSlot`` decorator
    from the ``qasync`` module. This allows static type checkers such
    as mypy or Pyright to correctly infer the signature of decorated
    async functions.

    Args:
        *args: Positional arguments forwarded to ``asyncSlot``.
        **kwargs: Keyword arguments forwarded to ``asyncSlot``.

    Returns:
        A decorator that preserves the type signature of the async
        function it decorates.
    """
    return cast("Callable[[F], F]", asyncSlot(*args, **kwargs))


def show_error_dialog(parent: QWidget, title: str, message: str) -> None:
    """Display an error dialog with a critical icon.

    This function creates a modal error dialog attached to the given parent
    widget. The dialog displays a title and a message to inform the user of
    an error. Execution is blocked until the user closes the dialog.

    Args:
        parent (QWidget): The parent widget for the dialog. The dialog will
        be centered on this widget.
        title (str): The title displayed in the window's title bar.
        message (str): The error message to display in the dialog body.

    Returns:
        None

    Notes:
        - This function uses a modal dialog; it will block interaction with
          other windows until closed.
        - For non-blocking dialogs, consider using `dialog.show()` instead
          of `dialog.exec()`.
    """
    dialog = QMessageBox(parent)
    dialog.setWindowTitle(title)
    dialog.setText(message)
    dialog.setIcon(QMessageBox.Icon.Critical)
    dialog.exec()
