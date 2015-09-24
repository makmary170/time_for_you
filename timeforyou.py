#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Main
from taskui import Ui_AddTask
from task import Task

class Main(QtWidgets.QMainWindow, Ui_Main, Ui_AddTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.task_add_menu.triggered.connect(self.openAddTask)

    def openAddTask(self):
        self.addtask = Ui_AddTask()
        self.addtask.ui = QtWidgets.QDialog()
        self.addtask.setupUi(self.addtask.ui)
        self.addtask.ui.show()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    app.exec()

