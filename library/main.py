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
        self.setWindowTitle("PhotoBlend")
        self.labels()
        self.buttons()
        self.checkboxes()
        self.setIcon()
        self.show()

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

    def checkboxes(self):
        self.add_checkbox = QCheckBox(self, "Add")
        self.add_checkbox.setText("Add")
        self.add_checkbox.setGeometry(25, 200, 150, 30)
        self.add_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.subtract_checkbox = QCheckBox(self, "Subtract")
        self.subtract_checkbox.setText("Subtract")
        self.subtract_checkbox.setGeometry(125, 200, 150, 30)
        self.subtract_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.mult_checkbox = QCheckBox(self, "Multiply")
        self.mult_checkbox.setText("Multiply")
        self.mult_checkbox.setGeometry(225, 200, 150, 30)
        self.mult_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.screen_checkbox = QCheckBox(self, "Screen")
        self.screen_checkbox.setText("Screen")
        self.screen_checkbox.setGeometry(25, 250, 150, 30)
        self.screen_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.overlay_checkbox = QCheckBox(self, "Overlay")
        self.overlay_checkbox.setText("Overlay")
        self.overlay_checkbox.setGeometry(125, 250, 150, 30)
        self.overlay_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.light_checkbox = QCheckBox(self, "Lighten")
        self.light_checkbox.setText("Lighten")
        self.light_checkbox.setGeometry(225, 250, 150, 30)
        self.light_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.dark_checkbox = QCheckBox(self, "Darken")
        self.dark_checkbox.setText("Darken")
        self.dark_checkbox.setGeometry(25, 300, 150, 30)
        self.dark_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.dodge_checkbox = QCheckBox(self, "Color Dodge")
        self.dodge_checkbox.setText("Color Dodge")
        self.dodge_checkbox.setGeometry(125, 300, 150, 30)
        self.dodge_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.burn_checkbox = QCheckBox(self, "Color Burn")
        self.burn_checkbox.setText("Color Burn")
        self.burn_checkbox.setGeometry(225, 300, 150, 30)
        self.burn_checkbox.stateChanged.connect(self.update_blend_checkboxes)

        self.crop_checkbox = QCheckBox(self, "Crop")
        self.crop_checkbox.setText("Crop")
        self.crop_checkbox.setGeometry(150, 450, 150, 30)

        self.gray_checkbox = QCheckBox(self, "Gray Scale")
        self.gray_checkbox.setText("Gray Scale")
        self.gray_checkbox.setGeometry(150, 500, 150, 30)
        self.gray_checkbox.stateChanged.connect(self.grayscale_clicked)

        self.filters_checkbox = QCheckBox(self, "Filters")
        self.filters_checkbox.setText("Filters")
        self.filters_checkbox.setGeometry(150, 600, 150, 30)

    def update_blend_checkboxes(self):
        # enable checkboxes if one is deselected (meaning none are selected)
        if self.num_checkboxes_selected() == 0:
            self.add_checkbox.setCheckable(True)
            self.subtract_checkbox.setCheckable(True)
            self.mult_checkbox.setCheckable(True)
            self.screen_checkbox.setCheckable(True)
            self.overlay_checkbox.setCheckable(True)
            self.light_checkbox.setCheckable(True)
            self.dark_checkbox.setCheckable(True)
            self.dodge_checkbox.setCheckable(True)
            self.burn_checkbox.setCheckable(True)

        # otherwise, disable all non-checked blend checkboxes
        else:
            if not self.add_checkbox.isChecked():
                self.add_checkbox.setCheckable(False)
            if not self.subtract_checkbox.isChecked():
                self.subtract_checkbox.setCheckable(False)
            if not self.mult_checkbox.isChecked():
                self.mult_checkbox.setCheckable(False)
            if not self.screen_checkbox.isChecked():
                self.screen_checkbox.setCheckable(False)
            if not self.overlay_checkbox.isChecked():
                self.overlay_checkbox.setCheckable(False)
            if not self.light_checkbox.isChecked():
                self.light_checkbox.setCheckable(False)
            if not self.dark_checkbox.isChecked():
                self.dark_checkbox.setCheckable(False)
            if not self.dodge_checkbox.isChecked():
                self.dodge_checkbox.setCheckable(False)
            if not self.burn_checkbox.isChecked():
                self.burn_checkbox.setCheckable(False)
        self.update_photo()

    def setIcon(self):
        appIcon = QIcon("./resources/icon.png")
        self.setWindowIcon(appIcon)

    def image1_clicked(self):
        self.image1 = QFileDialog.getOpenFileName(self, "Image 1", QDir.homePath())
        if self.image1[0] != '':  # don't update pane if user cancels file opening
            self.pixmap1 = QPixmap(self.image1[0])
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

    def update_photo(self):
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
        # if num_checkboxes == 0:
        #     msgBox = QMessageBox()
        #     msgBox.setText("Select a blending mode to blend images.")
        #     msgBox.setIcon(QMessageBox.Warning)
        #     msgBox.setWindowTitle("Warning")
        #     msgBox.exec_()
        # elif num_checkboxes > 1:
        #     msgBox = QMessageBox()
        #     msgBox.setText("You can only use one blending mode at a time.")
        #     msgBox.setIcon(QMessageBox.Warning)
        #     msgBox.setWindowTitle("Warning")
        #     msgBox.exec_()
        # else:
        image1_name = str(self.image1)
        image1_name = image1_name[2:]
        image2_name = str(self.image2)
        image2_name = image2_name[2:]
        image1_name = image1_name[:-19]
        image2_name = image2_name[:-19]

        # call blend functions below based on user selection
        # note that blend modes are mutually exclusive

        # addition blend
        if self.add_checkbox.isChecked():
            call_blend(image1_name, image2_name, "add")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")

        # subtraction blend
        elif self.subtract_checkbox.isChecked():
            call_blend(image1_name, image2_name, "subtract")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")

            # update below when the following functions are supported
            # multiply blend
        elif self.mult_checkbox.isChecked():
            call_blend(image1_name, image2_name, "multiply")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # screen blend
        elif self.screen_checkbox.isChecked():
            call_blend(image1_name, image2_name, "screen")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # overlay blend
        elif self.overlay_checkbox.isChecked():
            call_blend(image1_name, image2_name, "overlay")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # light blend
        elif self.light_checkbox.isChecked():
            call_blend(image1_name, image2_name, "lighten")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # dark blend
        elif self.dark_checkbox.isChecked():
            call_blend(image1_name, image2_name, "darken")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # color dodge blend
        elif self.dodge_checkbox.isChecked():
            call_blend(image1_name, image2_name, "color_dodge")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")
        # color burn blend
        elif self.burn_checkbox.isChecked():
            call_blend(image1_name, image2_name, "color_burn")
            result = QPixmap("test_image.jpg")
            self.pane_label3.setPixmap(
                result.scaled(self.pane_label3.width(), self.pane_label3.height(), QtCore.Qt.KeepAspectRatio))
            os.remove("test_image.jpg")

    def crop_clicked(self):
        pass

    def grayscale_clicked(self):
        image1_name = str(self.image1)
        image1_name = image1_name[2:]
        image1_name = image1_name[:-19]
        grayscale(image1_name)

    def save_clicked(self):
        save_name = QFileDialog.getSaveFileName(self, "Blended Image", QDir.homePath(), "Images (*.png *.xpm *.jpg)")
        self.pane_label.pixmap().save(save_name[0])

    def rotate_clicked(self):
        transform = QTransform().rotate(90.0)
        self.pane_label.setPixmap(self.pane_label.pixmap().transformed(transform))

    def filters_clicked(self):
        pass

    def main():
        wsl.set_display_to_host()
        app = QApplication(sys.argv)
        window = Window()
        browse1 = QPushButton
        sys.exit(app.exec_())

Window.main()

# if __name__ == '__main__':
#     wsl.set_display_to_host()
#     app = QApplication(sys.argv)
#     window = Window()
#     browse1 = QPushButton
#     sys.exit(app.exec_())
