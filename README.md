# 🤖 Jarvis AI Assistant  

Jarvis AI is a Python-based personal assistant inspired by *Iron Man's Jarvis*.  
It can listen to your voice, recognize commands, and perform actions such as:  
- Opening websites  
- Playing music  
- Telling the current time  
- Opening applications (like MS Word)  
- Responding with AI-powered answers  

---

## ⚡ Features
- 🎤 Voice recognition using `speech_recognition`  
- 🔊 Speech output using Windows SAPI (`win32com.client`)  
- 🌐 Opens popular websites like YouTube, Google, Instagram, Wikipedia  
- 🎶 Plays local music files  
- ⏰ Speaks the current time  
- 📄 Opens MS Word directly  
- 🧠 Generates smart AI responses using HuggingFace + OpenAI API  

---

## 🛠️ Requirements
Make sure you have the following installed:

- Python 3.8+  
- Required Python libraries:  
  ```bash
  pip install pywin32 SpeechRecognition pywhatkit openai
