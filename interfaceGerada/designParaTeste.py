# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interfaceVisual\designParaTeste.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 800))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabComparar = QtWidgets.QWidget()
        self.tabComparar.setObjectName("tabComparar")
        self.botaoComparar = QtWidgets.QPushButton(self.tabComparar)
        self.botaoComparar.setGeometry(QtCore.QRect(340, 680, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoComparar.setFont(font)
        self.botaoComparar.setObjectName("botaoComparar")
        self.labelSelecCIF = QtWidgets.QLabel(self.tabComparar)
        self.labelSelecCIF.setGeometry(QtCore.QRect(0, 0, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecCIF.setFont(font)
        self.labelSelecCIF.setStyleSheet("padding: 10px;")
        self.labelSelecCIF.setScaledContents(False)
        self.labelSelecCIF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelecCIF.setWordWrap(True)
        self.labelSelecCIF.setObjectName("labelSelecCIF")
        self.botaoSelecCIF = QtWidgets.QPushButton(self.tabComparar)
        self.botaoSelecCIF.setGeometry(QtCore.QRect(10, 50, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoSelecCIF.setFont(font)
        self.botaoSelecCIF.setObjectName("botaoSelecCIF")
        self.labelCaminhoCIFs = QtWidgets.QLabel(self.tabComparar)
        self.labelCaminhoCIFs.setGeometry(QtCore.QRect(0, 80, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCaminhoCIFs.setFont(font)
        self.labelCaminhoCIFs.setStyleSheet("padding: 10px;")
        self.labelCaminhoCIFs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCaminhoCIFs.setObjectName("labelCaminhoCIFs")
        self.labelSelecPadrao = QtWidgets.QLabel(self.tabComparar)
        self.labelSelecPadrao.setGeometry(QtCore.QRect(0, 130, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecPadrao.setFont(font)
        self.labelSelecPadrao.setStyleSheet("padding: 10px;")
        self.labelSelecPadrao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelecPadrao.setObjectName("labelSelecPadrao")
        self.botaoSelecPadrao = QtWidgets.QPushButton(self.tabComparar)
        self.botaoSelecPadrao.setGeometry(QtCore.QRect(10, 180, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoSelecPadrao.setFont(font)
        self.botaoSelecPadrao.setObjectName("botaoSelecPadrao")
        self.labelCaminhoPadrao = QtWidgets.QLabel(self.tabComparar)
        self.labelCaminhoPadrao.setGeometry(QtCore.QRect(0, 210, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCaminhoPadrao.setFont(font)
        self.labelCaminhoPadrao.setStyleSheet("padding: 10px;")
        self.labelCaminhoPadrao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCaminhoPadrao.setObjectName("labelCaminhoPadrao")
        self.labelSelecRadiacao = QtWidgets.QLabel(self.tabComparar)
        self.labelSelecRadiacao.setGeometry(QtCore.QRect(0, 260, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecRadiacao.setFont(font)
        self.labelSelecRadiacao.setStyleSheet("padding: 10px;")
        self.labelSelecRadiacao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelecRadiacao.setObjectName("labelSelecRadiacao")
        self.caixaRadiacoes = QtWidgets.QComboBox(self.tabComparar)
        self.caixaRadiacoes.setGeometry(QtCore.QRect(10, 310, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.caixaRadiacoes.setFont(font)
        self.caixaRadiacoes.setObjectName("caixaRadiacoes")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.caixaRadiacoes.addItem("")
        self.commandLinkButtonAjuda = QtWidgets.QCommandLinkButton(self.tabComparar)
        self.commandLinkButtonAjuda.setGeometry(QtCore.QRect(710, 0, 90, 40))
        self.commandLinkButtonAjuda.setObjectName("commandLinkButtonAjuda")
        self.tabWidget.addTab(self.tabComparar, "")
        self.tabDetectar = QtWidgets.QWidget()
        self.tabDetectar.setObjectName("tabDetectar")
        self.labelImagemGrafico = QtWidgets.QLabel(self.tabDetectar)
        self.labelImagemGrafico.setGeometry(QtCore.QRect(0, 110, 800, 580))
        self.labelImagemGrafico.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImagemGrafico.setObjectName("labelImagemGrafico")
        self.labelSelecionarPadraoNoTodo = QtWidgets.QLabel(self.tabDetectar)
        self.labelSelecionarPadraoNoTodo.setGeometry(QtCore.QRect(10, 0, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecionarPadraoNoTodo.setFont(font)
        self.labelSelecionarPadraoNoTodo.setStyleSheet("")
        self.labelSelecionarPadraoNoTodo.setObjectName("labelSelecionarPadraoNoTodo")
        self.labelCaminhoPadraoNoTodo = QtWidgets.QLabel(self.tabDetectar)
        self.labelCaminhoPadraoNoTodo.setGeometry(QtCore.QRect(0, 30, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCaminhoPadraoNoTodo.setFont(font)
        self.labelCaminhoPadraoNoTodo.setStyleSheet("padding: 10px;")
        self.labelCaminhoPadraoNoTodo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCaminhoPadraoNoTodo.setObjectName("labelCaminhoPadraoNoTodo")
        self.botaoSelecionarArquivoXy = QtWidgets.QPushButton(self.tabDetectar)
        self.botaoSelecionarArquivoXy.setGeometry(QtCore.QRect(260, 0, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoSelecionarArquivoXy.setFont(font)
        self.botaoSelecionarArquivoXy.setObjectName("botaoSelecionarArquivoXy")
        self.labelLimite = QtWidgets.QLabel(self.tabDetectar)
        self.labelLimite.setGeometry(QtCore.QRect(10, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelLimite.setFont(font)
        self.labelLimite.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLimite.setObjectName("labelLimite")
        self.pushButtonSalvarFigura = QtWidgets.QPushButton(self.tabDetectar)
        self.pushButtonSalvarFigura.setGeometry(QtCore.QRect(120, 690, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonSalvarFigura.setFont(font)
        self.pushButtonSalvarFigura.setObjectName("pushButtonSalvarFigura")
        self.pushButtonImportar = QtWidgets.QPushButton(self.tabDetectar)
        self.pushButtonImportar.setGeometry(QtCore.QRect(300, 690, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonImportar.setFont(font)
        self.pushButtonImportar.setObjectName("pushButtonImportar")
        self.pushButtonDetectar = QtWidgets.QPushButton(self.tabDetectar)
        self.pushButtonDetectar.setGeometry(QtCore.QRect(10, 690, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonDetectar.setFont(font)
        self.pushButtonDetectar.setObjectName("pushButtonDetectar")
        self.labelValorLimite = QtWidgets.QLabel(self.tabDetectar)
        self.labelValorLimite.setGeometry(QtCore.QRect(160, 80, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelValorLimite.setFont(font)
        self.labelValorLimite.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValorLimite.setObjectName("labelValorLimite")
        self.labelAjustarLimite = QtWidgets.QLabel(self.tabDetectar)
        self.labelAjustarLimite.setGeometry(QtCore.QRect(510, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelAjustarLimite.setFont(font)
        self.labelAjustarLimite.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAjustarLimite.setObjectName("labelAjustarLimite")
        self.doubleSpinBoxMudarLimite = QtWidgets.QDoubleSpinBox(self.tabDetectar)
        self.doubleSpinBoxMudarLimite.setGeometry(QtCore.QRect(660, 80, 100, 30))
        self.doubleSpinBoxMudarLimite.setMaximum(1000000.0)
        self.doubleSpinBoxMudarLimite.setObjectName("doubleSpinBoxMudarLimite")
        self.labelLimitAtual = QtWidgets.QLabel(self.tabDetectar)
        self.labelLimitAtual.setGeometry(QtCore.QRect(260, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelLimitAtual.setFont(font)
        self.labelLimitAtual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLimitAtual.setObjectName("labelLimitAtual")
        self.labelValorLimiteAjustar = QtWidgets.QLabel(self.tabDetectar)
        self.labelValorLimiteAjustar.setGeometry(QtCore.QRect(410, 80, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelValorLimiteAjustar.setFont(font)
        self.labelValorLimiteAjustar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValorLimiteAjustar.setObjectName("labelValorLimiteAjustar")
        self.commandLinkButtonAjuda_2 = QtWidgets.QCommandLinkButton(self.tabDetectar)
        self.commandLinkButtonAjuda_2.setGeometry(QtCore.QRect(710, 0, 90, 40))
        self.commandLinkButtonAjuda_2.setObjectName("commandLinkButtonAjuda_2")
        self.tabWidget.addTab(self.tabDetectar, "")
        self.tabCompararPoucosPicos = QtWidgets.QWidget()
        self.tabCompararPoucosPicos.setObjectName("tabCompararPoucosPicos")
        self.labelAdicionarPicos = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelAdicionarPicos.setGeometry(QtCore.QRect(0, 130, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelAdicionarPicos.setFont(font)
        self.labelAdicionarPicos.setStyleSheet("Padding: 10px;")
        self.labelAdicionarPicos.setObjectName("labelAdicionarPicos")
        self.comboBoxPico1 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.comboBoxPico1.setGeometry(QtCore.QRect(10, 180, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPico1.setFont(font)
        self.comboBoxPico1.setObjectName("comboBoxPico1")
        self.comboBoxPico1.addItem("")
        self.comboBoxPico2 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.comboBoxPico2.setGeometry(QtCore.QRect(120, 180, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPico2.setFont(font)
        self.comboBoxPico2.setObjectName("comboBoxPico2")
        self.comboBoxPico2.addItem("")
        self.comboBoxPico3 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.comboBoxPico3.setGeometry(QtCore.QRect(230, 180, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPico3.setFont(font)
        self.comboBoxPico3.setObjectName("comboBoxPico3")
        self.comboBoxPico3.addItem("")
        self.comboBoxPico4 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.comboBoxPico4.setGeometry(QtCore.QRect(340, 180, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPico4.setFont(font)
        self.comboBoxPico4.setObjectName("comboBoxPico4")
        self.comboBoxPico4.addItem("")
        self.comboBoxPico5 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.comboBoxPico5.setGeometry(QtCore.QRect(450, 180, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxPico5.setFont(font)
        self.comboBoxPico5.setObjectName("comboBoxPico5")
        self.comboBoxPico5.addItem("")
        self.labelSelecionarXlsx = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelSelecionarXlsx.setGeometry(QtCore.QRect(0, 0, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecionarXlsx.setFont(font)
        self.labelSelecionarXlsx.setStyleSheet("Padding: 10px;")
        self.labelSelecionarXlsx.setObjectName("labelSelecionarXlsx")
        self.botaoSelecionarArquivoXlsx = QtWidgets.QPushButton(self.tabCompararPoucosPicos)
        self.botaoSelecionarArquivoXlsx.setGeometry(QtCore.QRect(10, 50, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoSelecionarArquivoXlsx.setFont(font)
        self.botaoSelecionarArquivoXlsx.setObjectName("botaoSelecionarArquivoXlsx")
        self.labelCaminhoXlsx = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelCaminhoXlsx.setGeometry(QtCore.QRect(0, 80, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCaminhoXlsx.setFont(font)
        self.labelCaminhoXlsx.setStyleSheet("padding: 10px;")
        self.labelCaminhoXlsx.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCaminhoXlsx.setObjectName("labelCaminhoXlsx")
        self.botaoComparar_2 = QtWidgets.QPushButton(self.tabCompararPoucosPicos)
        self.botaoComparar_2.setGeometry(QtCore.QRect(340, 680, 120, 40))
        self.botaoComparar_2.setObjectName("botaoComparar_2")
        self.labelSelecCIF_2 = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelSelecCIF_2.setGeometry(QtCore.QRect(0, 210, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecCIF_2.setFont(font)
        self.labelSelecCIF_2.setStyleSheet("padding: 10px;")
        self.labelSelecCIF_2.setScaledContents(False)
        self.labelSelecCIF_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelecCIF_2.setWordWrap(True)
        self.labelSelecCIF_2.setObjectName("labelSelecCIF_2")
        self.botaoSelecCIF_2 = QtWidgets.QPushButton(self.tabCompararPoucosPicos)
        self.botaoSelecCIF_2.setGeometry(QtCore.QRect(10, 260, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.botaoSelecCIF_2.setFont(font)
        self.botaoSelecCIF_2.setObjectName("botaoSelecCIF_2")
        self.labelCaminhoCIFs_2 = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelCaminhoCIFs_2.setGeometry(QtCore.QRect(0, 290, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCaminhoCIFs_2.setFont(font)
        self.labelCaminhoCIFs_2.setStyleSheet("padding: 10px;")
        self.labelCaminhoCIFs_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCaminhoCIFs_2.setObjectName("labelCaminhoCIFs_2")
        self.labelSelecRadiacao_2 = QtWidgets.QLabel(self.tabCompararPoucosPicos)
        self.labelSelecRadiacao_2.setGeometry(QtCore.QRect(0, 340, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSelecRadiacao_2.setFont(font)
        self.labelSelecRadiacao_2.setStyleSheet("padding: 10px;")
        self.labelSelecRadiacao_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSelecRadiacao_2.setObjectName("labelSelecRadiacao_2")
        self.commandLinkButtonAjuda_3 = QtWidgets.QCommandLinkButton(self.tabCompararPoucosPicos)
        self.commandLinkButtonAjuda_3.setGeometry(QtCore.QRect(710, 0, 90, 40))
        self.commandLinkButtonAjuda_3.setObjectName("commandLinkButtonAjuda_3")
        self.caixaRadiacoes_2 = QtWidgets.QComboBox(self.tabCompararPoucosPicos)
        self.caixaRadiacoes_2.setGeometry(QtCore.QRect(10, 390, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.caixaRadiacoes_2.setFont(font)
        self.caixaRadiacoes_2.setObjectName("caixaRadiacoes_2")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.caixaRadiacoes_2.addItem("")
        self.tabWidget.addTab(self.tabCompararPoucosPicos, "")
        self.tabAjuda = QtWidgets.QWidget()
        self.tabAjuda.setObjectName("tabAjuda")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tabAjuda)
        self.verticalScrollBar.setGeometry(QtCore.QRect(770, 0, 30, 800))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.tabWidget.addTab(self.tabAjuda, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botaoComparar.setText(_translate("MainWindow", "Comparar"))
        self.labelSelecCIF.setText(_translate("MainWindow", "Selecione a pasta com os arquivos .cif\'s:"))
        self.botaoSelecCIF.setText(_translate("MainWindow", "Selecionar pasta"))
        self.labelCaminhoCIFs.setText(_translate("MainWindow", "O caminho aparecerá aqui quando selecionado"))
        self.labelSelecPadrao.setText(_translate("MainWindow", "Selecione a pasta com seu padrão de difração (.xlsx e .xy):"))
        self.botaoSelecPadrao.setText(_translate("MainWindow", "Selecionar pasta"))
        self.labelCaminhoPadrao.setText(_translate("MainWindow", "O caminho aparecerá aqui quando selecionado"))
        self.labelSelecRadiacao.setText(_translate("MainWindow", "Selecione a radiação característica (Angstrons):"))
        self.caixaRadiacoes.setItemText(0, _translate("MainWindow", "1,540598"))
        self.caixaRadiacoes.setItemText(1, _translate("MainWindow", "1,544426"))
        self.caixaRadiacoes.setItemText(2, _translate("MainWindow", "1,542512"))
        self.caixaRadiacoes.setItemText(3, _translate("MainWindow", "CuKa"))
        self.caixaRadiacoes.setItemText(4, _translate("MainWindow", "CuKa1"))
        self.caixaRadiacoes.setItemText(5, _translate("MainWindow", "CuKa2"))
        self.caixaRadiacoes.setItemText(6, _translate("MainWindow", "CuKb1"))
        self.caixaRadiacoes.setItemText(7, _translate("MainWindow", "CoKb1"))
        self.caixaRadiacoes.setItemText(8, _translate("MainWindow", "CoKa1"))
        self.caixaRadiacoes.setItemText(9, _translate("MainWindow", "CoKa2"))
        self.caixaRadiacoes.setItemText(10, _translate("MainWindow", "CoKa"))
        self.caixaRadiacoes.setItemText(11, _translate("MainWindow", "FeKb1"))
        self.caixaRadiacoes.setItemText(12, _translate("MainWindow", "FeKa1"))
        self.caixaRadiacoes.setItemText(13, _translate("MainWindow", "FeKa2"))
        self.caixaRadiacoes.setItemText(14, _translate("MainWindow", "FeKa"))
        self.caixaRadiacoes.setItemText(15, _translate("MainWindow", "CrKb1"))
        self.caixaRadiacoes.setItemText(16, _translate("MainWindow", "CrKa1"))
        self.caixaRadiacoes.setItemText(17, _translate("MainWindow", "CrKa2"))
        self.caixaRadiacoes.setItemText(18, _translate("MainWindow", "CrKa"))
        self.caixaRadiacoes.setItemText(19, _translate("MainWindow", "MoKa"))
        self.caixaRadiacoes.setItemText(20, _translate("MainWindow", "MoKa1"))
        self.caixaRadiacoes.setItemText(21, _translate("MainWindow", "MoKa2"))
        self.caixaRadiacoes.setItemText(22, _translate("MainWindow", "MoKb1"))
        self.caixaRadiacoes.setItemText(23, _translate("MainWindow", "AgKa"))
        self.caixaRadiacoes.setItemText(24, _translate("MainWindow", "AgKa1"))
        self.caixaRadiacoes.setItemText(25, _translate("MainWindow", "AgKa2"))
        self.caixaRadiacoes.setItemText(26, _translate("MainWindow", "AgKb1"))
        self.commandLinkButtonAjuda.setText(_translate("MainWindow", "Ajuda"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabComparar), _translate("MainWindow", "Comparar"))
        self.labelImagemGrafico.setText(_translate("MainWindow", "O gráfico aparecerá aqui quando selecionar um arquivo compatível"))
        self.labelSelecionarPadraoNoTodo.setText(_translate("MainWindow", "Selecione o arquivo .xy:"))
        self.labelCaminhoPadraoNoTodo.setText(_translate("MainWindow", "O caminho aparecerá aqui quando selecionado"))
        self.botaoSelecionarArquivoXy.setText(_translate("MainWindow", "Selecionar arquivo"))
        self.labelLimite.setText(_translate("MainWindow", "Limite padrão:"))
        self.pushButtonSalvarFigura.setText(_translate("MainWindow", "Salvar figura (.png)"))
        self.pushButtonImportar.setText(_translate("MainWindow", "Importar ângulos (.xlsx)"))
        self.pushButtonDetectar.setText(_translate("MainWindow", "Detectar"))
        self.labelValorLimite.setText(_translate("MainWindow", "-"))
        self.labelAjustarLimite.setText(_translate("MainWindow", "Ajustar limite:"))
        self.labelLimitAtual.setText(_translate("MainWindow", "Limite atual:"))
        self.labelValorLimiteAjustar.setText(_translate("MainWindow", "-"))
        self.commandLinkButtonAjuda_2.setText(_translate("MainWindow", "Ajuda"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetectar), _translate("MainWindow", "Detectar picos"))
        self.labelAdicionarPicos.setText(_translate("MainWindow", "Adicione até 5 picos (2theta graus):"))
        self.comboBoxPico1.setItemText(0, _translate("MainWindow", "Vazio"))
        self.comboBoxPico2.setItemText(0, _translate("MainWindow", "Vazio"))
        self.comboBoxPico3.setItemText(0, _translate("MainWindow", "Vazio"))
        self.comboBoxPico4.setItemText(0, _translate("MainWindow", "Vazio"))
        self.comboBoxPico5.setItemText(0, _translate("MainWindow", "Vazio"))
        self.labelSelecionarXlsx.setText(_translate("MainWindow", "Selecione o arquivo .xlsx:"))
        self.botaoSelecionarArquivoXlsx.setText(_translate("MainWindow", "Selecionar arquivo"))
        self.labelCaminhoXlsx.setText(_translate("MainWindow", "O caminho aparecerá aqui quando selecionado"))
        self.botaoComparar_2.setText(_translate("MainWindow", "Comparar"))
        self.labelSelecCIF_2.setText(_translate("MainWindow", "Selecione a pasta com os CIFs:"))
        self.botaoSelecCIF_2.setText(_translate("MainWindow", "Selecionar pasta"))
        self.labelCaminhoCIFs_2.setText(_translate("MainWindow", "O caminho aparecerá aqui quando selecionado"))
        self.labelSelecRadiacao_2.setText(_translate("MainWindow", "Selecione a radiação característica (Em angstrons):"))
        self.commandLinkButtonAjuda_3.setText(_translate("MainWindow", "Ajuda"))
        self.caixaRadiacoes_2.setItemText(0, _translate("MainWindow", "1,540598"))
        self.caixaRadiacoes_2.setItemText(1, _translate("MainWindow", "1,544426"))
        self.caixaRadiacoes_2.setItemText(2, _translate("MainWindow", "1,542512"))
        self.caixaRadiacoes_2.setItemText(3, _translate("MainWindow", "CuKa"))
        self.caixaRadiacoes_2.setItemText(4, _translate("MainWindow", "CuKa1"))
        self.caixaRadiacoes_2.setItemText(5, _translate("MainWindow", "CuKa2"))
        self.caixaRadiacoes_2.setItemText(6, _translate("MainWindow", "CuKb1"))
        self.caixaRadiacoes_2.setItemText(7, _translate("MainWindow", "CoKb1"))
        self.caixaRadiacoes_2.setItemText(8, _translate("MainWindow", "CoKa1"))
        self.caixaRadiacoes_2.setItemText(9, _translate("MainWindow", "CoKa2"))
        self.caixaRadiacoes_2.setItemText(10, _translate("MainWindow", "CoKa"))
        self.caixaRadiacoes_2.setItemText(11, _translate("MainWindow", "FeKb1"))
        self.caixaRadiacoes_2.setItemText(12, _translate("MainWindow", "FeKa1"))
        self.caixaRadiacoes_2.setItemText(13, _translate("MainWindow", "FeKa2"))
        self.caixaRadiacoes_2.setItemText(14, _translate("MainWindow", "FeKa"))
        self.caixaRadiacoes_2.setItemText(15, _translate("MainWindow", "CrKb1"))
        self.caixaRadiacoes_2.setItemText(16, _translate("MainWindow", "CrKa1"))
        self.caixaRadiacoes_2.setItemText(17, _translate("MainWindow", "CrKa2"))
        self.caixaRadiacoes_2.setItemText(18, _translate("MainWindow", "CrKa"))
        self.caixaRadiacoes_2.setItemText(19, _translate("MainWindow", "MoKa"))
        self.caixaRadiacoes_2.setItemText(20, _translate("MainWindow", "MoKa1"))
        self.caixaRadiacoes_2.setItemText(21, _translate("MainWindow", "MoKa2"))
        self.caixaRadiacoes_2.setItemText(22, _translate("MainWindow", "MoKb1"))
        self.caixaRadiacoes_2.setItemText(23, _translate("MainWindow", "AgKa"))
        self.caixaRadiacoes_2.setItemText(24, _translate("MainWindow", "AgKa1"))
        self.caixaRadiacoes_2.setItemText(25, _translate("MainWindow", "AgKa2"))
        self.caixaRadiacoes_2.setItemText(26, _translate("MainWindow", "AgKb1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompararPoucosPicos), _translate("MainWindow", "Comparar poucos picos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAjuda), _translate("MainWindow", "Ajuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())