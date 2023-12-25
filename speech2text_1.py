import speech_recognition as sr
import os
from TAPEX_project_2 import query
from assistant_spacy import speak
from TAPEX_project_2 import main

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: ", command)
        return command
    except sr.UnknownValueError:
        print("Sorry I couldn't hear that")
        return ""
def execute_command(command):
    if query in command:
        main()

a = execute_command()
print(a)
