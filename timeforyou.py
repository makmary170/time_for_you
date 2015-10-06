#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from os import path
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtSql
from task import FastTask

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.connect()
        self.fastTask = FastTask(self.gtdList, self.query, self.connectdb)   # Передаем объект модели классу Task                     
                   # для заполнения списка задач из БД
        #self.Task = Task(self.taskList)
        self.fast_task_add_menu.triggered.connect(self.openFastTaskUI)
        #self.task_add_menu.triggered.connect(self.openTaskUI)
        self.fastTask.genTasks()

    def connect(self):
        self.connectdb = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        self.connectdb.setDatabaseName(path.expanduser('~/tasks.db'))
        self.connectdb.open()
        self.query = QtSql.QSqlQuery(self.connectdb)
        self.query.exec('''CREATE TABLE if not exists tasks
                          (Name text, Desc text, Start text, Dedline text,
                           Priority text, Category text, Timework text)''')
        
    def openFastTaskUI(self):
        self.fastTask.exec()

    def openTaskUI(self):
        self.Task.exec()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    app.exec()

