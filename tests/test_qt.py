"""Test for qt."""

# pylint: disable=C0114,I1101
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)  # type: ignore[attr-defined]

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
