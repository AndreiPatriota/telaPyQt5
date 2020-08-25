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
        MainWindow.resize(511, 207)
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
        self.btnSoma = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSoma.setFont(font)
        self.btnSoma.setObjectName("btnSoma")
        self.horizontalLayout.addWidget(self.btnSoma)
        self.btnSubtrai = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSubtrai.setFont(font)
        self.btnSubtrai.setObjectName("btnSubtrai")
        self.horizontalLayout.addWidget(self.btnSubtrai)
        self.btnValor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnValor.setFont(font)
        self.btnValor.setObjectName("btnValor")
        self.horizontalLayout.addWidget(self.btnValor)
        self.leditValor = QtWidgets.QLineEdit(self.centralwidget)
        self.leditValor.setGeometry(QtCore.QRect(360, 120, 131, 31))
        self.leditValor.setObjectName("leditValor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnSoma.clicked.connect(MainWindow.on_btnSoma_click)
        self.btnSubtrai.clicked.connect(MainWindow.on_btnSubtrai_click)
        self.btnZera.clicked.connect(MainWindow.on_bntZera_click)
        self.btnValor.clicked.connect(MainWindow.on_btnValor_click)
        self.leditValor.textChanged['QString'].connect(MainWindow.on_leditValor_chaged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnZera.setText(_translate("MainWindow", "Zerar"))
        self.btnSoma.setText(_translate("MainWindow", "Soma"))
        self.btnSubtrai.setText(_translate("MainWindow", "Subtrai"))
        self.btnValor.setText(_translate("MainWindow", "+ Valor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

