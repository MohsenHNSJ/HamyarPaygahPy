# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mission_details_tab.ui'
##
# Created by: Qt User Interface Compiler version 6.10.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QLabel, QSizePolicy, QWidget


class Ui_mission_details_tab:
    def setupUi(self, mission_details_tab):
        if not mission_details_tab.objectName():
            mission_details_tab.setObjectName("mission_details_tab")
        mission_details_tab.resize(750, 650)
        mission_details_tab.setMinimumSize(QSize(750, 650))
        mission_details_tab.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        mission_details_tab.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.label = QLabel(mission_details_tab)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(310, 240, 57, 14))

        self.retranslateUi(mission_details_tab)

        QMetaObject.connectSlotsByName(mission_details_tab)

    # setupUi

    def retranslateUi(self, mission_details_tab):
        mission_details_tab.setWindowTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06af\u0632\u0627\u0631\u0634 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a",
                None,
            ),
        )
        self.label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "TextLabel",
                None,
            ),
        )

    # retranslateUi
