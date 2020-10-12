from PyQt5.QtCore import Qt
from gui.Forms import FormWidgetTable, OnlyTableForm,Main, OneRecordForm
from PyQt5 import QtWidgets, QtCore,QtGui
from gui.tablegui import *

import dbmanager as dbm
# pyuic5 gui/Forms/RemoveForm.ui -o gui/Forms/RemoveForm.py
# pyuic5 gui/Forms/FormTable.ui -o gui/Forms/FormTableWidget.py

class MainWindow(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    windows = []

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)


        self.nir.triggered.connect(self.opennirtable)
        self.prog.triggered.connect(self.openprogtable)
        self.vuz.triggered.connect(self.openvuztable)
        self.closeaction.triggered.connect(app.closeAllWindows)


        # self.windows.append(window)

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
      



