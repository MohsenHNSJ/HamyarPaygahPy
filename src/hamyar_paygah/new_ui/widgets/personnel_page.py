# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201,C0302,C0325
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001, PLR2004, C901, PLR0912
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'personnel_page.ui'
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
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_personnel_page:
    def setupUi(self, personnel_page):
        if not personnel_page.objectName():
            personnel_page.setObjectName("personnel_page")
        personnel_page.resize(1099, 757)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            personnel_page.sizePolicy().hasHeightForWidth(),
        )
        personnel_page.setSizePolicy(sizePolicy)
        personnel_page.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        personnel_page.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.verticalLayout = QVBoxLayout(personnel_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.section_1 = QWidget(personnel_page)
        self.section_1.setObjectName("section_1")
        self.horizontalLayout = QHBoxLayout(self.section_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.missions_count_label = QLabel(self.section_1)
        self.missions_count_label.setObjectName("missions_count_label")
        self.missions_count_label.setTextFormat(Qt.TextFormat.PlainText)
        self.missions_count_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )

        self.horizontalLayout.addWidget(self.missions_count_label)

        self.missions_count_field = QLineEdit(self.section_1)
        self.missions_count_field.setObjectName("missions_count_field")
        self.missions_count_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.missions_count_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.missions_count_field)

        self.patients_count_label = QLabel(self.section_1)
        self.patients_count_label.setObjectName("patients_count_label")
        self.patients_count_label.setTextFormat(Qt.TextFormat.PlainText)
        self.patients_count_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )

        self.horizontalLayout.addWidget(self.patients_count_label)

        self.patients_count_field = QLineEdit(self.section_1)
        self.patients_count_field.setObjectName("patients_count_field")
        self.patients_count_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.patients_count_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.patients_count_field)

        self.total_vehicle_accident_label = QLabel(self.section_1)
        self.total_vehicle_accident_label.setObjectName(
            "total_vehicle_accident_label",
        )
        self.total_vehicle_accident_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout.addWidget(self.total_vehicle_accident_label)

        self.total_vehicle_accident_field = QLineEdit(self.section_1)
        self.total_vehicle_accident_field.setObjectName(
            "total_vehicle_accident_field",
        )
        self.total_vehicle_accident_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_vehicle_accident_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.total_vehicle_accident_field)

        self.missions_over_60km_label = QLabel(self.section_1)
        self.missions_over_60km_label.setObjectName(
            "missions_over_60km_label",
        )
        self.missions_over_60km_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout.addWidget(self.missions_over_60km_label)

        self.missions_over_60km_field = QLineEdit(self.section_1)
        self.missions_over_60km_field.setObjectName(
            "missions_over_60km_field",
        )
        self.missions_over_60km_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.missions_over_60km_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.missions_over_60km_field)

        self.refueling_count_label = QLabel(self.section_1)
        self.refueling_count_label.setObjectName("refueling_count_label")
        self.refueling_count_label.setTextFormat(Qt.TextFormat.PlainText)
        self.refueling_count_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )

        self.horizontalLayout.addWidget(self.refueling_count_label)

        self.refueling_count_field = QLineEdit(self.section_1)
        self.refueling_count_field.setObjectName("refueling_count_field")
        self.refueling_count_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.refueling_count_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.refueling_count_field)

        self.patient_extraction_count_label = QLabel(self.section_1)
        self.patient_extraction_count_label.setObjectName(
            "patient_extraction_count_label",
        )
        self.patient_extraction_count_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )
        self.patient_extraction_count_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )

        self.horizontalLayout.addWidget(self.patient_extraction_count_label)

        self.patient_extraction_count_field = QLineEdit(self.section_1)
        self.patient_extraction_count_field.setObjectName(
            "patient_extraction_count_field",
        )
        self.patient_extraction_count_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.patient_extraction_count_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.patient_extraction_count_field)

        self.overall_distance_driven_label = QLabel(self.section_1)
        self.overall_distance_driven_label.setObjectName(
            "overall_distance_driven_label",
        )
        self.overall_distance_driven_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout.addWidget(self.overall_distance_driven_label)

        self.overall_distance_driven_field = QLineEdit(self.section_1)
        self.overall_distance_driven_field.setObjectName(
            "overall_distance_driven_field",
        )
        self.overall_distance_driven_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.overall_distance_driven_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.overall_distance_driven_field)

        self.verticalLayout.addWidget(self.section_1)

        self.average_times_groupBox = QGroupBox(personnel_page)
        self.average_times_groupBox.setObjectName("average_times_groupBox")
        self.average_times_groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.average_times_groupBox.setFlat(False)
        self.gridLayout = QGridLayout(self.average_times_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.average_emergency_location_presence_time_field = QLineEdit(
            self.average_times_groupBox,
        )
        self.average_emergency_location_presence_time_field.setObjectName(
            "average_emergency_location_presence_time_field",
        )
        self.average_emergency_location_presence_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.average_emergency_location_presence_time_field.setReadOnly(True)

        self.gridLayout.addWidget(
            self.average_emergency_location_presence_time_field,
            0,
            5,
            1,
            1,
        )

        self.average_reaction_time_field = QLineEdit(
            self.average_times_groupBox,
        )
        self.average_reaction_time_field.setObjectName(
            "average_reaction_time_field",
        )
        self.average_reaction_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.average_reaction_time_field.setReadOnly(True)

        self.gridLayout.addWidget(self.average_reaction_time_field, 0, 1, 1, 1)

        self.average_deliver_to_hospital_time_label = QLabel(
            self.average_times_groupBox,
        )
        self.average_deliver_to_hospital_time_label.setObjectName(
            "average_deliver_to_hospital_time_label",
        )
        self.average_deliver_to_hospital_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.gridLayout.addWidget(
            self.average_deliver_to_hospital_time_label,
            0,
            6,
            1,
            1,
        )

        self.average_arriving_time_field = QLineEdit(
            self.average_times_groupBox,
        )
        self.average_arriving_time_field.setObjectName(
            "average_arriving_time_field",
        )
        self.average_arriving_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.average_arriving_time_field.setReadOnly(True)

        self.gridLayout.addWidget(self.average_arriving_time_field, 0, 3, 1, 1)

        self.average_arriving_time_label = QLabel(self.average_times_groupBox)
        self.average_arriving_time_label.setObjectName(
            "average_arriving_time_label",
        )
        self.average_arriving_time_label.setTextFormat(Qt.TextFormat.PlainText)
        self.average_arriving_time_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter,
        )

        self.gridLayout.addWidget(self.average_arriving_time_label, 0, 2, 1, 1)

        self.average_mission_end_time_label = QLabel(
            self.average_times_groupBox,
        )
        self.average_mission_end_time_label.setObjectName(
            "average_mission_end_time_label",
        )
        self.average_mission_end_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.gridLayout.addWidget(
            self.average_mission_end_time_label,
            0,
            8,
            1,
            1,
        )

        self.average_reaction_time_label = QLabel(self.average_times_groupBox)
        self.average_reaction_time_label.setObjectName(
            "average_reaction_time_label",
        )
        self.average_reaction_time_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout.addWidget(self.average_reaction_time_label, 0, 0, 1, 1)

        self.average_deliver_to_hospital_field = QLineEdit(
            self.average_times_groupBox,
        )
        self.average_deliver_to_hospital_field.setObjectName(
            "average_deliver_to_hospital_field",
        )
        self.average_deliver_to_hospital_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.average_deliver_to_hospital_field.setReadOnly(True)

        self.gridLayout.addWidget(
            self.average_deliver_to_hospital_field,
            0,
            7,
            1,
            1,
        )

        self.average_emergency_location_presence_time_label = QLabel(
            self.average_times_groupBox,
        )
        self.average_emergency_location_presence_time_label.setObjectName(
            "average_emergency_location_presence_time_label",
        )
        self.average_emergency_location_presence_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.gridLayout.addWidget(
            self.average_emergency_location_presence_time_label,
            0,
            4,
            1,
            1,
        )

        self.average_mission_end_time_field = QLineEdit(
            self.average_times_groupBox,
        )
        self.average_mission_end_time_field.setObjectName(
            "average_mission_end_time_field",
        )
        self.average_mission_end_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.average_mission_end_time_field.setReadOnly(True)

        self.gridLayout.addWidget(
            self.average_mission_end_time_field,
            0,
            9,
            1,
            1,
        )

        self.verticalLayout.addWidget(self.average_times_groupBox)

        self.section_2 = QWidget(personnel_page)
        self.section_2.setObjectName("section_2")
        self.horizontalLayout_3 = QHBoxLayout(self.section_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.verticalLayout.addWidget(self.section_2)

        self.section_3 = QWidget(personnel_page)
        self.section_3.setObjectName("section_3")
        self.section_3.setMinimumSize(QSize(0, 600))
        self.horizontalLayout_2 = QHBoxLayout(self.section_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.missions_per_code_groupBox = QGroupBox(self.section_3)
        self.missions_per_code_groupBox.setObjectName(
            "missions_per_code_groupBox",
        )
        self.missions_per_code_groupBox.setMinimumSize(QSize(200, 0))
        self.missions_per_code_groupBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.verticalLayout_3 = QVBoxLayout(self.missions_per_code_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.missions_per_code_tableWidget = QTableWidget(
            self.missions_per_code_groupBox,
        )
        if self.missions_per_code_tableWidget.columnCount() < 2:
            self.missions_per_code_tableWidget.setColumnCount(2)
        self.missions_per_code_tableWidget.setObjectName(
            "missions_per_code_tableWidget",
        )
        self.missions_per_code_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.missions_per_code_tableWidget.setProperty(
            "showDropIndicator",
            False,
        )
        self.missions_per_code_tableWidget.setDragDropOverwriteMode(False)
        self.missions_per_code_tableWidget.setAlternatingRowColors(True)
        self.missions_per_code_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.missions_per_code_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.missions_per_code_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_code_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_code_tableWidget.setSortingEnabled(True)
        self.missions_per_code_tableWidget.setColumnCount(2)
        self.missions_per_code_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.missions_per_code_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.missions_per_code_tableWidget)

        self.horizontalLayout_2.addWidget(self.missions_per_code_groupBox)

        self.missions_per_hospital_groupBox = QGroupBox(self.section_3)
        self.missions_per_hospital_groupBox.setObjectName(
            "missions_per_hospital_groupBox",
        )
        self.missions_per_hospital_groupBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.verticalLayout_2 = QVBoxLayout(
            self.missions_per_hospital_groupBox,
        )
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.missions_per_hospital_tableWidget = QTableWidget(
            self.missions_per_hospital_groupBox,
        )
        if self.missions_per_hospital_tableWidget.columnCount() < 2:
            self.missions_per_hospital_tableWidget.setColumnCount(2)
        self.missions_per_hospital_tableWidget.setObjectName(
            "missions_per_hospital_tableWidget",
        )
        self.missions_per_hospital_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.missions_per_hospital_tableWidget.setProperty(
            "showDropIndicator",
            False,
        )
        self.missions_per_hospital_tableWidget.setDragDropOverwriteMode(False)
        self.missions_per_hospital_tableWidget.setAlternatingRowColors(True)
        self.missions_per_hospital_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.missions_per_hospital_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.missions_per_hospital_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_hospital_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_hospital_tableWidget.setSortingEnabled(True)
        self.missions_per_hospital_tableWidget.setColumnCount(2)
        self.missions_per_hospital_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.missions_per_hospital_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.missions_per_hospital_tableWidget)

        self.horizontalLayout_2.addWidget(self.missions_per_hospital_groupBox)

        self.missions_per_chief_complain_groupBox = QGroupBox(self.section_3)
        self.missions_per_chief_complain_groupBox.setObjectName(
            "missions_per_chief_complain_groupBox",
        )
        self.missions_per_chief_complain_groupBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.horizontalLayout_18 = QHBoxLayout(
            self.missions_per_chief_complain_groupBox,
        )
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.missions_per_chief_complain_tableWidget = QTableWidget(
            self.missions_per_chief_complain_groupBox,
        )
        if self.missions_per_chief_complain_tableWidget.columnCount() < 2:
            self.missions_per_chief_complain_tableWidget.setColumnCount(2)
        self.missions_per_chief_complain_tableWidget.setObjectName(
            "missions_per_chief_complain_tableWidget",
        )
        self.missions_per_chief_complain_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.missions_per_chief_complain_tableWidget.setProperty(
            "showDropIndicator",
            False,
        )
        self.missions_per_chief_complain_tableWidget.setDragDropOverwriteMode(
            False,
        )
        self.missions_per_chief_complain_tableWidget.setAlternatingRowColors(
            True,
        )
        self.missions_per_chief_complain_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.missions_per_chief_complain_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.missions_per_chief_complain_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_chief_complain_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_chief_complain_tableWidget.setSortingEnabled(True)
        self.missions_per_chief_complain_tableWidget.setColumnCount(2)
        self.missions_per_chief_complain_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.missions_per_chief_complain_tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_18.addWidget(
            self.missions_per_chief_complain_tableWidget,
        )

        self.horizontalLayout_2.addWidget(
            self.missions_per_chief_complain_groupBox,
        )

        self.verticalLayout.addWidget(self.section_3)

        self.retranslateUi(personnel_page)

        QMetaObject.connectSlotsByName(personnel_page)

    # setupUi

    def retranslateUi(self, personnel_page):
        personnel_page.setWindowTitle(
            QCoreApplication.translate(
                "personnel_page",
                "\u0635\u0641\u062d\u0647 \u062a\u062d\u0644\u06cc\u0644",
                None,
            ),
        )
        self.missions_count_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.missions_count_field.setText("")
        self.patients_count_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u062f\u062f\u062c\u0648:",
                None,
            ),
        )
        self.total_vehicle_accident_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u062a\u0635\u0627\u062f\u0641:",
                None,
            ),
        )
        self.missions_over_60km_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0628\u0627\u0644\u0627\u06cc 60 \u06a9\u06cc\u0644\u0648\u0645\u062a\u0631:",
                None,
            ),
        )
        self.refueling_count_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0633\u0648\u062e\u062a\u06af\u06cc\u0631\u06cc:",
                None,
            ),
        )
        self.patient_extraction_count_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u062e\u0627\u0631\u062c \u0633\u0627\u0632\u06cc \u0645\u0635\u062f\u0648\u0645:",
                None,
            ),
        )
        self.overall_distance_driven_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u06a9\u0644 \u0645\u0633\u0627\u0641\u062a \u067e\u06cc\u0645\u0648\u062f\u0647:",
                None,
            ),
        )
        self.average_times_groupBox.setTitle(
            QCoreApplication.translate(
                "personnel_page",
                "\u0645\u06cc\u0627\u0646\u06af\u06cc\u0646 \u0632\u0645\u0627\u0646",
                None,
            ),
        )
        self.average_reaction_time_field.setText("")
        self.average_deliver_to_hospital_time_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u062d\u0648\u06cc\u0644 \u0628\u0647 \u0628\u06cc\u0645\u0627\u0631\u0633\u062a\u0627\u0646:",
                None,
            ),
        )
        self.average_arriving_time_field.setText("")
        self.average_arriving_time_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u0631\u0633\u06cc\u062f\u0646 \u0628\u0631 \u0628\u0627\u0644\u06cc\u0646 \u0628\u06cc\u0645\u0627\u0631:",
                None,
            ),
        )
        self.average_mission_end_time_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u067e\u0627\u06cc\u0627\u0646 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.average_reaction_time_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062d\u0631\u06a9\u062a \u0627\u0632 \u067e\u0627\u06cc\u06af\u0627\u0647:",
                None,
            ),
        )
        self.average_emergency_location_presence_time_label.setText(
            QCoreApplication.translate(
                "personnel_page",
                "\u062d\u0636\u0648\u0631 \u062f\u0631 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.missions_per_code_groupBox.setTitle(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u062f\u0631 \u0647\u0631 \u06a9\u062f",
                None,
            ),
        )
        self.missions_per_hospital_groupBox.setTitle(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0628\u0647 \u062a\u0641\u06a9\u06cc\u06a9 \u0628\u06cc\u0645\u0627\u0631\u0633\u062a\u0627\u0646",
                None,
            ),
        )
        self.missions_per_chief_complain_groupBox.setTitle(
            QCoreApplication.translate(
                "personnel_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0628\u0647 \u062a\u0641\u06a9\u06cc\u06a9 \u0634\u06a9\u0627\u06cc\u062a \u0627\u0635\u0644\u06cc",
                None,
            ),
        )

    # retranslateUi
