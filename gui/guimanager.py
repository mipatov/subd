import os
import codecs
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from gui.Forms import OnlyTableForm,Main, OrderForm
from PyQt5 import QtWidgets, QtCore,QtGui#, QtHelp
from gui.tablegui import *
from gui.ordergui import *


import dbmanager as dbm
# pyuic5 gui/Forms/RemoveForm.ui -o gui/Forms/RemoveForm.py
# pyuic5 gui/Forms/FormTable.ui -o gui/Forms/FormTableWidget.py

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class MainWindow(QtWidgets.QMainWindow, Main.Ui_MainWindow):


    def __init__(self, app, offline = False):
        super().__init__()
        self.setupUi(self)

        if(offline) :
            self.nir.setEnabled(False)
            self.prog.setEnabled(False)
            self.vuz.setEnabled(False)
            self.orderbtn.setEnabled(False)

            self.setWindowTitle(f'[OFFLINE MODE] {self.windowTitle()}')

        self.nir.triggered.connect(self.opennirtable)
        self.prog.triggered.connect(self.openprogtable)
        self.vuz.triggered.connect(self.openvuztable)
        self.closebtn.triggered.connect(app.closeAllWindows)
        self.orderbtn.triggered.connect(self.openorderform)
        self.aboutbtn.triggered.connect(self.aboutdialog)
        self.helpbtn.triggered.connect(self.showhelp)

        # self.statusbar.showMessage("")


        # self.analys1.triggered.connect(self.opennirtable)
        # self.analys2.triggered.connect(self.openprogtable)
        # self.analys3.triggered.connect(self.openanalis3table)

        self.analys1.setEnabled(False)
        self.analys2.setEnabled(False)
        self.analys3.setEnabled(False)

        self.mdi = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi)

        # self.windows.append(window)

    # def closeApp(self):


    def opennirtable(self):
        self.mdi.closeAllSubWindows()
        nirTable = dbm.GetTableNir()
        window = FuncTable(nirTable, "Данные о НИР",self)
        sub = self.mdi.addSubWindow(window)
        sub.showMaximized()

        # self.windows.append(window)



    def openprogtable(self):
        self.mdi.closeAllSubWindows()
        table = dbm.GetProgTable()
        window = OnlyTable(table, "Данные о программах",self)
        sub = self.mdi.addSubWindow(window)
        sub.showMaximized()

    def openvuztable(self):
        self.mdi.closeAllSubWindows()
        table = dbm.GetVuzTable()
        window = OnlyTable(table, "Данные о вузах",self)
        sub = self.mdi.addSubWindow(window)
        sub.showMaximized()

    def openorderform(self):
        self.mdi.closeAllSubWindows()
        window = Order(self)
        # window.show()
        sub = self.mdi.addSubWindow(window)
        sub.showMaximized()

    def aboutdialog(self):
        self.about = QtWidgets.QDialog()
        self.about.setWindowTitle("О программе")


        label = QtWidgets.QLabel(self.about)
        font = QtGui.QFont()
        font.setPointSize(12)
        label.setFont(font)
        abouttext = """Программа 'Сопровождение НТП'
    
Разработчики:
    студенты НИУ МЭИ ИВТИ УИТ 
    группы А-01-18
        Ипатов М.А.
        Ермакова М.И.
        Иванов С.Е.
        """
        label.setText(abouttext)

        layout = QtWidgets.QGridLayout(self.about)
        layout.addWidget(label)

        self.about.show()

    def showhelp(self):
        self.helpview = QWebEngineView()

        path = f"{self.projpath}\\doc\\doc.htm"
        if not os.path.exists(path):
            print("Не удалось найти справочные материалы")
            return 
        self.helpview.load(QUrl.fromLocalFile(path))
        self.helpview.setWindowTitle("Справка")
        self.helpview.resize(800,600)
        self.helpview.show()



