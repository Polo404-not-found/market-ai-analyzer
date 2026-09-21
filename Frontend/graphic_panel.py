
import pyqtgraph as pg
from PySide6.QtCore import QPointF, QRectF, Slot
from PySide6.QtGui import QPainter, QPicture
from PySide6.QtWidgets import QVBoxLayout, QWidget


class CandleChartGenerator(pg.GraphicsObject):
    def __init__(self, data):
        super().__init__()
        self.data = data 
        self.picture = QPicture()
        self.generate_picture()

    def generate_picture(self):
        painter = QPainter(self.picture)
        candle_width = 0.3
        for timestamp, open_price, close_price, low_price, high_price in self.data:
            if close_price >= open_price:
                painter.setPen(pg.mkPen("#26a69a"))
                painter.setBrush(pg.mkBrush("#26a69a"))
            else:
                painter.setPen(pg.mkPen("#ef5350"))
                painter.setBrush(pg.mkBrush("#ef5350"))
                
            painter.drawLine(QPointF(timestamp, low_price), QPointF(timestamp, high_price))
            top_y = min(open_price, close_price)
            height = abs(close_price - open_price)
            painter.drawRect(QRectF(timestamp - candle_width, top_y, candle_width * 2, height))

        painter.end()

    def paint(self, painter, *args):
        painter.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QRectF(self.picture.boundingRect())
    
class CandleChart(QWidget):
    def __init__(self):
        super().__init__()

        self.graphic = pg.PlotWidget()
        self.graphic.setBackground('#1e1e1e')
        self.graphic.showGrid(x=True, y=True, alpha=0.3)

        layout = QVBoxLayout()
        layout.addWidget(self.graphic)
        self.setLayout(layout)

    @Slot(object, str, str)
    def receive_prices(self, data_list, _report, ticker):
        self.graphic.clear()
        self.graphic.setTitle(f"Financial analytics {ticker}", color='#ffffff', size='12pt')
        formatted_data = []
        
        if hasattr(data_list, "iterrows"):
            for index, (_, row) in enumerate(data_list.iterrows()):
                formatted_data.append((index, row['Open'], row['Close'], row['Low'], row['High']))

        elif isinstance(data_list, list):
            for index, row in enumerate(data_list):
                formatted_data.append((index, row['Open'], row['Close'], row['Low'], row['High']))

        if formatted_data:
            candles = CandleChartGenerator(formatted_data)
            self.graphic.addItem(candles)
            self.graphic.autoRange()