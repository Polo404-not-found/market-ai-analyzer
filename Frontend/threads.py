from PySide6.QtCore import QThread, Signal

class analysis_thread(QThread):
    success = Signal(object, str, str)
    error = Signal(str)

    def __init__(self, controller, ticker, period):
        super().__init__()
        self.controller = controller
        self.ticker = ticker
        self.period = period

    def run(self):
        try:
            processed_data, report = self.controller.Coordinate_Data(self.ticker, self.period)
            self.success.emit(processed_data, report, self.ticker)
        except ValueError as e:
            self.error.emit(f"Error: {e}")
        except Exception as e:
            self.error.emit(f"Unexpected Crash: {e}")
