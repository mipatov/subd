from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel
from Forms import FormViewTable
from Forms import FormWidgetTable
from PyQt5 import QtWidgets
from fieldDict import *


class TableViewWindow(QtWidgets.QMainWindow, FormViewTable.Ui_MainWindow):
    def __init__(self, table):
        super().__init__()
        self.setupUi(self)

        n, m = len(table[0]), len(table)

        model = QSqlTableModel(self)
        model.setTable("ntp")
        model.setHeaderData(0, Qt.Horizontal, "Id")
        model.setHeaderData(1, Qt.Horizontal, "Name")
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.select()

        self.tableView.setModel(model)

class TableWidgetWindow(QtWidgets.QMainWindow, FormWidgetTable.Ui_MainWindow):
    def __init__(self, table,name):
        super().__init__()
        self.setupUi(self)

        n, m = len(table[0]), len(table)

        self.setWindowTitle(name)

        self.tableWidget.setColumnCount(n)
        self.tableWidget.setRowCount(m)
        self.tableWidget.setHorizontalHeaderLabels(GetTupleOfFullName(table[0].keys()))
        self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.setColumnWidth(n-1,len(table[0]["NIR"])*5)

        for i in range(0, m):
            j = 0
            for cname in table[0].keys():
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][cname])))
                j += 1
