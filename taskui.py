# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskui.ui'
#
# Created: Fri Oct  2 06:29:41 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(339, 311)
        self.gridLayout_2 = QtWidgets.QGridLayout(AddTask)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(AddTask)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QtCore.QSize(240, 27))
        self.nameEdit.setMaximumSize(QtCore.QSize(16777215, 27))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btn = QtWidgets.QDialogButtonBox(AddTask)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn.setObjectName("btn")
        self.gridLayout_2.addWidget(self.btn, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(AddTask)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setBaseSize(QtCore.QSize(0, 0))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.setPrior = QtWidgets.QComboBox(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setPrior.sizePolicy().hasHeightForWidth())
        self.setPrior.setSizePolicy(sizePolicy)
        self.setPrior.setMinimumSize(QtCore.QSize(30, 0))
        self.setPrior.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setPrior.setBaseSize(QtCore.QSize(30, 0))
        self.setPrior.setObjectName("setPrior")
        self.setPrior.addItem("")
        self.setPrior.addItem("")
        self.setPrior.addItem("")
        self.gridLayout.addWidget(self.setPrior, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(AddTask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.retranslateUi(AddTask)
        self.setPrior.setCurrentIndex(1)
        self.btn.accepted.connect(AddTask.accept)
        self.btn.rejected.connect(AddTask.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Создать задачу"))
        self.label.setText(_translate("AddTask", "Название:"))
        self.label_3.setText(_translate("AddTask", "Описание:"))
        self.label_2.setText(_translate("AddTask", "Приоритет:"))
        self.label_6.setText(_translate("AddTask", "Категория:"))
        self.label_7.setText(_translate("AddTask", "Трудозатраты:"))
        self.setPrior.setCurrentText(_translate("AddTask", "Средний"))
        self.setPrior.setItemText(0, _translate("AddTask", "Низкий"))
        self.setPrior.setItemText(1, _translate("AddTask", "Средний"))
        self.setPrior.setItemText(2, _translate("AddTask", "Высокий"))
        self.label_5.setText(_translate("AddTask", "Дата окончания:"))
        self.label_4.setText(_translate("AddTask", "Дата начала:"))

