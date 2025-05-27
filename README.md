# 🎙️ Halo – Your Personal Voice Assistant

Halo is a Python-based voice assistant with a modern PyQt6 interface, voice/text input, and customizable commands.

---

## 🧠 Features
✅ Clean dark-themed GUI built with PyQt6  
✅ Voice recognition using `speech_recognition`  
✅ Text-to-speech with `pyttsx3`  
✅ Modular command system (`halo_commands.py`)  
✅ Animated AI face window (Cortana-style)  
✅ Threaded voice + manual input (non-blocking UI)  
✅ Command logging (`halo_log.txt`)  
✅ Works offline for most features  
✅ Dark mode with blue highlight styling  
✅ Scaled UI and animated GIF rendering with `QMovie`  

---

## 🗣️ Supported Voice/Text Commands

- “Open YouTube”  
- “What time is it?”  
- “Tell me a joke”  
- “Check the weather”  
- “Open Chrome”  
- “Play music”  
- “Show log”  
- “Flip a coin”  
- “Exit”  

---

## 🖼️ Preview

![Preview](Gifs/halo-cortana.gif)

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/rinnemunch/halo.git
cd halo
``` 
2. Create and activate a virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
``` 

3. Install dependencies 
```bash 
pip install -r requirements.txt
``` 
If pyaudio fails: 
```bash 
pip install pipwin
pipwin install pyaudio
``` 
4. Start Halo 
```bash 
python main.py
``` 

📂 Example Log
```bash 
[2025-05-25 07:01:45] You: tell me a joke
[2025-05-25 07:01:46] Halo: I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.
``` 
💻 Requirements 
- Python 3.10+
- Microphone (optional – typing works too)
- Internet (only needed for weather queries) 

