# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201,C0302,C0325
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001, PLR2004
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'analysis_page.ui'
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


class Ui_analysis_page:
    def setupUi(self, analysis_page):
        if not analysis_page.objectName():
            analysis_page.setObjectName("analysis_page")
        analysis_page.resize(700, 1064)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            analysis_page.sizePolicy().hasHeightForWidth(),
        )
        analysis_page.setSizePolicy(sizePolicy)
        analysis_page.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        analysis_page.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.verticalLayout = QVBoxLayout(analysis_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.section_1 = QWidget(analysis_page)
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

        self.verticalLayout.addWidget(self.section_1)

        self.section_2 = QWidget(analysis_page)
        self.section_2.setObjectName("section_2")
        self.horizontalLayout_2 = QHBoxLayout(self.section_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.missions_per_result_groupBox = QGroupBox(self.section_2)
        self.missions_per_result_groupBox.setObjectName(
            "missions_per_result_groupBox",
        )
        self.missions_per_result_groupBox.setMaximumSize(QSize(16777215, 400))
        self.missions_per_result_groupBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.verticalLayout_3 = QVBoxLayout(self.missions_per_result_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.missions_per_result_tableWidget = QTableWidget(
            self.missions_per_result_groupBox,
        )
        if self.missions_per_result_tableWidget.columnCount() < 2:
            self.missions_per_result_tableWidget.setColumnCount(2)
        self.missions_per_result_tableWidget.setObjectName(
            "missions_per_result_tableWidget",
        )
        self.missions_per_result_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.missions_per_result_tableWidget.setProperty(
            "showDropIndicator",
            False,
        )
        self.missions_per_result_tableWidget.setDragDropOverwriteMode(False)
        self.missions_per_result_tableWidget.setAlternatingRowColors(True)
        self.missions_per_result_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.missions_per_result_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.missions_per_result_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_result_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.missions_per_result_tableWidget.setSortingEnabled(True)
        self.missions_per_result_tableWidget.setColumnCount(2)
        self.missions_per_result_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.missions_per_result_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.missions_per_result_tableWidget)

        self.horizontalLayout_2.addWidget(self.missions_per_result_groupBox)

        self.missions_per_hospital_groupBox = QGroupBox(self.section_2)
        self.missions_per_hospital_groupBox.setObjectName(
            "missions_per_hospital_groupBox",
        )
        self.missions_per_hospital_groupBox.setMaximumSize(
            QSize(16777215, 400),
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

        self.verticalLayout.addWidget(self.section_2)

        self.section_3 = QWidget(analysis_page)
        self.section_3.setObjectName("section_3")
        self.horizontalLayout_3 = QHBoxLayout(self.section_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.total_iranian_patient_label = QLabel(self.section_3)
        self.total_iranian_patient_label.setObjectName(
            "total_iranian_patient_label",
        )
        self.total_iranian_patient_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_3.addWidget(self.total_iranian_patient_label)

        self.total_iranian_patient_field = QLineEdit(self.section_3)
        self.total_iranian_patient_field.setObjectName(
            "total_iranian_patient_field",
        )
        self.total_iranian_patient_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_iranian_patient_field.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.total_iranian_patient_field)

        self.total_foreign_patient_label = QLabel(self.section_3)
        self.total_foreign_patient_label.setObjectName(
            "total_foreign_patient_label",
        )
        self.total_foreign_patient_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_3.addWidget(self.total_foreign_patient_label)

        self.total_foreign_patient_field = QLineEdit(self.section_3)
        self.total_foreign_patient_field.setObjectName(
            "total_foreign_patient_field",
        )
        self.total_foreign_patient_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_foreign_patient_field.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.total_foreign_patient_field)

        self.verticalLayout.addWidget(self.section_3)

        self.section_4 = QWidget(analysis_page)
        self.section_4.setObjectName("section_4")
        self.horizontalLayout_4 = QHBoxLayout(self.section_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.total_male_patients_label = QLabel(self.section_4)
        self.total_male_patients_label.setObjectName(
            "total_male_patients_label",
        )
        self.total_male_patients_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.total_male_patients_label)

        self.total_male_patients_field = QLineEdit(self.section_4)
        self.total_male_patients_field.setObjectName(
            "total_male_patients_field",
        )
        self.total_male_patients_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_male_patients_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.total_male_patients_field)

        self.total_female_patients_label = QLabel(self.section_4)
        self.total_female_patients_label.setObjectName(
            "total_female_patients_label",
        )
        self.total_female_patients_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.total_female_patients_label)

        self.total_female_patients_field = QLineEdit(self.section_4)
        self.total_female_patients_field.setObjectName(
            "total_female_patients_field",
        )
        self.total_female_patients_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_female_patients_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.total_female_patients_field)

        self.total_unknown_gender_label = QLabel(self.section_4)
        self.total_unknown_gender_label.setObjectName(
            "total_unknown_gender_label",
        )
        self.total_unknown_gender_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.total_unknown_gender_label)

        self.total_unknown_gender_field = QLineEdit(self.section_4)
        self.total_unknown_gender_field.setObjectName(
            "total_unknown_gender_field",
        )
        self.total_unknown_gender_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.total_unknown_gender_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.total_unknown_gender_field)

        self.verticalLayout.addWidget(self.section_4)

        self.section_5 = QWidget(analysis_page)
        self.section_5.setObjectName("section_5")
        self.horizontalLayout_5 = QHBoxLayout(self.section_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.consumables_list_groupBox = QGroupBox(self.section_5)
        self.consumables_list_groupBox.setObjectName(
            "consumables_list_groupBox",
        )
        self.consumables_list_groupBox.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.horizontalLayout_6 = QHBoxLayout(self.consumables_list_groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.consumables_list_tableWidget = QTableWidget(
            self.consumables_list_groupBox,
        )
        if self.consumables_list_tableWidget.columnCount() < 2:
            self.consumables_list_tableWidget.setColumnCount(2)
        self.consumables_list_tableWidget.setObjectName(
            "consumables_list_tableWidget",
        )
        self.consumables_list_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.consumables_list_tableWidget.setProperty(
            "showDropIndicator",
            False,
        )
        self.consumables_list_tableWidget.setDragDropOverwriteMode(False)
        self.consumables_list_tableWidget.setAlternatingRowColors(True)
        self.consumables_list_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.consumables_list_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.consumables_list_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.consumables_list_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.consumables_list_tableWidget.setSortingEnabled(True)
        self.consumables_list_tableWidget.setColumnCount(2)
        self.consumables_list_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.consumables_list_tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_6.addWidget(self.consumables_list_tableWidget)

        self.horizontalLayout_5.addWidget(self.consumables_list_groupBox)

        self.drugs_list_groupBox = QGroupBox(self.section_5)
        self.drugs_list_groupBox.setObjectName("drugs_list_groupBox")
        self.drugs_list_groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_7 = QHBoxLayout(self.drugs_list_groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.drugs_list_tableWidget = QTableWidget(self.drugs_list_groupBox)
        if self.drugs_list_tableWidget.columnCount() < 2:
            self.drugs_list_tableWidget.setColumnCount(2)
        self.drugs_list_tableWidget.setObjectName("drugs_list_tableWidget")
        self.drugs_list_tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.drugs_list_tableWidget.setProperty("showDropIndicator", False)
        self.drugs_list_tableWidget.setDragDropOverwriteMode(False)
        self.drugs_list_tableWidget.setAlternatingRowColors(True)
        self.drugs_list_tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )
        self.drugs_list_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )
        self.drugs_list_tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.drugs_list_tableWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel,
        )
        self.drugs_list_tableWidget.setSortingEnabled(True)
        self.drugs_list_tableWidget.setRowCount(0)
        self.drugs_list_tableWidget.setColumnCount(2)
        self.drugs_list_tableWidget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.drugs_list_tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_7.addWidget(self.drugs_list_tableWidget)

        self.horizontalLayout_5.addWidget(self.drugs_list_groupBox)

        self.verticalLayout.addWidget(self.section_5)

        self.retranslateUi(analysis_page)

        QMetaObject.connectSlotsByName(analysis_page)

    # setupUi

    def retranslateUi(self, analysis_page):
        analysis_page.setWindowTitle(
            QCoreApplication.translate(
                "analysis_page",
                "\u0635\u0641\u062d\u0647 \u062a\u062d\u0644\u06cc\u0644",
                None,
            ),
        )
        self.missions_count_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.patients_count_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u062f\u062f\u062c\u0648:",
                None,
            ),
        )
        self.missions_per_result_groupBox.setTitle(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0628\u0647 \u062a\u0641\u06a9\u06cc\u06a9 \u0646\u062a\u06cc\u062c\u0647",
                None,
            ),
        )
        self.missions_per_hospital_groupBox.setTitle(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u0627\u0645\u0648\u0631\u06cc\u062a \u0628\u0647 \u062a\u0641\u06a9\u06cc\u06a9 \u0628\u06cc\u0645\u0627\u0631\u0633\u062a\u0627\u0646",
                None,
            ),
        )
        self.total_iranian_patient_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u062f\u062f\u062c\u0648 \u0627\u06cc\u0631\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.total_foreign_patient_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u062f\u062f\u062c\u0648 \u063a\u06cc\u0631\u0627\u06cc\u0631\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.total_male_patients_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062a\u0639\u062f\u0627\u062f \u0645\u062f\u062f\u062c\u0648 \u0622\u0642\u0627:",
                None,
            ),
        )
        self.total_female_patients_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062e\u0627\u0646\u0645:",
                None,
            ),
        )
        self.total_unknown_gender_label.setText(
            QCoreApplication.translate(
                "analysis_page",
                "\u062c\u0646\u0633\u06cc\u062a \u0646\u0627\u0645\u0634\u062e\u0635:",
                None,
            ),
        )
        self.consumables_list_groupBox.setTitle(
            QCoreApplication.translate(
                "analysis_page",
                "\u0644\u06cc\u0633\u062a \u0627\u0642\u0644\u0627\u0645 \u0645\u0635\u0631\u0641\u06cc",
                None,
            ),
        )
        self.drugs_list_groupBox.setTitle(
            QCoreApplication.translate(
                "analysis_page",
                "\u0644\u06cc\u0633\u062a \u062f\u0627\u0631\u0648\u0647\u0627\u06cc \u0645\u0635\u0631\u0641\u06cc",
                None,
            ),
        )

    # retranslateUi
