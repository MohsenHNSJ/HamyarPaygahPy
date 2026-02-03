# pylint: disable=C0114,E0611,W0611,C0115,C0103,R0205,C0116,R0915,C0301,W1406,W0201
# ruff: noqa: UP009, RUF100, F401, D100, N801, D101, N803, ANN001, UP004, N802, D102, ANN201,UP025,N806,PGH003,PLR0915, E501, Q003
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
        self.PromptLabel = QLabel(ServerConfigDialog)
        self.PromptLabel.setObjectName("PromptLabel")
        sizePolicy.setHeightForWidth(
            self.PromptLabel.sizePolicy().hasHeightForWidth(),
        )
        self.PromptLabel.setSizePolicy(sizePolicy)
        self.PromptLabel.setMinimumSize(QSize(400, 40))
        self.PromptLabel.setMaximumSize(QSize(400, 40))
        self.PromptLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.PromptLabel.setScaledContents(False)
        self.PromptLabel.setWordWrap(True)
        self.PromptLabel.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction,
        )

        self.verticalLayout.addWidget(self.PromptLabel)

        self.ServerAddressInput = QLineEdit(ServerConfigDialog)
        self.ServerAddressInput.setObjectName("ServerAddressInput")
        sizePolicy.setHeightForWidth(
            self.ServerAddressInput.sizePolicy().hasHeightForWidth(),
        )
        self.ServerAddressInput.setSizePolicy(sizePolicy)
        self.ServerAddressInput.setMinimumSize(QSize(380, 22))
        self.ServerAddressInput.setMaximumSize(QSize(390, 22))
        self.ServerAddressInput.setAutoFillBackground(False)
        self.ServerAddressInput.setInputMethodHints(
            Qt.InputMethodHint.ImhUrlCharactersOnly,
        )
        self.ServerAddressInput.setMaxLength(512)
        self.ServerAddressInput.setFrame(True)
        self.ServerAddressInput.setCursorMoveStyle(
            Qt.CursorMoveStyle.VisualMoveStyle,
        )
        self.ServerAddressInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.ServerAddressInput)

        self.InvalidInputLabel = QLabel(ServerConfigDialog)
        self.InvalidInputLabel.setObjectName("InvalidInputLabel")
        self.InvalidInputLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.InvalidInputLabel.sizePolicy().hasHeightForWidth(),
        )
        self.InvalidInputLabel.setSizePolicy(sizePolicy)
        self.InvalidInputLabel.setMinimumSize(QSize(400, 15))
        self.InvalidInputLabel.setMaximumSize(QSize(400, 15))
        font1 = QFont()
        font1.setFamilies(["Sans Serif"])
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.InvalidInputLabel.setFont(font1)
        self.InvalidInputLabel.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout.addWidget(self.InvalidInputLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize,
        )
        self.SaveButton = QPushButton(ServerConfigDialog)
        self.SaveButton.setObjectName("SaveButton")
        self.SaveButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout.addWidget(self.SaveButton)

        self.AbortButton = QPushButton(ServerConfigDialog)
        self.AbortButton.setObjectName("AbortButton")
        self.AbortButton.setMinimumSize(QSize(0, 0))
        self.AbortButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.AbortButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ServerConfigDialog)

        self.SaveButton.setDefault(True)

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
        self.PromptLabel.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "No server address available.\nEnter server address to continue:",
                None,
            ),
        )
        self.ServerAddressInput.setText("")
        self.ServerAddressInput.setPlaceholderText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "http://xxx.xxx.xxx.xxx/AsayarService/",
                None,
            ),
        )
        self.InvalidInputLabel.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                '<font color ="#FF0000">Server address invalid!</font>',
                None,
            ),
        )
        self.SaveButton.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "&Save",
                None,
            ),
        )
        self.AbortButton.setText(
            QCoreApplication.translate(
                "ServerConfigDialog",
                "&Abort",
                None,
            ),
        )

    # retranslateUi
