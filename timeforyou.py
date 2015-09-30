#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Main
from task import Task

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.workTask = Task(self.taskList)   # Передаем объект модели классу Task                     
        self.workTask.connect()               # для заполнения списка задач из БД
        self.fast_task_add_menu.triggered.connect(self.openTaskUI)
        self.workTask.genTasks() 
        
    def openTaskUI(self):
        self.workTask.exec()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    app.exec()

