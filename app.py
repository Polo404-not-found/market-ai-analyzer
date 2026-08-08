import sys
import os
import ctypes
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget
from PySide6.QtGui import QIcon
from Frontend.control_panel import controlpanel
from Frontend.graphic_panel import candle_chart
from Frontend.ai_config import AIConfigDock

try:
    myappid = 'dev.market_ai_analyzer.system.1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market AI Analyzer")
        self.resize(1100, 650)

        icon_path = get_resource_path("Market_AI_Analyze.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.ai_config_dock = AIConfigDock(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.ai_config_dock)
        self.control_panel = controlpanel(ai_config_dock=self.ai_config_dock)
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
    
    icon_path = get_resource_path("Market_AI_Analyze.ico")
    app.setWindowIcon(QIcon(icon_path))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())