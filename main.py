import sys
import speech_recognition as sr
import pyttsx3
import threading
from datetime import datetime
from halo_commands import handle_command
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit, QPushButton
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from halo_face_window import show_halo_face

# ---------------- App + Window ----------------
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Halo Assistant")
window.resize(500, 450)

layout = QVBoxLayout()

output_box = QTextEdit()
output_box.setReadOnly(True)
output_box.setFont(QFont("Consolas", 11, weight=QFont.Weight.Bold))
layout.addWidget(output_box)

# Manual Entry Box
manual_entry = QLineEdit()
manual_entry.setPlaceholderText("Type a command...")
manual_entry.setFixedHeight(30)
layout.addWidget(manual_entry)

# Submit Button
submit_button = QPushButton("Submit Text")
submit_button.clicked.connect(lambda: run_manual_command())
submit_button.setFixedHeight(30)
layout.addWidget(submit_button)

# Speak Button
speak_button = QPushButton("Speak")
speak_button.clicked.connect(lambda: run_voice_command())
speak_button.setFixedHeight(30)
layout.addWidget(speak_button)

# Log Button
log_button = QPushButton("View Log")
log_button.clicked.connect(lambda: show_log())
log_button.setFixedHeight(30)
layout.addWidget(log_button)

palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor("#121212"))
palette.setColor(QPalette.ColorRole.Base, QColor("#1e1e1e"))
palette.setColor(QPalette.ColorRole.Text, QColor("#A9C6FF"))
palette.setColor(QPalette.ColorRole.Button, QColor("#003f73"))
palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))


button_style = """
QPushButton {
    background-color: #003f73;
    color: white;
    border-radius: 6px;
    padding: 6px;
}
QPushButton:hover {
    background-color: #005A9C;
}
"""

submit_button.setStyleSheet(button_style)
speak_button.setStyleSheet(button_style)
log_button.setStyleSheet(button_style)


app.setPalette(palette)
window.setLayout(layout)
window.show()
face_ref = show_halo_face(window, "Gifs/halo-cortana.gif")

# ---------------- Voice Engine ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[1].id)


# ---------------- Helper Functions ----------------
def print_to_gui(text):
    output_box.append(text)


def speak_gui(text):
    print_to_gui(f"Halo: {text}")
    engine.say(text)
    engine.runAndWait()


def log_command(user_command, halo_response):
    with open("halo_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] You: {user_command}\n")
        file.write(f"[{timestamp}] Halo: {halo_response}\n\n")


def listen():
    print_to_gui("✅ Entered listen()")
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print_to_gui("🎙️ Microphone opened.")
            recognizer.adjust_for_ambient_noise(source)
            print_to_gui("🔊 Calibrated for ambient noise.")
            audio = recognizer.listen(source)
            print_to_gui("📡 Processing audio...")
    except Exception as mic_error:
        print_to_gui(f"⚠️ Mic error: {mic_error}")
        return ""

    try:
        command = recognizer.recognize_google(audio)
        print_to_gui(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak_gui("Sorry, I didn’t catch that.")
    except sr.RequestError:
        speak_gui("Speech recognition is unavailable.")
    except Exception as e:
        print_to_gui(f"⚠️ Recognition error: {e}")
    return ""


def run_manual_command():
    cmd = manual_entry.text()
    manual_entry.clear()
    if cmd:
        print_to_gui(f"You: {cmd}")
        threading.Thread(target=handle_command, args=(cmd, window, speak_gui, log_command, print_to_gui)).start()


def run_voice_command():
    def threaded_listen():
        print_to_gui("🧵 Voice thread started.")
        try:
            result = listen()
            if result:
                handle_command(result, window, speak_gui, log_command, print_to_gui)
            else:
                print_to_gui("❌ No voice input received.")
        except Exception as e:
            print_to_gui(f"🛑 Error in voice thread: {str(e)}")

    threading.Thread(target=threaded_listen).start()


def show_log():
    try:
        with open("halo_log.txt", "r", encoding="utf-8") as file:
            log_content = file.read()
            print_to_gui(f"--- HALO LOG ---\n{log_content}")
    except:
        print_to_gui("No log file found.")


# ---------------- Start ----------------
def startup_message():
    speak_gui("Hello, I'm Halo. How can I help?")


threading.Thread(target=startup_message).start()

# Final app run
sys.exit(app.exec())
