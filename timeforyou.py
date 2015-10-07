#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtSql
from task import FastTask

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.data = QtCore.QDir(QtCore.QDir.homePath() + "/.config/")
        self.data.mkdir("timeforyou")
        self.connect()
        self.fastTask = FastTask(self.gtdList, self.taskList, self.query, self.connectdb)
        self.fast_task_add_menu.triggered.connect(self.openFastTaskUI)
        self.add_fast_task_bar.triggered.connect(self.openFastTaskUI)
        self.fastTask.genGTDTasks()
        self.fastTask.genAllTasks()

    def connect(self):
        self.connectdb = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        self.connectdb.setDatabaseName(self.data.path() + "/timeforyou/tasks.db")
        self.connectdb.open()
        self.query = QtSql.QSqlQuery(self.connectdb)
        self.query.exec('''CREATE TABLE if not exists tasks
                          (Name text, Desc text, Start text, Deadline text,
                           Priority text, Category text, Timework text)''')
        
    def openFastTaskUI(self):
        self.fastTask.exec()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    app.exec()
    if app.aboutToQuit:
            mainwindow.connectdb.close()
