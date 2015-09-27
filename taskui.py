# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskui.ui'
#
# Created: Sat Sep 26 08:07:07 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(400, 288)
        self.gridLayout = QtWidgets.QGridLayout(AddTask)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AddTask)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(AddTask)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddTask)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.descEdit = QtWidgets.QTextEdit(AddTask)
        self.descEdit.setObjectName("descEdit")
        self.gridLayout.addWidget(self.descEdit, 1, 1, 1, 1)
        self.btn = QtWidgets.QDialogButtonBox(AddTask)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 2, 1, 1, 1)

        self.retranslateUi(AddTask)
        self.btn.accepted.connect(AddTask.accept)
        self.btn.rejected.connect(AddTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Создание задачи"))
        self.label.setText(_translate("AddTask", "Название:"))
        self.label_2.setText(_translate("AddTask", "Описание:"))

