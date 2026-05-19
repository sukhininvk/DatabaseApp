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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableView, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.upperLeftLayout = QHBoxLayout()
        self.upperLeftLayout.setObjectName(u"upperLeftLayout")
        self.connectButton = QPushButton(self.verticalLayoutWidget)
        self.connectButton.setObjectName(u"connectButton")

        self.upperLeftLayout.addWidget(self.connectButton)

        self.refreshButton = QPushButton(self.verticalLayoutWidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.upperLeftLayout.addWidget(self.refreshButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.upperLeftLayout.addItem(self.horizontalSpacer)


        self.leftLayout.addLayout(self.upperLeftLayout)

        self.treeView = QTreeView(self.verticalLayoutWidget)
        self.treeView.setObjectName(u"treeView")
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
        self.upperRightLayout = QHBoxLayout()
        self.upperRightLayout.setObjectName(u"upperRightLayout")
        self.insertRowButton = QPushButton(self.verticalLayoutWidget_2)
        self.insertRowButton.setObjectName(u"insertRowButton")

        self.upperRightLayout.addWidget(self.insertRowButton)

        self.updateRowButton = QPushButton(self.verticalLayoutWidget_2)
        self.updateRowButton.setObjectName(u"updateRowButton")

        self.upperRightLayout.addWidget(self.updateRowButton)

        self.deleteRowButton = QPushButton(self.verticalLayoutWidget_2)
        self.deleteRowButton.setObjectName(u"deleteRowButton")

        self.upperRightLayout.addWidget(self.deleteRowButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.upperRightLayout.addItem(self.horizontalSpacer_2)


        self.rightLayout.addLayout(self.upperRightLayout)

        self.tableView = QTableView(self.verticalLayoutWidget_2)
        self.tableView.setObjectName(u"tableView")

        self.rightLayout.addWidget(self.tableView)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DatabaseApp", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.insertRowButton.setText(QCoreApplication.translate("MainWindow", u"Insert Row", None))
        self.updateRowButton.setText(QCoreApplication.translate("MainWindow", u"Update Row", None))
        self.deleteRowButton.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
    # retranslateUi

