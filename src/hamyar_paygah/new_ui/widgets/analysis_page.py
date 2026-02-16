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
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_analysis_page:
    def setupUi(self, analysis_page):
        if not analysis_page.objectName():
            analysis_page.setObjectName("analysis_page")
        analysis_page.resize(600, 600)
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

    # retranslateUi
