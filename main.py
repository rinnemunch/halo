import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import random
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Optional: switch to female voice


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
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")

    elif "chrome" in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")

    elif "joke" in command:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs.",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
            "What do you call 8 hobbits? A hobbyte."
        ]
        speak(random.choice(jokes))

    elif "play music" in command:
        music_path = "C:\\Users\\fulto\\Music\\StopTheCar.mp3."
        os.startfile(music_path)

    elif "weather" in command:
        speak("Checking the weather...")
        try:
            res = requests.get("https://wttr.in/?format=3")
            speak(res.text)
        except:
            speak("Sorry, couldn't get the weather right now.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye.")
        exit()

    else:
        speak("Sorry, I don't know that command yet.")


if __name__ == "__main__":
    speak("Hello, I'm Halo. How can I help?")
    while True:
        user_input = listen()
        if user_input:
            handle_command(user_input)
