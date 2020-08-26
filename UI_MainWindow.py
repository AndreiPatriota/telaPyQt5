# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(220, 10, 91, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.btnZera = QtWidgets.QPushButton(self.centralwidget)
        self.btnZera.setGeometry(QtCore.QRect(20, 80, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnZera.setFont(font)
        self.btnZera.setObjectName("btnZera")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 319, 39))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSoma1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSoma1.setFont(font)
        self.btnSoma1.setObjectName("btnSoma1")
        self.horizontalLayout.addWidget(self.btnSoma1)
        self.btnSoma2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSoma2.setFont(font)
        self.btnSoma2.setObjectName("btnSoma2")
        self.horizontalLayout.addWidget(self.btnSoma2)
        self.btnValor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnValor.setFont(font)
        self.btnValor.setObjectName("btnValor")
        self.horizontalLayout.addWidget(self.btnValor)
        self.leditValor = QtWidgets.QLineEdit(self.centralwidget)
        self.leditValor.setGeometry(QtCore.QRect(350, 120, 141, 31))
        self.leditValor.setObjectName("leditValor")
        self.cmbOp = QtWidgets.QComboBox(self.centralwidget)
        self.cmbOp.setGeometry(QtCore.QRect(20, 170, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cmbOp.setFont(font)
        self.cmbOp.setObjectName("cmbOp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnZera.clicked.connect(MainWindow.on_btnZera_click)
        self.btnSoma1.clicked.connect(MainWindow.on_btnSoma1_click)
        self.btnSoma2.clicked.connect(MainWindow.on_btnSoma2_click)
        self.btnValor.clicked.connect(MainWindow.on_btnValor_click)
        self.leditValor.textChanged['QString'].connect(MainWindow.on_leditValor_change)
        self.cmbOp.currentIndexChanged['int'].connect(MainWindow.on_cmbOp_change)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnZera.setText(_translate("MainWindow", "Zerar"))
        self.btnSoma1.setText(_translate("MainWindow", "+ 1"))
        self.btnSoma2.setText(_translate("MainWindow", "+2"))
        self.btnValor.setText(_translate("MainWindow", "+ Valor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

