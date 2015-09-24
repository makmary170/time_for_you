#!/usr/bin/python3

# -*- coding: utf-8 -*-

from PyQt5 import QtSql
from os import path

class Task:
    def __init__(self, name, desc):

        self.name = name
        self.desc = desc
        
        connect = QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        connect.setDatabaseName(path.expanduser('~/tasks.db'))
        connect.open()
        cursor = QtSql.QSqlQuery(connect)
        cursor.exec('''CREATE TABLE if not exists Tasks
                          (Name text, Desc text)''')
 
        cursor.exec("INSERT INTO tasks VALUES ('%s','%s')" % (self.name, self.desc))
        
        connect.close()

if __name__ == "__main__":
    task1 = Task('test', 'test desc')
    print (task1.name)
    print (task1.desc)

        

