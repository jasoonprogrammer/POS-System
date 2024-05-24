# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAction.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector, datetime
import LoginForm, ProductRegistrationMain, InventoryManagement, AccountManagement, ReportGeneration, AccountSetup, DatabaseCreate
from cryptography.fernet import Fernet
class Ui_Form(object):
    def showReportGeneration(self):
        ReportGenerationWidget.show()
        Form.hide()

    def showAccountManagement(self):
        AccountManagementWidget.show()
        Form.hide()

    def showDeliveryRecorder(self):
        InventoryManagementWidget.show()
        InventoryManagement_ui.setTable()
        Form.hide()

    def showProductRegistration(self):
        ProductRegistrationWidget.show()
        ProductRegistration_ui.setTable()
        Form.hide()
    def setupUi(self, Form, conn):
        self.conn = conn
        self.c = self.conn.cursor()
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(676, 209)
        self.label = QtWidgets.QLabel()
        self.widget = QtWidgets.QWidget(self.Form)
        self.widget.setGeometry(QtCore.QRect(50, 30, 571, 131))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("QtIcons/AccountManagement.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent = lambda x: self.showAccountManagement()
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("QtIcons/DeliveryRecording.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = lambda x: self.showDeliveryRecorder()
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("QtIcons/ProductManagement.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent = lambda x: self.showProductRegistration()
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("QtIcons/ReportGeneration.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.mousePressEvent = lambda x: self.showReportGeneration()
        self.horizontalLayout.addWidget(self.label_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Admin Action"))


if __name__ == "__main__":
    import sys
    import os
    from dotenv import load_dotenv
    app = QtWidgets.QApplication(sys.argv)
    if datetime.datetime.now() >= datetime.datetime(month = 6, day = 3, year = 2024):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Trial Expired")
        msg.setText("Please contact developer")
        msg.exec_()
        del msg
        sys.exit()
    else:
        load_dotenv()
        conn = DatabaseCreate.setupConnection()
        if not conn:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Connection Error")
            msg.setText("Please start your localhost")
            msg.exec_()
            sys.exit()

        c = conn.cursor()
        c.execute("SELECT * from user where is_admin = True")
        result = c.fetchone()
        if not result:
            AccountSetupWidget = QtWidgets.QWidget()
            AccountSetup_ui = AccountSetup.Ui_Form()
            AccountSetup_ui.setupUi(AccountSetupWidget, conn)
            AccountSetupWidget.show()
        else:
            Form = QtWidgets.QWidget()
            ui = Ui_Form()
            ui.setupUi(Form, conn)
            LoginFormWidget = QtWidgets.QWidget()
            LoginForm_ui = LoginForm.Ui_Form()
            LoginForm_ui.setupUi(LoginFormWidget, Form, ui, is_admin = True)
            LoginFormWidget.show()
            ProductRegistrationWidget = QtWidgets.QMainWindow()
            ProductRegistration_ui = ProductRegistrationMain.Ui_MainWindow()
            ProductRegistration_ui.setupUi(ProductRegistrationWidget, ui)
            InventoryManagementWidget = QtWidgets.QWidget()
            InventoryManagement_ui = InventoryManagement.Ui_Form()
            InventoryManagement_ui.setupUi(InventoryManagementWidget, ui)
            AccountManagementWidget = QtWidgets.QWidget()
            AccountManagement_ui = AccountManagement.Ui_Form()
            AccountManagement_ui.setupUi(AccountManagementWidget, ui)
            ReportGenerationWidget = QtWidgets.QWidget()
            ReportGeneration_ui = ReportGeneration.Ui_Form()
            ReportGeneration_ui.setupUi(ReportGenerationWidget, ui)



    # Form.show()
    sys.exit(app.exec_())