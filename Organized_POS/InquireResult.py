# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InquireResult.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def keyCapture(self, eve):
        if QtCore.Qt.Key_Return == eve.key() or QtCore.Qt.Key_Escape:
            self.Dialog.hide()
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(350, 151)
        self.Dialog.keyPressEvent = self.keyCapture
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inquireName = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inquireName.setFont(font)
        self.inquireName.setAlignment(QtCore.Qt.AlignCenter)
        self.inquireName.setObjectName("inquireName")
        self.verticalLayout.addWidget(self.inquireName)
        self.inquirePrice = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.inquirePrice.setFont(font)
        self.inquirePrice.setStyleSheet("color: green;")
        self.inquirePrice.setAlignment(QtCore.Qt.AlignCenter)
        self.inquirePrice.setObjectName("inquirePrice")
        self.verticalLayout.addWidget(self.inquirePrice)
        self.inquireStock = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.inquireStock.setFont(font)
        self.inquireStock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inquireStock.setObjectName("inquireStock")
        self.verticalLayout.addWidget(self.inquireStock)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.inquireName.setText(_translate("Dialog", "Product Name"))
        self.inquirePrice.setText(_translate("Dialog", "0.00"))
        self.inquireStock.setText(_translate("Dialog", "In Stock: 50"))
import qt_resources_rc

