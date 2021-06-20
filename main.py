from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
#import os
#import wsl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setGeometry(0, 0, 1300, 800)
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
        self.setMaximumHeight(2000)
        self.setMaximumWidth(2000)
        self.setWindowTitle("PhotoBlend")
        #self.setStyleSheet("background:black")
        self.labels()
        self.buttons()
        self.checkboxes()
        self.sliders()
        self.setIcon()
        self.show()

        self.images_selected = {"image1": False, "image2": False}       

        
    def labels(self):
        self.pane_label = QLabel(self)
        self.pane_label.setStyleSheet("border: 1px solid black")
        self.pane_label.setGeometry(600, 50, 500, 500)

        self.preview_label = QLabel(self)
        self.preview_label.setText("Image preview")
        self.preview_label.setGeometry(800, 0, 100, 25)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Blending Modes")
        #self.blend_label.setStyleSheet("color:white")
        self.blend_label.setGeometry(137, 150, 150, 30)


    def buttons(self):
        self.file_select1 = QPushButton("Select the first image", self)
        self.file_select1.setGeometry(25, 25, 300, 30)
        self.file_select1.clicked.connect(self.image1_clicked)

        self.file_select2 = QPushButton("Select the second image", self)
        self.file_select2.setGeometry(25, 100, 300, 30)
        self.file_select2.clicked.connect(self.image2_clicked)

        self.blend = QPushButton("Blend Images", self)
        self.blend.setGeometry(25, 350, 300, 30)
        self.blend.clicked.connect(self.blend_clicked)
        
        self.rotate_button = QPushButton(self)
        self.rotate_button.setText("Rotate Clockwise")
        self.rotate_button.setGeometry(25, 750, 150, 30)

        self.save_button = QPushButton("Save image", self)
        self.save_button.setGeometry(800, 600, 100, 30)


    def checkboxes(self):
        self.add_checkbox = QCheckBox(self, "Add")
        self.add_checkbox.setText("Add")
        self.add_checkbox.setGeometry(25, 200, 150, 30)
        self.subtract_checkbox = QCheckBox(self, "Subtract")
        self.subtract_checkbox.setText("Subtract")
        self.subtract_checkbox.setGeometry(125, 200, 150, 30)

        self.mult_checkbox = QCheckBox(self, "Multiply")
        self.mult_checkbox.setText("Multiply")
        self.mult_checkbox.setGeometry(225, 200, 150, 30)

        self.screen_checkbox = QCheckBox(self, "Screen")
        self.screen_checkbox.setText("Screen")
        self.screen_checkbox.setGeometry(25, 250, 150, 30)

        self.overlay_checkbox = QCheckBox(self, "Overlay")
        self.overlay_checkbox.setText("Overlay")
        self.overlay_checkbox.setGeometry(125, 250, 150, 30)

        self.light_checkbox = QCheckBox(self, "Lighten")
        self.light_checkbox.setText("Lighten")
        self.light_checkbox.setGeometry(225, 250, 150, 30)

        self.dark_checkbox = QCheckBox(self, "Darken")
        self.dark_checkbox.setText("Darken")
        self.dark_checkbox.setGeometry(25, 300, 150, 30)

        self.dodge_checkbox = QCheckBox(self, "Color Dodge")
        self.dodge_checkbox.setText("Color Dodge")
        self.dodge_checkbox.setGeometry(125, 300, 150, 30)

        self.burn_checkbox = QCheckBox(self, "Color Burn")
        self.burn_checkbox.setText("Color Burn")
        self.burn_checkbox.setGeometry(225, 300, 150, 30)

        self.crop_checkbox = QCheckBox(self, "Crop")
        self.crop_checkbox.setText("Crop")
        self.crop_checkbox.setGeometry(25, 450, 150, 30)

        self.gray_checkbox = QCheckBox(self, "Gray Scale")
        self.gray_checkbox.setText("Gray Scale")
        self.gray_checkbox.setGeometry(25, 500, 150, 30)

        self.filters_checkbox = QCheckBox(self, "Filters")
        self.filters_checkbox.setText("Filters")
        self.filters_checkbox.setGeometry(25, 700, 150, 30)


    def sliders(self):
        self.gray_slider = QSlider(Qt.Horizontal, self)
        self.gray_slider.setRange(0, 255)
        self.gray_slider.setTickInterval(1)
        self.gray_slider.setGeometry(25, 550, 150, 30)
        

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


    def image1_clicked(self):
        self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())
        self.pane_label.setPixmap(QPixmap(self.image1[0]))
        self.pane_label.setGeometry(800, 100, self.pane_label.pixmap().width(), self.pane_label.pixmap().height())
        self.images_selected["image1"] = True


    def image2_clicked(self):
        self.image2 = QFileDialog.getOpenFileName(self, "Image 2", QDir.homePath())
        self.pane_label.setPixmap(QPixmap(self.image2[0]))
        self.pane_label.setGeometry(700, 100, self.pane_label.pixmap().width(), self.pane_label.pixmap().height())
        self.images_selected["image1"] = True
        
        
    def num_checkboxes_selected(self):
        clicked_counter = 0
        if self.add_checkbox.isChecked():
            clicked_counter += 1
        if self.subtract_checkbox.isChecked():
            clicked_counter += 1
        if self.mult_checkbox.isChecked():
            clicked_counter += 1
        if self.screen_checkbox.isChecked():
            clicked_counter += 1
        if self.overlay_checkbox.isChecked():
            clicked_counter += 1
        if self.light_checkbox.isChecked():
            clicked_counter += 1
        if self.dark_checkbox.isChecked():
            clicked_counter += 1
        if self.dodge_checkbox.isChecked():
            clicked_counter += 1
        if self.burn_checkbox.isChecked():
            clicked_counter += 1

        return clicked_counter
        

    def blend_clicked(self):
        # check that two images have been selected
        if not self.images_selected["image1"] or not self.images_selected["image2"]:
            msgBox = QMessageBox()
            msgBox.setText("Ensure two images are selected to blend.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        # check for number of blending modes selected
        # this can be updated if certain blending modes are not mutually exclusive
        num_checkboxes = self.num_checkboxes_selected()
        if num_checkboxes == 0:
            msgBox = QMessageBox()
            msgBox.setText("Select a blending mode to blend images.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        elif num_checkboxes > 1:
            msgBox = QMessageBox()
            msgBox.setText("You can only use one blending mode at a time.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()
        else:
            pass


    def crop_clicked(self):
        pass


    def grayscale_clicked(self):
        pass


    def filters_clicked(self):
        pass


if __name__ == '__main__':
    #wsl.set_display_to_host()
    app = QApplication(sys.argv)
    window = Window()
    browse1 = QPushButton
    sys.exit(app.exec_())