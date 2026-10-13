# Voice-command assistant: say 'YouTube' or 'Google' and the assistant opens that website; say 'exit' to quit.
#
# Combines speech recognition (speech -> text), simple keyword matching and text-to-speech (the spoken reply).
# Requires: pip install SpeechRecognition pyaudio pyttsx3 (and an internet connection for recognition).

import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialise the text-to-speech engine
engine = pyttsx3.init()

# Helper: say the given text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recogniser object
r = sr.Recognizer()

# Keep listening for commands until the user says 'exit'
while True:
    with sr.Microphone() as source:
        print("Listenting...")

        # Calibrate for background noise
        r.adjust_for_ambient_noise(source)
        # Record audio until the speaker pauses
        audio = r.listen(source)

    try:
        # Convert the audio to lowercase text (uses Google's Web Speech API)
        command = r.recognize_google(audio).lower()
        print(command)

        # Simple keyword-based command matching
        if "youtube" in command:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "exit" in command:
            speak("Goodbye")
            break
        else:
            speak("Command not found.")

    # NOTE: a bare `except` hides every error; catching sr.UnknownValueError / sr.RequestError would be more precise
    except:
        speak("Please repeat.")


