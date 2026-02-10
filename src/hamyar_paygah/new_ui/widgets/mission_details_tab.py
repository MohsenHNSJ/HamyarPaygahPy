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
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
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

        self.horizontalLayout.addWidget(self.mission_id_line_edit)

        self.patient_id_label = QLabel(self.search_parameters)
        self.patient_id_label.setObjectName("patient_id_label")
        self.patient_id_label.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.patient_id_label)

        self.patient_id_line_edit = QLineEdit(self.search_parameters)
        self.patient_id_line_edit.setObjectName("patient_id_line_edit")
        self.patient_id_line_edit.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.patient_id_line_edit)

        self.search_button = QPushButton(self.search_parameters)
        self.search_button.setObjectName("search_button")
        self.search_button.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout.addWidget(self.search_button)

        self.verticalLayout_2.addWidget(self.search_parameters)

        self.mission_details = QVBoxLayout()
        self.mission_details.setObjectName("mission_details")
        self.mission_details.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint,
        )
        self.information_section = QWidget(mission_details_tab)
        self.information_section.setObjectName("information_section")
        self.information_section.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.information_section)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.patient_name_label = QLabel(self.information_section)
        self.patient_name_label.setObjectName("patient_name_label")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred,
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.patient_name_label.sizePolicy().hasHeightForWidth(),
        )
        self.patient_name_label.setSizePolicy(sizePolicy1)
        self.patient_name_label.setMaximumSize(QSize(55, 30))
        self.patient_name_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_2.addWidget(self.patient_name_label)

        self.patient_name_field = QLineEdit(self.information_section)
        self.patient_name_field.setObjectName("patient_name_field")
        self.patient_name_field.setMaximumSize(QSize(200, 22))
        self.patient_name_field.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.patient_name_field)

        self.age_label = QLabel(self.information_section)
        self.age_label.setObjectName("age_label")
        self.age_label.setMaximumSize(QSize(25, 30))
        self.age_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_2.addWidget(self.age_label)

        self.age_field = QLineEdit(self.information_section)
        self.age_field.setObjectName("age_field")
        self.age_field.setMaximumSize(QSize(100, 22))
        self.age_field.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.age_field)

        self.nationality_label = QLabel(self.information_section)
        self.nationality_label.setObjectName("nationality_label")
        self.nationality_label.setMaximumSize(QSize(30, 30))
        self.nationality_label.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout_2.addWidget(self.nationality_label)

        self.iranian_nationality_checkBox = QCheckBox(self.information_section)
        self.iranian_nationality_checkBox.setObjectName(
            "iranian_nationality_checkBox",
        )
        self.iranian_nationality_checkBox.setEnabled(False)
        self.iranian_nationality_checkBox.setMaximumSize(QSize(50, 22))
        self.iranian_nationality_checkBox.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.iranian_nationality_checkBox)

        self.foreign_nationality_checkBox = QCheckBox(self.information_section)
        self.foreign_nationality_checkBox.setObjectName(
            "foreign_nationality_checkBox",
        )
        self.foreign_nationality_checkBox.setEnabled(False)
        self.foreign_nationality_checkBox.setMaximumSize(QSize(75, 20))

        self.horizontalLayout_2.addWidget(self.foreign_nationality_checkBox)

        self.mission_details.addWidget(self.information_section)

        self.verticalLayout_2.addLayout(self.mission_details)

        self.retranslateUi(mission_details_tab)

        self.search_button.setDefault(True)

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

    # retranslateUi
