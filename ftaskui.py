# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ftaskui.ui'
#
# Created: Wed Sep 30 17:40:59 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFastTask(object):
    def setupUi(self, AddFastTask):
        AddFastTask.setObjectName("AddFastTask")
        AddFastTask.resize(360, 259)
        self.gridLayout = QtWidgets.QGridLayout(AddFastTask)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AddFastTask)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(AddFastTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.nameEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddFastTask)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.setPrior = QtWidgets.QComboBox(AddFastTask)
        self.setPrior.setMinimumSize(QtCore.QSize(30, 0))
        self.setPrior.setMaximumSize(QtCore.QSize(110, 16777215))
        self.setPrior.setBaseSize(QtCore.QSize(30, 0))
        self.setPrior.setObjectName("setPrior")
        self.setPrior.addItem("")
        self.setPrior.addItem("")
        self.setPrior.addItem("")
        self.gridLayout.addWidget(self.setPrior, 1, 1, 1, 1)
        self.btn = QtWidgets.QDialogButtonBox(AddFastTask)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 2, 1, 1, 1)

        self.retranslateUi(AddFastTask)
        self.setPrior.setCurrentIndex(1)
        self.btn.accepted.connect(AddFastTask.accept)
        self.btn.rejected.connect(AddFastTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFastTask)

    def retranslateUi(self, AddFastTask):
        _translate = QtCore.QCoreApplication.translate
        AddFastTask.setWindowTitle(_translate("AddFastTask", "Быстрое создание задачи"))
        self.label.setText(_translate("AddFastTask", "Название:"))
        self.label_2.setText(_translate("AddFastTask", "Приоритет:"))
        self.setPrior.setCurrentText(_translate("AddFastTask", "Средний"))
        self.setPrior.setItemText(0, _translate("AddFastTask", "Низкий"))
        self.setPrior.setItemText(1, _translate("AddFastTask", "Средний"))
        self.setPrior.setItemText(2, _translate("AddFastTask", "Высокий"))

