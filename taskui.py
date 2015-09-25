# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskui.ui'
#
# Created: Fri Sep 25 04:14:34 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(AddTask)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(AddTask)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameEdit = QtWidgets.QLineEdit(AddTask)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_2 = QtWidgets.QLabel(AddTask)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.descEdit = QtWidgets.QTextEdit(AddTask)
        self.descEdit.setObjectName("descEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.descEdit)
        self.btn = QtWidgets.QDialogButtonBox(AddTask)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn)

        self.retranslateUi(AddTask)
        self.btn.accepted.connect(AddTask.accept)
        self.btn.rejected.connect(AddTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Создание задачи"))
        self.label.setText(_translate("AddTask", "Название:"))
        self.label_2.setText(_translate("AddTask", "Описание:"))

