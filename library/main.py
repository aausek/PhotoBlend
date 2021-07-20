from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
#from library.library import call_blend
from library import call_blend
#from filters import grayscale
import sys
import os
import wsl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1300, 800)
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
        self.setMaximumHeight(1000)
        self.setMaximumWidth(1000)
        self.images_selected = {"image1": False, "image2": False}
        self.current_button = QRadioButton()
        self.setWindowTitle("PhotoBlend")
        self.labels()
        self.buttons()
        self.radio_buttons()
        self.setIcon()
        self.show()

        self.images_selected = {"image1": False, "image2": False}

        # persistence
        cwd = os.getcwd()
        # check if persistent data exists. If not, create file for it.
        filename = "persistentData.txt"
        self.persistentData = cwd + "/" + filename

        if not os.path.exists(filename):
            open(filename, 'w').close()


    def labels(self):
        if not self.images_selected["image1"] or not self.images_selected["image2"]:
            self.pane_label = QLabel(self)
            self.pane_label.setStyleSheet("border: 1px solid black")
            self.pane_label.setGeometry(400, 75, 500, 500)

        elif self.images_selected["image1"] and self.images_selected["image2"]:
            self.pane_label.close()
            self.pane_label1 = QLabel(self)
            self.pane_label1.setStyleSheet("border: 1px solid black")
            self.pane_label1.setGeometry(400, 75, 250, 250)
            self.pane_label1.setPixmap(
                self.pixmap1.scaled(self.pane_label1.width(), self.pane_label1.height(), QtCore.Qt.KeepAspectRatio))
            self.pane_label1.setVisible(True)

            self.pane_label2 = QLabel(self)
            self.pane_label2.setStyleSheet("border: 1px solid black")
            self.pane_label2.setGeometry(700, 75, 250, 250)
            self.pane_label2.setPixmap(
                self.pixmap2.scaled(self.pane_label2.width(), self.pane_label2.height(), QtCore.Qt.KeepAspectRatio))
            self.pane_label2.setVisible(True)

            self.pane_label3 = QLabel(self)
            self.pane_label3.setStyleSheet("border: 1px solid black")
            self.pane_label3.setGeometry(500, 350, 300, 300)
            self.pane_label3.setVisible(True)

        self.preview_label = QLabel(self)
        self.preview_label.setText("Image preview")
        self.preview_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: black;")
        self.preview_label.setGeometry(600, 25, 100, 25)

        self.blend_label = QLabel(self)
        self.blend_label.setText("Image Selection")
        self.blend_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: black;")
        self.blend_label.setGeometry(137, 25, 100, 30)

        self.modes_label = QLabel(self)
        self.modes_label.setText("Blending Modes")
        self.modes_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: black;")
        self.modes_label.setGeometry(137, 150, 100, 30)

        self.rotation_label = QLabel(self)
        self.rotation_label.setText("Image Rotations")
        self.rotation_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: black;")
        self.rotation_label.setGeometry(137, 650, 100, 30)

        self.options_label = QLabel(self)
        self.options_label.setText("Other Options")
        self.options_label.setStyleSheet(
            "border-bottom-width: 1px; border-bottom-style: solid;border-radius: 0px; border-color: black;")
        self.options_label.setGeometry(137, 400, 100, 30)

    def buttons(self):
        self.file_select1 = QPushButton("Select the first image", self)
        self.file_select1.setGeometry(75, 70, 200, 30)
        self.file_select1.clicked.connect(self.image1_clicked)

        self.file_select2 = QPushButton("Select the second image", self)
        self.file_select2.setGeometry(75, 100, 200, 30)
        self.file_select2.clicked.connect(self.image2_clicked)

        self.rotate_button = QPushButton("Rotate", self)
        self.rotate_button.setText("Rotate Clockwise")
        self.rotate_button.setGeometry(75, 700, 200, 30)
        self.rotate_button.clicked.connect(self.rotate_clicked)

        self.save_button = QPushButton("Save image", self)
        self.save_button.setGeometry(555, 700, 200, 30)
        self.save_button.clicked.connect(self.save_clicked)

    def radio_buttons(self):
        self.add_radio_button = QRadioButton(self, "Add")
        self.add_radio_button.setText("Add")
        self.add_radio_button.setGeometry(25, 200, 150, 30)
        self.add_radio_button.setToolTip('Addition of tonal values')
        self.add_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.subtract_radio_button = QRadioButton(self, "Subtract")
        self.subtract_radio_button.setText("Subtract")
        self.subtract_radio_button.setGeometry(125, 200, 150, 30)
        self.subtract_radio_button.setToolTip('Subtracts pixel values from image 1')
        self.subtract_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.mult_radio_button = QRadioButton(self, "Multiply")
        self.mult_radio_button.setText("Multiply")
        self.mult_radio_button.setGeometry(225, 200, 150, 30)
        self.mult_radio_button.setToolTip('Multiplies tonal values of the fore and background''s pixels')
        self.mult_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.screen_radio_button = QRadioButton(self, "Screen")
        self.screen_radio_button.setText("Screen")
        self.screen_radio_button.setGeometry(25, 250, 150, 30)
        self.screen_radio_button.setToolTip('Fore and background are negatively multiplied')
        self.screen_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.opacity_radio_button = QRadioButton(self, "Opacity")
        self.opacity_radio_button.setText("80% Opacity")
        self.opacity_radio_button.setGeometry(25, 350, 150, 30)
        self.opacity_radio_button.setToolTip('80% Transparency mode')
        self.opacity_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.redchannel_radio_button = QRadioButton(self, "Red Channel")
        self.redchannel_radio_button.setText("Red Channel")
        self.redchannel_radio_button.setGeometry(125, 350, 150, 30)
        self.redchannel_radio_button.setToolTip('Enhances red pixels from images')
        self.redchannel_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.overlay_radio_button = QRadioButton(self, "Overlay")
        self.overlay_radio_button.setText("Overlay")
        self.overlay_radio_button.setGeometry(125, 250, 150, 30)
        self.overlay_radio_button.setToolTip('Combination of Multiply and Screen modes')
        self.overlay_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.light_radio_button = QRadioButton(self, "Lighten")
        self.light_radio_button.setText("Lighten")
        self.light_radio_button.setGeometry(225, 250, 150, 30)
        self.light_radio_button.setToolTip('Takes the respective lighter pixel into the output image')
        self.light_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.dark_radio_button = QRadioButton(self, "Darken")
        self.dark_radio_button.setText("Darken")
        self.dark_radio_button.setGeometry(25, 300, 150, 30)
        self.dark_radio_button.setToolTip('Takes the respective darker pixel into the output image')
        self.dark_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.dodge_radio_button = QRadioButton(self, "Color Dodge")
        self.dodge_radio_button.setText("Color Dodge")
        self.dodge_radio_button.setGeometry(125, 300, 150, 30)
        self.dodge_radio_button.setToolTip('Enhances brightness of background based on foreground light')
        self.dodge_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.burn_radio_button = QRadioButton(self, "Color Burn")
        self.burn_radio_button.setText("Color Burn")
        self.burn_radio_button.setGeometry(225, 300, 150, 30)
        self.burn_radio_button.setToolTip('The background image is darkened by the foreground')
        self.burn_radio_button.clicked.connect(self.update_blend_radio_buttons)

        self.crop_radio_button = QRadioButton(self, "Crop")
        self.crop_radio_button.setText("Crop")
        self.crop_radio_button.setGeometry(150, 450, 150, 30)

        self.gray_radio_button = QRadioButton(self, "Gray Scale")
        self.gray_radio_button.setText("Gray Scale")
        self.gray_radio_button.setGeometry(150, 500, 150, 30)
        self.gray_radio_button.clicked.connect(self.grayscale_clicked)

        self.filters_radio_button = QRadioButton(self, "Filters")
        self.filters_radio_button.setText("Filters")
        self.filters_radio_button.setGeometry(150, 600, 150, 30)

    def update_blend_radio_buttons(self):
        # enable radio_buttons if one is deselected (meaning none are selected)
        self.add_radio_button.setCheckable(True)
        self.subtract_radio_button.setCheckable(True)
        self.mult_radio_button.setCheckable(True)
        self.screen_radio_button.setCheckable(True)
        self.opacity_radio_button.setCheckable(True)
        self.redchannel_radio_button.setCheckable(True)
        self.overlay_radio_button.setCheckable(True)
        self.light_radio_button.setCheckable(True)
        self.dark_radio_button.setCheckable(True)
        self.dodge_radio_button.setCheckable(True)
        self.burn_radio_button.setCheckable(True)
        self.pane_label3.clear()

        self.update_photo()

    def setIcon(self):
        appIcon = QIcon("./resources/icon.png")
        self.setWindowIcon(appIcon)

    def image1_clicked(self):
        self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())
        if self.image1[0] != '':  # don't update pane if user cancels file opening
            self.pixmap1 = QPixmap(self.image1[0])
            if self.images_selected["image2"]:
                self.pane_label1.setPixmap(
                    self.pixmap1.scaled(self.pane_label1.width(), self.pane_label1.height(), QtCore.Qt.KeepAspectRatio))
            else:
                self.pane_label.setPixmap(
                    self.pixmap1.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
            self.images_selected["image1"] = True

    def image2_clicked(self):
        self.image2 = QFileDialog.getOpenFileName(self, "Image 2", QDir.homePath())
        if self.image2[0] != '':  # don't update pane if user cancels file opening
            self.pixmap2 = QPixmap(self.image2[0])
            if self.pixmap2.width() != self.pixmap1.width() and self.pixmap2.height() != self.pixmap1.height():
                msgBox = QMessageBox()
                msgBox.setText("Images are not the same size.")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Warning")
                msgBox.exec_()
            else:
                self.pane_label.setPixmap(
                    self.pixmap2.scaled(self.pane_label.width(), self.pane_label.height(), QtCore.Qt.KeepAspectRatio))
                self.images_selected["image2"] = True
                self.labels()

    def update_photo(self):
        # check that two images have been selected
        if not self.images_selected["image1"] or not self.images_selected["image2"]:
            msgBox = QMessageBox()
            msgBox.setText("Ensure two images are selected to blend.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.exec_()

        image1_name = str(self.image1)
        image1_name = image1_name[2:]
        image2_name = str(self.image2)
        image2_name = image2_name[2:]
        image1_name = image1_name[:-19]
        image2_name = image2_name[:-19]

        # call blend functions below based on user selection
        # note that blend modes are mutually exclusive

        # addition blend
        if self.add_radio_button.isChecked():
            call_blend(image1_name, image2_name, "add")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")

        # subtraction blend
        elif self.subtract_radio_button.isChecked():
            call_blend(image1_name, image2_name, "subtract")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")

        # update below when the following functions are supported
        # multiply blend
        elif self.mult_radio_button.isChecked():
            call_blend(image1_name, image2_name, "multiply")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # screen blend
        elif self.screen_radio_button.isChecked():
            call_blend(image1_name, image2_name, "screen")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # opacity blend
        elif self.opacity_radio_button.isChecked():
            call_blend(image1_name, image2_name, "opacity")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # opacity blend
        elif self.redchannel_radio_button.isChecked():
            call_blend(image1_name, image2_name, "redchannel")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # overlay blend
        elif self.overlay_radio_button.isChecked():
            call_blend(image1_name, image2_name, "overlay")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # light blend
        elif self.light_radio_button.isChecked():
            call_blend(image1_name, image2_name, "lighten")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # dark blend
        elif self.dark_radio_button.isChecked():
            call_blend(image1_name, image2_name, "darken")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # color dodge blend
        elif self.dodge_radio_button.isChecked():
            call_blend(image1_name, image2_name, "color_dodge")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")
        # color burn blend
        elif self.burn_radio_button.isChecked():
            call_blend(image1_name, image2_name, "color_burn")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            #os.remove("test_image.jpg")

    def crop_clicked(self):
        pass

    def grayscale_clicked(self):
        image1_name = str(self.image1)
        image1_name = image1_name[2:]
        image1_name = image1_name[:-19]
        grayscale(image1_name)

    def save_clicked(self):
        save_name = QFileDialog.getSaveFileName(self, "Blended Image", QDir.homePath(), "Images (*.png *.xpm *.jpg)")
        if self.images_selected["image1"] and not self.images_selected["image2"]:
            QPixmap("test_image.jpg").save(save_name[0])
        else:
            QPixmap("test_image.jpg").save(save_name[0])

        # save created image's name in persistent data
        file = open(self.persistentData, 'a')
        file.write(save_name[0])
        file.close()

    def rotate_clicked(self):
        transform = QTransform().rotate(90.0)

        if self.images_selected["image1"] and not self.images_selected["image2"]:
            self.pane_label.setPixmap(self.pane_label.pixmap().transformed(transform))
        else:
            self.pane_label3.setPixmap(self.pane_label3.pixmap().transformed(transform))

    def filters_clicked(self):
        pass

    def main():
        wsl.set_display_to_host()
        app = QApplication(sys.argv)
        window = Window()
        browse1 = QPushButton
        sys.exit(app.exec_())


Window.main()