#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Main

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()

    #task1 = Task('test')
    task1 = QtGui.QStandardItem('hello')
    window.model.appendRow(task1)
    
    window.show()
    app.exec()

