# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def checkBind(self, eve):
        if eve.key() == QtCore.Qt.Key_Return:
            self.selectProduct()

    def selectProduct(self):
        curr_row = self.searchTable.currentRow()
        if curr_row == -1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("No item selected")
            msg.setText("Please select a product to add to the list")
            msg.exec_()
            del msg
        else:
            buttonReply = QtWidgets.QMessageBox.question(self.Form, 'Hold this sale?', "Add this product?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                barcode = self.searchTable.item(curr_row, 0).text()
                self.parent.productTable.addItem(barcode, 1, self.parent)
                self.parent.productTable.setCurrentCell(0, 1)
                self.Form.hide()
                self.searchArea.setText("")
                self.searchArea.setFocus()
                    
    def searchProduct(self):
        val = self.searchArea.text()
        self.c.execute(f"SELECT barcode, name, price, stock FROM product WHERE barcode LIKE '%{val}%' or name LIKE '%{val}%'")
        results = self.c.fetchall()
        self.searchTable.setRowCount(len(results))
        for i, result in enumerate(results):
            for col in range(4):
                if col == 1 or col == 0:
                    align = QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter
                else:
                    align = QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
                item = QtWidgets.QTableWidgetItem(str(result[col]))
                item.setTextAlignment(align)
                self.searchTable.setItem(i, col, item)
    def setupUi(self, Form, c, parent):
        self.parent = parent
        self.c = c
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.setFixedSize(702, 350)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 680, 320))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.searchLabel.setFont(font)
        self.searchLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchArea = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchArea.sizePolicy().hasHeightForWidth())
        self.searchArea.setBaseSize(QtCore.QSize(0, 30))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchArea.setFont(font)
        self.searchArea.setText("")
        self.searchArea.setObjectName("searchArea")
        self.searchArea.textChanged.connect(self.searchProduct)
        self.horizontalLayout.addWidget(self.searchArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.searchTable = QtWidgets.QTableWidget(self.layoutWidget)
        self.searchTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.searchTable.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        self.searchTable.verticalHeader().hide()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchTable.setFont(font)
        self.searchTable.setObjectName("searchTable")
        self.searchTable.setColumnCount(4)
        self.searchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(3, item)
        self.searchTable.setColumnWidth(0, 90)
        self.searchTable.setColumnWidth(1, 390)
        self.searchTable.setColumnWidth(2, 90)
        self.searchTable.setColumnWidth(3, 90)
        self.searchTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.verticalLayout.addWidget(self.searchTable)
        self.searchTable.doubleClicked.connect(self.selectProduct)
        self.searchTable.setRowCount(0)
        self.searchTable.keyPressEvent = self.checkBind
        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.searchProduct()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Product Search"))
        self.searchLabel.setText(_translate("Form", "Search Product:"))
        self.searchArea.setPlaceholderText(_translate("Form", "Barcode or Name Here"))
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Barcode"))
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Description"))
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Price"))
        item = self.searchTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
