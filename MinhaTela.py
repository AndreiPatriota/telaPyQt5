import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from UI_MainWindow import Ui_MainWindow

class MinhaTela(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        #INICIALIZAÇÕES VÃO AQUI
        self.valLcdNumber = 0.0
        self.lcdNumber.display(self.valLcdNumber)
        self.custom_value = 0.0
        self.btnValor.setText('+0')
        self.cmbOp.addItems(['soma', 'subtrai'])


    #EVENT-HANDLERS VÃO AQUI
    @QtCore.pyqtSlot()
    def on_btnSoma1_click(self):
        self.valLcdNumber += int(self.btnSoma1.text())
        self.lcdNumber.display(self.valLcdNumber)


    @QtCore.pyqtSlot()
    def on_btnSoma2_click(self):
        self.valLcdNumber += int(self.btnSoma2.text())
        self.lcdNumber.display(self.valLcdNumber)


    @QtCore.pyqtSlot()
    def on_btnZera_click(self):
        try:
            val = QMessageBox.question(self, 'Mensagem', 'Deseja Zerar o Display?',QMessageBox.Yes, QMessageBox.No)
            if val == QMessageBox.Yes:
                self.valLcdNumber = 0
                self.lcdNumber.display(int(self.valLcdNumber))
                QMessageBox.information(self, 'Tudo Certo','Display Zerado!')
            elif val == QMessageBox.No:
                QMessageBox.information(self, 'Tudo Certo','Operação cancelada!')
        except Exception as erro:
            QMessageBox.critical(f'{erro.__class__}')


    @QtCore.pyqtSlot()
    def on_leditValor_change(self):
        tx = str(self.leditValor.text())
        if len(tx) >= 1 and tx.isnumeric():
            self.btnValor.setText(f'+{tx}' if self.cmbOp.currentText()== 'soma' else f'-{tx}')

    @QtCore.pyqtSlot()
    def on_btnValor_click(self):
        self.valLcdNumber += int(self.btnValor.text())
        self.lcdNumber.display(self.valLcdNumber)


    @QtCore.pyqtSlot()
    def on_cmbOp_change(self):
        if self.cmbOp.currentText() == 'soma':
            self.btnSoma1.setText('+1')
            self.btnSoma2.setText('+2')
            self.btnValor.setText('+' + self.btnValor.text()[1:])
        elif self.cmbOp.currentText() == 'subtrai':
            self.btnSoma1.setText('-1')
            self.btnSoma2.setText('-2')
            self.btnValor.setText('-' + self.btnValor.text()[1:])


#FUNÇÃO MAIN PADRÃO
def main():
    app = QApplication([])

    win = MinhaTela()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


