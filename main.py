import random
import sys


from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setupUi()
        self.flag = False
        self.pushButton.clicked.connect(self.run)
        
    def setupUi(self):
        self.pushButton = self.findChild(QPushButton, 'pushButton')
        

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_rnd_circles(qp)
            qp.end()

    def run(self):
        self.flag = True
        self.repaint()

    def draw_rnd_circles(self, qp):
        x = random.randint(110, 450)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(100, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
