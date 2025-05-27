from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt


class HaloFaceWindow(QDialog):
    def __init__(self, parent=None, gif_path="halo_face.gif"):
        super().__init__(parent)
        self.setWindowTitle("Halo's Face")
        self.setFixedSize(300, 300)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 300, 300)

        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()

        # Try to place to the right of the main window
        if parent:
            x = parent.x() + parent.width() + 20
            y = parent.y()
            self.move(x, y)


def show_halo_face(parent=None):
    face_window = HaloFaceWindow(parent)
    face_window.show()
    return face_window
