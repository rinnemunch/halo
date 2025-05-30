import webbrowser
import os
import random
import requests
from datetime import datetime


def handle_command(command, window=None, speak_gui=None, log_command=None, print_to_gui=None):
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
        if window:
            window.quit()

    elif "flip a coin" in command or "coin toss" in command:
        result = random.choice(["heads", "tails"])
        response = f"It's {result}."
        speak_gui(response)
        log_command(command, response)

    elif "open notepad" in command:
        response = "Opening Notepad."
        speak_gui(response)
        log_command(command, response)
        os.system("start notepad")

    elif "fact" in command:
        facts = [
            "Honey never spoils. Archaeologists have found 3000-year-old jars of honey in ancient Egyptian tombs.",
            "Bananas are berries, but strawberries aren't.",
            "Octopuses have three hearts and blue blood."
        ]
        response = random.choice(facts)
        speak_gui(response)
        log_command(command, response)

    else:
        response = "Sorry, I don't know that command yet."
        speak_gui(response)
        log_command(command, response)
