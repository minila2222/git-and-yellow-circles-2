import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            color = QColor(circle[3], circle[4], circle[5])
            painter.setBrush(color)
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.circles.append((x, y, diameter, red, green, blue))
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.circle_widget = CircleWidget()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.button = QPushButton("Add Circle")
        self.button.clicked.connect(self.circle_widget.add_circle)

        layout.addWidget(self.circle_widget)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Random Circles")
        self.resize(800, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
