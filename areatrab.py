# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from cadastrocarro import Ui_Cadcarro  # Importe a interface de cadastro
from cadastropneu import Ui_Cadpneu
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 1051, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 26))
        self.menubar.setObjectName("menubar")
        self.menuFrota = QtWidgets.QMenu(self.menubar)
        self.menuFrota.setObjectName("menuFrota")
        self.menuPneus = QtWidgets.QMenu(self.menubar)
        self.menuPneus.setObjectName("menuPneus")
        self.menuRelatorios = QtWidgets.QMenu(self.menubar)
        self.menuRelatorios.setObjectName("menuRelatorios")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdicionar_veiculo = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_veiculo.setObjectName("actionAdicionar_veiculo")
        self.actionEditar_veiculo = QtWidgets.QAction(MainWindow)
        self.actionEditar_veiculo.setObjectName("actionEditar_veiculo")
        self.actionApagar_veiculo = QtWidgets.QAction(MainWindow)
        self.actionApagar_veiculo.setObjectName("actionApagar_veiculo")
        self.actionAdicionar_pneus = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_pneus.setObjectName("actionAdicionar_pneus")
        self.actionEditar_pneus = QtWidgets.QAction(MainWindow)
        self.actionEditar_pneus.setObjectName("actionEditar_pneus")
        self.actionRemover_pneus = QtWidgets.QAction(MainWindow)
        self.actionRemover_pneus.setObjectName("actionRemover_pneus")
        self.actionEstado_dos_pneus = QtWidgets.QAction(MainWindow)
        self.actionEstado_dos_pneus.setObjectName("actionEstado_dos_pneus")
        self.actionEstado_da_frota = QtWidgets.QAction(MainWindow)
        self.actionEstado_da_frota.setObjectName("actionEstado_da_frota")
        self.menuFrota.addAction(self.actionAdicionar_veiculo)
        self.menuFrota.addAction(self.actionEditar_veiculo)
        self.menuFrota.addAction(self.actionApagar_veiculo)
        self.menuPneus.addAction(self.actionAdicionar_pneus)
        self.menuPneus.addAction(self.actionEditar_pneus)
        self.menuPneus.addAction(self.actionRemover_pneus)
        self.menuRelatorios.addAction(self.actionEstado_dos_pneus)
        self.menuRelatorios.addAction(self.actionEstado_da_frota)
        self.menubar.addAction(self.menuFrota.menuAction())
        self.menubar.addAction(self.menuPneus.menuAction())
        self.menubar.addAction(self.menuRelatorios.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conecte a ação ao método para abrir a janela de cadastro
        self.actionAdicionar_veiculo.triggered.connect(self.openCadastroWindow)
        self.actionAdicionar_pneus.triggered.connect(self.openCadpneuWindow)

        # Configure o banco de dados
        self.setupDatabase()

        # Carregue os dados na tabela
        self.loadData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Placa"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Modelo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ano"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Renavam"))
        self.menuFrota.setTitle(_translate("MainWindow", "Frota"))
        self.menuPneus.setTitle(_translate("MainWindow", "Pneus"))
        self.menuRelatorios.setTitle(_translate("MainWindow", "Relatorios"))
        self.actionAdicionar_veiculo.setText(_translate("MainWindow", "Adicionar veículo"))
        self.actionEditar_veiculo.setText(_translate("MainWindow", "Editar veículo"))
        self.actionApagar_veiculo.setText(_translate("MainWindow", "Apagar veículo"))
        self.actionAdicionar_pneus.setText(_translate("MainWindow", "Adicionar pneus"))
        self.actionEditar_pneus.setText(_translate("MainWindow", "Editar pneus"))
        self.actionRemover_pneus.setText(_translate("MainWindow", "Remover pneus"))
        self.actionEstado_dos_pneus.setText(_translate("MainWindow", "Estado dos pneus"))
        self.actionEstado_da_frota.setText(_translate("MainWindow", "Estado da frota"))

    def setupDatabase(self):
        try:
            # Configura o banco de dados
            self.conn = sqlite3.connect('pneusfrota.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Erro', f'Erro ao conectar com o banco de dados: {e}')
            exit()

    def loadData(self):
        try:
            self.cursor.execute("SELECT * FROM Carro")
            rows = self.cursor.fetchall()

            self.tableWidget.setRowCount(len(rows))
            for row_num, row_data in enumerate(rows):
                for col_num, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Erro', f'Erro ao carregar dados do banco de dados: {e}')

    def openCadastroWindow(self):
        # Método para abrir a janela de cadastro
        self.cadastroDialog = QtWidgets.QDialog()
        self.cadastroUI = Ui_Cadcarro()
        self.cadastroUI.setupUi(self.cadastroDialog)
        self.cadastroUI.pushButton.clicked.connect(
            self.addCarro)  # Conectar o botão de cadastro ao método de adicionar carro
        self.cadastroDialog.exec_()

    def addCarro(self):
        # Método para adicionar um carro no banco de dados
        placa = self.cadastroUI.lineEdit.text()
        marca = self.cadastroUI.lineEdit_2.text()
        modelo = self.cadastroUI.lineEdit_3.text()
        ano = self.cadastroUI.lineEdit_4.text()
        renavam = self.cadastroUI.lineEdit_5.text()

        if placa and marca and modelo and ano and renavam:
            try:
                comando = "INSERT INTO Carro (placa, marca, modelo, ano, renavam) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(comando, (placa, marca, modelo, ano, renavam))
                self.conn.commit()
                QtWidgets.QMessageBox.information(self.cadastroDialog, 'Sucesso', 'Carro cadastrado com sucesso!')
                self.cadastroDialog.close()
                self.loadData()  # Recarregue os dados na tabela
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(self.cadastroDialog, 'Erro', f'Erro ao adicionar carro: {e}')
        else:
            QtWidgets.QMessageBox.warning(self.cadastroDialog, 'Erro', 'Todos os campos são obrigatórios!')

    def openCadpneuWindow(self):
        # Método para abrir a janela de cadastro de pneus
        self.cadastroDialog = QtWidgets.QDialog()
        self.cadastroUI = Ui_Cadpneu()
        self.cadastroUI.setupUi(self.cadastroDialog)
        self.cadastroDialog.exec_()
