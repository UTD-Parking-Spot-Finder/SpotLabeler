from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap, QImage
from PySide2 import QtGui


class SpotViewWidget(QLabel):

    def __init__(self, mainWindow):
        QLabel.__init__(self)

        self.mainWindow = mainWindow

        self.setMinimumWidth(400)
        self.setMinimumHeight(600)

    def showImage(self, img):
        q_img = QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_img)
        self.setPixmap(pixmap)