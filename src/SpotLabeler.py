import sys
from src.ImageLabel import ImageLabel
from src.SpotViewWidget import SpotViewWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QGroupBox, QHBoxLayout


class SpotLabeler(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Spot Labeler")

        widget = QWidget(self)
        layout = QGridLayout(widget)

        # Image Label
        self.imageLabel = ImageLabel(self)
        imageGroupBox = QGroupBox("Lot Image")
        imageLayout = QHBoxLayout()
        imageLayout.addWidget(self.imageLabel)
        imageGroupBox.setLayout(imageLayout)

        # Spot View
        self.spotView = SpotViewWidget(self)
        spotGroupBox = QGroupBox("Spot View")
        spotLayout = QHBoxLayout()
        spotLayout.addWidget(self.spotView)
        spotGroupBox.setLayout(spotLayout)

        layout.addWidget(imageGroupBox, 0, 0)
        layout.addWidget(spotGroupBox, 0, 1)
        #layout.addWidget(horizontalGroupBox, 1, 0, 1, 2)

        self.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    window = SpotLabeler()
    window.show()
    sys.exit(app.exec_())