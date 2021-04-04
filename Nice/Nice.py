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

def count(word):
    word = word.lower()
    r1 = sr.Recognizer()
    counter = 0
    speak("you may now talk")
    print("you may now talk")   
    while True:
        with sr.Microphone() as source:
            audio = r1.listen(source)
    
        text = None
        try:
            text = r1.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, could not understand.")
            print("Sorry, could not understand.")
    
        if text != None:
            print(text)
            text = text.lower()
            if word in text:
                counter += text.count(word)
                print(counter)
                #speak("You have said " + word + " " + str(counter) + " time" + ("s" if counter != 1 else ""))

            if "how many times have I said nice" in text:
                speak("You have said " + word + " " + str(counter) + " time" + ("s" if counter != 1 else ""))

            if "stop stop stop" in text:
                break

count("nice")