from PyQt5.QtCore import Qt
from Forms import FormWidgetTable, OnlyTableForm,Main
from PyQt5 import QtWidgets, QtCore,QtGui
from fielddict import *
import dbmanager as dbm
# pyuic5 Forms/name.ui -o Forms/name.py


class GUI_Common():
    cRow = -1
    def setColortoRow(self,table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def rowselection(self,):
        r = self.tableWidget.currentRow()

        self.setColortoRow(self.tableWidget, r, QtGui.QColor(0x6E86D6))
        if self.cRow != -1 and self.cRow !=r:

            self.setColortoRow(self.tableWidget, self.cRow, QtGui.QColor(0xFFFFFF))
        self.cRow = r
        if QtWidgets.QMainWindow in self.__class__.__bases__:
            self.statusBar().showMessage(f'Строка {r+1}')


class TableClass(GUI_Common):
    def FillTable(self,table):
        n, m = len(table[0]), len(table)

        self.tableWidget.setRowCount(m)
        for i in range(0, m):
            j = 0
            for cname in table[0].keys():
                item = QtWidgets.QTableWidgetItem(str(table[i][cname]))
                item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
                j += 1

    def SetUpTable(self, table):
        n, m = len(table[0]), len(table)
        self.tableWidget.setColumnCount(n)
        self.tableWidget.setHorizontalHeaderLabels(GetTupleOfFullName(table[0].keys()))
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.clicked.connect(self.rowselection)
        self.FillTable(table)


class FuncTable(QtWidgets.QMainWindow, FormWidgetTable.Ui_MainWindow,TableClass):
    sortdesc = False
    sorttype = 0

    def __init__(self, table, name):
        super().__init__()
        self.setupUi(self)

        self.sortbox.currentIndexChanged.connect(self.sort)
        self.sortbtn.clicked.connect(self.togglesort)

        self.setWindowTitle(name)
        self.SetUpTable(table)

    def sort(self,i):
        self.sorttype = i
        table = dbm.GetTableNir(self.sorttype,self.sortdesc)
        self.FillTable(table)
        # print(i)

    def togglesort(self):
        self.sortdesc = not self.sortdesc
        table = dbm.GetTableNir(self.sorttype,self.sortdesc)
        self.FillTable(table)

        if not self.sortdesc:
            self.sortbtn.setText("↑")
        else:
            self.sortbtn.setText("↓")
        # print("sort desc: "+str(self.sortdesc))


class OnlyTable(QtWidgets.QDialog, OnlyTableForm.Ui_Dialog, TableClass):
    def __init__(self, table,name):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(name)
        self.SetUpTable(table)
        # self.FillTable(table)


class MainWindow(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    windows = []

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)


        self.nir.triggered.connect(self.opennirtable)
        self.prog.triggered.connect(self.openprogtable)
        self.vuz.triggered.connect(self.openvuztable)
        self.closeaction.triggered.connect(app.closeAllWindows)

    # def closeApp(self):


    def opennirtable(self):
        nirTable = dbm.GetTableNir()
        window = FuncTable(nirTable, "Данные о НИР")
        window.show()
        self.windows.append(window)



    def openprogtable(self):
        table = dbm.GetProgTable()
        window = OnlyTable(table, "Данные о программах")
        window.show()

        self.windows.append(window)


    def openvuztable(self):
        table = dbm.GetVuzTable()
        window = OnlyTable(table, "Данные о вузах")
        window.show()
        self.windows.append(window)
      




