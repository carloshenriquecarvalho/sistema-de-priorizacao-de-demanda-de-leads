from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QMainWindow
from src.domain.priorizacao import calcular_priorizacao

app = QApplication()
window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
layout = QGridLayout()

central_widget.setLayout(layout)

botao = QPushButton("Texto do botão")

def exemplo_slot(status_bar):
    status_bar.showMessage("Nova Mensagem")

# bar
status_bar = window.statusBar()
status_bar.showMessage("Mensagem")

# menu
menu_bar = window.menuBar()
primeiro_menu = menu_bar.addMenu("Menu")
acao = primeiro_menu.addAction("Acao 1")
acao.triggered.connect(lambda: exemplo_slot(status_bar))

layout.addWidget(botao, 1, 1)

window.show()
app.exec()