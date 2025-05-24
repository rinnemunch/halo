import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
import random
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Optional: switch to female voice


def log_command(user_command, halo_response):
    with open("halo_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] You: {user_command}\n")
        file.write(f"[{timestamp}] Halo: {halo_response}\n\n")


def speak(text):
    print(f"Halo: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
    except sr.RequestError:
        speak("Speech recognition is unavailable.")
    return ""


def handle_command(command):
    if "youtube" in command:
        response = "Opening YouTube."
        speak(response)
        log_command(command, response)
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}."
        speak(response)
        log_command(command, response)

    elif "chrome" in command:
        response = "Opening Google Chrome."
        speak(response)
        log_command(command, response)
        os.system("start chrome")

    elif "joke" in command:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs.",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
            "What do you call 8 hobbits? A hobbyte."
        ]
        response = random.choice(jokes)
        speak(response)
        log_command(command, response)

    elif "play music" in command:
        music_path = "C:\\Users\\fulto\\Music\\StopTheCar.mp3"
        response = "Playing music."
        speak(response)
        log_command(command, response)
        os.startfile(music_path)

    elif "weather" in command:
        response = "Checking the weather..."
        speak(response)
        try:
            res = requests.get("https://wttr.in/?format=3")
            speak(res.text)
            log_command(command, res.text)
        except:
            error_response = "Sorry, couldn't get the weather right now."
            speak(error_response)
            log_command(command, error_response)

    elif "log" in command or "show log" in command:
        response = "Showing your recent commands."
        speak(response)
        log_command(command, response)
        with open("halo_log.txt", "r", encoding="utf-8") as file:
            print(file.read())

    elif "exit" in command or "quit" in command:
        response = "Goodbye."
        speak(response)
        log_command(command, response)
        exit()

    else:
        response = "Sorry, I don't know that command yet."
        speak(response)
        log_command(command, response)


if __name__ == "__main__":
    speak("Hello, I'm Halo. How can I help?")
    while True:
        user_input = listen()
        if user_input:
            handle_command(user_input)
