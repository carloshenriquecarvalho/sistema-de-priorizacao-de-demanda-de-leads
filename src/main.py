import src.domain.priorizacao as priorizacao
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QStringListModel
from src.ui.ui_janela_principal import Ui_MainWindow

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Sistema gerenciador de Demanda de Leads")

        self.modelo = QStringListModel(self)
        self.ui.listView.setModel(self.modelo)

        self.resultados = []

        self.ui.botao_calcular.clicked.connect(self.calcular)

    def calcular(self):
        nome_consultor = self.ui.input_vendedor.text().strip()
        quantidade_texto = self.ui.input_quantidade_de_leads.text().strip()
        conversao_texto = self.ui.input_conversao.text().strip()

        if not nome_consultor:
            QMessageBox.warning(self, "Campo Obrigatório", "Informe o nome do Vendedor")
            return

        try:
            quantidade = int(quantidade_texto)
            conversao = float(conversao_texto.replace(",", "."))
        except ValueError:
            QMessageBox.warning(
                self,
                "Dados inválidos",
                "Informe a quantidade de leads como número inteiro ",
                "e a taxa de conversão como um número real"
            )
            return

        if quantidade < 0 or not 0 <= conversao <= 100:
            QMessageBox.warning(
                self,
                "Dados inválidos.",
                "A quantidade de leads não pode ser negativa e ",
                "a conversão deve estar entre 0 e 100"
            )
            return

        etapa_vazia = self.ui.input_etapa_vazia.isChecked()
         
        resultado = priorizacao.calcular_pontuacao(
            nome_consultor=nome_consultor,
            etapa_novo_lead_vazia=etapa_vazia,
            quantidade_leads_ativos=quantidade,
            taxa_conversao=conversao
        )

        if not resultado["elegivel"]:
            QMessageBox.information(
                self,
                "Vendedor não elegível",
                f"O {nome_consultor} não está elegível a receber leads, "
                "pois a etapa NOVO LEAD não está vazia." 
            )
            return

        self.resultados.append(resultado)

        self.resultados.sort(
            key=lambda item: item["prioridade"],
            reverse=False
        )

        itens = [
            f"{item["nome"]} - "
            f"Prioridade: {item["prioridade"]:.2f}"
            for item in self.resultados
        ]

        self.modelo.setStringList(itens)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()

    sys.exit(app.exec())
