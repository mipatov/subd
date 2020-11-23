import dbmanager as dbm
from PyQt5.QtCore import Qt
from gui.Forms import FormTableWidget, OnlyTableForm,OrderForm
from PyQt5 import QtWidgets, QtCore,QtGui

class Order(QtWidgets.QDialog, OrderForm.Ui_Dialog,):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent


        self.setWindowTitle("Финансирование НИР")
        self.countcurrentfin()

        rx = QtCore.QRegExp("-*\\d{0,30}\\.*\\d{0,10}")
        validator = QtGui.QRegExpValidator(rx, self)
        # self.onlyDouble = QtGui.QDoubleValidator()
        self.sumfin.setValidator(validator)
        self.percentfin.setValidator(validator)
        self.allowfin = {'sum':True,'percent':True}

        self.discard.clicked.connect(self.close)
        self.acceptbtn.clicked.connect(self.acceptorder)
        self.acceptbtn.setEnabled(False)

        self.sumfin.textChanged.connect(self.changesumfin)
        self.percentfin.textChanged.connect(self.changepercentfin)
        self.quartcombo.currentIndexChanged.connect(self.checkcorrectfill)

    def countcurrentfin(self):
        fin = dbm.getSumFin()
        self.fin = fin
        self.ffinlabel.setText(f"{fin['ffin']} руб.")
        self.pfinlabel.setText(f"{fin['pfin']} руб.")


    def changesumfin(self):
        if not self.allowfin['sum']: return

        self.allowfin['percent'] = False
        self.recountsumpercent('sum')
        self.allowfin['percent'] = True

        self.checkcorrectfill()

    def changepercentfin(self):
        if not self.allowfin['percent']: return

        self.allowfin['sum'] = False
        self.recountsumpercent('percent')
        self.allowfin['sum'] = True

        self.checkcorrectfill()

    def recountsumpercent(self,field):
        if field =="sum":
            text = self.sumfin.text()
            if text == "":
                self.percentfin.setText('')
                return

            sum = float(text)
            percent = sum/float(self.fin['pfin'])*100
            self.percentfin.setText(str(round(percent,5)))
        elif field =="percent":
            text = self.percentfin.text()
            if text == "":
                self.sumfin.setText('')
                return
            percent = float(text)
            sum = percent/100*float(self.fin['pfin'])
            self.sumfin.setText(str(round(sum,5)))
        else:
            print("wrong field")


    def checkcorrectfill(self):
        correct = self.quartcombo.currentIndex()>0 and self.sumfin.text()!="" and self.percentfin.text()!=""
        self.acceptbtn.setEnabled(correct)



    def acceptorder(self):
        print("apply fin order")
