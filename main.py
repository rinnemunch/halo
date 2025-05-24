import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

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
        os.system("start chrome")  # Works on Windows
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
