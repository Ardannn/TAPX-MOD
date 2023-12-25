import spacy
import speech_recognition as sr
import pyttsx3
def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Set the voice ID for Microsoft Zira Desktop
    zira_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"

    # Set the voice
    engine.setProperty('voice', zira_voice_id)

    # Say the text
    engine.say(text)

    # Wait for the speech to finish
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
    # Load the English language model from SpaCy
    nlp = spacy.load("en_core_web_sm")

    while True:
        # Recognize speech command
        user_input = recognize_speech()

        # Process the recognized command using SpaCy
        doc = nlp(user_input)

        # Respond to the command
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
