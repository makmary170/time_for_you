#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sqlite3, os
from os import path

class Task:
    def __init__(self, name, desc):

        self.name = name
        self.desc = desc
        
        connect = sqlite3.connect(path.expanduser('~/tasks.db'))
        cursor = connect.cursor()
        cursor.execute('''CREATE TABLE if not exists Tasks
                          (Name text, Desc text)''')
 
        cursor.execute("INSERT INTO tasks VALUES ('%s','%s')" % (self.name, self.desc))
        
        connect.commit()
        connect.close()

if __name__ == "__main__":
    task1 = Task('test', 'test desc')
    print (task1.name)
    print (task1.desc)

        

