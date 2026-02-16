# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201,C0302,C0325
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001, PLR2004
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'region_analyzer_tab.ui'
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
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_region_analyzer_tab:
    def setupUi(self, region_analyzer_tab):
        if not region_analyzer_tab.objectName():
            region_analyzer_tab.setObjectName("region_analyzer_tab")
        region_analyzer_tab.resize(700, 684)
        region_analyzer_tab.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        region_analyzer_tab.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.verticalLayout = QVBoxLayout(region_analyzer_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QScrollArea(region_analyzer_tab)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            "scrollAreaWidgetContents",
        )
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 680, 664))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.missions_list_search_filters = QWidget(
            self.scrollAreaWidgetContents,
        )
        self.missions_list_search_filters.setObjectName(
            "missions_list_search_filters",
        )
        self.horizontalLayout_2 = QHBoxLayout(
            self.missions_list_search_filters,
        )
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.from_date_label = QLabel(self.missions_list_search_filters)
        self.from_date_label.setObjectName("from_date_label")
        self.from_date_label.setMaximumSize(QSize(50, 16777215))
        self.from_date_label.setTextFormat(Qt.TextFormat.PlainText)
        self.from_date_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )
        self.from_date_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.horizontalLayout_2.addWidget(self.from_date_label)

        self.from_date_picker = QDateEdit(self.missions_list_search_filters)
        self.from_date_picker.setObjectName("from_date_picker")
        self.from_date_picker.setWrapping(False)
        self.from_date_picker.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.from_date_picker.setAccelerated(True)
        self.from_date_picker.setCorrectionMode(
            QAbstractSpinBox.CorrectionMode.CorrectToNearestValue,
        )
        self.from_date_picker.setMaximumDate(QDate(2100, 12, 31))
        self.from_date_picker.setMinimumDate(QDate(2000, 9, 14))
        self.from_date_picker.setCurrentSection(
            QDateTimeEdit.Section.YearSection,
        )
        self.from_date_picker.setCalendarPopup(True)
        self.from_date_picker.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.horizontalLayout_2.addWidget(self.from_date_picker)

        self.to_date_label = QLabel(self.missions_list_search_filters)
        self.to_date_label.setObjectName("to_date_label")
        self.to_date_label.setMaximumSize(QSize(50, 16777215))
        self.to_date_label.setTextFormat(Qt.TextFormat.PlainText)
        self.to_date_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.horizontalLayout_2.addWidget(self.to_date_label)

        self.to_date_picker = QDateEdit(self.missions_list_search_filters)
        self.to_date_picker.setObjectName("to_date_picker")
        self.to_date_picker.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.to_date_picker.setAccelerated(True)
        self.to_date_picker.setCorrectionMode(
            QAbstractSpinBox.CorrectionMode.CorrectToNearestValue,
        )
        self.to_date_picker.setMaximumDate(QDate(2100, 12, 31))
        self.to_date_picker.setMinimumDate(QDate(2000, 9, 14))
        self.to_date_picker.setCurrentSection(
            QDateTimeEdit.Section.YearSection,
        )
        self.to_date_picker.setCalendarPopup(True)
        self.to_date_picker.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.horizontalLayout_2.addWidget(self.to_date_picker)

        self.line = QFrame(self.missions_list_search_filters)
        self.line.setObjectName("line")
        self.line.setMinimumSize(QSize(30, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.region_label = QLabel(self.missions_list_search_filters)
        self.region_label.setObjectName("region_label")
        self.region_label.setMaximumSize(QSize(50, 16777215))
        self.region_label.setTextFormat(Qt.TextFormat.PlainText)
        self.region_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.horizontalLayout_2.addWidget(self.region_label)

        self.region_picker = QComboBox(self.missions_list_search_filters)
        self.region_picker.setObjectName("region_picker")
        self.region_picker.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToContents,
        )

        self.horizontalLayout_2.addWidget(self.region_picker)

        self.line_2 = QFrame(self.missions_list_search_filters)
        self.line_2.setObjectName("line_2")
        self.line_2.setMinimumSize(QSize(30, 0))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.load_button = QPushButton(self.missions_list_search_filters)
        self.load_button.setObjectName("load_button")

        self.horizontalLayout_2.addWidget(self.load_button)

        self.verticalLayout_2.addWidget(self.missions_list_search_filters)

        self.analysis_tab_container = QTabWidget(self.scrollAreaWidgetContents)
        self.analysis_tab_container.setObjectName("analysis_tab_container")

        self.verticalLayout_2.addWidget(self.analysis_tab_container)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(region_analyzer_tab)

        self.analysis_tab_container.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(region_analyzer_tab)

    # setupUi

    def retranslateUi(self, region_analyzer_tab):
        region_analyzer_tab.setWindowTitle(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u062a\u062d\u0644\u06cc\u0644 \u0645\u0646\u0637\u0642\u0647",
                None,
            ),
        )
        self.from_date_label.setText(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e:",
                None,
            ),
        )
        self.from_date_picker.setDisplayFormat(
            QCoreApplication.translate("region_analyzer_tab", "dd/MM/yyyy", None),
        )
        self.to_date_label.setText(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e:",
                None,
            ),
        )
        self.to_date_picker.setDisplayFormat(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "dd/MM/yyyy",
                None,
            ),
        )
        self.region_label.setText(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u0645\u0646\u0637\u0642\u0647:",
                None,
            ),
        )
        self.region_picker.setPlaceholderText(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u0639\u0628\u0627\u0633 \u0622\u0628\u0627\u062f",
                None,
            ),
        )
        self.load_button.setText(
            QCoreApplication.translate(
                "region_analyzer_tab",
                "\u062f\u0631\u06cc\u0627\u0641\u062a",
                None,
            ),
        )

    # retranslateUi
