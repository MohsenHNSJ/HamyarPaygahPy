"""View model for Missions list table view."""

# mypy: ignore-errors
# ruff: noqa: ARG002, ANN001, N802, E501
# pylint: disable=W0613,C0103,E0611,C0301

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QWidget

from hamyar_paygah.models.mission_model import Mission
from hamyar_paygah.utils.date_utils import convert_string_iso_date_to_string_persian_date


class MissionTableModel(QAbstractTableModel):
    """Model for Qt TableView to show missions data."""

    def __init__(self, missions_list: list[Mission], parent: QWidget | None = None) -> None:
        """Initialize the model for missions list table."""
        super().__init__(parent)

        # Save the list of missions
        self._missions_list = missions_list

        # Name the columns
        self._columns = [
            ("شماره ماموریت", lambda m: m.id),
            ("نام مددجو", lambda m: m.patient_name),
            ("شماره مددجو", lambda m: m.patient_id),
            ("کد آمبولانس", lambda m: m.ambulance_code),
            ("نام بیمارستان", lambda m: m.hospital_name),
            ("تاریخ", lambda m: convert_string_iso_date_to_string_persian_date(m.date)),
            ("آدرس", lambda m: m.address),
            ("نتیجه", lambda m: m.result),
        ]

    def rowCount(self, parent=QModelIndex()) -> int:  # noqa: B008
        """Returns the number of rows under the given parent.

        When the parent is valid it means that rowCount
        is returning the number of children of parent.
        """
        return len(self._missions_list)

    def columnCount(self, parent=QModelIndex()) -> int:  # noqa: B008
        """Returns the number of columns for the children of the given parent.

        In most subclasses, the number of columns is independent of the parent.
        """
        return len(self._columns)

    def data(self, index: QModelIndex, role=Qt.DisplayRole) -> None | str:  # type: ignore[]
        """Returns the data stored under the given role for the item referred to by the index."""
        if not index.isValid():
            return None

        mission = self._missions_list[index.row()]
        _, getter = self._columns[index.column()]

        if role == Qt.DisplayRole:  # type: ignore[]
            value = getter(mission)
            return "" if value is None else str(value)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole) -> None | str | int:  # type: ignore[]
        """Returns the data for the given role and section in the header with the specified orientation.

        For horizontal headers, the section number corresponds to the column number.
        Similarly, for vertical headers, the section number corresponds to the row number.
        """
        if role != Qt.DisplayRole:  # type: ignore[]
            return None

        if orientation == Qt.Horizontal:  # type: ignore[]
            return self._columns[section][0]

        return section + 1
