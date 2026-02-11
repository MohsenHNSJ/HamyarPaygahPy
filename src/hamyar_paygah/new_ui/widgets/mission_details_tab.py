# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201,C0302
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
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
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
        self.iranian_nationality_checkBox.setEnabled(False)
        self.iranian_nationality_checkBox.setMaximumSize(QSize(50, 22))
        self.iranian_nationality_checkBox.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.iranian_nationality_checkBox)

        self.foreign_nationality_checkBox = QCheckBox(
            self.information_section_1,
        )
        self.foreign_nationality_checkBox.setObjectName(
            "foreign_nationality_checkBox",
        )
        self.foreign_nationality_checkBox.setEnabled(False)
        self.foreign_nationality_checkBox.setMaximumSize(QSize(75, 20))

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
        self.is_male_checkBox.setEnabled(False)
        self.is_male_checkBox.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.is_male_checkBox)

        self.is_female_checkBox = QCheckBox(self.information_section_2)
        self.is_female_checkBox.setObjectName("is_female_checkBox")
        self.is_female_checkBox.setEnabled(False)
        self.is_female_checkBox.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.is_female_checkBox)

        self.is_gender_unknown_checkbox = QCheckBox(self.information_section_2)
        self.is_gender_unknown_checkbox.setObjectName(
            "is_gender_unknown_checkbox",
        )
        self.is_gender_unknown_checkbox.setEnabled(False)
        self.is_gender_unknown_checkbox.setMaximumSize(QSize(85, 16777215))

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
        self.is_vehicle_accident_checkBox.setEnabled(False)
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

        self.verticalLayout_2.addWidget(self.mission_data_tab_widget)

        self.retranslateUi(mission_details_tab)

        self.search_button.setDefault(True)
        self.mission_data_tab_widget.setCurrentIndex(0)

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

    # retranslateUi
