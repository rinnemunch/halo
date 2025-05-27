from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt
import os


class HaloFaceWindow(QDialog):
    def __init__(self, parent=None, gif_path="Gifs/halo_face_v2.gif"):
        super().__init__(parent)
        self.setWindowTitle("Halo's Face")
        self.setFixedSize(300, 300)

        print(f"[DEBUG] Looking for: {os.path.abspath(gif_path)}")
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 300, 300)

        self.movie = QMovie(gif_path)
        print(f"[DEBUG] Movie valid: {self.movie.isValid()}")
        self.label.setMovie(self.movie)
        self.movie.start()

        if parent:
            x = parent.x() + parent.width() + 20
            y = parent.y()
            self.move(x, y)


def show_halo_face(parent=None, gif_path="Gifs/halo-cortana.gif"):
    face_window = HaloFaceWindow(parent, gif_path)
    face_window.show()
    return face_window


