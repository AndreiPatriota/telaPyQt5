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
        self.btnValor.setText('0')


    #EVENT-HANDLERS VÃO AQUI
    @QtCore.pyqtSlot()
    def on_btnSoma_click(self):
        self.valLcdNumber += 1
        self.lcdNumber.display(self.valLcdNumber)


    @QtCore.pyqtSlot()
    def on_btnSubtrai_click(self):
        self.valLcdNumber -= 2
        self.lcdNumber.display(self.valLcdNumber)


    @QtCore.pyqtSlot()
    def on_bntZera_click(self):
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
    def on_leditValor_chaged(self):
        tx = str(self.leditValor.text())
        print('entrou')
        if len(tx) >= 1:
            if tx[0].isnumeric():
                self.btnValor.setText(tx)
            elif tx[0] == '-' and tx[1:].isnumeric():
                self.btnValor.setText(tx)

    @QtCore.pyqtSlot()
    def on_btnValor_click(self):
        valor = int(self.btnValor.text())
        self.valLcdNumber += valor
        self.lcdNumber.display(self.valLcdNumber)



#FUNÇÃO MAIN PADRÃO
def main():
    app = QApplication([])

    win = MinhaTela()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


