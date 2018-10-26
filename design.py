# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 600))
        MainWindow.setBaseSize(QtCore.QSize(850, 600))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background:#4a4a50;\n"
"color:#f2f2f9\n"
"\n"
"\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.labelBefore = QtWidgets.QLabel(self.centralwidget)
        self.labelBefore.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.labelBefore.setFont(font)
        self.labelBefore.setObjectName("labelBefore")
        self.verticalLayout_3.addWidget(self.labelBefore, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setMouseTracking(False)
        self.listWidget.setStyleSheet("background:#f2f2f9;\n"
"color:#2b3237")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.labelAfter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.labelAfter.setFont(font)
        self.labelAfter.setObjectName("labelAfter")
        self.verticalLayout_3.addWidget(self.labelAfter, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.listWidgetAfter = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetAfter.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.listWidgetAfter.setFont(font)
        self.listWidgetAfter.setStyleSheet("background:#f2f2f9;\n"
"color:#2b3237")
        self.listWidgetAfter.setObjectName("listWidgetAfter")
        self.verticalLayout_3.addWidget(self.listWidgetAfter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowse.setStyleSheet("QPushButton {\n"
"background-color:#2e87e7;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color:#2b7ad0;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}")
        self.btnBrowse.setAutoDefault(False)
        self.btnBrowse.setDefault(False)
        self.btnBrowse.setFlat(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.verticalLayout.addWidget(self.btnBrowse)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер песен"))
        self.labelBefore.setText(_translate("MainWindow", "Список песен до редактирования"))
        self.labelAfter.setText(_translate("MainWindow", "Список песен после редактирования"))
        self.btnBrowse.setText(_translate("MainWindow", "Выбрать папку"))

