import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLineEdit, QTextBrowser
from PySide6.QtCore import Slot 
from Backend.main import ControladorApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market AI Analyzer")
        self.controlador = ControladorApp()
        self.texto = QTextBrowser()
        self.button = QPushButton("Analizar")
        self.period = QComboBox()
        self.ticker = QLineEdit()

        self.texto.setPlaceholderText("Aqui se mostrara la informacion")
        
        self.ticker.setPlaceholderText("Ej: BTC-USD, AAPL, TSLA")

        self.period.addItems(["1d", "5d", "1mo", "3mo", "6mo", "1y", "max"])
        self.button.clicked.connect(self.ejecutar_analisis)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ticker: "))
        layout.addWidget(self.ticker)
        layout.addWidget(QLabel("Periodo: "))
        layout.addWidget(self.period)
        layout.addWidget(self.texto)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def ejecutar_analisis(self):
        ticker = self.ticker.text().strip().upper()
        periodo = self.period.currentText()


        if not ticker :
            self.label.setText("Por favor ingrese datros validos")
            return
        
        try:
            data_lista, reporte = self.controlador.Coordinar_Datos(ticker = ticker, periodo = periodo)
            self.texto.setMarkdown(reporte)
        except ValueError as e:
            self.label.setText(f"Error {e}")
        except Exception as e:
            self.label.setText(f"Ocurrio un error inesperado {e}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

