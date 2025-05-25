import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
import random
import requests
import tkinter as tk
from tkinter import scrolledtext
import threading

# ---------------- GUI Setup ----------------
window = tk.Tk()
window.title("Halo Assistant")
window.geometry("500x450")

# Output frame
output_frame = tk.Frame(window)
output_frame.pack(fill=tk.BOTH, expand=True)

output_box = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, state='disabled', height=15)
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry frame
entry_frame = tk.Frame(window)
entry_frame.pack(fill=tk.X)

manual_entry = tk.Entry(entry_frame)
manual_entry.pack(padx=10, pady=(0, 10), fill=tk.X)


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[1].id)


# ---------------- Helper Functions ----------------

def print_to_gui(text):
    output_box.config(state='normal')
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)
    output_box.config(state='disabled')


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


# ---------------- Command Handler ----------------

def handle_command(command):
    if "youtube" in command:
        response = "Opening YouTube."
        speak_gui(response)
        log_command(command, response)
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}."
        speak_gui(response)
        log_command(command, response)

    elif "chrome" in command:
        response = "Opening Google Chrome."
        speak_gui(response)
        log_command(command, response)
        os.system("start chrome")

    elif "joke" in command:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs.",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
            "What do you call 8 hobbits? A hobbyte."
        ]
        response = random.choice(jokes)
        speak_gui(response)
        log_command(command, response)

    elif "play music" in command:
        music_path = "C:\\Users\\fulto\\Music\\StopTheCar.mp3"
        response = "Playing music."
        speak_gui(response)
        log_command(command, response)
        os.startfile(music_path)

    elif "weather" in command:
        response = "Checking the weather..."
        speak_gui(response)
        try:
            res = requests.get("https://wttr.in/?format=3")
            speak_gui(res.text)
            log_command(command, res.text)
        except:
            error_response = "Sorry, couldn't get the weather right now."
            speak_gui(error_response)
            log_command(command, error_response)

    elif "log" in command or "show log" in command:
        response = "Showing your recent commands."
        speak_gui(response)
        log_command(command, response)
        try:
            with open("halo_log.txt", "r", encoding="utf-8") as file:
                print_to_gui(file.read())
        except:
            print_to_gui("No log found.")

    elif "exit" in command or "quit" in command:
        response = "Goodbye."
        speak_gui(response)
        log_command(command, response)
        window.quit()

    else:
        response = "Sorry, I don't know that command yet."
        speak_gui(response)
        log_command(command, response)


# ---------------- GUI Event Functions ----------------

def run_manual_command():
    cmd = manual_entry.get()
    manual_entry.delete(0, tk.END)
    if cmd:
        print_to_gui(f"You: {cmd}")
        threading.Thread(target=handle_command, args=(cmd,)).start()


def run_voice_command():
    def threaded_listen():
        print_to_gui("🧵 Voice thread started.")
        try:
            result = listen()
            if result:
                handle_command(result)
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

# ---------------- Buttons ----------------

print_to_gui("✅ GUI finished loading. Adding buttons now.")
tk.Button(window, text="TEST SPEAK", command=run_voice_command).pack(pady=5)
tk.Button(window, text="Submit Text", command=run_manual_command).pack(pady=5)
tk.Button(window, text="View Log", command=show_log).pack(pady=5)

window.mainloop()
