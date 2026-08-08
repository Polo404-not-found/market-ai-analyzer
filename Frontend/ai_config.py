from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QComboBox, QDockWidget, QFormLayout, QLabel, QWidget

class AIConfigDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("AI Configuration", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        content = QWidget()
        layout = QFormLayout(content)
        self.language_box = QComboBox()
        self.language_box.addItems(["Español", "English"])
        layout.addRow(QLabel("Language:"), self.language_box)

        self.technicality_levels = QComboBox()
        self.technicality_levels.addItems(["Low", "Medium", "High"])
        layout.addRow(QLabel("Technicality Level:"), self.technicality_levels)

        self.setWidget(content)

    def get_configuration(self):
        return {"language": self.language_box.currentText(), "technicality_level": self.technicality_levels.currentText()}
