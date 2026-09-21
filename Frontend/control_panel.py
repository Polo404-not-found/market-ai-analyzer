from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from Backend.config import ConfigManager
from Backend.main import AppController
from Frontend.ai_config import AIConfigDock
from Frontend.threads import AnalysisThread


class ControlPanel(QWidget):
    analyze_signal = Signal(object, str, str)

    def __init__(self, ai_config_dock: AIConfigDock, parent=None):
        super().__init__(parent)
        self.controller = AppController()
        self.text = QTextBrowser()
        self.button = QPushButton("Analyze")
        self.period = QComboBox()
        self.ticker = QLineEdit()
        self.ai_config_dock = ai_config_dock

        self.input_api_key = QLineEdit()
        self.input_api_key.setEchoMode(QLineEdit.Password)
        self.input_api_key.setPlaceholderText("You'r API key")
        save_key = ConfigManager.load_api_key()
        if save_key:
            self.input_api_key.setText(save_key)    

        self.text.setPlaceholderText("You'r info will be displayed here")
        self.ticker.setPlaceholderText("Ej: BTC-USD, AAPL, TSLA")
        self.period.addItems(["1d", "5d", "1mo", "3mo", "6mo", "1y", "max"])
        self.button.clicked.connect(self.analyze)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Gemini API key:"))
        left_layout.addWidget(self.input_api_key)

        left_layout.addWidget(QLabel("Ticker: "))
        left_layout.addWidget(self.ticker)
        left_layout.addWidget(QLabel("Periodo: "))
        left_layout.addWidget(self.period)
        left_layout.addWidget(self.text)
        left_layout.addWidget(self.button)

        self.setLayout(left_layout)

    @Slot()
    def analyze(self):
        api_key = self.input_api_key.text().strip()
        ticker = self.ticker.text().strip().upper()
        period = self.period.currentText()

        if not api_key or not ticker or not period:
            self.text.setText("Please fill in all fields.")
            return

        ai_config = {}
        if self.ai_config_dock:
            ai_config = self.ai_config_dock.get_configuration()
        language = ai_config.get("language", "English")
        technicality_level = ai_config.get("technicality_level", "Medium")

        ConfigManager.save_api_key(api_key)

        self.button.setEnabled(False)
        self.button.setText("Analysing...")
        self.text.setText("Analysing data, please wait...")

        self.worker_thread = AnalysisThread(self.controller, ticker, period, language, technicality_level)
        self.worker_thread.success.connect(self.on_analysis_success)
        self.worker_thread.error.connect(self.on_analysis_error)
        self.worker_thread.start()


    @Slot(object, str, str)
    def on_analysis_success(self, processed_data, report, ticker):
        self.text.setMarkdown(report)
        self.analyze_signal.emit(processed_data, report, ticker)
        self.button.setEnabled(True)
        self.button.setText("Analyze")

    @Slot(str)
    def on_analysis_error(self, error_message):
        self.text.setText(error_message)
        self.button.setEnabled(True)
        self.button.setText("Analyze")