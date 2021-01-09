from PyQt5.QtWidgets import QMainWindow, QApplication
from menu_principal import Ui_MainWindow
from view_porta_correr_2fv_suprema import *
import sys

class Main(QMainWindow):

	def __init__(self):
		super().__init__()
		self.principal = Ui_MainWindow()
		self.principal.setupUi(self)

		self.principal.pushButton_pc2fv_suprema.clicked.connect(self.bt_porta_correr_2fv_suprema)
		self.principal.pushButton_jc2fv_suprema.clicked.connect(self.bt_janela_correr_2fv_suprema)

	def bt_porta_correr_2fv_suprema(self):
		self.window = QtWidgets.QMainWindow()
		self.porta_correr = Ui_Porta_correr_2fv_suprema()
		self.porta_correr.setupUi(self.window)
		self.window.show()


	def bt_janela_correr_2fv_suprema(self):
		print('Janela correr 2 folhas vidro - Suprema')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = Main()
    tela.show()
    sys.exit(app.exec_())