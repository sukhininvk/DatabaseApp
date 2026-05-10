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
    QPushButton, QSizePolicy, QSplitter, QTableView,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.CentralWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Splitter = QSplitter(self.CentralWidget)
        self.Splitter.setObjectName(u"Splitter")
        self.Splitter.setOrientation(Qt.Orientation.Horizontal)
        self.verticalLayoutWidget = QWidget(self.Splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.LeftLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.LeftLayout.setObjectName(u"LeftLayout")
        self.LeftLayout.setContentsMargins(0, 0, 0, 0)
        self.UpperLeftLayout = QHBoxLayout()
        self.UpperLeftLayout.setObjectName(u"UpperLeftLayout")
        self.ConnectButton = QPushButton(self.verticalLayoutWidget)
        self.ConnectButton.setObjectName(u"ConnectButton")

        self.UpperLeftLayout.addWidget(self.ConnectButton)

        self.RefreshButton = QPushButton(self.verticalLayoutWidget)
        self.RefreshButton.setObjectName(u"RefreshButton")

        self.UpperLeftLayout.addWidget(self.RefreshButton)


        self.LeftLayout.addLayout(self.UpperLeftLayout)

        self.TreeView = QTreeView(self.verticalLayoutWidget)
        self.TreeView.setObjectName(u"TreeView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TreeView.sizePolicy().hasHeightForWidth())
        self.TreeView.setSizePolicy(sizePolicy)

        self.LeftLayout.addWidget(self.TreeView)

        self.Splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.Splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.RightLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.RightLayout.setObjectName(u"RightLayout")
        self.RightLayout.setContentsMargins(0, 0, 0, 0)
        self.UpperRightLayout = QHBoxLayout()
        self.UpperRightLayout.setObjectName(u"UpperRightLayout")
        self.InsertButton = QPushButton(self.verticalLayoutWidget_2)
        self.InsertButton.setObjectName(u"InsertButton")

        self.UpperRightLayout.addWidget(self.InsertButton)

        self.UpdateButton = QPushButton(self.verticalLayoutWidget_2)
        self.UpdateButton.setObjectName(u"UpdateButton")

        self.UpperRightLayout.addWidget(self.UpdateButton)

        self.DeleteButton = QPushButton(self.verticalLayoutWidget_2)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.UpperRightLayout.addWidget(self.DeleteButton)

        self.SQLQueryButton = QPushButton(self.verticalLayoutWidget_2)
        self.SQLQueryButton.setObjectName(u"SQLQueryButton")

        self.UpperRightLayout.addWidget(self.SQLQueryButton)


        self.RightLayout.addLayout(self.UpperRightLayout)

        self.TableView = QTableView(self.verticalLayoutWidget_2)
        self.TableView.setObjectName(u"TableView")

        self.RightLayout.addWidget(self.TableView)

        self.Splitter.addWidget(self.verticalLayoutWidget_2)

        self.horizontalLayout_2.addWidget(self.Splitter)

        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DatabaseApp", None))
        self.ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.RefreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.InsertButton.setText(QCoreApplication.translate("MainWindow", u"Insert Row", None))
        self.UpdateButton.setText(QCoreApplication.translate("MainWindow", u"Update Row", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
        self.SQLQueryButton.setText(QCoreApplication.translate("MainWindow", u"SQL Query", None))
    # retranslateUi

