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
    QApplication,
    QHeaderView,
    QMainWindow,
    QMenuBar,
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
        main_window.setMinimumSize(QSize(500, 500))
        main_window.setAcceptDrops(False)
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
                "Main Menu",
                None,
            ),
        )
        # if QT_CONFIG(statustip)
        self.missions_list_tab.setStatusTip(
            QCoreApplication.translate(
                "main_window",
                "Missions list tab",
                None,
            ),
        )
        # endif // QT_CONFIG(statustip)
        self.tab_widget.setTabText(
            self.tab_widget.indexOf(
                self.missions_list_tab,
            ),
            QCoreApplication.translate("main_window", "Missions List", None),
        )
        self.tab_widget.setTabText(
            self.tab_widget.indexOf(
                self.tab_2,
            ),
            QCoreApplication.translate("main_window", "Tab 2", None),
        )

    # retranslateUi
