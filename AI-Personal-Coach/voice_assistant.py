import speech_recognition as sr
from gtts import gTTS
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Bolo...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="hi-IN")
    except:
        return "Kuch samajh nahi aaya"

def speak(text):
    tts = gTTS(text=text, lang="hi/english")
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Linux/Mac
    # os.system("start response.mp3")  # Windows

if __name__ == "__main__":
    user_speech = listen()
    print(f"User bola: {user_speech}")
    speak("Aapne bola: " + user_speech)
