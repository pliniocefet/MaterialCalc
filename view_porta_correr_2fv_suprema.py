# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'porta_correr_2f_vidro_Suprema.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from relatorio import Ui_relatorio

class Ui_Porta_correr_2fv_suprema(object):

    def abrir_relatorio(self):
        self.window = QtWidgets.QMainWindow()
        self.relatorio = Ui_relatorio()
        self.relatorio.setupUi(self.window)
        self.window.show()

    def setupUi(self, Porta_correr_2fv_suprema):
        Porta_correr_2fv_suprema.setObjectName("Porta_correr_2fv_suprema")
        Porta_correr_2fv_suprema.resize(296, 173)
        Porta_correr_2fv_suprema.setMinimumSize(QtCore.QSize(280, 150))
        self.centralwidget = QtWidgets.QWidget(Porta_correr_2fv_suprema)
        self.centralwidget.setObjectName("centralwidget")
        self.label_descritivo = QtWidgets.QLabel(self.centralwidget)
        self.label_descritivo.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.label_descritivo.setObjectName("label_descritivo")
        self.lineEdit_largura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_largura.setGeometry(QtCore.QRect(60, 40, 71, 20))
        self.lineEdit_largura.setObjectName("lineEdit_largura")
        self.lineEdit_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_altura.setGeometry(QtCore.QRect(50, 72, 81, 20))
        self.lineEdit_altura.setObjectName("lineEdit_altura")
        self.label_largura = QtWidgets.QLabel(self.centralwidget)
        self.label_largura.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_largura.setObjectName("label_largura")
        self.label_altura = QtWidgets.QLabel(self.centralwidget)
        self.label_altura.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_altura.setObjectName("label_altura")
        self.pushButton_inserir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inserir.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.pushButton_inserir.setObjectName("pushButton_inserir")
        self.pushButton_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_limpar.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton_limpar.setObjectName("pushButton_limpar")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.pushButton_relatorio = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_relatorio.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.pushButton_relatorio.setObjectName("pushButton_relatorio")
        self.label_quantidade = QtWidgets.QLabel(self.centralwidget)
        self.label_quantidade.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.label_quantidade.setObjectName("label_quantidade")
        self.lineEdit_quantidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantidade.setGeometry(QtCore.QRect(50, 100, 81, 20))
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        Porta_correr_2fv_suprema.setCentralWidget(self.centralwidget)

        self.retranslateUi(Porta_correr_2fv_suprema)
        QtCore.QMetaObject.connectSlotsByName(Porta_correr_2fv_suprema)
        Porta_correr_2fv_suprema.setTabOrder(self.lineEdit_largura, self.lineEdit_altura)
        Porta_correr_2fv_suprema.setTabOrder(self.lineEdit_altura, self.lineEdit_quantidade)
        Porta_correr_2fv_suprema.setTabOrder(self.lineEdit_quantidade, self.pushButton_inserir)
        Porta_correr_2fv_suprema.setTabOrder(self.pushButton_inserir, self.pushButton_limpar)
        Porta_correr_2fv_suprema.setTabOrder(self.pushButton_limpar, self.pushButton_voltar)
        Porta_correr_2fv_suprema.setTabOrder(self.pushButton_voltar, self.pushButton_relatorio)

        self.pushButton_relatorio.clicked.connect(self.abrir_relatorio)

    def retranslateUi(self, Porta_correr_2fv_suprema):
        _translate = QtCore.QCoreApplication.translate
        Porta_correr_2fv_suprema.setWindowTitle(_translate("Porta_correr_2fv_suprema", "Porta de correr 2 folhas com vidro - Linha Suprema"))
        self.label_descritivo.setText(_translate("Porta_correr_2fv_suprema", "Portas de correr 2 folhas com vidros da linha Suprema"))
        self.label_largura.setText(_translate("Porta_correr_2fv_suprema", "Largura:"))
        self.label_altura.setText(_translate("Porta_correr_2fv_suprema", "Altura:"))
        self.pushButton_inserir.setText(_translate("Porta_correr_2fv_suprema", "Inserir"))
        self.pushButton_limpar.setText(_translate("Porta_correr_2fv_suprema", "Limpar"))
        self.pushButton_voltar.setText(_translate("Porta_correr_2fv_suprema", "Voltar"))
        self.pushButton_relatorio.setText(_translate("Porta_correr_2fv_suprema", "Relatório"))
        self.label_quantidade.setText(_translate("Porta_correr_2fv_suprema", "Quant:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Porta_correr_2fv_suprema = QtWidgets.QMainWindow()
    ui = Ui_Porta_correr_2fv_suprema()
    ui.setupUi(Porta_correr_2fv_suprema)
    Porta_correr_2fv_suprema.show()
    sys.exit(app.exec_())
