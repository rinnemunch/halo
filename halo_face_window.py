from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt, QSize
import os


class HaloFaceWindow(QDialog):
    def __init__(self, parent=None, gif_path="Gifs/halo-cortana.gif"):
        super().__init__(parent)
        self.setWindowTitle("Halo's Face")

        print(f"[DEBUG] Looking for: {os.path.abspath(gif_path)}")

        self.movie = QMovie(gif_path)
        print(f"[DEBUG] Movie valid: {self.movie.isValid()}")

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setMovie(self.movie)


        fallback_size = QSize(300, 300)
        gif_size = self.movie.frameRect().size()
        size = gif_size if gif_size.width() > 0 else fallback_size

        self.label.resize(size)
        self.setFixedSize(size)

        self.movie.start()

        if parent:
            x = parent.x() + parent.width() + 20
            y = parent.y()
            self.move(x, y)


def show_halo_face(parent=None, gif_path="Gifs/halo-cortana.gif"):
    face_window = HaloFaceWindow(parent, gif_path)
    face_window.show()
    return face_window
