# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'query_editor_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_QueryEditorWindow(object):
    def setupUi(self, QueryEditorWindow):
        if not QueryEditorWindow.objectName():
            QueryEditorWindow.setObjectName(u"QueryEditorWindow")
        QueryEditorWindow.resize(800, 600)
        self.actionNew_Window = QAction(QueryEditorWindow)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.CentralWidget = QWidget(QueryEditorWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.CentralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UpperLayout = QVBoxLayout()
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.PlainTextEdit = QPlainTextEdit(self.CentralWidget)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        font.setPointSize(12)
        self.PlainTextEdit.setFont(font)
        self.PlainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.PlainTextEdit.setTabStopDistance(40.000000000000000)

        self.UpperLayout.addWidget(self.PlainTextEdit)


        self.verticalLayout_2.addLayout(self.UpperLayout)

        self.LowerLayout = QHBoxLayout()
        self.LowerLayout.setObjectName(u"LowerLayout")
        self.HorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.LowerLayout.addItem(self.HorizontalSpacer)

        self.ExecButton = QPushButton(self.CentralWidget)
        self.ExecButton.setObjectName(u"ExecButton")

        self.LowerLayout.addWidget(self.ExecButton)


        self.verticalLayout_2.addLayout(self.LowerLayout)

        QueryEditorWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(QueryEditorWindow)

        QMetaObject.connectSlotsByName(QueryEditorWindow)
    # setupUi

    def retranslateUi(self, QueryEditorWindow):
        QueryEditorWindow.setWindowTitle(QCoreApplication.translate("QueryEditorWindow", u"SQL Query Editor", None))
        self.actionNew_Window.setText(QCoreApplication.translate("QueryEditorWindow", u"New Window", None))
        self.ExecButton.setText(QCoreApplication.translate("QueryEditorWindow", u"Execute", None))
    # retranslateUi

