#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtSql

class FastTask(QtWidgets.QDialog):
    
    def __init__(self, gtdList, taskList, query, connectdb):
        super().__init__()
        uic.loadUi('ui/ftaskui.ui', self)
        self.btn.accepted.connect(lambda: self.createTask(self.nameEdit.text(), self.setPrior.currentText()))
        self.gtdList = gtdList # Объект списка класса Main. Делаем его атрибутом для вызова в функциях
        self.taskList = taskList
        self.query = query
        self.connectdb = connectdb
        
    def createTask(self, name, prior):
        if len(self.nameEdit.text()):
            self.query.exec("INSERT INTO tasks (Name, Priority)\
                            VALUES ('%s','%s')" % (name, prior))
            self.genGTDTasks()
            self.genAllTasks()
        
    def genGTDTasks(self):
        self.queryGTD = QtSql.QSqlQuery("select Name, Priority from tasks", self.connectdb)
        if (self.gtdList.count() == 0): # Доп. проверка, чтобы не добавлять сущ. задачи. Если не равно 0, доб. последнее значение (см. else
            while (self.queryGTD.next()):
                self.taskItem = QtWidgets.QListWidgetItem(self.queryGTD.value("Name"))
                self.priority = self.queryGTD.value("Priority")
                self.taskItem.setCheckState(QtCore.Qt.Unchecked)
                self.setTaskColor(self.taskItem, self.priority)
                self.gtdList.addItem(self.taskItem)
        else:
            self.queryGTD.last()
            self.taskItem = QtWidgets.QListWidgetItem(self.queryGTD.value("Name"))
            self.priority = self.queryGTD.value("Priority")
            self.taskItem.setCheckState(QtCore.Qt.Unchecked)
            self.setTaskColor(self.taskItem, self.priority)
            self.gtdList.addItem(self.taskItem)

    def genAllTasks(self):
        data = ["Name", "Desc", "Priority", "Category", "Start", "Deadline"]
        self.queryList = QtSql.QSqlQuery('select %s from tasks' % ', '.join(data), self.connectdb) # Из списка в строку с ,
        elements = QtSql.QSqlQuery('select count(*) from tasks', self.connectdb) # Кол-во записей в таблице БД
        elements.first()
        column = 0
        if (self.taskList.rowCount() == 0):
            self.taskList.setRowCount(elements.value(0)) # На основе кол-ва записей создаем кол-во строк в таблице задач
            
            while (self.queryList.next()):
                self.priority = self.queryList.value("Priority")
                for dataitem in data:
                    self.taskItem = QtWidgets.QTableWidgetItem(self.queryList.value(dataitem))
                    self.setTaskColor(self.taskItem, self.priority)
                    self.taskList.setItem(0, column, self.taskItem)
                    column+=1
        else:
            self.queryList.last()
            self.priority = self.queryList.value("Priority")
            needRow = self.taskList.rowCount() + 1 # Задаем общее число строк: кол-во существующих + 1
            self.taskList.setRowCount(needRow)
            for dataitem in data:
                    self.taskItem = QtWidgets.QTableWidgetItem(self.queryList.value(dataitem))
                    self.setTaskColor(self.taskItem, self.priority)
                    self.taskList.setItem(needRow - 1, column, self.taskItem) # -1, потому что нумерация с 0!
                    column+=1

    def setTaskColor(self, taskItem, priority):
        """Функция определения цвета на основе приоритета задачи. После определения добавляет item"""
        green = QtGui.QBrush(QtGui.QColor(96, 209, 39))
        orange = QtGui.QBrush(QtGui.QColor(243, 165, 52))
        red  = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        self.taskItem = taskItem
        if self.taskItem.__class__ == QtWidgets.QListWidgetItem:
            if priority == "Низкий":
                        self.taskItem.setForeground(green)
            elif priority == "Средний":
                        self.taskItem.setForeground(orange)
            elif priority == "Высокий":
                        self.taskItem.setForeground(red)
            
        elif self.taskItem.__class__ == QtWidgets.QTableWidgetItem:
            if priority == "Низкий":
                        self.taskItem.setBackground(green)
            elif priority == "Средний":
                        self.taskItem.setBackground(orange)
            elif priority == "Высокий":
                        self.taskItem.setBackground(red)
            
