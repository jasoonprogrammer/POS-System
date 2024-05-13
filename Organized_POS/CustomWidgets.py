from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "test")

c = conn.cursor()


def isFloat(value) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def isInt(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


ARROW_UP = 16777235
ARROW_DOWN = 16777237
NUMPAD_PLUS = 43
NUMPAD_MINUS = 45

class HoverLabel(QtWidgets.QLabel):
    
    def setHover(self, eve):
        self.setPixmap(QtGui.QPixmap(self.hover_image))
    
    def setDefault(self, eve):
        self.setPixmap(QtGui.QPixmap(self.initial_image))

        
    def __init__(self, parent, initial_image, size, objectName, mount = None):
        super().__init__(parent)
        self.size = size
        self.initial_image = initial_image
        self.setScaledContents(True)
        self.hover_image = self.initial_image.replace(".png", "_Hovered.png")
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterEvent = self.setHover
        self.leaveEvent = self.setDefault
        self.setPixmap(QtGui.QPixmap(self.initial_image))
        self.setMinimumSize(QtCore.QSize(self.size[0], self.size[1]))
        self.setMaximumSize(QtCore.QSize(self.size[0], self.size[1]))
        self.setBaseSize(QtCore.QSize(self.size[0], self.size[1]))
        self.setObjectName(objectName)
        if mount != None:
            self.mount = mount
            self.mount.addWidget(self)

class CustomTableWidget(QtWidgets.QTableWidget):
    def addQty(self):
        row = self.currentRow()
        if row >= 0:
            qty = self.item(row, 3).text()
            qty = int(qty)
            qty += 1
            price = self.item(row, 2).text()
            total = float(price) * qty
            total = "{:,.2f}".format(total)
            align = QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
            qty_item = QtWidgets.QTableWidgetItem(str(qty))
            qty_item.setTextAlignment(align)
            total_item = QtWidgets.QTableWidgetItem(str(total))
            total_item.setTextAlignment(align)
            self.setItem(row, 3, qty_item)
            self.setItem(row, 5, total_item)

    def subQty(self):
        row = self.currentRow()
        if row >= 0:
            qty = self.item(row, 3).text()
            qty = int(qty)
            if qty > 1:
                qty -= 1
                price = self.item(row, 2).text()
                total = float(price) * qty
                total = "{:,.2f}".format(total)
                align = QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
                qty_item = QtWidgets.QTableWidgetItem(str(qty))
                qty_item.setTextAlignment(align)
                total_item = QtWidgets.QTableWidgetItem(str(total))
                total_item.setTextAlignment(align)
                self.setItem(row, 3, qty_item)
                self.setItem(row, 5, total_item)


    def keyCapture(self, eve, parent):
        if eve.key() == NUMPAD_PLUS:
            self.addQty()
        elif eve.key() == NUMPAD_MINUS:
            self.subQty()
        if eve.key() == ARROW_UP:
            currentRow = self.currentRow()
            if self.currentRow() < 0:
                self.setCurrentCell(self.rowCount() - 1, 1)
            else:
                self.setCurrentCell(self.currentRow() - 1, 1)
            parent.capturedKeys.clear()
        if eve.key() == ARROW_DOWN:
            row = self.currentRow()
            self.setCurrentCell(row + 1, 1)
            parent.capturedKeys.clear()
        parent.setOutput()
        if eve.key() == QtCore.Qt.Key_Escape:
            parent.barcodeArea.setFocus()
    def addItem(self, barcode, qty, parent):
        
        c.execute("SELECT name, price FROM product WHERE barcode = %s", (barcode,))
        result = c.fetchone()
        if result:
            row = self.rowCount()
            self.setRowCount(row + 1)
            total = qty * result[1]
            arr = [barcode, result[0], "{:,.2f}".format(result[1]), qty, 0, "{:,.2f}".format(total)]
            row_range = list(range(row))
            row_range.reverse()
            for r in row_range:
                for col in range(6):
                    if col == 1:
                        align = QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter
                    else:
                        align = QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
                    text = self.item(r, col).text()
                    item = QtWidgets.QTableWidgetItem(str(text))
                    item.setTextAlignment(align)
                    self.setItem(r + 1, col, item)
            for i, col in enumerate(arr):
                if i == 1:
                    align = QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter
                else:
                    align = QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
                item = QtWidgets.QTableWidgetItem(str(col))
                item.setTextAlignment(align)
                self.setItem(0, i, item)
            parent.setOutput()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Barcode not found")
            msg.setText("No product is registered with this barcode")
            msg.exec_()
            del msg

    def removeItem(self, parent):
        if self.rowCount() > 0:
            buttonReply = QtWidgets.QMessageBox.question(parent, 'Confirm Void', "Void this product from list?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                row = self.currentRow()
                self.removeRow(row)
                self.clearFocus()
                parent.barcodeArea.setFocus()
            del buttonReply
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("No more items")
            msg.setText("Can't remove from an empty table.")
            msg.exec_()
            del msg