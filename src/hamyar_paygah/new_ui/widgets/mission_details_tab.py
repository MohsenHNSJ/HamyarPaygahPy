# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201,C0302,C0325
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001, PLR2004
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
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_mission_details_tab:
    def setupUi(self, mission_details_tab):
        if not mission_details_tab.objectName():
            mission_details_tab.setObjectName("mission_details_tab")
        mission_details_tab.resize(750, 650)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mission_details_tab.sizePolicy().hasHeightForWidth(),
        )
        mission_details_tab.setSizePolicy(sizePolicy)
        mission_details_tab.setMinimumSize(QSize(750, 650))
        mission_details_tab.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        mission_details_tab.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.verticalLayout_2 = QVBoxLayout(mission_details_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_parameters = QWidget(mission_details_tab)
        self.search_parameters.setObjectName("search_parameters")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum,
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.search_parameters.sizePolicy().hasHeightForWidth(),
        )
        self.search_parameters.setSizePolicy(sizePolicy1)
        self.search_parameters.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.search_parameters)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mission_id_label = QLabel(self.search_parameters)
        self.mission_id_label.setObjectName("mission_id_label")
        self.mission_id_label.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout.addWidget(self.mission_id_label)

        self.mission_id_line_edit = QLineEdit(self.search_parameters)
        self.mission_id_line_edit.setObjectName("mission_id_line_edit")
        self.mission_id_line_edit.setMaximumSize(QSize(16777215, 22))
        self.mission_id_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mission_id_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.mission_id_line_edit)

        self.patient_id_label = QLabel(self.search_parameters)
        self.patient_id_label.setObjectName("patient_id_label")
        self.patient_id_label.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.patient_id_label)

        self.patient_id_line_edit = QLineEdit(self.search_parameters)
        self.patient_id_line_edit.setObjectName("patient_id_line_edit")
        self.patient_id_line_edit.setMaximumSize(QSize(16777215, 22))
        self.patient_id_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.patient_id_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.patient_id_line_edit)

        self.search_button = QPushButton(self.search_parameters)
        self.search_button.setObjectName("search_button")
        self.search_button.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.search_button)

        self.verticalLayout_2.addWidget(self.search_parameters)

        self.mission_data_tab_widget = QTabWidget(mission_details_tab)
        self.mission_data_tab_widget.setObjectName("mission_data_tab_widget")
        self.mission_data_tab_widget.setDocumentMode(False)
        self.information_tab = QWidget()
        self.information_tab.setObjectName("information_tab")
        self.verticalLayout = QVBoxLayout(self.information_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pre_information_section_1 = QWidget(self.information_tab)
        self.pre_information_section_1.setObjectName(
            "pre_information_section_1",
        )
        self.pre_information_section_1.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.pre_information_section_1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.last_update_label = QLabel(self.pre_information_section_1)
        self.last_update_label.setObjectName("last_update_label")
        self.last_update_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_5.addWidget(self.last_update_label)

        self.last_update_field = QLineEdit(self.pre_information_section_1)
        self.last_update_field.setObjectName("last_update_field")
        self.last_update_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_update_field.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.last_update_field)

        self.base_station_label = QLabel(self.pre_information_section_1)
        self.base_station_label.setObjectName("base_station_label")
        self.base_station_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_5.addWidget(self.base_station_label)

        self.base_station_field = QLineEdit(self.pre_information_section_1)
        self.base_station_field.setObjectName("base_station_field")
        self.base_station_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.base_station_field.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.base_station_field)

        self.verticalLayout.addWidget(self.pre_information_section_1)

        self.pre_information_section_2 = QWidget(self.information_tab)
        self.pre_information_section_2.setObjectName(
            "pre_information_section_2",
        )
        self.pre_information_section_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.pre_information_section_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.document_serial_number_label = QLabel(
            self.pre_information_section_2,
        )
        self.document_serial_number_label.setObjectName(
            "document_serial_number_label",
        )
        self.document_serial_number_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_4.addWidget(self.document_serial_number_label)

        self.document_serial_number_field = QLineEdit(
            self.pre_information_section_2,
        )
        self.document_serial_number_field.setObjectName(
            "document_serial_number_field",
        )
        self.document_serial_number_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.document_serial_number_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.document_serial_number_field)

        self.caller_number_label = QLabel(self.pre_information_section_2)
        self.caller_number_label.setObjectName("caller_number_label")
        self.caller_number_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.caller_number_label)

        self.caller_number_field = QLineEdit(self.pre_information_section_2)
        self.caller_number_field.setObjectName("caller_number_field")
        self.caller_number_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caller_number_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.caller_number_field)

        self.backup_number_label = QLabel(self.pre_information_section_2)
        self.backup_number_label.setObjectName("backup_number_label")
        self.backup_number_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.backup_number_label)

        self.backup_number_field = QLineEdit(self.pre_information_section_2)
        self.backup_number_field.setObjectName("backup_number_field")
        self.backup_number_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.backup_number_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.backup_number_field)

        self.ambulance_code_label = QLabel(self.pre_information_section_2)
        self.ambulance_code_label.setObjectName("ambulance_code_label")
        self.ambulance_code_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_4.addWidget(self.ambulance_code_label)

        self.ambulance_code_field = QLineEdit(self.pre_information_section_2)
        self.ambulance_code_field.setObjectName("ambulance_code_field")
        self.ambulance_code_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ambulance_code_field.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.ambulance_code_field)

        self.verticalLayout.addWidget(self.pre_information_section_2)

        self.information_section_1 = QWidget(self.information_tab)
        self.information_section_1.setObjectName("information_section_1")
        self.information_section_1.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.information_section_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.patient_name_label = QLabel(self.information_section_1)
        self.patient_name_label.setObjectName("patient_name_label")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred,
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.patient_name_label.sizePolicy().hasHeightForWidth(),
        )
        self.patient_name_label.setSizePolicy(sizePolicy2)
        self.patient_name_label.setMaximumSize(QSize(55, 30))
        self.patient_name_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_3.addWidget(self.patient_name_label)

        self.patient_name_field = QLineEdit(self.information_section_1)
        self.patient_name_field.setObjectName("patient_name_field")
        self.patient_name_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.patient_name_field.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.patient_name_field)

        self.age_label = QLabel(self.information_section_1)
        self.age_label.setObjectName("age_label")
        self.age_label.setMaximumSize(QSize(25, 30))
        self.age_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_3.addWidget(self.age_label)

        self.age_field = QLineEdit(self.information_section_1)
        self.age_field.setObjectName("age_field")
        self.age_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.age_field.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.age_field)

        self.nationality_label = QLabel(self.information_section_1)
        self.nationality_label.setObjectName("nationality_label")
        self.nationality_label.setMaximumSize(QSize(30, 30))
        self.nationality_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_3.addWidget(self.nationality_label)

        self.iranian_nationality_checkBox = QCheckBox(
            self.information_section_1,
        )
        self.iranian_nationality_checkBox.setObjectName(
            "iranian_nationality_checkBox",
        )
        self.iranian_nationality_checkBox.setEnabled(True)
        self.iranian_nationality_checkBox.setMaximumSize(QSize(50, 22))
        self.iranian_nationality_checkBox.setMouseTracking(False)
        self.iranian_nationality_checkBox.setFocusPolicy(
            Qt.FocusPolicy.NoFocus,
        )
        self.iranian_nationality_checkBox.setInputMethodHints(
            Qt.InputMethodHint.ImhNone,
        )
        self.iranian_nationality_checkBox.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.iranian_nationality_checkBox)

        self.foreign_nationality_checkBox = QCheckBox(
            self.information_section_1,
        )
        self.foreign_nationality_checkBox.setObjectName(
            "foreign_nationality_checkBox",
        )
        self.foreign_nationality_checkBox.setEnabled(True)
        self.foreign_nationality_checkBox.setMaximumSize(QSize(75, 20))
        self.foreign_nationality_checkBox.setMouseTracking(False)
        self.foreign_nationality_checkBox.setFocusPolicy(
            Qt.FocusPolicy.NoFocus,
        )

        self.horizontalLayout_3.addWidget(self.foreign_nationality_checkBox)

        self.verticalLayout.addWidget(self.information_section_1)

        self.information_section_2 = QWidget(self.information_tab)
        self.information_section_2.setObjectName("information_section_2")
        self.information_section_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.information_section_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gender_label = QLabel(self.information_section_2)
        self.gender_label.setObjectName("gender_label")
        self.gender_label.setMaximumSize(QSize(45, 22))
        self.gender_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_2.addWidget(self.gender_label)

        self.is_male_checkBox = QCheckBox(self.information_section_2)
        self.is_male_checkBox.setObjectName("is_male_checkBox")
        self.is_male_checkBox.setEnabled(True)
        self.is_male_checkBox.setMaximumSize(QSize(40, 16777215))
        self.is_male_checkBox.setMouseTracking(False)
        self.is_male_checkBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.is_male_checkBox)

        self.is_female_checkBox = QCheckBox(self.information_section_2)
        self.is_female_checkBox.setObjectName("is_female_checkBox")
        self.is_female_checkBox.setEnabled(True)
        self.is_female_checkBox.setMaximumSize(QSize(45, 16777215))
        self.is_female_checkBox.setMouseTracking(False)
        self.is_female_checkBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.is_female_checkBox)

        self.is_gender_unknown_checkbox = QCheckBox(self.information_section_2)
        self.is_gender_unknown_checkbox.setObjectName(
            "is_gender_unknown_checkbox",
        )
        self.is_gender_unknown_checkbox.setEnabled(True)
        self.is_gender_unknown_checkbox.setMaximumSize(QSize(85, 16777215))
        self.is_gender_unknown_checkbox.setMouseTracking(False)
        self.is_gender_unknown_checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.is_gender_unknown_checkbox)

        self.national_code_label = QLabel(self.information_section_2)
        self.national_code_label.setObjectName("national_code_label")
        self.national_code_label.setMaximumSize(QSize(45, 16777215))
        self.national_code_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_2.addWidget(self.national_code_label)

        self.national_code_field = QLineEdit(self.information_section_2)
        self.national_code_field.setObjectName("national_code_field")
        self.national_code_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.national_code_field.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.national_code_field)

        self.verticalLayout.addWidget(self.information_section_2)

        self.summary_section = QWidget(self.information_tab)
        self.summary_section.setObjectName("summary_section")
        self.horizontalLayout_6 = QHBoxLayout(self.summary_section)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mission_summary_field = QPlainTextEdit(self.summary_section)
        self.mission_summary_field.setObjectName("mission_summary_field")
        font = QFont()
        font.setPointSize(11)
        self.mission_summary_field.setFont(font)
        self.mission_summary_field.setAcceptDrops(False)
        self.mission_summary_field.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft,
        )
        self.mission_summary_field.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents,
        )
        self.mission_summary_field.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.mission_summary_field)

        self.verticalLayout.addWidget(self.summary_section)

        self.mission_data_tab_widget.addTab(self.information_tab, "")
        self.times_and_distances_tab = QWidget()
        self.times_and_distances_tab.setObjectName("times_and_distances_tab")
        self.verticalLayout_4 = QVBoxLayout(self.times_and_distances_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.times_section_91 = QWidget(self.times_and_distances_tab)
        self.times_section_91.setObjectName("times_section_91")
        self.times_section_91.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_16 = QHBoxLayout(self.times_section_91)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.mission_date_label = QLabel(self.times_section_91)
        self.mission_date_label.setObjectName("mission_date_label")
        self.mission_date_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_16.addWidget(self.mission_date_label)

        self.mission_date_field = QLineEdit(self.times_section_91)
        self.mission_date_field.setObjectName("mission_date_field")
        self.mission_date_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mission_date_field.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.mission_date_field)

        self.mission_received_label = QLabel(self.times_section_91)
        self.mission_received_label.setObjectName("mission_received_label")
        self.mission_received_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_16.addWidget(self.mission_received_label)

        self.mission_received_field = QLineEdit(self.times_section_91)
        self.mission_received_field.setObjectName("mission_received_field")
        self.mission_received_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mission_received_field.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.mission_received_field)

        self.verticalLayout_4.addWidget(self.times_section_91)

        self.times_section_1 = QWidget(self.times_and_distances_tab)
        self.times_section_1.setObjectName("times_section_1")
        self.times_section_1.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.times_section_1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.senior_staff_label = QLabel(self.times_section_1)
        self.senior_staff_label.setObjectName("senior_staff_label")
        self.senior_staff_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_7.addWidget(self.senior_staff_label)

        self.senior_staff_field = QLineEdit(self.times_section_1)
        self.senior_staff_field.setObjectName("senior_staff_field")
        self.senior_staff_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.senior_staff_field.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.senior_staff_field)

        self.first_staff_label = QLabel(self.times_section_1)
        self.first_staff_label.setObjectName("first_staff_label")
        self.first_staff_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_7.addWidget(self.first_staff_label)

        self.first_staff_field = QLineEdit(self.times_section_1)
        self.first_staff_field.setObjectName("first_staff_field")
        self.first_staff_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_staff_field.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.first_staff_field)

        self.second_staff_label = QLabel(self.times_section_1)
        self.second_staff_label.setObjectName("second_staff_label")
        self.second_staff_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_7.addWidget(self.second_staff_label)

        self.second_staff_field = QLineEdit(self.times_section_1)
        self.second_staff_field.setObjectName("second_staff_field")
        self.second_staff_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.second_staff_field.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.second_staff_field)

        self.refuel_odo_label = QLabel(self.times_section_1)
        self.refuel_odo_label.setObjectName("refuel_odo_label")

        self.horizontalLayout_7.addWidget(self.refuel_odo_label)

        self.refuel_odo_field = QLineEdit(self.times_section_1)
        self.refuel_odo_field.setObjectName("refuel_odo_field")
        self.refuel_odo_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.refuel_odo_field.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.refuel_odo_field)

        self.verticalLayout_4.addWidget(self.times_section_1)

        self.times_section_2 = QWidget(self.times_and_distances_tab)
        self.times_section_2.setObjectName("times_section_2")
        self.times_section_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.times_section_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.depart_from_station_odo_label = QLabel(self.times_section_2)
        self.depart_from_station_odo_label.setObjectName(
            "depart_from_station_odo_label",
        )
        self.depart_from_station_odo_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_8.addWidget(self.depart_from_station_odo_label)

        self.depart_from_station_odo_field = QLineEdit(self.times_section_2)
        self.depart_from_station_odo_field.setObjectName(
            "depart_from_station_odo_field",
        )
        self.depart_from_station_odo_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.depart_from_station_odo_field.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.depart_from_station_odo_field)

        self.depart_from_station_time_label = QLabel(self.times_section_2)
        self.depart_from_station_time_label.setObjectName(
            "depart_from_station_time_label",
        )
        self.depart_from_station_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_8.addWidget(self.depart_from_station_time_label)

        self.depart_from_station_time_field = QLineEdit(self.times_section_2)
        self.depart_from_station_time_field.setObjectName(
            "depart_from_station_time_field",
        )
        self.depart_from_station_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.depart_from_station_time_field.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.depart_from_station_time_field)

        self.time_to_depart_label = QLabel(self.times_section_2)
        self.time_to_depart_label.setObjectName("time_to_depart_label")
        self.time_to_depart_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_8.addWidget(self.time_to_depart_label)

        self.time_to_depart_field = QLineEdit(self.times_section_2)
        self.time_to_depart_field.setObjectName("time_to_depart_field")
        self.time_to_depart_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_to_depart_field.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.time_to_depart_field)

        self.verticalLayout_4.addWidget(self.times_section_2)

        self.times_section_3 = QWidget(self.times_and_distances_tab)
        self.times_section_3.setObjectName("times_section_3")
        self.times_section_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.times_section_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.arrive_at_emergency_time_label = QLabel(self.times_section_3)
        self.arrive_at_emergency_time_label.setObjectName(
            "arrive_at_emergency_time_label",
        )
        self.arrive_at_emergency_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_9.addWidget(self.arrive_at_emergency_time_label)

        self.arrive_at_emergency_time_field = QLineEdit(self.times_section_3)
        self.arrive_at_emergency_time_field.setObjectName(
            "arrive_at_emergency_time_field",
        )
        self.arrive_at_emergency_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_emergency_time_field.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.arrive_at_emergency_time_field)

        self.time_to_arrive_label = QLabel(self.times_section_3)
        self.time_to_arrive_label.setObjectName("time_to_arrive_label")
        self.time_to_arrive_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_9.addWidget(self.time_to_arrive_label)

        self.time_to_arrive_field = QLineEdit(self.times_section_3)
        self.time_to_arrive_field.setObjectName("time_to_arrive_field")
        self.time_to_arrive_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_to_arrive_field.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.time_to_arrive_field)

        self.arrive_at_emergency_odo_label = QLabel(self.times_section_3)
        self.arrive_at_emergency_odo_label.setObjectName(
            "arrive_at_emergency_odo_label",
        )
        self.arrive_at_emergency_odo_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_9.addWidget(self.arrive_at_emergency_odo_label)

        self.arrive_at_emergency_odo_field = QLineEdit(self.times_section_3)
        self.arrive_at_emergency_odo_field.setObjectName(
            "arrive_at_emergency_odo_field",
        )
        self.arrive_at_emergency_odo_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_emergency_odo_field.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.arrive_at_emergency_odo_field)

        self.verticalLayout_4.addWidget(self.times_section_3)

        self.times_section_4 = QWidget(self.times_and_distances_tab)
        self.times_section_4.setObjectName("times_section_4")
        self.times_section_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.times_section_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.depart_from_emergency_time_label = QLabel(self.times_section_4)
        self.depart_from_emergency_time_label.setObjectName(
            "depart_from_emergency_time_label",
        )
        self.depart_from_emergency_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_10.addWidget(
            self.depart_from_emergency_time_label,
        )

        self.depart_from_emergency_time_field = QLineEdit(self.times_section_4)
        self.depart_from_emergency_time_field.setObjectName(
            "depart_from_emergency_time_field",
        )
        self.depart_from_emergency_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.depart_from_emergency_time_field.setReadOnly(True)

        self.horizontalLayout_10.addWidget(
            self.depart_from_emergency_time_field,
        )

        self.time_at_emergency_label = QLabel(self.times_section_4)
        self.time_at_emergency_label.setObjectName("time_at_emergency_label")
        self.time_at_emergency_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_10.addWidget(self.time_at_emergency_label)

        self.time_at_emergency_field = QLineEdit(self.times_section_4)
        self.time_at_emergency_field.setObjectName("time_at_emergency_field")
        self.time_at_emergency_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_at_emergency_field.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.time_at_emergency_field)

        self.verticalLayout_4.addWidget(self.times_section_4)

        self.times_section_5 = QWidget(self.times_and_distances_tab)
        self.times_section_5.setObjectName("times_section_5")
        self.times_section_5.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.times_section_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.arrive_at_hospital_time_label = QLabel(self.times_section_5)
        self.arrive_at_hospital_time_label.setObjectName(
            "arrive_at_hospital_time_label",
        )
        self.arrive_at_hospital_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_11.addWidget(self.arrive_at_hospital_time_label)

        self.arrive_at_hospital_time_field = QLineEdit(self.times_section_5)
        self.arrive_at_hospital_time_field.setObjectName(
            "arrive_at_hospital_time_field",
        )
        self.arrive_at_hospital_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_hospital_time_field.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.arrive_at_hospital_time_field)

        self.time_to_hospital_label = QLabel(self.times_section_5)
        self.time_to_hospital_label.setObjectName("time_to_hospital_label")
        self.time_to_hospital_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_11.addWidget(self.time_to_hospital_label)

        self.time_to_hospital_field = QLineEdit(self.times_section_5)
        self.time_to_hospital_field.setObjectName("time_to_hospital_field")
        self.time_to_hospital_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_to_hospital_field.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.time_to_hospital_field)

        self.arrive_at_hospital_odo_label = QLabel(self.times_section_5)
        self.arrive_at_hospital_odo_label.setObjectName(
            "arrive_at_hospital_odo_label",
        )
        self.arrive_at_hospital_odo_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_11.addWidget(self.arrive_at_hospital_odo_label)

        self.arrive_at_hospital_odo_field = QLineEdit(self.times_section_5)
        self.arrive_at_hospital_odo_field.setObjectName(
            "arrive_at_hospital_odo_field",
        )
        self.arrive_at_hospital_odo_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_hospital_odo_field.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.arrive_at_hospital_odo_field)

        self.verticalLayout_4.addWidget(self.times_section_5)

        self.times_section_6 = QWidget(self.times_and_distances_tab)
        self.times_section_6.setObjectName("times_section_6")
        self.times_section_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.times_section_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.deliver_to_hospital_time_label = QLabel(self.times_section_6)
        self.deliver_to_hospital_time_label.setObjectName(
            "deliver_to_hospital_time_label",
        )
        self.deliver_to_hospital_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_12.addWidget(self.deliver_to_hospital_time_label)

        self.deliver_to_hospital_time_field = QLineEdit(self.times_section_6)
        self.deliver_to_hospital_time_field.setObjectName(
            "deliver_to_hospital_time_field",
        )
        self.deliver_to_hospital_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.deliver_to_hospital_time_field.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.deliver_to_hospital_time_field)

        self.time_to_deliver_label = QLabel(self.times_section_6)
        self.time_to_deliver_label.setObjectName("time_to_deliver_label")
        self.time_to_deliver_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_12.addWidget(self.time_to_deliver_label)

        self.time_to_deliver_field = QLineEdit(self.times_section_6)
        self.time_to_deliver_field.setObjectName("time_to_deliver_field")
        self.time_to_deliver_field.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.time_to_deliver_field)

        self.verticalLayout_4.addWidget(self.times_section_6)

        self.times_section_7 = QWidget(self.times_and_distances_tab)
        self.times_section_7.setObjectName("times_section_7")
        self.times_section_7.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.times_section_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.mission_complete_time_label = QLabel(self.times_section_7)
        self.mission_complete_time_label.setObjectName(
            "mission_complete_time_label",
        )
        self.mission_complete_time_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_13.addWidget(self.mission_complete_time_label)

        self.mission_complete_time_field = QLineEdit(self.times_section_7)
        self.mission_complete_time_field.setObjectName(
            "mission_complete_time_field",
        )
        self.mission_complete_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.mission_complete_time_field.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.mission_complete_time_field)

        self.time_to_complete_label = QLabel(self.times_section_7)
        self.time_to_complete_label.setObjectName("time_to_complete_label")
        self.time_to_complete_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_13.addWidget(self.time_to_complete_label)

        self.time_to_complete_field = QLineEdit(self.times_section_7)
        self.time_to_complete_field.setObjectName("time_to_complete_field")
        self.time_to_complete_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_to_complete_field.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.time_to_complete_field)

        self.mission_complete_odo_label = QLabel(self.times_section_7)
        self.mission_complete_odo_label.setObjectName(
            "mission_complete_odo_label",
        )
        self.mission_complete_odo_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_13.addWidget(self.mission_complete_odo_label)

        self.mission_complete_odo_field = QLineEdit(self.times_section_7)
        self.mission_complete_odo_field.setObjectName(
            "mission_complete_odo_field",
        )
        self.mission_complete_odo_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.mission_complete_odo_field.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.mission_complete_odo_field)

        self.verticalLayout_4.addWidget(self.times_section_7)

        self.times_section_8 = QWidget(self.times_and_distances_tab)
        self.times_section_8.setObjectName("times_section_8")
        self.times_section_8.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_14 = QHBoxLayout(self.times_section_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.arrive_at_station_time_label = QLabel(self.times_section_8)
        self.arrive_at_station_time_label.setObjectName(
            "arrive_at_station_time_label",
        )
        self.arrive_at_station_time_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_14.addWidget(self.arrive_at_station_time_label)

        self.arrive_at_station_time_field = QLineEdit(self.times_section_8)
        self.arrive_at_station_time_field.setObjectName(
            "arrive_at_station_time_field",
        )
        self.arrive_at_station_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_station_time_field.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.arrive_at_station_time_field)

        self.arrive_at_station_odo_label = QLabel(self.times_section_8)
        self.arrive_at_station_odo_label.setObjectName(
            "arrive_at_station_odo_label",
        )
        self.arrive_at_station_odo_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_14.addWidget(self.arrive_at_station_odo_label)

        self.arrive_at_station_odo_field = QLineEdit(self.times_section_8)
        self.arrive_at_station_odo_field.setObjectName(
            "arrive_at_station_odo_field",
        )
        self.arrive_at_station_odo_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.arrive_at_station_odo_field.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.arrive_at_station_odo_field)

        self.verticalLayout_4.addWidget(self.times_section_8)

        self.times_section_9 = QWidget(self.times_and_distances_tab)
        self.times_section_9.setObjectName("times_section_9")
        self.times_section_9.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_15 = QHBoxLayout(self.times_section_9)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.overall_mission_time_label = QLabel(self.times_section_9)
        self.overall_mission_time_label.setObjectName(
            "overall_mission_time_label",
        )
        self.overall_mission_time_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_15.addWidget(self.overall_mission_time_label)

        self.overall_mission_time_field = QLineEdit(self.times_section_9)
        self.overall_mission_time_field.setObjectName(
            "overall_mission_time_field",
        )
        self.overall_mission_time_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.overall_mission_time_field.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.overall_mission_time_field)

        self.overall_mission_distance_label = QLabel(self.times_section_9)
        self.overall_mission_distance_label.setObjectName(
            "overall_mission_distance_label",
        )
        self.overall_mission_distance_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_15.addWidget(self.overall_mission_distance_label)

        self.overall_mission_distance_field = QLineEdit(self.times_section_9)
        self.overall_mission_distance_field.setObjectName(
            "overall_mission_distance_field",
        )
        self.overall_mission_distance_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.overall_mission_distance_field.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.overall_mission_distance_field)

        self.verticalLayout_4.addWidget(self.times_section_9)

        self.mission_data_tab_widget.addTab(self.times_and_distances_tab, "")
        self.location_and_emergency_tab = QWidget()
        self.location_and_emergency_tab.setObjectName(
            "location_and_emergency_tab",
        )
        self.verticalLayout_3 = QVBoxLayout(self.location_and_emergency_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.section_1 = QWidget(self.location_and_emergency_tab)
        self.section_1.setObjectName("section_1")
        self.section_1.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_17 = QHBoxLayout(self.section_1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.address_label = QLabel(self.section_1)
        self.address_label.setObjectName("address_label")
        self.address_label.setMaximumSize(QSize(16777215, 30))
        self.address_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_17.addWidget(self.address_label)

        self.address_plain_text_edit = QPlainTextEdit(self.section_1)
        self.address_plain_text_edit.setObjectName("address_plain_text_edit")
        self.address_plain_text_edit.setMaximumSize(QSize(16777215, 100))
        self.address_plain_text_edit.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.address_plain_text_edit)

        self.verticalLayout_3.addWidget(self.section_1)

        self.section_2 = QWidget(self.location_and_emergency_tab)
        self.section_2.setObjectName("section_2")
        self.section_2.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_18 = QHBoxLayout(self.section_2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.chief_complaint_label = QLabel(self.section_2)
        self.chief_complaint_label.setObjectName("chief_complaint_label")
        self.chief_complaint_label.setMaximumSize(QSize(16777215, 30))
        self.chief_complaint_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_18.addWidget(self.chief_complaint_label)

        self.chief_complaint_field = QLineEdit(self.section_2)
        self.chief_complaint_field.setObjectName("chief_complaint_field")
        self.chief_complaint_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chief_complaint_field.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.chief_complaint_field)

        self.type_of_location_label = QLabel(self.section_2)
        self.type_of_location_label.setObjectName("type_of_location_label")
        self.type_of_location_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_18.addWidget(self.type_of_location_label)

        self.type_of_location_field = QLineEdit(self.section_2)
        self.type_of_location_field.setObjectName("type_of_location_field")
        self.type_of_location_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.type_of_location_field.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.type_of_location_field)

        self.type_of_location_other_info_label = QLabel(self.section_2)
        self.type_of_location_other_info_label.setObjectName(
            "type_of_location_other_info_label",
        )
        self.type_of_location_other_info_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_18.addWidget(
            self.type_of_location_other_info_label,
        )

        self.type_of_location_other_info_field = QLineEdit(self.section_2)
        self.type_of_location_other_info_field.setObjectName(
            "type_of_location_other_info_field",
        )
        self.type_of_location_other_info_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.type_of_location_other_info_field.setReadOnly(True)

        self.horizontalLayout_18.addWidget(
            self.type_of_location_other_info_field,
        )

        self.verticalLayout_3.addWidget(self.section_2)

        self.section_3 = QWidget(self.location_and_emergency_tab)
        self.section_3.setObjectName("section_3")
        self.section_3.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_19 = QHBoxLayout(self.section_3)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.accident_type_label = QLabel(self.section_3)
        self.accident_type_label.setObjectName("accident_type_label")
        self.accident_type_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_19.addWidget(self.accident_type_label)

        self.accident_type_field = QLineEdit(self.section_3)
        self.accident_type_field.setObjectName("accident_type_field")
        self.accident_type_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accident_type_field.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.accident_type_field)

        self.illness_type_label = QLabel(self.section_3)
        self.illness_type_label.setObjectName("illness_type_label")
        self.illness_type_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_19.addWidget(self.illness_type_label)

        self.illness_type_field = QLineEdit(self.section_3)
        self.illness_type_field.setObjectName("illness_type_field")
        self.illness_type_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.illness_type_field.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.illness_type_field)

        self.emergency_other_info_label = QLabel(self.section_3)
        self.emergency_other_info_label.setObjectName(
            "emergency_other_info_label",
        )
        self.emergency_other_info_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_19.addWidget(self.emergency_other_info_label)

        self.emergency_other_info_field = QLineEdit(self.section_3)
        self.emergency_other_info_field.setObjectName(
            "emergency_other_info_field",
        )
        self.emergency_other_info_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.emergency_other_info_field.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.emergency_other_info_field)

        self.is_vehicle_accident_checkBox = QCheckBox(self.section_3)
        self.is_vehicle_accident_checkBox.setObjectName(
            "is_vehicle_accident_checkBox",
        )
        self.is_vehicle_accident_checkBox.setEnabled(True)
        self.is_vehicle_accident_checkBox.setMouseTracking(False)
        self.is_vehicle_accident_checkBox.setFocusPolicy(
            Qt.FocusPolicy.NoFocus,
        )
        self.is_vehicle_accident_checkBox.setCheckable(True)
        self.is_vehicle_accident_checkBox.setChecked(False)

        self.horizontalLayout_19.addWidget(self.is_vehicle_accident_checkBox)

        self.verticalLayout_3.addWidget(self.section_3)

        self.section_4 = QWidget(self.location_and_emergency_tab)
        self.section_4.setObjectName("section_4")
        self.section_4.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_20 = QHBoxLayout(self.section_4)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.role_in_accident_label = QLabel(self.section_4)
        self.role_in_accident_label.setObjectName("role_in_accident_label")
        self.role_in_accident_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_20.addWidget(self.role_in_accident_label)

        self.role_in_accident_field = QLineEdit(self.section_4)
        self.role_in_accident_field.setObjectName("role_in_accident_field")
        self.role_in_accident_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.role_in_accident_field.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.role_in_accident_field)

        self.role_in_accident_other_info_label = QLabel(self.section_4)
        self.role_in_accident_other_info_label.setObjectName(
            "role_in_accident_other_info_label",
        )
        self.role_in_accident_other_info_label.setTextFormat(
            Qt.TextFormat.PlainText,
        )

        self.horizontalLayout_20.addWidget(
            self.role_in_accident_other_info_label,
        )

        self.role_in_accident_other_info_field = QLineEdit(self.section_4)
        self.role_in_accident_other_info_field.setObjectName(
            "role_in_accident_other_info_field",
        )
        self.role_in_accident_other_info_field.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.role_in_accident_other_info_field.setReadOnly(True)

        self.horizontalLayout_20.addWidget(
            self.role_in_accident_other_info_field,
        )

        self.vehicle_type_label = QLabel(self.section_4)
        self.vehicle_type_label.setObjectName("vehicle_type_label")
        self.vehicle_type_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_20.addWidget(self.vehicle_type_label)

        self.vehicle_type_field = QLineEdit(self.section_4)
        self.vehicle_type_field.setObjectName("vehicle_type_field")
        self.vehicle_type_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vehicle_type_field.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.vehicle_type_field)

        self.verticalLayout_3.addWidget(self.section_4)

        self.mission_data_tab_widget.addTab(
            self.location_and_emergency_tab,
            "",
        )
        self.symptoms_tab = QWidget()
        self.symptoms_tab.setObjectName("symptoms_tab")
        self.verticalLayout_5 = QVBoxLayout(self.symptoms_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vital_signs_group_Box = QGroupBox(self.symptoms_tab)
        self.vital_signs_group_Box.setObjectName("vital_signs_group_Box")
        self.vital_signs_group_Box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.vital_signs_group_Box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vital_signs_table_Widget = QTableWidget(
            self.vital_signs_group_Box,
        )
        if self.vital_signs_table_Widget.rowCount() < 10:
            self.vital_signs_table_Widget.setRowCount(10)
        self.vital_signs_table_Widget.setObjectName(
            "vital_signs_table_Widget",
        )
        self.vital_signs_table_Widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.vital_signs_table_Widget.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight,
        )
        self.vital_signs_table_Widget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )
        self.vital_signs_table_Widget.setTabKeyNavigation(False)
        self.vital_signs_table_Widget.setProperty("showDropIndicator", False)
        self.vital_signs_table_Widget.setAlternatingRowColors(True)
        self.vital_signs_table_Widget.setSelectionMode(
            QAbstractItemView.SelectionMode.NoSelection,
        )
        self.vital_signs_table_Widget.setCornerButtonEnabled(False)
        self.vital_signs_table_Widget.setRowCount(10)
        self.vital_signs_table_Widget.setSupportedDragActions(
            Qt.DropAction.IgnoreAction,
        )
        self.vital_signs_table_Widget.verticalHeader().setDefaultSectionSize(30)
        self.vital_signs_table_Widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.vital_signs_table_Widget)

        self.verticalLayout_5.addWidget(self.vital_signs_group_Box)

        self.symptoms_section = QWidget(self.symptoms_tab)
        self.symptoms_section.setObjectName("symptoms_section")
        self.symptoms_section.setMaximumSize(QSize(16777215, 175))
        self.gridLayout = QGridLayout(self.symptoms_section)
        self.gridLayout.setObjectName("gridLayout")
        self.symptoms_group_box = QGroupBox(self.symptoms_section)
        self.symptoms_group_box.setObjectName("symptoms_group_box")
        self.symptoms_group_box.setMaximumSize(QSize(16777215, 175))
        self.symptoms_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.symptoms_group_box.setFlat(False)
        self.symptoms_group_box.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.symptoms_group_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.has_sensory_motor_disturbance_checkbox = QCheckBox(
            self.symptoms_group_box,
        )
        self.has_sensory_motor_disturbance_checkbox.setObjectName(
            "has_sensory_motor_disturbance_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_sensory_motor_disturbance_checkbox,
            2,
            1,
            1,
            1,
        )

        self.has_memory_loss_post_trauma_checkbox = QCheckBox(
            self.symptoms_group_box,
        )
        self.has_memory_loss_post_trauma_checkbox.setObjectName(
            "has_memory_loss_post_trauma_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_memory_loss_post_trauma_checkbox,
            1,
            0,
            1,
            1,
        )

        self.has_abdominal_pain_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_abdominal_pain_checkbox.setObjectName(
            "has_abdominal_pain_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_abdominal_pain_checkbox,
            1,
            1,
            1,
            1,
        )

        self.has_shortness_of_breath_checkbox = QCheckBox(
            self.symptoms_group_box,
        )
        self.has_shortness_of_breath_checkbox.setObjectName(
            "has_shortness_of_breath_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_shortness_of_breath_checkbox,
            0,
            4,
            1,
            1,
        )

        self.has_altered_consciousness_checkbox = QCheckBox(
            self.symptoms_group_box,
        )
        self.has_altered_consciousness_checkbox.setObjectName(
            "has_altered_consciousness_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_altered_consciousness_checkbox,
            2,
            2,
            1,
            1,
        )

        self.has_vomiting_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_vomiting_checkbox.setObjectName("has_vomiting_checkbox")

        self.gridLayout_2.addWidget(self.has_vomiting_checkbox, 1, 3, 1, 1)

        self.has_bleeding_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_bleeding_checkbox.setObjectName("has_bleeding_checkbox")

        self.gridLayout_2.addWidget(self.has_bleeding_checkbox, 1, 5, 1, 1)

        self.has_diarrhea_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_diarrhea_checkbox.setObjectName("has_diarrhea_checkbox")

        self.gridLayout_2.addWidget(self.has_diarrhea_checkbox, 1, 6, 1, 1)

        self.has_double_vision_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_double_vision_checkbox.setObjectName(
            "has_double_vision_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_double_vision_checkbox,
            0,
            3,
            1,
            1,
        )

        self.has_headache_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_headache_checkbox.setObjectName("has_headache_checkbox")

        self.gridLayout_2.addWidget(self.has_headache_checkbox, 1, 2, 1, 1)

        self.has_blurred_vision_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_blurred_vision_checkbox.setObjectName(
            "has_blurred_vision_checkbox",
        )

        self.gridLayout_2.addWidget(
            self.has_blurred_vision_checkbox,
            0,
            5,
            1,
            1,
        )

        self.has_dizziness_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_dizziness_checkbox.setObjectName("has_dizziness_checkbox")

        self.gridLayout_2.addWidget(self.has_dizziness_checkbox, 1, 4, 1, 1)

        self.has_fainting_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_fainting_checkbox.setObjectName("has_fainting_checkbox")

        self.gridLayout_2.addWidget(self.has_fainting_checkbox, 0, 1, 1, 1)

        self.has_fever_chills_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_fever_chills_checkbox.setObjectName(
            "has_fever_chills_checkbox",
        )

        self.gridLayout_2.addWidget(self.has_fever_chills_checkbox, 0, 2, 1, 1)

        self.has_chest_pain_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_chest_pain_checkbox.setObjectName("has_chest_pain_checkbox")

        self.gridLayout_2.addWidget(self.has_chest_pain_checkbox, 0, 0, 1, 1)

        self.has_sweating_checkbox = QCheckBox(self.symptoms_group_box)
        self.has_sweating_checkbox.setObjectName("has_sweating_checkbox")

        self.gridLayout_2.addWidget(self.has_sweating_checkbox, 0, 6, 1, 1)

        self.has_weakness_checkBox = QCheckBox(self.symptoms_group_box)
        self.has_weakness_checkBox.setObjectName("has_weakness_checkBox")

        self.gridLayout_2.addWidget(self.has_weakness_checkBox, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.symptoms_group_box, 0, 0, 1, 1)

        self.verticalLayout_5.addWidget(self.symptoms_section)

        self.other_symptoms_section = QWidget(self.symptoms_tab)
        self.other_symptoms_section.setObjectName("other_symptoms_section")
        self.other_symptoms_section.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_21 = QHBoxLayout(self.other_symptoms_section)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.other_symptoms_label = QLabel(self.other_symptoms_section)
        self.other_symptoms_label.setObjectName("other_symptoms_label")
        self.other_symptoms_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_21.addWidget(self.other_symptoms_label)

        self.other_symptoms_field = QPlainTextEdit(self.other_symptoms_section)
        self.other_symptoms_field.setObjectName("other_symptoms_field")
        self.other_symptoms_field.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.other_symptoms_field)

        self.verticalLayout_5.addWidget(self.other_symptoms_section)

        self.mission_data_tab_widget.addTab(self.symptoms_tab, "")
        self.history_and_trauma_tab = QWidget()
        self.history_and_trauma_tab.setObjectName("history_and_trauma_tab")
        self.verticalLayout_8 = QVBoxLayout(self.history_and_trauma_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget = QWidget(self.history_and_trauma_tab)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.medical_history_group_box = QGroupBox(self.widget)
        self.medical_history_group_box.setObjectName(
            "medical_history_group_box",
        )
        self.medical_history_group_box.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.gridLayout_3 = QGridLayout(self.medical_history_group_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.has_gastrointestinal_disease_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_gastrointestinal_disease_checkBox.setObjectName(
            "has_gastrointestinal_disease_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_gastrointestinal_disease_checkBox,
            0,
            0,
            1,
            1,
        )

        self.has_hypertension_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_hypertension_checkBox.setObjectName(
            "has_hypertension_checkBox",
        )

        self.gridLayout_3.addWidget(self.has_hypertension_checkBox, 0, 6, 1, 1)

        self.has_special_conditions_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_special_conditions_checkBox.setObjectName(
            "has_special_conditions_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_special_conditions_checkBox,
            0,
            4,
            1,
            1,
        )

        self.has_infectious_disease_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_infectious_disease_checkBox.setObjectName(
            "has_infectious_disease_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_infectious_disease_checkBox,
            0,
            2,
            1,
            1,
        )

        self.has_diabetes_checkBox = QCheckBox(self.medical_history_group_box)
        self.has_diabetes_checkBox.setObjectName("has_diabetes_checkBox")

        self.gridLayout_3.addWidget(self.has_diabetes_checkBox, 0, 3, 1, 1)

        self.has_seizure_disorder_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_seizure_disorder_checkBox.setObjectName(
            "has_seizure_disorder_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_seizure_disorder_checkBox,
            0,
            1,
            1,
            1,
        )

        self.has_pulmonary_disease_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_pulmonary_disease_checkBox.setObjectName(
            "has_pulmonary_disease_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_pulmonary_disease_checkBox,
            0,
            5,
            1,
            1,
        )

        self.has_malignancy_history_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_malignancy_history_checkBox.setObjectName(
            "has_malignancy_history_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_malignancy_history_checkBox,
            1,
            3,
            1,
            1,
        )

        self.has_substance_abuse_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_substance_abuse_checkBox.setObjectName(
            "has_substance_abuse_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_substance_abuse_checkBox,
            1,
            4,
            1,
            1,
        )

        self.has_renal_disease_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_renal_disease_checkBox.setObjectName(
            "has_renal_disease_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_renal_disease_checkBox,
            1,
            2,
            1,
            1,
        )

        self.has_cardiac_disease_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_cardiac_disease_checkBox.setObjectName(
            "has_cardiac_disease_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_cardiac_disease_checkBox,
            1,
            1,
            1,
            1,
        )

        self.has_disability_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_disability_checkBox.setObjectName("has_disability_checkBox")

        self.gridLayout_3.addWidget(self.has_disability_checkBox, 1, 5, 1, 1)

        self.has_asthma_checkBox = QCheckBox(self.medical_history_group_box)
        self.has_asthma_checkBox.setObjectName("has_asthma_checkBox")

        self.gridLayout_3.addWidget(self.has_asthma_checkBox, 1, 6, 1, 1)

        self.has_stroke_history_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_stroke_history_checkBox.setObjectName(
            "has_stroke_history_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_stroke_history_checkBox,
            1,
            0,
            1,
            1,
        )

        self.has_psychiatric_disorder_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_psychiatric_disorder_checkBox.setObjectName(
            "has_psychiatric_disorder_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_psychiatric_disorder_checkBox,
            2,
            0,
            1,
            1,
        )

        self.has_prior_trauma_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_prior_trauma_checkBox.setObjectName(
            "has_prior_trauma_checkBox",
        )

        self.gridLayout_3.addWidget(self.has_prior_trauma_checkBox, 2, 1, 1, 1)

        self.has_surgical_history_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.has_surgical_history_checkBox.setObjectName(
            "has_surgical_history_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.has_surgical_history_checkBox,
            2,
            2,
            1,
            1,
        )

        self.other_medical_history_checkBox = QCheckBox(
            self.medical_history_group_box,
        )
        self.other_medical_history_checkBox.setObjectName(
            "other_medical_history_checkBox",
        )

        self.gridLayout_3.addWidget(
            self.other_medical_history_checkBox,
            2,
            3,
            1,
            1,
        )

        self.verticalLayout_7.addWidget(self.medical_history_group_box)

        self.medical_history_other_info = QWidget(self.widget)
        self.medical_history_other_info.setObjectName(
            "medical_history_other_info",
        )
        self.medical_history_other_info.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_22 = QHBoxLayout(self.medical_history_other_info)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.current_medications_label = QLabel(
            self.medical_history_other_info,
        )
        self.current_medications_label.setObjectName(
            "current_medications_label",
        )
        self.current_medications_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_22.addWidget(self.current_medications_label)

        self.current_medications_field = QPlainTextEdit(
            self.medical_history_other_info,
        )
        self.current_medications_field.setObjectName(
            "current_medications_field",
        )
        self.current_medications_field.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.current_medications_field)

        self.drug_allergies_label = QLabel(self.medical_history_other_info)
        self.drug_allergies_label.setObjectName("drug_allergies_label")
        self.drug_allergies_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_22.addWidget(self.drug_allergies_label)

        self.drug_allergies_field = QPlainTextEdit(
            self.medical_history_other_info,
        )
        self.drug_allergies_field.setObjectName("drug_allergies_field")
        self.drug_allergies_field.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents,
        )
        self.drug_allergies_field.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.drug_allergies_field)

        self.verticalLayout_7.addWidget(self.medical_history_other_info)

        self.examine_eye_lung_heart_group_box = QGroupBox(self.widget)
        self.examine_eye_lung_heart_group_box.setObjectName(
            "examine_eye_lung_heart_group_box",
        )
        self.examine_eye_lung_heart_group_box.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )
        self.horizontalLayout_23 = QHBoxLayout(
            self.examine_eye_lung_heart_group_box,
        )
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.eye_group_box = QGroupBox(self.examine_eye_lung_heart_group_box)
        self.eye_group_box.setObjectName("eye_group_box")
        self.eye_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.eye_group_box)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.right_eye_examine_label = QLabel(self.eye_group_box)
        self.right_eye_examine_label.setObjectName("right_eye_examine_label")
        self.right_eye_examine_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_4.addWidget(self.right_eye_examine_label, 0, 0, 1, 1)

        self.right_eye_examine_field = QLineEdit(self.eye_group_box)
        self.right_eye_examine_field.setObjectName("right_eye_examine_field")
        self.right_eye_examine_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_eye_examine_field.setReadOnly(True)

        self.gridLayout_4.addWidget(self.right_eye_examine_field, 0, 1, 1, 1)

        self.left_eye_examine_label = QLabel(self.eye_group_box)
        self.left_eye_examine_label.setObjectName("left_eye_examine_label")
        self.left_eye_examine_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_4.addWidget(self.left_eye_examine_label, 1, 0, 1, 1)

        self.left_eye_examine_field = QLineEdit(self.eye_group_box)
        self.left_eye_examine_field.setObjectName("left_eye_examine_field")
        self.left_eye_examine_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_eye_examine_field.setReadOnly(True)

        self.gridLayout_4.addWidget(self.left_eye_examine_field, 1, 1, 1, 1)

        self.horizontalLayout_23.addWidget(self.eye_group_box)

        self.lung_group_box = QGroupBox(self.examine_eye_lung_heart_group_box)
        self.lung_group_box.setObjectName("lung_group_box")
        self.lung_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_24 = QHBoxLayout(self.lung_group_box)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.right_lung_group_box = QGroupBox(self.lung_group_box)
        self.right_lung_group_box.setObjectName("right_lung_group_box")
        self.right_lung_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.right_lung_group_box)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lung_sound_label = QLabel(self.right_lung_group_box)
        self.lung_sound_label.setObjectName("lung_sound_label")
        self.lung_sound_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_5.addWidget(self.lung_sound_label, 0, 0, 1, 1)

        self.breathing_rhythm_label = QLabel(self.right_lung_group_box)
        self.breathing_rhythm_label.setObjectName("breathing_rhythm_label")
        self.breathing_rhythm_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_5.addWidget(self.breathing_rhythm_label, 1, 0, 1, 1)

        self.right_lung_rhythm_field = QLineEdit(self.right_lung_group_box)
        self.right_lung_rhythm_field.setObjectName("right_lung_rhythm_field")
        self.right_lung_rhythm_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_lung_rhythm_field.setReadOnly(True)

        self.gridLayout_5.addWidget(self.right_lung_rhythm_field, 1, 2, 1, 1)

        self.right_lung_sound_field = QLineEdit(self.right_lung_group_box)
        self.right_lung_sound_field.setObjectName("right_lung_sound_field")
        self.right_lung_sound_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_lung_sound_field.setReadOnly(True)

        self.gridLayout_5.addWidget(self.right_lung_sound_field, 0, 2, 1, 1)

        self.horizontalLayout_24.addWidget(self.right_lung_group_box)

        self.left_lung_group_box = QGroupBox(self.lung_group_box)
        self.left_lung_group_box.setObjectName("left_lung_group_box")
        self.left_lung_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.left_lung_group_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.left_lung_rhythm_field = QLineEdit(self.left_lung_group_box)
        self.left_lung_rhythm_field.setObjectName("left_lung_rhythm_field")
        self.left_lung_rhythm_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_lung_rhythm_field.setReadOnly(True)

        self.gridLayout_6.addWidget(self.left_lung_rhythm_field, 1, 0, 1, 1)

        self.left_lung_sound_field = QLineEdit(self.left_lung_group_box)
        self.left_lung_sound_field.setObjectName("left_lung_sound_field")
        self.left_lung_sound_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_lung_sound_field.setReadOnly(True)

        self.gridLayout_6.addWidget(self.left_lung_sound_field, 0, 0, 1, 1)

        self.horizontalLayout_24.addWidget(self.left_lung_group_box)

        self.horizontalLayout_23.addWidget(self.lung_group_box)

        self.heart_group_box = QGroupBox(self.examine_eye_lung_heart_group_box)
        self.heart_group_box.setObjectName("heart_group_box")
        self.heart_group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_7 = QGridLayout(self.heart_group_box)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.heart_rhythm_field = QLineEdit(self.heart_group_box)
        self.heart_rhythm_field.setObjectName("heart_rhythm_field")
        self.heart_rhythm_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.heart_rhythm_field.setReadOnly(True)

        self.gridLayout_7.addWidget(self.heart_rhythm_field, 1, 1, 1, 1)

        self.heart_sound_field = QLineEdit(self.heart_group_box)
        self.heart_sound_field.setObjectName("heart_sound_field")
        self.heart_sound_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.heart_sound_field.setReadOnly(True)

        self.gridLayout_7.addWidget(self.heart_sound_field, 0, 1, 1, 1)

        self.heart_rhythm_label = QLabel(self.heart_group_box)
        self.heart_rhythm_label.setObjectName("heart_rhythm_label")
        self.heart_rhythm_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_7.addWidget(self.heart_rhythm_label, 1, 0, 1, 1)

        self.heart_sound_label = QLabel(self.heart_group_box)
        self.heart_sound_label.setObjectName("heart_sound_label")
        self.heart_sound_label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_7.addWidget(self.heart_sound_label, 0, 0, 1, 1)

        self.horizontalLayout_23.addWidget(self.heart_group_box)

        self.verticalLayout_7.addWidget(self.examine_eye_lung_heart_group_box)

        self.verticalLayout_8.addWidget(self.widget)

        self.mission_data_tab_widget.addTab(self.history_and_trauma_tab, "")

        self.verticalLayout_2.addWidget(self.mission_data_tab_widget)

        self.retranslateUi(mission_details_tab)

        self.search_button.setDefault(True)
        self.mission_data_tab_widget.setCurrentIndex(4)

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
        self.mission_id_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u0645\u0627\u0631\u0647 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a",
                None,
            ),
        )
        self.patient_id_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u0645\u0627\u0631\u0647 \u0645\u062f\u062f\u062c\u0648",
                None,
            ),
        )
        self.search_button.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062c\u0633\u062a\u062c\u0648",
                None,
            ),
        )
        self.last_update_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0622\u062e\u0631\u06cc\u0646 \u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc \u067e\u0631\u0648\u0646\u062f\u0647:",
                None,
            ),
        )
        self.base_station_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0631\u06a9\u0632:",
                None,
            ),
        )
        self.document_serial_number_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u0645\u0627\u0631\u0647 \u0633\u0631\u06cc\u0627\u0644 \u067e\u0631\u0648\u0646\u062f\u0647:",
                None,
            ),
        )
        self.caller_number_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633:",
                None,
            ),
        )
        self.backup_number_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633:",
                None,
            ),
        )
        self.ambulance_code_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u062f \u0622\u0645\u0628\u0648\u0644\u0627\u0646\u0633:",
                None,
            ),
        )
        self.patient_name_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0627\u0645 \u0645\u062f\u062f\u062c\u0648:",
                None,
            ),
        )
        self.age_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0646:",
                None,
            ),
        )
        self.nationality_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0644\u06cc\u062a:",
                None,
            ),
        )
        self.iranian_nationality_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u06cc\u0631\u0627\u0646\u06cc",
                None,
            ),
        )
        self.foreign_nationality_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u063a\u06cc\u0631 \u0627\u06cc\u0631\u0627\u0646\u06cc",
                None,
            ),
        )
        self.gender_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062c\u062a\u0633\u06cc\u062a:",
                None,
            ),
        )
        self.is_male_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0622\u0642\u0627",
                None,
            ),
        )
        self.is_female_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062e\u0627\u0646\u0645",
                None,
            ),
        )
        self.is_gender_unknown_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0627\u0645\u0634\u062e\u0635",
                None,
            ),
        )
        self.national_code_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u062f \u0645\u0644\u06cc:",
                None,
            ),
        )
        self.mission_data_tab_widget.setTabText(
            self.mission_data_tab_widget.indexOf(
                self.information_tab,
            ),
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06af\u0632\u0627\u0631\u0634",
                None,
            ),
        )
        self.mission_date_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0627\u0631\u06cc\u062e \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.mission_received_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u062f\u0631\u06cc\u0627\u0641\u062a \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.senior_staff_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u062f \u0627\u0631\u0634\u062f:",
                None,
            ),
        )
        self.first_staff_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u062f \u0627\u0648\u0644:",
                None,
            ),
        )
        self.second_staff_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u062f \u062f\u0648\u0645:",
                None,
            ),
        )
        self.refuel_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u0633\u0648\u062e\u062a\u06af\u06cc\u0631\u06cc:",
                None,
            ),
        )
        self.depart_from_station_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u062d\u0631\u06a9\u062a \u0627\u0632 \u067e\u0627\u06cc\u06af\u0627\u0647:",
                None,
            ),
        )
        self.depart_from_station_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u062d\u0631\u06a9\u062a \u0627\u0632 \u067e\u0627\u06cc\u06af\u0627\u0647:",
                None,
            ),
        )
        self.time_to_depart_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u062a\u0627 \u062d\u0631\u06a9\u062a:",
                None,
            ),
        )
        self.arrive_at_emergency_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.time_to_arrive_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u062a\u0627 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.arrive_at_emergency_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.depart_from_emergency_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u062d\u0631\u06a9\u062a \u0627\u0632 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.time_at_emergency_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u062f\u0631 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.arrive_at_hospital_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u0631\u06a9\u0632 \u062f\u0631\u0645\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.time_to_hospital_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u062a\u0627 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u0631\u06a9\u0632 \u062f\u0631\u0645\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.arrive_at_hospital_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u0645\u0631\u06a9\u0632\u062f\u0631\u0645\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.deliver_to_hospital_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u062a\u062d\u0648\u06cc\u0644 \u0628\u0647 \u0645\u0631\u06a9\u0632 \u062f\u0631\u0645\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.time_to_deliver_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u062a\u062d\u0648\u06cc\u0644 \u0628\u0647 \u0645\u0631\u06a9\u0632 \u062f\u0631\u0645\u0627\u0646\u06cc:",
                None,
            ),
        )
        self.mission_complete_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u067e\u0627\u06cc\u0627\u0646 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.time_to_complete_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u067e\u0627\u06cc\u0627\u0646 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.mission_complete_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u067e\u0627\u06cc\u0627\u0646 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.arrive_at_station_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0632\u0645\u0627\u0646 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u067e\u0627\u06cc\u06af\u0627\u0647:",
                None,
            ),
        )
        self.arrive_at_station_odo_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u06cc\u0644\u0648\u0645\u062a\u0631 \u0631\u0633\u06cc\u062f\u0646 \u0628\u0647 \u067e\u0627\u06cc\u06af\u0627\u0647:",
                None,
            ),
        )
        self.overall_mission_time_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062f\u062a \u0632\u0645\u0627\u0646 \u06a9\u0644 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.overall_mission_distance_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0633\u0627\u0641\u062a \u06a9\u0644 \u0645\u0627\u0645\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.mission_data_tab_widget.setTabText(
            self.mission_data_tab_widget.indexOf(self.times_and_distances_tab),
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0633\u0627\u0641\u062a \u0648 \u0632\u0645\u0627\u0646",
                None,
            ),
        )
        self.address_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0622\u062f\u0631\u0633 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.chief_complaint_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0634\u06a9\u0627\u06cc\u062a \u0627\u0635\u0644\u06cc:",
                None,
            ),
        )
        self.type_of_location_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0648\u0639 \u0645\u062d\u0644 \u0641\u0648\u0631\u06cc\u062a:",
                None,
            ),
        )
        self.type_of_location_other_info_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0627\u06cc\u0631 \u0627\u0637\u0644\u0627\u0639\u0627\u062a:",
                None,
            ),
        )
        self.accident_type_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0648\u0639 \u062d\u0627\u062f\u062b\u0647:",
                None,
            ),
        )
        self.illness_type_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0648\u0639 \u0628\u06cc\u0645\u0627\u0631\u06cc:",
                None,
            ),
        )
        self.emergency_other_info_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0627\u06cc\u0631 \u0627\u0637\u0644\u0627\u0639\u0627\u062a:",
                None,
            ),
        )
        self.is_vehicle_accident_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0635\u0627\u062f\u0641",
                None,
            ),
        )
        self.role_in_accident_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0642\u0634 \u062d\u0627\u062f\u062b\u0647 \u062f\u06cc\u062f\u0647:",
                None,
            ),
        )
        self.role_in_accident_other_info_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0627\u06cc\u0631 \u0627\u0637\u0644\u0627\u0639\u0627\u062a:",
                None,
            ),
        )
        self.vehicle_type_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0646\u0648\u0639 \u062e\u0648\u062f\u0631\u0648:",
                None,
            ),
        )
        self.mission_data_tab_widget.setTabText(
            self.mission_data_tab_widget.indexOf(self.location_and_emergency_tab),
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u062d\u0644 \u0648 \u0646\u0648\u0639 \u0641\u0648\u0631\u06cc\u062a",
                None,
            ),
        )
        self.vital_signs_group_Box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0639\u0644\u0627\u0626\u0645 \u062d\u06cc\u0627\u062a\u06cc",
                None,
            ),
        )
        self.symptoms_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0639\u0644\u0627\u0626\u0645 \u0647\u0645\u0631\u0627\u0647",
                None,
            ),
        )
        self.has_sensory_motor_disturbance_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u062e\u062a\u0644\u0627\u0644 \u062d\u0633\u06cc \u062d\u0631\u06a9\u062a\u06cc",
                None,
            ),
        )
        self.has_memory_loss_post_trauma_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0641\u0631\u0627\u0645\u0648\u0634\u06cc \u067e\u0633 \u0627\u0632 \u0636\u0631\u0628\u0647",
                None,
            ),
        )
        self.has_abdominal_pain_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062f\u0631\u062f \u0634\u06a9\u0645\u06cc",
                None,
            ),
        )
        self.has_shortness_of_breath_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0646\u06af\u06cc \u0646\u0641\u0633",
                None,
            ),
        )
        self.has_altered_consciousness_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u062e\u062a\u0644\u0627\u0644 \u0647\u0648\u0634\u06cc\u0627\u0631\u06cc",
                None,
            ),
        )
        self.has_vomiting_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u0633\u062a\u0641\u0631\u0627\u063a",
                None,
            ),
        )
        self.has_bleeding_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062e\u0648\u0646\u0631\u06cc\u0632\u06cc",
                None,
            ),
        )
        self.has_diarrhea_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u0633\u0647\u0627\u0644",
                None,
            ),
        )
        self.has_double_vision_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062f\u0648\u0628\u06cc\u0646\u06cc",
                None,
            ),
        )
        self.has_headache_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0631\u062f\u0631\u062f",
                None,
            ),
        )
        self.has_blurred_vision_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0627\u0631\u06cc \u062f\u06cc\u062f",
                None,
            ),
        )
        self.has_dizziness_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0631\u06af\u06cc\u062c\u0647",
                None,
            ),
        )
        self.has_fainting_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0628\u06cc\u0647\u0648\u0634\u06cc",
                None,
            ),
        )
        self.has_fever_chills_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0628 \u0648 \u0644\u0631\u0632",
                None,
            ),
        )
        self.has_chest_pain_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062f\u0631\u062f \u0642\u0641\u0633\u0647 \u0633\u06cc\u0646\u0647",
                None,
            ),
        )
        self.has_sweating_checkbox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0639\u0631\u06cc\u0642",
                None,
            ),
        )
        self.has_weakness_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0636\u0639\u0641 \u0648 \u0628\u06cc \u062d\u0627\u0644\u06cc",
                None,
            ),
        )
        self.other_symptoms_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0627\u06cc\u0631 \u0639\u0644\u0627\u0626\u0645 \u0647\u0645\u0631\u0627\u0647:",
                None,
            ),
        )
        self.mission_data_tab_widget.setTabText(
            self.mission_data_tab_widget.indexOf(self.symptoms_tab),
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0639\u0644\u0627\u0626\u0645 \u062d\u06cc\u0627\u062a\u06cc \u0648 \u0647\u0645\u0631\u0627\u0647",
                None,
            ),
        )
        self.medical_history_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0627\u0631\u06cc\u062e\u0686\u0647 \u067e\u0632\u0634\u06a9\u06cc",
                None,
            ),
        )
        self.has_gastrointestinal_disease_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06af\u0648\u0627\u0631\u0634\u06cc",
                None,
            ),
        )
        self.has_hypertension_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u0641\u0632\u0627\u06cc\u0634 \u0641\u0634\u0627\u0631\u062e\u0648\u0646",
                None,
            ),
        )
        self.has_special_conditions_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0628\u06cc\u0645\u0627\u0631\u06cc \u062e\u0627\u0635",
                None,
            ),
        )
        self.has_infectious_disease_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0639\u0641\u0648\u0646\u06cc",
                None,
            ),
        )
        self.has_diabetes_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062f\u06cc\u0627\u0628\u062a",
                None,
            ),
        )
        self.has_seizure_disorder_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0634\u0646\u062c",
                None,
            ),
        )
        self.has_pulmonary_disease_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u06cc\u0648\u06cc",
                None,
            ),
        )
        self.has_malignancy_history_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0628\u062f\u062e\u06cc\u0645\u06cc",
                None,
            ),
        )
        self.has_substance_abuse_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0648\u0621 \u0645\u0635\u0631\u0641 \u0645\u0648\u0627\u062f",
                None,
            ),
        )
        self.has_renal_disease_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u06a9\u0644\u06cc\u0648\u06cc",
                None,
            ),
        )
        self.has_cardiac_disease_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0642\u0644\u0628\u06cc",
                None,
            ),
        )
        self.has_disability_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0639\u0644\u0648\u0644\u06cc\u062a",
                None,
            ),
        )
        self.has_asthma_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0622\u0633\u0645",
                None,
            ),
        )
        self.has_stroke_history_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u06a9\u062a\u0647 \u0645\u063a\u0632\u06cc",
                None,
            ),
        )
        self.has_psychiatric_disorder_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0627\u062e\u062a\u0644\u0627\u0644 \u0631\u0648\u0627\u0646\u06cc",
                None,
            ),
        )
        self.has_prior_trauma_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0631\u0648\u0645\u0627",
                None,
            ),
        )
        self.has_surgical_history_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062c\u0631\u0627\u062d\u06cc",
                None,
            ),
        )
        self.other_medical_history_checkBox.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0627\u06cc\u0631",
                None,
            ),
        )
        self.current_medications_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062f\u0627\u0631\u0648\u0647\u0627\u06cc \u0641\u0639\u0644\u06cc:",
                None,
            ),
        )
        self.drug_allergies_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062d\u0633\u0627\u0633\u06cc\u062a \u062f\u0627\u0631\u0648\u06cc\u06cc:",
                None,
            ),
        )
        self.examine_eye_lung_heart_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0639\u0627\u06cc\u0646\u0647 \u0686\u0634\u0645\u060c \u0642\u0644\u0628 \u0648 \u0631\u06cc\u0647",
                None,
            ),
        )
        self.eye_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0645\u0631\u062f\u0645\u06a9",
                None,
            ),
        )
        self.right_eye_examine_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u0627\u0633\u062a",
                None,
            ),
        )
        self.left_eye_examine_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0686\u067e",
                None,
            ),
        )
        self.lung_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u06cc\u0647",
                None,
            ),
        )
        self.right_lung_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u0627\u0633\u062a",
                None,
            ),
        )
        self.lung_sound_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0645\u0639",
                None,
            ),
        )
        self.breathing_rhythm_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u06cc\u062a\u0645",
                None,
            ),
        )
        self.left_lung_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0686\u067e",
                None,
            ),
        )
        self.heart_group_box.setTitle(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0642\u0644\u0628",
                None,
            ),
        )
        self.heart_rhythm_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0631\u06cc\u062a\u0645",
                None,
            ),
        )
        self.heart_sound_label.setText(
            QCoreApplication.translate(
                "mission_details_tab",
                "\u0633\u0645\u0639",
                None,
            ),
        )
        self.mission_data_tab_widget.setTabText(
            self.mission_data_tab_widget.indexOf(self.history_and_trauma_tab),
            QCoreApplication.translate(
                "mission_details_tab",
                "\u062a\u0627\u0631\u06cc\u062e\u0686\u0647 \u0648 \u0645\u0639\u0627\u06cc\u0646\u0627\u062a",
                None,
            ),
        )

    # retranslateUi
