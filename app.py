from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from Frontend.control_panel import controlpanel
from Frontend.graphic_panel import candle_chart
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market AI Analyzer")
        self.resize(1100, 650)

        self.control_panel = controlpanel()
        self.candle_chart = candle_chart()

        self.control_panel.analyze_signal.connect(self.candle_chart.recieve_data)

        layout = QHBoxLayout()
        layout.addWidget(self.control_panel, stretch=1)
        layout.addWidget(self.candle_chart, stretch=2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())