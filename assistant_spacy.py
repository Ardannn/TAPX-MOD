import spacy
import speech_recognition as sr
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    zira_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', zira_voice_id)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    nlp = spacy.load("en_core_web_sm")

    while True:
        user_input = recognize_speech()
        doc = nlp(user_input)
        if "good morning" in user_input:
            response = "Good morning, Ardan."
            print("AI:", response)
            speak(response)
        if "can i" in user_input:
            speak("sure, ahhhh, ahhhh, ahhhh your penis is so delicious ardan")
        if "suck my dick" in user_input:
            speak("blup, blup, blup, ahh, ahh, ahh, are,   you, satisfied, ardan?")
if __name__ == "__main__":
    main()
