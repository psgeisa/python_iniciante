import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

#janela principal
class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        #estrutura principal
        self.topo = 100 #distancia do topo
        self.esquerda = 200
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        #botão para consulta das minhas férias
        botaoA = QPushButton('Minhas Férias', self)
        botaoA.move(10, 10)
        botaoA.resize(100,40)
        botaoA.setStyleSheet('QPushButton {background-color:#5F9EA0; font: bold; font-size: 12px}')
        botaoA.clicked.connect(self.MinhasFerias)

        #botão para consulta de férias da minha equipe
        botaoB = QPushButton('Férias do Time', self)
        botaoB.move(130, 10)
        botaoB.resize(100,40)
        botaoB.setStyleSheet('QPushButton {background-color:#FFA500; font: bold; font-size: 12px}')
        botaoB.clicked.connect(self.FeriasEquipe)


        #rodar o programa
        self.CarregarJanela()
        
    def CarregarJanela (self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def MinhasFerias(self):
        print('Você quer consultar suas férias!')

    def FeriasEquipe(self):
        print('Você quer consultar as férias da equipe!')

app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())
