from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1024,980)
        self.setMinimumSize(600,500)
        self.setWindowOpacity(0.9)
        self.setWindowTitle("Aras: Analysis Reoprting And Simulation")
app=QApplication(sys.argv)
Window=Mywindow()
Window.show()
sys.exit(app.exec())
