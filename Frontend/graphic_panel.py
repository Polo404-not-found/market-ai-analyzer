from operator import index

import pyqtgraph as pg
from PySide6.QtGui import QPicture, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Slot, QPointF, QRectF 

class candle_chart_generator(pg.GraphicsObject):
    def __init__(self, data):
        super().__init__()
        self.data = data 
        self.picture = QPicture()
        self.generate_picture()

    def generate_picture(self):
        p = QPainter(self.picture)
        w = 0.3
        for t, open_p, close_p, low_p, high_p in self.data:
            if close_p >= open_p:
                p.setPen(pg.mkPen("#26a69a"))
                p.setBrush(pg.mkBrush("#26a69a"))
            else:
                p.setPen(pg.mkPen("#ef5350"))
                p.setBrush(pg.mkBrush("#ef5350"))
                
            p.drawLine(QPointF(t, low_p), QPointF(t, high_p))
            top_y = min(open_p, close_p)
            height = abs(close_p - open_p)
            p.drawRect(QRectF(t - w, top_y, w * 2, height))

        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QRectF(self.picture.boundingRect())
    
class candle_chart(QWidget):
    def __init__(self):
        super().__init__()

        self.graphic = pg.PlotWidget()
        self.graphic.setBackground('#1e1e1e')
        self.graphic.showGrid(x=True, y=True, alpha=0.3)

        layout = QVBoxLayout()
        layout.addWidget(self.graphic)
        self.setLayout(layout)

    @Slot(object, str, str)
    def recieve_data(self, data_lista, report, ticker):
        self.graphic.clear()
        self.graphic.setTitle(f"Financial analytics {ticker}", color='#ffffff', size='12pt')
        formatted_data = []
        
        if hasattr(data_lista, "iterrows"):
            for idx, (index, row) in enumerate(data_lista.iterrows()):
                formatted_data.append((idx, row['Open'], row['Close'], row['Low'], row['High']))

        elif isinstance(data_lista, list):
            for idx, row in enumerate(data_lista):
                formatted_data.append((idx, row['Open'], row['Close'], row['Low'], row['High']))

        if formatted_data:
            velas = candle_chart_generator(formatted_data)
            self.graphic.addItem(velas)
            self.graphic.autoRange()