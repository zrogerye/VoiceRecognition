import speech_recognition as sr
import playsound
import os
from gtts import *

def speak(text):
    tts = gTTS(text)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")



speak("hello")
