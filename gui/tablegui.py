from gui.guimanager import *
from gui.onerecordgui import *
from fielddict import *
import dbmanager as dbm
from PyQt5.QtCore import Qt
from gui.Forms import FormWidgetTable, OnlyTableForm,Main
from PyQt5 import QtWidgets, QtCore,QtGui
# pyuic5 Forms/name.ui -o Forms/name.py

class TableClass():
    cRow = -1
    cRec = ("","")

    def setColortoRow(self,table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def rowselection(self):
        r = self.tableWidget.currentRow()
        self.selectirow(r)


    def selectirow(self,r):
        self.setColortoRow(self.tableWidget, r, QtGui.QColor(0x6E86D6))
        if self.cRow != -1 and self.cRow !=r:

            self.setColortoRow(self.tableWidget, self.cRow, QtGui.QColor(0xFFFFFF))
        self.cRow = r
        if QtWidgets.QMainWindow in self.__class__.__bases__:
            self.statusBar().showMessage(f'Строка {r+1}')
            self.cRec = (self.tableWidget.item(r, 0).text(),self.tableWidget.item(r, 1).text())
            print(self.cRec)

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
    dialog = None

    def __init__(self, table, name):
        super().__init__()
        self.setupUi(self)

        self.sortbox.currentIndexChanged.connect(self.sort)
        self.sortbtn.clicked.connect(self.togglesort)
        self.addbtn.clicked.connect(self.addrec)
        self.deletebtn.clicked.connect(self.removeRec)

        self.setWindowTitle(name)
        self.SetUpTable(table)

    def removeRec(self):
        window = RemoveRecord(self.cRec,self)
        window.show()
        self.dialog = window


    def findrec(self,prog,f):
        progs = self.tableWidget.findItems(prog, Qt.MatchExactly)
        progsind = tuple((pr.row()) for pr in progs)

        for i in progsind:
            if int(self.tableWidget.item(i,1).text())==f:
                print(i)
                self.selectirow(i)
                self.tableWidget.scrollToItem(self.tableWidget.item(i,0))
                return i




    def sort(self,i):
        self.sorttype = i

        table = dbm.GetTableNir(self.sorttype,self.sortdesc)
        self.FillTable(table)
        if self.cRec[1]!="":
            self.findrec(self.cRec[0],int(self.cRec[1]))
        # print(i)

    def addrec(self):
        # prog , f = "", 0
        window = AddRecord("Добавление записи",self)
        window.show()
        # window.parent = self
        self.dialog = window

    def togglesort(self):
        self.sortdesc = not self.sortdesc
        table = dbm.GetTableNir(self.sorttype,self.sortdesc)
        self.FillTable(table)
        self.findrec(self.cRec[0], self.cRec[1])

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