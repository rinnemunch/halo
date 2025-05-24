# 🎙️ Halo – Your Personal Voice Assistant

**Halo** is a fully offline voice-controlled assistant built with Python.  
It listens to your voice, talks back, opens apps, checks the time, tells jokes, plays music, and even logs your commands.

---

## 🧠 Features

✅ Voice recognition (speech-to-text using `speech_recognition`)  
✅ Text-to-speech responses using `pyttsx3`  
✅ Commands:
- “Open YouTube”
- “What time is it?”
- “Tell me a joke”
- “Check the weather”
- “Open Chrome”
- “Play music”
- “Show log”
- “Exit”

✅ Offline command logging (`halo_log.txt`)  
✅ Run in terminal or via PyCharm  
✅ No internet needed for most features  

---

## 🖼️ Preview

#Coming soon I need to build a GUI!

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/rinnemunch/halo.git
cd halo
```` 
2. Create and activate virtual environment 
```bash
python -m venv venv
.\venv\Scripts\activate     # Windows
````  

3. Install requirements
```bash
pip install -r requirements.txt
````   

Or manually:  
```bash
pip install speechrecognition pyttsx3 pyaudio requests
pip install pipwin && pipwin install pyaudio  # if needed
````    
4. Start Halo 
```bash
python main.py
````    

📂 Log Example 
```bash
[2025-05-23 20:45:17] You: what time is it
[2025-05-23 20:45:17] Halo: The current time is 08:45 PM.
````    

💻 Requirements 
Python 3.10+

Microphone input

Internet for weather only (optional)

