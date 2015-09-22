# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Sep 22 11:53:08 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(764, 545)
        self.centralWidget = QtWidgets.QWidget(Main)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(0, 50, 431, 431))
        self.tableView.setObjectName("tableView")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(440, 0, 321, 200))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(430, 260, 321, 221))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(570, 220, 61, 31))
        self.label.setObjectName("label")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralWidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1010, 270, 16, 211))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 161, 31))
        self.label_2.setObjectName("label_2")
        Main.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 764, 25))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menuBar)
        self.menu_6.setObjectName("menu_6")
        Main.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Main)
        self.mainToolBar.setObjectName("mainToolBar")
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(Main)
        self.action.setObjectName("action")
        self.menu_3.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu_6.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.label.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#345abc;\">GTD</span></p></body></html>"))
        self.label_2.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#345abc;\">Расписание</span></p></body></html>"))
        self.menu.setTitle(_translate("Main", "Файл"))
        self.menu_2.setTitle(_translate("Main", "Правка"))
        self.menu_3.setTitle(_translate("Main", "Задачи"))
        self.menu_4.setTitle(_translate("Main", "Помощь"))
        self.menu_5.setTitle(_translate("Main", "Категории"))
        self.menu_6.setTitle(_translate("Main", "Дневник"))
        self.action.setText(_translate("Main", "Добавить задачу"))

