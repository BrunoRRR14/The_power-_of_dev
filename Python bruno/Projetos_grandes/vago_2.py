import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora com PyQt5")

        # Layout
        layout = QVBoxLayout()
        
         # Caixa de entrada
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Digite uma expressão (ex: 2 + 3 * 4)")
        layout.addWidget(self.entrada)

        # Botão
        self.botao = QPushButton("Calcular")
        self.botao.clicked.connect(self.calcular)
        layout.addWidget(self.botao)

        # Resultado
        self.resultado = QLabel("Resultado: ")
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def calcular(self):
        expressao = self.entrada.text()
        try:
            resultado = eval(expressao)
            self.resultado.setText(f"Resultado: {resultado}")
        except Exception as e:
            self.resultado.setText("Erro: expressão inválida.")



# Execução
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec_())