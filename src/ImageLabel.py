import cv2 as cv
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap, QImage
from PySide2 import QtGui

class ImageLabel(QLabel):

    def __init__(self, mainWindow):
        QLabel.__init__(self)

        self.mainWindow = mainWindow
        self.original = None
        self.currentMat = None

        self.setMinimumWidth(400)
        self.setMinimumHeight(300)

    def setImage(self, mat):
        self.original = mat
        self.currentMat = mat.copy()
        self.updateView()

    def updateView(self):
        if self.currentMat is None:
            return

        img = QImage(self.currentMat.data, self.currentMat.shape[1], self.currentMat.shape[0],
                     QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(img)
        self.setPixmap(pixmap)
        self.setMinimumHeight(self.currentMat.shape[0])
        self.setMinimumWidth(self.currentMat.shape[1])
        self.setMaximumHeight(self.currentMat.shape[0])
        self.setMaximumWidth(self.currentMat.shape[1])
        self.currentMat = self.original.copy()

    def drawConnectedPoints(self, points):
        if self.currentMat is None:
            return

        size = len(points)
        for i in range(0, size):
            pi = points[i]
            cv.circle(self.currentMat, (pi[0], pi[1]), 1, (0, 255, 0), 2)
            if i > 0:
                cv.line(self.currentMat, points[i], points[i-1], (0, 255, 0))

        if size == 4:
            cv.line(self.currentMat, points[0], points[3], (0, 255, 0))