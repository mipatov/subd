# pyuic5 Forms/name.ui -o Forms/name.py
from gui.guimanager import *
import dbmanager as dbm
from PyQt5.QtCore import Qt
from gui.Forms import RemoveForm, OneRecordForm
from PyQt5 import QtWidgets, QtCore,QtGui

class AddRecord(QtWidgets.QDialog, OneRecordForm.Ui_Dialog):
    # parent = None
    def __init__(self,name,parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(name)
        self.parent = parent

        self.errorlabel.setHidden(True)
        self.dateerror.setHidden(True)
        self.numerror.setHidden(True)
        self.finerror.setHidden(True)
        self.grntierror.setHidden(True)


        self.prog.addItems(dbm.GetProgTuple())
        self.setprojnumtip()
        self.prog.currentIndexChanged.connect(self.setprojnumtip)
        self.isp.addItems(dbm.GetVuzTuple())
        self.onlyInt = QtGui.QIntValidator()
        self.pfin.setValidator(self.onlyInt)
        self.srok_k.setValidator(self.onlyInt)
        self.srok_n.setValidator(self.onlyInt)
        # self.srok_k.textChanged.connect(self.changefld)
        # self.srok_n.textChanged.connect(self.changefld)
        self.savebtn.clicked.connect(self.saverecord)
        self.discardbtn.clicked.connect(self.discard)
        mask = "00.00.00;_"
        self.GRNTI.setInputMask(mask)
        self.GRNTI2.setInputMask(mask)
        self.GRNTI2.setHidden(True)
        self.grntibtn.clicked.connect(self.togglegrnti)

    def togglegrnti(self):
        if self.grntibtn.text() == "+":
            self.GRNTI2.setHidden(False)
            self.grntibtn.setText("-")
        else:
            self.GRNTI2.setHidden(True)
            self.grntibtn.setText("+")

    def check(self):
        correct  = True
        self.errorlabel.setHidden(True)
        self.dateerror.setHidden(True)
        self.numerror.setHidden(True)
        self.finerror.setHidden(True)
        self.grntierror.setHidden(True)

        noempty = (self.pfin,self.ruk,self.ruk2,self.srok_k,self.srok_n)

        if not dbm.CheckProjNum(self.prog.currentText(), self.f.value()):
            self.numerror.setHidden(False)
            correct = False

        for fld in noempty:
            if fld.text() == "" or "_" in fld.text():
                correct = False
                self.errorlabel.setHidden(False)


        if self.NIR.toPlainText() == "":
            correct = False
            self.errorlabel.setHidden(False)

        if len(self.GRNTI.text()) !=8:
            correct = False
            self.grntierror.setHidden(False)

        if not self.GRNTI2.isHidden() and len(self.GRNTI2.text()) !=8:
            correct = False
            self.grntierror.setHidden(False)

        if correct:
            if int(self.srok_k.text()) < int(self.srok_n.text()):
                self.dateerror.setHidden(False)
                correct = False

            if int(self.pfin.text()) <= 0:
                self.finerror.setHidden(False)
                correct = False

        return correct




    def saverecord(self):

        if self.check():
            print("save new rec")
            ctypes  = ("Ф","П","Р")
            ctype = ctypes[self.CODTYPE.currentIndex()]
            grnti = self.GRNTI.text()
            if not self.GRNTI2.isHidden():
                grnti+= "; "+ self.GRNTI2.text()
            dbm.AddRecord(self.prog.currentText(),self.f.value(),self.NIR.toPlainText(),self.isp.currentText(),self.srok_n.text(),self.srok_k.text(),self.ruk.text(),self.ruk2.text(),grnti,ctype,self.pfin.text())

            prog, f = self.prog.currentText(),self.f.value()

            self.parent.FillTable(dbm.GetTableNir(sort=self.parent.sorttype, desc=self.parent.sortdesc))
            self.parent.findrec(prog, f)
            self.close()

    def discard(self):
        self.close()



    def setprojnumtip(self):
        print(self.prog.currentText())
        i = dbm.GetMaxProjInProg(self.prog.currentText())
        # self.f.setMinimum(int(i)+1)
        self.f.setValue(int(i) + 1)
        print(i)

class RemoveRecord(QtWidgets.QDialog, RemoveForm.Ui_Dialog):

    def __init__(self,cRec,parent):
        super().__init__()
        self.setupUi(self)
        self.cRec  = cRec
        self.parent = parent
        self.setWindowTitle("Подтвержедние удаления")
        self.rec.setText(f"Программа: '{cRec[0]}' \n№ {cRec[1]}")
        self.ok.clicked.connect(self.removerec)
        self.cancel.clicked.connect(self.close)

    def removerec(self):
        dbm.RemoveRecord(self.cRec[0],self.cRec[1])
        self.parent.FillTable(dbm.GetTableNir(sort=self.parent.sorttype, desc=self.parent.sortdesc))
        self.close()