# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Forms/orderform.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 475)
        Dialog.setModal(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.pfinlabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pfinlabel.setFont(font)
        self.pfinlabel.setObjectName("pfinlabel")
        self.gridLayout_2.addWidget(self.pfinlabel, 1, 1, 1, 1)
        self.ffinlabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ffinlabel.setFont(font)
        self.ffinlabel.setObjectName("ffinlabel")
        self.gridLayout_2.addWidget(self.ffinlabel, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 3, 1, 1)
        self.quartcombo = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quartcombo.setFont(font)
        self.quartcombo.setObjectName("quartcombo")
        self.quartcombo.addItem("")
        self.quartcombo.setItemText(0, "")
        self.quartcombo.addItem("")
        self.quartcombo.addItem("")
        self.quartcombo.addItem("")
        self.quartcombo.addItem("")
        self.gridLayout_3.addWidget(self.quartcombo, 1, 2, 1, 1)
        self.sumfin = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sumfin.setFont(font)
        self.sumfin.setObjectName("sumfin")
        self.gridLayout_3.addWidget(self.sumfin, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 2)
        self.percentfin = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.percentfin.setFont(font)
        self.percentfin.setObjectName("percentfin")
        self.gridLayout_3.addWidget(self.percentfin, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.countbtn = QtWidgets.QPushButton(Dialog)
        self.countbtn.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countbtn.setFont(font)
        self.countbtn.setObjectName("countbtn")
        self.verticalLayout.addWidget(self.countbtn)
        self.acceptbtn = QtWidgets.QPushButton(Dialog)
        self.acceptbtn.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acceptbtn.setFont(font)
        self.acceptbtn.setObjectName("acceptbtn")
        self.verticalLayout.addWidget(self.acceptbtn)
        self.discard = QtWidgets.QPushButton(Dialog)
        self.discard.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discard.setFont(font)
        self.discard.setObjectName("discard")
        self.verticalLayout.addWidget(self.discard)
        self.gridLayout_4.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 2, 5, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 1, 5, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Факт:"))
        self.pfinlabel.setText(_translate("Dialog", "00000"))
        self.ffinlabel.setText(_translate("Dialog", "00000"))
        self.label_3.setText(_translate("Dialog", "План:"))
        self.label_2.setText(_translate("Dialog", "Суммарнторное финансирование:"))
        self.label_10.setText(_translate("Dialog", "руб."))
        self.label_11.setText(_translate("Dialog", "%"))
        self.quartcombo.setItemText(1, _translate("Dialog", "I квартал"))
        self.quartcombo.setItemText(2, _translate("Dialog", "II квартал"))
        self.quartcombo.setItemText(3, _translate("Dialog", "III квартал"))
        self.quartcombo.setItemText(4, _translate("Dialog", "IV квартал"))
        self.label_12.setText(_translate("Dialog", "↨"))
        self.label_5.setText(_translate("Dialog", "Выдача распоряжения:"))
        self.label_8.setText(_translate("Dialog", "Процент от плана:"))
        self.label.setText(_translate("Dialog", "Квартал:"))
        self.label_7.setText(_translate("Dialog", "Сумма: "))
        self.countbtn.setText(_translate("Dialog", "Раcсчитать"))
        self.acceptbtn.setText(_translate("Dialog", "Утвердить"))
        self.discard.setText(_translate("Dialog", "Отменить"))
        self.label_6.setText(_translate("Dialog", "Распоряжение:"))
