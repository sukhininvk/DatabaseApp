# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        if not ConnectionDialog.objectName():
            ConnectionDialog.setObjectName(u"ConnectionDialog")
        ConnectionDialog.resize(350, 176)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectionDialog.sizePolicy().hasHeightForWidth())
        ConnectionDialog.setSizePolicy(sizePolicy)
        ConnectionDialog.setMinimumSize(QSize(350, 176))
        ConnectionDialog.setMaximumSize(QSize(350, 176))
        ConnectionDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ConnectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperLayout = QGridLayout()
        self.upperLayout.setObjectName(u"upperLayout")
        self.passwordLabel = QLabel(ConnectionDialog)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.upperLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)

        self.usernameLineEdit = QLineEdit(ConnectionDialog)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.upperLayout.addWidget(self.usernameLineEdit, 1, 1, 1, 1)

        self.hostnameLineEdit = QLineEdit(ConnectionDialog)
        self.hostnameLineEdit.setObjectName(u"hostnameLineEdit")

        self.upperLayout.addWidget(self.hostnameLineEdit, 0, 1, 1, 1)

        self.hostnameLabel = QLabel(ConnectionDialog)
        self.hostnameLabel.setObjectName(u"hostnameLabel")
        self.hostnameLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hostnameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.upperLayout.addWidget(self.hostnameLabel, 0, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(ConnectionDialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLineEdit.setClearButtonEnabled(False)

        self.upperLayout.addWidget(self.passwordLineEdit, 2, 1, 1, 1)

        self.usernameLabel = QLabel(ConnectionDialog)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.upperLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)

        self.databaseLineEdit = QLineEdit(ConnectionDialog)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")

        self.upperLayout.addWidget(self.databaseLineEdit, 3, 1, 1, 1)

        self.databaseLabel = QLabel(ConnectionDialog)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.upperLayout.addWidget(self.databaseLabel, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.upperLayout)

        self.lowerLayout = QHBoxLayout()
        self.lowerLayout.setObjectName(u"lowerLayout")
        self.lowerLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lowerLayout.addItem(self.horizontalSpacer)

        self.connectButton = QPushButton(ConnectionDialog)
        self.connectButton.setObjectName(u"connectButton")

        self.lowerLayout.addWidget(self.connectButton)

        self.cancelButton = QPushButton(ConnectionDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.lowerLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.lowerLayout)


        self.retranslateUi(ConnectionDialog)

        QMetaObject.connectSlotsByName(ConnectionDialog)
    # setupUi

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(QCoreApplication.translate("ConnectionDialog", u"Connect to MySQL Server", None))
        self.passwordLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Password:", None))
        self.hostnameLineEdit.setInputMask("")
        self.hostnameLineEdit.setPlaceholderText("")
        self.hostnameLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Hostname:", None))
        self.usernameLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Username:", None))
        self.databaseLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Database:", None))
        self.connectButton.setText(QCoreApplication.translate("ConnectionDialog", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("ConnectionDialog", u"Cancel", None))
    # retranslateUi

