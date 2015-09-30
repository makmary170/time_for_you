#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from ftaskui import Ui_AddFastTask

class Task(QtWidgets.QDialog, Ui_AddFastTask):
    
    def __init__(self, taskList):
        super().__init__()
        self.setupUi(self)
        self.btn.accepted.connect(lambda: self.createTask(self.nameEdit.text(), self.descEdit.toPlainText()))
        self.taskList = taskList # Объект списка класса Main. Делаем его атрибутом для вызова в функциях

    def connect(self):
        self.connectdb = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        self.connectdb.setDatabaseName(path.expanduser('~/tasks.db'))
        self.connectdb.open()
        self.query = QtSql.QSqlQuery(self.connectdb)
        self.query.exec('''CREATE TABLE if not exists tasks
                          (Name text, Desc text)''')
        
    def createTask(self, name, desc):
        if len(self.nameEdit.text()):
            self.query.exec("INSERT INTO tasks VALUES ('%s','%s')" % (name, desc))
            self.genTasks()
            self.close()
        else:
            self.textError = QtWidgets.QLabel(self)
            self.textError.setGeometry(QtCore.QRect(40, 120, 431, 20))
            self.textError.setObjectName("textError")
            self.textError.setText("<html><head/><body><p><span style=\" font-size:12pt; color:#e21414;\">Название должно содержать не менее 3-ех символов!</span></p></body></html>")
            self.textError.show()
        
    def genTasks(self):
        self.query = QtSql.QSqlQuery("select Name from tasks", self.connectdb)
        if (self.taskList.count() == 0): # Доп. проверка, чтобы не добавлять сущ. задачи. Если не равно 0, доб. последнее значение
            while (self.query.next()):
                self.taskItem = QtWidgets.QListWidgetItem(self.query.value("Name"))
                self.taskItem.setCheckState(QtCore.Qt.Unchecked)
                self.taskList.addItem(self.taskItem)
        else:
            self.query.last()
            self.taskItem = QtWidgets.QListWidgetItem(self.query.value("Name"))
            self.taskItem.setCheckState(QtCore.Qt.Unchecked)
            self.taskList.addItem(self.taskItem)
