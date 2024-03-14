# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1422, 754)
        self.setOneDriveProject_action = QAction(MainWindow)
        self.setOneDriveProject_action.setObjectName(u"setOneDriveProject_action")
        self.setServerProject_action = QAction(MainWindow)
        self.setServerProject_action.setObjectName(u"setServerProject_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.middle_vLayout = QVBoxLayout()
        self.middle_vLayout.setObjectName(u"middle_vLayout")
        self.upper_vSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.middle_vLayout.addItem(self.upper_vSpacer)

        self.remove_pushButton = QPushButton(self.frame)
        self.remove_pushButton.setObjectName(u"remove_pushButton")
        self.remove_pushButton.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(False)
        self.remove_pushButton.setFont(font)
        self.remove_pushButton.setStyleSheet(u"")

        self.middle_vLayout.addWidget(self.remove_pushButton)

        self.middle_vSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.middle_vLayout.addItem(self.middle_vSpacer)

        self.add_pushButton = QPushButton(self.frame)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMinimumSize(QSize(0, 60))
        self.add_pushButton.setFont(font)

        self.middle_vLayout.addWidget(self.add_pushButton)

        self.lower_vSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.middle_vLayout.addItem(self.lower_vSpacer)


        self.gridLayout.addLayout(self.middle_vLayout, 0, 1, 1, 1)

        self.action_hLayout = QHBoxLayout()
        self.action_hLayout.setObjectName(u"action_hLayout")
        self.cancel_pushButton = QPushButton(self.frame)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setMinimumSize(QSize(150, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setKerning(False)
        self.cancel_pushButton.setFont(font1)
        self.cancel_pushButton.setFocusPolicy(Qt.StrongFocus)
        self.cancel_pushButton.setAcceptDrops(False)

        self.action_hLayout.addWidget(self.cancel_pushButton)

        self.action_hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.action_hLayout.addItem(self.action_hSpacer)

        self.copyToServer_pushButton = QPushButton(self.frame)
        self.copyToServer_pushButton.setObjectName(u"copyToServer_pushButton")
        self.copyToServer_pushButton.setMinimumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.copyToServer_pushButton.setFont(font2)

        self.action_hLayout.addWidget(self.copyToServer_pushButton)


        self.gridLayout.addLayout(self.action_hLayout, 1, 0, 1, 3)

        self.summary_vLayout = QVBoxLayout()
        self.summary_vLayout.setObjectName(u"summary_vLayout")
        self.summary_label = QLabel(self.frame)
        self.summary_label.setObjectName(u"summary_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_label.sizePolicy().hasHeightForWidth())
        self.summary_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.summary_label.setFont(font3)

        self.summary_vLayout.addWidget(self.summary_label)

        self.summaryTable_treeWidget = QTreeWidget(self.frame)
        self.summaryTable_treeWidget.setObjectName(u"summaryTable_treeWidget")
        self.summaryTable_treeWidget.setLayoutDirection(Qt.LeftToRight)
        self.summaryTable_treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.summaryTable_treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.summaryTable_treeWidget.setIconSize(QSize(0, 0))

        self.summary_vLayout.addWidget(self.summaryTable_treeWidget)


        self.gridLayout.addLayout(self.summary_vLayout, 0, 2, 1, 1)

        self.assets_vLayout = QVBoxLayout()
        self.assets_vLayout.setObjectName(u"assets_vLayout")
        self.assets_label = QLabel(self.frame)
        self.assets_label.setObjectName(u"assets_label")
        sizePolicy.setHeightForWidth(self.assets_label.sizePolicy().hasHeightForWidth())
        self.assets_label.setSizePolicy(sizePolicy)
        self.assets_label.setFont(font3)

        self.assets_vLayout.addWidget(self.assets_label)

        self.assetBrowser_treeView = QTreeView(self.frame)
        self.assetBrowser_treeView.setObjectName(u"assetBrowser_treeView")
        self.assetBrowser_treeView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.assets_vLayout.addWidget(self.assetBrowser_treeView)


        self.gridLayout.addLayout(self.assets_vLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1422, 21))
        self.menuUser = QMenu(self.menubar)
        self.menuUser.setObjectName(u"menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuUser.menuAction())
        self.menuUser.addAction(self.setOneDriveProject_action)
        self.menuUser.addAction(self.setServerProject_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.setOneDriveProject_action.setText(QCoreApplication.translate("MainWindow", u"Set OneDrive Project...", None))
        self.setServerProject_action.setText(QCoreApplication.translate("MainWindow", u"Set Server Project...", None))
        self.remove_pushButton.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.copyToServer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Copy to Server", None))
        self.summary_label.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        ___qtreewidgetitem = self.summaryTable_treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Asset", None));
        self.assets_label.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.menuUser.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
    # retranslateUi

