# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskui.ui'
#
# Created: Thu Sep 24 04:17:01 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddTask)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(AddTask)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 60, 171, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(AddTask)
        self.textEdit.setGeometry(QtCore.QRect(150, 130, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(AddTask)
        self.label.setGeometry(QtCore.QRect(60, 60, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddTask)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 81, 17))
        self.label_2.setObjectName("label_2")
        self.action343 = QtWidgets.QAction(AddTask)
        self.action343.setObjectName("action343")

        self.retranslateUi(AddTask)
        self.buttonBox.accepted.connect(AddTask.accept)
        self.buttonBox.rejected.connect(AddTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Dialog"))
        self.label.setText(_translate("AddTask", "Название:"))
        self.label_2.setText(_translate("AddTask", "Описание:"))
        self.action343.setText(_translate("AddTask", "343"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTask = QtWidgets.QDialog()
    ui = Ui_AddTask()
    ui.setupUi(AddTask)
    AddTask.show()
    sys.exit(app.exec_())

