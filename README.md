# 🎙️ Halo – Your Personal Voice Assistant


## Halo is a Python-based voice assistant with a clean GUI, speech-to-text, and offline command execution.
It listens to your voice, speaks responses, controls your apps, and keeps a log of everything you say.

## 🧠 Features
✅ GUI built with tkinter (Dark mode coming soon)
✅ Voice recognition using speech_recognition
✅ Text-to-speech with pyttsx3
✅ Modular command system (halo_commands.py)
✅ Threaded input so the UI stays responsive
✅ Command logging (halo_log.txt)
✅ Works offline for most features

## 🗣️ Supported voice/text commands:

“Open YouTube”

“What time is it?”

“Tell me a joke”

“Check the weather”

“Open Chrome”

“Play music”

“Show log”

“Exit”

## 🖼️ Preview

![Preview](Gifs/animation.gif)


## 🚀 How to Run

### 1. Clone the repo
bash
````
git clone https://github.com/rinnemunch/halo.git
cd halo
````

### 2. Create and activate a virtual environment
bash 
````
python -m venv venv
.\venv\Scripts\activate  # Windows
````

### 3. Install dependencies
bash
````
pip install -r requirements.txt 
````

### If you have issues with pyaudio, use:
bash 
````
pip install pipwin
pipwin install pyaudio
````

### 4. Start Halo
bash
````
python main.py
````
## 📂 Example Log
bash
````
[2025-05-25 07:01:45] You: tell me a joke
[2025-05-25 07:01:46] Halo: I told my computer I needed a break, and now it won’t stop sending me Kit-Kats. (Yes I searched up corny jokes lol)
````
## 💻 Requirements
Python 3.10+

Microphone (optional – all commands can also be typed)

Internet (only needed for weather queries)