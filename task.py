#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from taskui import Ui_AddTask

class Task(QtWidgets.QDialog, Ui_AddTask):
    
    def __init__(self, taskList):
        super().__init__()
        self.setupUi(self)
        self.btn.accepted.connect(lambda: self.createTask(self.nameEdit.text(), self.descEdit.toPlainText()))
        self.taskList = taskList # Объект модели списка класса Main. Делаем его атрибутом для вызова в функциях

    def connect(self):
        self.connectdb = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        self.connectdb.setDatabaseName(path.expanduser('~/tasks.db'))
        self.connectdb.open()
        self.query = QtSql.QSqlQuery(self.connectdb)
        
    def createTask(self, name, desc):
        self.query.exec('''CREATE TABLE if not exists tasks
                          (Name text, Desc text)''')
 
        self.query.exec("INSERT INTO tasks VALUES ('%s','%s')" % (name, desc))
        self.genTasks()
        
    def genTasks(self):
        self.query = QtSql.QSqlQuery("select Name from tasks", self.connectdb)
        if (self.taskList.rowCount() == 0): # Доп. проверка, чтобы не добавлять сущ. задачи. Если не равно 0, доб. последнее значение
            while (self.query.next()):
                self.taskList.appendRow(QtGui.QStandardItem(self.query.value("Name")))
        else:
            self.query.last()
            self.taskList.appendRow(QtGui.QStandardItem(self.query.value("Name")))
