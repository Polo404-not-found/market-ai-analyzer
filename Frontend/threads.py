from PySide6.QtCore import QThread, Signal

class analysis_thread(QThread):
    success = Signal(object, str, str)
    error = Signal(str)

    def __init__(self, controller, ticker, period, language = "English", technicality_level = "Medium"):
        super().__init__()
        self.controller = controller
        self.ticker = ticker
        self.period = period
        self.language = language
        self.technicality = technicality_level

    def run(self):
        try:
            processed_data, report = self.controller.Coordinate_Data(self.ticker, self.period, self.language, self.technicality)
            self.success.emit(processed_data, report, self.ticker)
        except ValueError as e:
            self.error.emit(f"Error: {e}")
        except Exception as e:
            self.error.emit(f"Unexpected Crash: {e}")
