import speech_recognition as sr
import pyttsx3

# Init TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice (optional)


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


if __name__ == "__main__":
    speak("Hello, I'm Halo. Say something.")
    user_command = listen()
    if user_command:
        speak(f"You said: {user_command}")
