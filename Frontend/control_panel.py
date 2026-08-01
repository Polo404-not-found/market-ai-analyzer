from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QLineEdit, QTextBrowser
from PySide6.QtCore import Signal, Slot
from Backend.main import ControladorApp
from Backend.config import ConfigManager

class controlpanel(QWidget):
    analyze_signal = Signal(object, str, str)
    def __init__(self):
        super().__init__()
        self.controlador = ControladorApp()
        self.texto = QTextBrowser()
        self.button = QPushButton("Analizar")
        self.period = QComboBox()
        self.ticker = QLineEdit()
        ## Api
        self.input_api_key = QLineEdit()
        self.input_api_key.setEchoMode(QLineEdit.Password)
        self.input_api_key.setPlaceholderText("Pega tu gemini API key")
        key_guardada = ConfigManager.cargar_api_key()
        if key_guardada:
            self.input_api_key.setText(key_guardada)    

        self.texto.setPlaceholderText("Aqui se mostrara la informacion")
        self.ticker.setPlaceholderText("Ej: BTC-USD, AAPL, TSLA")
        self.period.addItems(["1d", "5d", "1mo", "3mo", "6mo", "1y", "max"])
        self.button.clicked.connect(self.ejecutar_analisis)

        layout_izquierdo =  QVBoxLayout()
        layout_izquierdo.addWidget(QLabel("Gemini API key:"))
        layout_izquierdo.addWidget(self.input_api_key)

        layout_izquierdo.addWidget(QLabel("Ticker: "))
        layout_izquierdo.addWidget(self.ticker)
        layout_izquierdo.addWidget(QLabel("Periodo: "))
        layout_izquierdo.addWidget(self.period)
        layout_izquierdo.addWidget(self.texto)
        layout_izquierdo.addWidget(self.button)

        self.setLayout(layout_izquierdo)

    @Slot()
    def ejecutar_analisis(self):
        api_key = self.input_api_key.text().strip()
        ticker = self.ticker.text().strip().upper()
        periodo = self.period.currentText()

        if not api_key or not ticker or not periodo:
            self.texto.setText("Por favor, completa todos los campos antes de analizar.")
            return
        ConfigManager.guardar_api_key(api_key)

        try:
            data_lista, reporte = self.controlador.Coordinar_Datos(ticker, periodo)
            self.texto.setMarkdown(reporte)
            self.analyze_signal.emit(data_lista, reporte, ticker)
        except ValueError as e:
            self.texto.setText(f"Error: {e}")
        except Exception as e:
            self.texto.setText(f"Error inesperado: {e}")
