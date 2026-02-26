"""View model for consumables list table in Mission details view."""

# mypy: ignore-errors
# ruff: noqa: ANN001,B008,ARG002,N802
# pylint: disable=W0613,C0103,E0611,C0301
from collections import Counter
from typing import Literal

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class ConsumablesTableModel(QAbstractTableModel):
    """Table model for displaying consumables used in a mission."""

    COLUMN_ITEM = 0
    COLUMN_QUANTITY = 1

    def __init__(self, items: Counter[str] | None = None, parent=None) -> None:
        """Initialize the model with a Counter of consumable items."""
        super().__init__(parent)
        self._items: list[tuple[str, int]] = []
        self.set_items(items or Counter())

    def set_items(self, items: Counter[str]) -> None:
        """Replace model data with new consumables."""
        # Signal the model is changing to update any connected views
        self.beginResetModel()

        # Sort descending by quantity
        self._items = sorted(
            items.items(),
            key=lambda x: (-x[1], x[0]),
        )

        self.endResetModel()

    def rowCount(self, parent=QModelIndex()) -> int:
        """Returns the number of rows in the model.

        which corresponds to the number of unique consumable items.
        """
        if parent.isValid():
            return 0
        return len(self._items)

    def columnCount(self, parent=QModelIndex()) -> int:
        """Returns the number of columns in the model."""
        return 2

    def data(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        index: QModelIndex,
        role=Qt.DisplayRole,  # type: ignore[untyped-arg]
    ) -> None | str | int:
        """Returns the data to be displayed for a given cell based on the role."""
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        item_name, quantity = self._items[row]

        if role == Qt.DisplayRole:  # type: ignore[untyped-compare]
            if column == self.COLUMN_ITEM:
                return item_name
            if column == self.COLUMN_QUANTITY:
                return quantity

        return None

    def headerData(
        self,
        section,
        orientation,
        role=Qt.DisplayRole,  # pyright: ignore[reportAttributeAccessIssue]
    ) -> Literal["نوع", "تعداد"] | None:
        """Returns the header data for the given section and orientation based on the role."""
        if role != Qt.DisplayRole:  # pyright: ignore[reportAttributeAccessIssue]
            return None

        if orientation == Qt.Horizontal:  # type: ignore[untyped-compare]
            if section == self.COLUMN_ITEM:
                return "نوع"
            if section == self.COLUMN_QUANTITY:
                return "تعداد"

        return None
