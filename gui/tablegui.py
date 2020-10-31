from gui.guimanager import *
from gui.onerecordgui import *
from fielddict import *
import dbmanager as dbm
from PyQt5.QtCore import Qt
from gui.Forms import FormTableWidget, OnlyTableForm,FilterForm
from PyQt5 import QtWidgets, QtCore,QtGui
# pyuic5 Forms/name.ui -o Forms/name.py

class TableClass():
    cRow = -1
    cRec = ("","")
    wparent = None

    def setColortoRow(self,table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def rowselection(self):
        r = self.tableWidget.currentRow()
        self.selectirow(r)


    def selectirow(self,r):
        try:
            self.setColortoRow(self.tableWidget, r, QtGui.QColor(0x6E86D6))
            if self.cRow != -1 and self.cRow !=r:
                self.setColortoRow(self.tableWidget, self.cRow, QtGui.QColor(0xFFFFFF))
            self.cRow = r
            if QtWidgets.QMainWindow in self.__class__.__bases__:
                self.statusBar().showMessage(f'Строка {r+1}')
                self.cRec = (self.tableWidget.item(r, 0).text(),self.tableWidget.item(r, 1).text())
                # print(self.cRec)
        except BaseException:
            print("something wrong! try again")
            return

    def FillTable(self,table):
        if len(table) ==0:
            print("empty table")
            self.tableWidget.setRowCount(0)
            return

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
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.clicked.connect(self.rowselection)
        self.FillTable(table)

    def closeEvent(self, event):
        print(dir(self.wparent))
        if "mdi" in dir(self.wparent):
            self.wparent.mdi.closeAllSubWindows()




class FuncTable(QtWidgets.QMainWindow, FormTableWidget.Ui_MainWindow,TableClass):
    # sortdesc = False
    # sorttype = 0
    # filter = {}
    # dialog = None


    def __init__(self, table, name,wparent = None):
        super().__init__()
        self.setupUi(self)
        self.sortdesc = False
        self.sorttype = 0
        self.filter = {}
        self.dialog = None
        self.wparent = wparent

        self.sortbox.currentIndexChanged.connect(self.sort)
        self.sortbtn.clicked.connect(self.togglesort)
        self.addbtn.clicked.connect(self.addrec)
        self.editbtn.clicked.connect(self.editrec)
        self.deletebtn.clicked.connect(self.removeRec)
        self.filterbtn.clicked.connect(self.setFilter)

        self.setupanalys()

        self.setWindowTitle(name)
        self.SetUpTable(table)

    def setFilter(self):
        window = Filter(self)
        window.show()
        self.dialog = window

    def removeRec(self):
        if self.selectioncheck():
            return
        window = RemoveRecord(self.cRec,self)
        window.show()
        self.dialog = window

    def findrec(self,prog,f):
        progs = self.tableWidget.findItems(prog, Qt.MatchExactly)
        progsind = tuple((pr.row()) for pr in progs)
        print("find " + prog + str(f))
        for i in progsind:
            if int(self.tableWidget.item(i,1).text())==f:
                # print(i)
                self.selectirow(i)
                self.tableWidget.scrollToItem(self.tableWidget.item(i,0))
                return i

    def sort(self,i):
        self.sorttype = i

        table = dbm.GetTableNir(self.sorttype,self.sortdesc,self.filter)
        self.FillTable(table)
        if self.cRec[1]!="":
            self.findrec(self.cRec[0],int(self.cRec[1]))
        # print(i)

    def addrec(self):
        window = AddRecord(self)
        window.show()
        self.dialog = window

    def editrec(self):
        if self.selectioncheck():
            return
        window = EditRecord(self)
        window.show()
        self.dialog = window

    def selectioncheck(self):
        if self.cRow ==-1:
            self.statusBar().showMessage(f'Выберите запись!')
        return self.cRow ==-1

    def togglesort(self):
        self.sortdesc = not self.sortdesc
        table = dbm.GetTableNir(self.sorttype,self.sortdesc,self.filter)
        self.FillTable(table)
        if self.cRec[1] != "":
            self.findrec(self.cRec[0],int(self.cRec[1]))

        if not self.sortdesc:
            self.sortbtn.setText("↑")
        else:
            self.sortbtn.setText("↓")

    def setupanalys(self):
        # self.parent.analys1.triggered.connect(self.opennirtable)
        # self.parent.analys2.triggered.connect(self.openprogtable)
        self.wparent.analys3.triggered.connect(self.openanalis3table)

        self.wparent.analys1.setEnabled(False)
        self.wparent.analys2.setEnabled(False)
        self.wparent.analys3.setEnabled(True)

    def openanalis3table(self):
        fulltype = {"Ф":"Фундаментальное исследование","П":"Прикладное исседование","Р":"Экспериментальная разработка"}
        table = dbm.GetAnalisTable(0)
        for row in table:
            row["Тип"] = fulltype[row["Тип"]]

        window = OnlyTable(table, self.wparent.analys3.text(),self)
        window.tableWidget.resizeColumnsToContents()
        window.show()

        self.dialog = window

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # self.filter = {}
        self.wparent.mdi.closeAllSubWindows()
        self.wparent.analys1.setEnabled(False)
        self.wparent.analys2.setEnabled(False)
        self.wparent.analys3.setEnabled(False)

        if self.dialog:
            self.dialog.close()


class OnlyTable(QtWidgets.QDialog, OnlyTableForm.Ui_Dialog, TableClass):
    def __init__(self, table,name,wparent = None):
        super().__init__()
        self.setupUi(self)
        self.wparent = wparent
        self.setWindowTitle(name)
        self.title.setText(name)
        self.SetUpTable(table)

        
class Filter(QtWidgets.QDialog, FilterForm.Ui_Dialog,):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent


        self.applybtn.clicked.connect(self.applyFilter)
        self.discardbtn.clicked.connect(self.discardFilter)

        self.prog.addItem("")
        self.prog.addItems(dbm.GetProgTuple())

        self.allowgeocombo = True

        self.setupGeofilter()

        self.prog.currentTextChanged.connect(self.checkEnableButtons)
        self.checkprog.stateChanged.connect(self.checkEnableButtons)


        if parent.filter != {}: # заполнение формы текущим фильтром
            if "prog" in parent.filter.keys():
                self.checkprog.setCheckState(Qt.CheckState(2))
                self.prog.setCurrentText(parent.filter["prog"])

        self.checkEnableButtons()

        if self.canApply():
            self.applybtn.setEnabled(True)

    def setupGeofilter(self):
        combo = [self.fedokrug,self.subj,self.city,self.vuz]
        keys = ["region","oblname","city","z2"]
        self.geodict = dict(zip(keys,combo))

        for cmb in self.geodict.values(): # пустые строки в комбо
            cmb.addItem("")


        self.geoinfo = dbm.GetFullGeoinfo()

        for key,cmb in self.geodict.items():# заполнение без ограничений
            cmb.addItems(sorted(self.geoinfo[key]))


        self.fedokrug.currentIndexChanged.connect(self.changefedokrug)
        self.subj.currentIndexChanged.connect(self.changesubj)
        self.city.currentIndexChanged.connect(self.changecity)
        self.vuz.currentIndexChanged.connect(self.changevuz)
        self.checkgeo.stateChanged.connect(self.checkEnableButtons)

        if self.parent.filter != {}: # заполнение формы текущим фильтром
            if "geo" in self.parent.filter.keys():
                self.checkgeo.setCheckState(Qt.CheckState(2))
                gfltr = self.parent.filter['geo']
                for i in range(len(gfltr)):
                    cmb = list(self.geodict.values())[i]
                    key = list(self.geodict.keys())[i]
                    cmb.setCurrentText(gfltr[key])

    def changefedokrug(self):
        if not self.allowgeocombo:
            return
        self.geoinfo = dbm.GetGeoinfo("region",self.fedokrug.currentText())
        self.refillGeofilter(0)


    def changesubj(self):
        if not self.allowgeocombo:
            return
        self.geoinfo = dbm.GetGeoinfo("oblname",self.subj.currentText())
        self.refillGeofilter(1)


    def changecity(self):
        if not self.allowgeocombo:
            return
        self.geoinfo = dbm.GetGeoinfo("city",self.city.currentText())
        self.refillGeofilter(2)


    def changevuz(self):
        if not self.allowgeocombo:
            return
        self.geoinfo = dbm.GetGeoinfo("z2",self.vuz.currentText())
        self.refillGeofilter(3)

    def refillGeofilter(self,i):
        """i - номер комбобокса, который изменен"""

        self.allowgeocombo = False
        # if self.fedokrug.currentText() !="":


        fullgeoinfo = dbm.GetFullGeoinfo()

        for cmb in self.geodict.values(): # очистка комбо
            cmb.clear()

        geofltr = {}

        for j in range(4):
            cmb = list(self.geodict.values())[j]
            key = list(self.geodict.keys())[j]
            if j<=i :
                # cmb.addItem("")
                cmb.addItems(sorted(fullgeoinfo[key]))
                cmb.setCurrentText(list(self.geoinfo[key])[0])
                geofltr[key] = cmb.currentText()
            else:
                cmb.addItem("")
                cmb.addItems(sorted(self.geoinfo[key]))


        self.parent.filter['geo'] = geofltr

        self.allowgeocombo = True

        self.checkEnableButtons()


    def fillGeofilter(self):
        # self.fedokrug.clear()
        # self.subj.clear()
        # self.city.clear()
        # self.vuz.clear()
        pass


    def applyFilter(self):
        if self.checkprog.checkState() == 2 and self.prog.currentText() != "":
            self.parent.filter["prog"] = self.prog.currentText()

        if self.checkprog.checkState() == 0 and "prog" in self.parent.filter.keys():
            self.parent.filter.pop("prog")

        if self.checkgeo.checkState() == 0 and "geo" in self.parent.filter.keys():
            self.parent.filter.pop("geo")

        print("filter apply -> " + str(self.parent.filter))

        if self.parent.filter == {}:
            return

        self.fillTable(self.parent.filter)
        self.close()

    def checkEnableButtons(self):
        self.applybtn.setEnabled(self.canApply())
        self.discardbtn.setEnabled(bool(self.parent.filter))


    def discardFilter(self):
        self.checkprog.setCheckState(Qt.CheckState(0))
        self.checkgeo.setCheckState(Qt.CheckState(0))

        if not self.parent.filter:
            return

        self.fillTable()
        self.parent.filter = {}
        self.close()



    def fillTable(self,filter = None):
        table = dbm.GetTableNir(self.parent.sorttype,self.parent.sortdesc,filter)
        self.parent.FillTable(table)
        filtermes = ""

        if filter:
            mes = 'Фильтрация установлена'

            if "prog" in self.parent.filter.keys():
                filtermes+= f" Программа: {self.prog.currentText()}; "
            if "geo" in self.parent.filter.keys():
                title = {"Z2": "Вуз",
                        "REGION": "Фед. округ",
                        "CITY": "Город",
                        "OBLNAME": "Субъект", }
                geofilter = list(self.parent.filter['geo'].items())
                f, n = geofilter[-1]
                filtermes += f"{title[f.upper()]}: {n}"
                # filtermes+= f" Программа: {self.prog.currentText()}"
        else:
            mes = 'Фильтрация отменена'

        self.parent.filterlabel.setText(filtermes)
        self.parent.statusBar().showMessage(mes)


        self.parent.setFocus()
        self.parent.activateWindow()
        self.parent.raise_()

    def canApply(self):
        canprog = self.checkprog.checkState() == 2 and self.prog.currentText() != ""
        cangeo = self.checkgeo.checkState() == 2 and (self.fedokrug.currentText() != "")
        return canprog or cangeo