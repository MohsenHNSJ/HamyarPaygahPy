# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_menu.ui'
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
    QAbstractItemView,
    QAbstractScrollArea,
    QAbstractSpinBox,
    QApplication,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_main_window:
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.setWindowModality(Qt.WindowModality.NonModal)
        main_window.resize(800, 600)
        main_window.setMinimumSize(QSize(800, 600))
        main_window.setAcceptDrops(False)
        main_window.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        main_window.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout = QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("vertical_layout")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.missions_list_tab = QWidget()
        self.missions_list_tab.setObjectName("missions_list_tab")
        self.verticalLayout_2 = QVBoxLayout(self.missions_list_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.missions_list_search_filters = QWidget(self.missions_list_tab)
        self.missions_list_search_filters.setObjectName(
            "missions_list_search_filters",
        )
        self.horizontalLayout = QHBoxLayout(self.missions_list_search_filters)
        self.horizontalLayout.setObjectName("horizontalLayout")
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

        self.horizontalLayout.addWidget(self.from_date_label)

        self.from_date_picker = QDateEdit(self.missions_list_search_filters)
        self.from_date_picker.setObjectName("from_date_picker")
        self.from_date_picker.setMaximumSize(QSize(110, 16777215))
        self.from_date_picker.setWrapping(False)
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

        self.horizontalLayout.addWidget(self.from_date_picker)

        self.to_date_label = QLabel(self.missions_list_search_filters)
        self.to_date_label.setObjectName("to_date_label")
        self.to_date_label.setMaximumSize(QSize(50, 16777215))
        self.to_date_label.setTextFormat(Qt.TextFormat.PlainText)
        self.to_date_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.horizontalLayout.addWidget(self.to_date_label)

        self.to_date_picker = QDateEdit(self.missions_list_search_filters)
        self.to_date_picker.setObjectName("to_date_picker")
        self.to_date_picker.setMaximumSize(QSize(110, 16777215))
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

        self.horizontalLayout.addWidget(self.to_date_picker)

        self.line = QFrame(self.missions_list_search_filters)
        self.line.setObjectName("line")
        self.line.setMinimumSize(QSize(30, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.region_label = QLabel(self.missions_list_search_filters)
        self.region_label.setObjectName("region_label")
        self.region_label.setMaximumSize(QSize(50, 16777215))
        self.region_label.setTextFormat(Qt.TextFormat.PlainText)
        self.region_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.horizontalLayout.addWidget(self.region_label)

        self.region_picker = QComboBox(self.missions_list_search_filters)
        self.region_picker.setObjectName("region_picker")
        self.region_picker.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.region_picker)

        self.line_2 = QFrame(self.missions_list_search_filters)
        self.line_2.setObjectName("line_2")
        self.line_2.setMinimumSize(QSize(30, 0))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.load_button = QPushButton(self.missions_list_search_filters)
        self.load_button.setObjectName("load_button")
        self.load_button.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.load_button)

        self.verticalLayout_2.addWidget(self.missions_list_search_filters)

        self.missions_list_table = QTableView(self.missions_list_tab)
        self.missions_list_table.setObjectName("missions_list_table")
        self.missions_list_table.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents,
        )
        self.missions_list_table.setProperty("showDropIndicator", False)
        self.missions_list_table.setDragDropOverwriteMode(False)
        self.missions_list_table.setAlternatingRowColors(True)
        self.missions_list_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.missions_list_table.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_list_table.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_list_table.setSortingEnabled(True)
        self.missions_list_table.horizontalHeader().setMinimumSectionSize(80)

        self.verticalLayout_2.addWidget(self.missions_list_table)

        self.tab_widget.addTab(self.missions_list_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_widget.addTab(self.tab_2, "")

        self.vertical_layout.addWidget(self.tab_widget)

        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName("menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 800, 19))
        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.retranslateUi(main_window)

        self.tab_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(
            QCoreApplication.translate(
                "main_window",
                "\u0647\u0645\u06cc\u0627\u0631 \u067e\u0627\u06cc\u06af\u0627\u0647",
                None,
            ),
        )
        self.from_date_label.setText(
            QCoreApplication.translate(
                "main_window",
                "\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e:",
                None,
            ),
        )
        self.from_date_picker.setDisplayFormat(
            QCoreApplication.translate("main_window", "dd/MM/yyyy", None),
        )
        self.to_date_label.setText(
            QCoreApplication.translate(
                "main_window",
                "\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e:",
                None,
            ),
        )
        self.to_date_picker.setDisplayFormat(
            QCoreApplication.translate("main_window", "dd/MM/yyyy", None),
        )
        self.region_label.setText(
            QCoreApplication.translate(
                "main_window",
                "\u0645\u0646\u0637\u0642\u0647:",
                None,
            ),
        )
        self.region_picker.setPlaceholderText(
            QCoreApplication.translate(
                "main_window",
                "\u0639\u0628\u0627\u0633 \u0622\u0628\u0627\u062f",
                None,
            ),
        )
        self.load_button.setText(
            QCoreApplication.translate(
                "main_window",
                "\u062f\u0631\u06cc\u0627\u0641\u062a",
                None,
            ),
        )
        self.tab_widget.setTabText(
            self.tab_widget.indexOf(self.missions_list_tab),
            QCoreApplication.translate(
                "main_window",
                "\u0644\u06cc\u0633\u062a \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0647\u0627",
                None,
            ),
        )
        self.tab_widget.setTabText(
            self.tab_widget.indexOf(
                self.tab_2,
            ),
            QCoreApplication.translate("main_window", "Tab 2", None),
        )

    # retranslateUi
