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
        ConnectionDialog.resize(350, 144)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectionDialog.sizePolicy().hasHeightForWidth())
        ConnectionDialog.setSizePolicy(sizePolicy)
        ConnectionDialog.setMinimumSize(QSize(350, 144))
        ConnectionDialog.setMaximumSize(QSize(350, 144))
        ConnectionDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ConnectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UpperLayout = QGridLayout()
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.HostnameLineEdit = QLineEdit(ConnectionDialog)
        self.HostnameLineEdit.setObjectName(u"HostnameLineEdit")

        self.UpperLayout.addWidget(self.HostnameLineEdit, 0, 1, 1, 1)

        self.UsernameLineEdit = QLineEdit(ConnectionDialog)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.UpperLayout.addWidget(self.UsernameLineEdit, 1, 1, 1, 1)

        self.PasswordLineEdit = QLineEdit(ConnectionDialog)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordLineEdit.setClearButtonEnabled(False)

        self.UpperLayout.addWidget(self.PasswordLineEdit, 2, 1, 1, 1)

        self.PasswordLabel = QLabel(ConnectionDialog)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.UpperLayout.addWidget(self.PasswordLabel, 2, 0, 1, 1)

        self.HostnameLabel = QLabel(ConnectionDialog)
        self.HostnameLabel.setObjectName(u"HostnameLabel")
        self.HostnameLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HostnameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.UpperLayout.addWidget(self.HostnameLabel, 0, 0, 1, 1)

        self.UsernameLabel = QLabel(ConnectionDialog)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        self.UsernameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.UpperLayout.addWidget(self.UsernameLabel, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.UpperLayout)

        self.LowerLayout = QHBoxLayout()
        self.LowerLayout.setObjectName(u"LowerLayout")
        self.LowerLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.HorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.LowerLayout.addItem(self.HorizontalSpacer)

        self.ConnectButton = QPushButton(ConnectionDialog)
        self.ConnectButton.setObjectName(u"ConnectButton")

        self.LowerLayout.addWidget(self.ConnectButton)

        self.CancelButton = QPushButton(ConnectionDialog)
        self.CancelButton.setObjectName(u"CancelButton")

        self.LowerLayout.addWidget(self.CancelButton)


        self.verticalLayout.addLayout(self.LowerLayout)


        self.retranslateUi(ConnectionDialog)

        QMetaObject.connectSlotsByName(ConnectionDialog)
    # setupUi

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(QCoreApplication.translate("ConnectionDialog", u"Connect to MySQL Server", None))
        self.PasswordLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Password:", None))
        self.HostnameLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Hostname:", None))
        self.UsernameLabel.setText(QCoreApplication.translate("ConnectionDialog", u"Username:", None))
        self.ConnectButton.setText(QCoreApplication.translate("ConnectionDialog", u"OK", None))
        self.CancelButton.setText(QCoreApplication.translate("ConnectionDialog", u"Cancel", None))
    # retranslateUi

