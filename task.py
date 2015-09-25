#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from taskui import Ui_AddTask
from os import path

class AddTask(QtWidgets.QDialog, Ui_AddTask):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.accepted.connect(lambda: self.createTask(self.nameEdit.text(), self.descEdit.toPlainText()))
        
    def createTask(self, name, desc):
        connectdb = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        connectdb.setDatabaseName(path.expanduser('~/tasks.db'))
        connectdb.open()
        cursor = QtSql.QSqlQuery(connectdb)
        cursor.exec('''CREATE TABLE if not exists Tasks
                          (Name text, Desc text)''')
 
        cursor.exec("INSERT INTO tasks VALUES ('%s','%s')" % (name, desc))
        
        connectdb.close()

        

