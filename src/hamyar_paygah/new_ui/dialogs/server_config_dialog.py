# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003, FBT003, ERA001
# mypy: ignore-errors
# type: ignore[all]
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'server_config_dialog.ui'
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
    QDialog,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_ServerConfigDialog:
    def setupUi(self, ServerConfigDialog):
        if not ServerConfigDialog.objectName():
            ServerConfigDialog.setObjectName("ServerConfigDialog")
        ServerConfigDialog.setWindowModality(
            Qt.WindowModality.ApplicationModal,
        )
        ServerConfigDialog.resize(400, 150)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            ServerConfigDialog.sizePolicy().hasHeightForWidth(),
        )
        ServerConfigDialog.setSizePolicy(sizePolicy)
        ServerConfigDialog.setMinimumSize(QSize(400, 150))
        ServerConfigDialog.setMaximumSize(QSize(418, 150))
        font = QFont()
        font.setFamilies(["Sans Serif"])
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        ServerConfigDialog.setFont(font)
        ServerConfigDialog.setContextMenuPolicy(
            Qt.ContextMenuPolicy.NoContextMenu,
        )
        ServerConfigDialog.setLocale(
            QLocale(QLocale.English, QLocale.UnitedStates),
        )
        ServerConfigDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ServerConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.prompt_label = QLabel(ServerConfigDialog)
        self.prompt_label.setObjectName("prompt_label")
        sizePolicy.setHeightForWidth(
            self.prompt_label.sizePolicy().hasHeightForWidth(),
        )
        self.prompt_label.setSizePolicy(sizePolicy)
        self.prompt_label.setMinimumSize(QSize(400, 40))
        self.prompt_label.setMaximumSize(QSize(400, 40))
        self.prompt_label.setTextFormat(Qt.TextFormat.PlainText)
        self.prompt_label.setScaledContents(False)
        self.prompt_label.setWordWrap(True)
        self.prompt_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.verticalLayout.addWidget(self.prompt_label)

        self.server_address_input = QLineEdit(ServerConfigDialog)
        self.server_address_input.setObjectName("server_address_input")
        sizePolicy.setHeightForWidth(
            self.server_address_input.sizePolicy().hasHeightForWidth(),
        )
        self.server_address_input.setSizePolicy(sizePolicy)
        self.server_address_input.setMinimumSize(QSize(380, 22))
        self.server_address_input.setMaximumSize(QSize(390, 22))
        self.server_address_input.setAutoFillBackground(False)
        self.server_address_input.setInputMethodHints(
            Qt.InputMethodHint.ImhUrlCharactersOnly,
        )
        self.server_address_input.setMaxLength(512)
        self.server_address_input.setFrame(True)
        self.server_address_input.setCursorMoveStyle(
            Qt.CursorMoveStyle.VisualMoveStyle,
        )
        self.server_address_input.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.server_address_input)

        self.invalid_input_label = QLabel(ServerConfigDialog)
        self.invalid_input_label.setObjectName("invalid_input_label")
        self.invalid_input_label.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.invalid_input_label.sizePolicy().hasHeightForWidth(),
        )
        self.invalid_input_label.setSizePolicy(sizePolicy)
        self.invalid_input_label.setMinimumSize(QSize(400, 15))
        self.invalid_input_label.setMaximumSize(QSize(400, 15))
        font1 = QFont()
        font1.setFamilies(["Sans Serif"])
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.invalid_input_label.setFont(font1)
        self.invalid_input_label.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout.addWidget(self.invalid_input_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize,
        )
        self.save_button = QPushButton(ServerConfigDialog)
        self.save_button.setObjectName("save_button")
        self.save_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.save_button)

        self.abort_button = QPushButton(ServerConfigDialog)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.setMinimumSize(QSize(0, 0))
        self.abort_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.abort_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ServerConfigDialog)

        self.save_button.setDefault(True)

        QMetaObject.connectSlotsByName(ServerConfigDialog)

    # setupUi

    def retranslateUi(self, ServerConfigDialog):
        ServerConfigDialog.setWindowTitle(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "Server configuration",
                None,
            ),
        )
        self.prompt_label.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "No server address available.\nEnter server address to continue:",
                None,
            ),
        )
        self.server_address_input.setText("")
        self.server_address_input.setPlaceholderText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "http://xxx.xxx.xxx.xxx/AsayarService/",
                None,
            ),
        )
        self.invalid_input_label.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                '<font color ="#FF0000">Server address invalid!</font>',
                None,
            ),
        )
        self.save_button.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "&Save",
                None,
            ),
        )
        self.abort_button.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "&Abort",
                None,
            ),
        )

    # retranslateUi
