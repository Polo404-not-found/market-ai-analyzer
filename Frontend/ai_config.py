import webbrowser

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QComboBox,
    QDockWidget,
    QFormLayout,
    QLabel,
    QPushButton,
    QWidget,
)


class AIConfigDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("AI Configuration", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        content = QWidget()
        layout = QFormLayout(content)
        self.language_box = QComboBox()
        self.language_box.addItems(["Español", "English",])
        layout.addRow(QLabel("Language:"), self.language_box)

        self.technicality_levels = QComboBox()
        self.technicality_levels.addItems(["Low", "Medium", "High"])
        layout.addRow(QLabel("Technicality Level:"), self.technicality_levels)

        self.api_button = QPushButton("Get API")
        self.api_button.clicked.connect(self.get_api)
        layout.addRow(QLabel("Get you'r API key"), self.api_button)

        self.setWidget(content)

    def get_configuration(self):
        return {"language": self.language_box.currentText(), "technicality_level": self.technicality_levels.currentText()}
    
    @Slot()
    def get_api(self):
        webbrowser.open("https://aistudio.google.com/api-keys?project=gen-lang-client-0110284720")
