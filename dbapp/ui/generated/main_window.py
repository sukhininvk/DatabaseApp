# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSplitter,
    QTableWidget, QTableWidgetItem, QTreeView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionFetch = QAction(MainWindow)
        self.actionFetch.setObjectName(u"actionFetch")
        self.actionFetch.setEnabled(False)
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.actionDisconnect.setEnabled(False)
        self.actionDeleteRow = QAction(MainWindow)
        self.actionDeleteRow.setObjectName(u"actionDeleteRow")
        self.actionDeleteRow.setEnabled(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.leftLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.verticalLayoutWidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy1)

        self.leftLayout.addWidget(self.treeView)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.rightLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)

        self.rightLayout.addWidget(self.tableWidget)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 33))
        self.menuDatabase = QMenu(self.menuBar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuDatabase.menuAction())
        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionFetch)
        self.menuDatabase.addAction(self.actionDisconnect)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DatabaseApp", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect to Server", None))
        self.actionFetch.setText(QCoreApplication.translate("MainWindow", u"Fetch Databases", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.actionDeleteRow.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
    # retranslateUi

