#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Main
from task import AddTask

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.task_add_menu.triggered.connect(self.openTaskUI)

    def openTaskUI(self):
        self.addtask = AddTask()
        self.addtask.ui = QtWidgets.QDialog()
        self.addtask.setupUi(self.addtask.ui)
        self.addtask.ui.show()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    app.exec()

