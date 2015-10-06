#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtSql

class FastTask(QtWidgets.QDialog):
    
    def __init__(self, gtdList, taskList, query, connectdb):
        super().__init__()
        uic.loadUi('ui/ftaskui.ui', self)
        self.btn.accepted.connect(lambda: self.createTask(self.nameEdit.text(), self.setPrior.itemText))
        self.gtdList = gtdList # Объект списка класса Main. Делаем его атрибутом для вызова в функциях
        self.taskList = taskList
        self.query = query
        self.connectdb = connectdb
        
    def createTask(self, name, prior):
        if len(self.nameEdit.text()):
            self.query.exec("INSERT INTO tasks (Name, Priority)\
                            VALUES ('%s','%s')" % (name, prior))
            self.genTasks()
        
    def genTasks(self):
        self.queryGTD = QtSql.QSqlQuery("select Name from tasks", self.connectdb)
        if (self.gtdList.count() == 0): # Доп. проверка, чтобы не добавлять сущ. задачи. Если не равно 0, доб. последнее значение
            while (self.queryGTD.next()):
                self.taskItem = QtWidgets.QListWidgetItem(self.queryGTD.value("Name"))
                self.taskItem.setCheckState(QtCore.Qt.Unchecked)
                self.gtdList.addItem(self.taskItem)
        else:
            self.queryGTD.last()
            self.taskItem = QtWidgets.QListWidgetItem(self.queryGTD.value("Name"))
            self.taskItem.setCheckState(QtCore.Qt.Unchecked)
            self.gtdList.addItem(self.taskItem)

        #self.queryList = QtSql.QSqlQuery("select * from tasks", self.connectdb)
        #if (self.taskList.rowCount() == 0):
         #   while (self.queryList.next()):
          #      self.taskItem = QtWidgets.QTableWidgetItem(self.queryList.value("Name", "Desc", "Priority", "Group", "Start", "Deadline"))
           #     self.taskList.addItem(self.taskItem)
