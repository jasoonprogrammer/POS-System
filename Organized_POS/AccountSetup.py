# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

class Ui_Form(object):
    def createAdmin(self):
        username = self.usernameEntry.text()
        password = self.passwordEntry.text()
        confirmPassword = self.confirmPasswordEntry.text()
        firstName = self.firstNameEntry.text()
        lastName = self.lastNameEntry.text()
        self.c.execute("select id from user where username = %s", (username, ))
        exist = self.c.fetchone()
        if len(username) < 5:
            self.showError("Length Error", "Username should be atleast 5 characters")
        elif len(password) < 5:
            self.showError("Length Error", "Password should be atleast 5 characters")
        elif len(firstName) < 3:
            self.showError("Length Error", "First Name must be atleast 3 characters")
        elif len(lastName) < 3:
            self.showError("Length Error", "Last Name must be atleast 3 characters")
        elif password != confirmPassword:
            self.showError("Password don't match", "Your passwords don't match")
        else:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encMessage = fernet.encrypt(password.encode())
            self.c.execute("INSERT INTO user (username, password, hash_key, first_name, last_name, is_admin) VALUES (%s, %s, %s, %s, %s, true)", (username, encMessage, key, firstName.title(), lastName.title()))
            self.conn.commit()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Admin Account Create")
            msg.setText("You can now use the account to login.")
            msg.exec_()
            del msg
            exit()
    def showError(self, title, body):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(body)
        msg.exec_()
        del msg

    def setupUi(self, Form, conn):
        self.conn = conn
        self.c = self.conn.cursor()
        Form.setObjectName("Form")
        Form.resize(367, 144)
        Form.closeEvent = lambda x: exit()
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {background-color: #198754; color: white; border-radius: 8px;} QPushButton:hover {background-color: #146C43, color: white; border-radius: 5px;}")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(130, 70, 98, 39))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.confirmPasswordLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.verticalLayout.addWidget(self.confirmPasswordLabel)
        self.confirmPasswordEntry = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmPasswordEntry.sizePolicy().hasHeightForWidth())
        self.confirmPasswordEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.confirmPasswordEntry.setFont(font)
        self.confirmPasswordEntry.setStyleSheet("padding-left: 5px;")
        self.confirmPasswordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordEntry.setObjectName("confirmPasswordEntry")
        self.verticalLayout.addWidget(self.confirmPasswordEntry)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 98, 39))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_2.addWidget(self.passwordLabel)
        self.passwordEntry = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordEntry.sizePolicy().hasHeightForWidth())
        self.passwordEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setStyleSheet("padding-left: 5px;")
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setObjectName("passwordEntry")
        self.verticalLayout_2.addWidget(self.passwordEntry)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(240, 20, 98, 39))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.usernameLabel = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout_3.addWidget(self.usernameLabel)
        self.usernameEntry = QtWidgets.QLineEdit(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameEntry.sizePolicy().hasHeightForWidth())
        self.usernameEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.usernameEntry.setFont(font)
        self.usernameEntry.setStyleSheet("padding-left: 5px;")
        self.usernameEntry.setObjectName("usernameEntry")
        self.verticalLayout_3.addWidget(self.usernameEntry)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(20, 20, 98, 39))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.firstNameLabel = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.verticalLayout_4.addWidget(self.firstNameLabel)
        self.firstNameEntry = QtWidgets.QLineEdit(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNameEntry.sizePolicy().hasHeightForWidth())
        self.firstNameEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.firstNameEntry.setFont(font)
        self.firstNameEntry.setStyleSheet("padding-left: 5px;")
        self.firstNameEntry.setObjectName("firstNameEntry")
        self.verticalLayout_4.addWidget(self.firstNameEntry)
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(130, 20, 98, 39))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lastNameLabel = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.verticalLayout_5.addWidget(self.lastNameLabel)
        self.lastNameEntry = QtWidgets.QLineEdit(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastNameEntry.sizePolicy().hasHeightForWidth())
        self.lastNameEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.lastNameEntry.setFont(font)
        self.lastNameEntry.setStyleSheet("padding-left: 5px;")
        self.lastNameEntry.setObjectName("lastNameEntry")
        self.verticalLayout_5.addWidget(self.lastNameEntry)
        self.firstNameEntry.setFocus()
        Form.setTabOrder(self.firstNameEntry, self.lastNameEntry)
        Form.setTabOrder(self.lastNameEntry, self.usernameEntry)
        Form.setTabOrder(self.usernameEntry, self.passwordEntry)
        Form.setTabOrder(self.passwordEntry, self.confirmPasswordEntry)
        Form.setTabOrder(self.confirmPasswordEntry, self.lastNameEntry)
        Form.setTabOrder(self.firstNameEntry, self.lastNameEntry)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.createAdmin)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Admin Account Create"))
        self.pushButton.setText(_translate("Form", "Create Account"))
        self.confirmPasswordLabel.setText(_translate("Form", "Confirm Password"))
        self.passwordLabel.setText(_translate("Form", "Password"))
        self.usernameLabel.setText(_translate("Form", "Username"))
        self.firstNameLabel.setText(_translate("Form", "First Name"))
        self.lastNameLabel.setText(_translate("Form", "Last Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
