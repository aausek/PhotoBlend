from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
import os
import wsl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("PhotoBlend")
        #self.setStyleSheet("background:black")
        self.preview = QLabel(self)
        self.preview.setStyleSheet("border: 1px solid black")
        #self.preview.setPixmap(QPixmap("Alex.jpg"))
        #self.preview.setGeometry(1000, 100, 1000, self.preview.pixmap().height())
        self.preview.setGeometry(1000, 50, 800, 800)
        self.temp_label = QLabel(self)
        self.temp_label.setText("Image Preview")
        self.temp_label.setGeometry(1350, 400, 100, 100)
        self.labels()
        self.buttons()
        self.checkboxes()
        self.sliders()
        self.show()

    def labels(self):
        self.blend_label = QLabel(self)
        self.blend_label.setText("Blending Modes")
        #self.blend_label.setStyleSheet("color:white")
        self.blend_label.setGeometry(25, 100, 150, 30)


    def buttons(self):
        self.file_select1 = QPushButton("Select the first image", self)
        self.file_select1.setGeometry(25, 25, 300, 30)
        self.file_select1.clicked.connect(self.clicked)

        self.file_select2 = QPushButton("Select the second image", self)
        self.file_select2.setGeometry(25, 150, 300, 30)
        self.file_select2.clicked.connect(self.clicked)

        self.rotate_button = QPushButton(self)
        self.rotate_button.setText("Rotate Clockwise")
        self.rotate_button.setGeometry(25, 900, 150, 30)

        self.save_button = QPushButton("Save image", self)
        self.save_button.setGeometry(1350, 900, 100, 30)


    def checkboxes(self):
        self.add_checkbox = QCheckBox(self, "Add")
        self.add_checkbox.setText("Add")
        self.add_checkbox.setGeometry(25, 200, 150, 30)

        self.subtract_checkbox = QCheckBox(self, "Subtract")
        self.subtract_checkbox.setText("Subtract")
        self.subtract_checkbox.setGeometry(75, 200, 150, 30)

        self.mult_checkbox = QCheckBox(self, "Multiply")
        self.mult_checkbox.setText("Multiply")
        self.mult_checkbox.setGeometry(150, 200, 150, 30)

        self.screen_checkbox = QCheckBox(self, "Screen")
        self.screen_checkbox.setText("Screen")
        self.screen_checkbox.setGeometry(225, 200, 150, 30)

        self.overlay_checkbox = QCheckBox(self, "Overlay")
        self.overlay_checkbox.setText("Overlay")
        self.overlay_checkbox.setGeometry(300, 200, 150, 30)

        self.light_checkbox = QCheckBox(self, "Lighten")
        self.light_checkbox.setText("Lighten")
        self.light_checkbox.setGeometry(25, 250, 150, 30)

        self.dark_checkbox = QCheckBox(self, "Darken")
        self.dark_checkbox.setText("Darken")
        self.dark_checkbox.setGeometry(100, 250, 150, 30)

        self.dodge_checkbox = QCheckBox(self, "Color Dodge")
        self.dodge_checkbox.setText("Color Dodge")
        self.dodge_checkbox.setGeometry(175, 250, 150, 30)

        self.dark_checkbox = QCheckBox(self, "Color Burn")
        self.dark_checkbox.setText("Color Burn")
        self.dark_checkbox.setGeometry(275, 250, 150, 30)

        self.crop_checkbox = QCheckBox(self, "Crop")
        self.crop_checkbox.setText("Crop")
        self.crop_checkbox.setGeometry(25, 350, 150, 30)

        self.gray_checkbox = QCheckBox(self, "Gray Scale")
        self.gray_checkbox.setText("Gray Scale")
        self.gray_checkbox.setGeometry(25, 500, 150, 30)

        self.gray_checkbox = QCheckBox(self, "Filters")
        self.gray_checkbox.setText("Filters")
        self.gray_checkbox.setGeometry(25, 700, 150, 30)


    def sliders(self):
        self.gray_slider = QSlider(Qt.Horizontal, self)
        self.gray_slider.setRange(0, 255)
        self.gray_slider.setTickInterval(1)
        self.gray_slider.setGeometry(25, 600, 150, 30)


    def clicked(self):
            self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())


if __name__ == '__main__':
    #wsl.set_display_to_host()
    app = QApplication(sys.argv)
    window = Window()
    browse1 = QPushButton
    sys.exit(app.exec_())