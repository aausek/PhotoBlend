from PySide2 import QtCore
from PySide2.QtCore import QDir
from PySide2.QtWidgets import QGridLayout, QApplication, QLabel, QWidget, QMainWindow, QFileDialog, QPushButton
from PySide2.QtGui import QPixmap
import sys
import os
import wsl

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("PhotoBlend")
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("Replace with image name inside project folder"))
        self.image.setGeometry(800, 0, self.image.pixmap().width(), self.image.pixmap().height())
        self.buttons()
        self.show()

    def buttons(self):
        self.button1 = QPushButton("Select the first image", self)
        self.button1.setGeometry(0, 0, 150, 30)
        self.button1.clicked.connect(self.clicked)
        self.button2 = QPushButton("Select the second image", self)
        self.button2.setGeometry(0, 0, 150, 30)
        self.button2.move(500, 0)
        self.button2.clicked.connect(self.clicked)

    def clicked(self):
            self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())

if __name__ == '__main__':
    #wsl.set_display_to_host()
    app = QApplication(sys.argv)
    window = Window()
    browse1 = QPushButton
    sys.exit(app.exec_())