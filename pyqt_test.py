import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont


class HaloTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Halo PyQt Test")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Hello, I'm Halo. How can I help?")
        layout.addWidget(self.label)

        self.button1 = QPushButton("Speak")
        self.button1.clicked.connect(lambda: self.label.setText("You clicked Speak"))
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Submit Text")
        self.button2.clicked.connect(lambda: self.label.setText("You clicked Submit"))
        layout.addWidget(self.button2)

        self.button3 = QPushButton("View Log")
        self.button3.clicked.connect(lambda: self.label.setText("You clicked View Log"))
        layout.addWidget(self.button3)

        self.setLayout(layout)


app = QApplication(sys.argv)
app.setFont(QFont("Consolas", 11, weight=QFont.Weight.Bold))
window = HaloTest()
app.setStyleSheet("""
    QWidget {
        background-color: white;
        font-family: Segoe UI;
    }
    QPushButton {
        background-color: #1E90FF;
        color: white;
        border-radius: 6px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #1C86EE;
    }
    QLabel {
        color: #1E90FF;
        font-size: 14px;
    }
""")

window.show()
sys.exit(app.exec())
