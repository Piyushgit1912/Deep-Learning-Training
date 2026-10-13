# Speech-to-text: listen to the microphone once and print what was said.
#
# Uses the SpeechRecognition library; the audio is sent to Google's free Web Speech API, so an internet connection is required.
# Requires: pip install SpeechRecognition pyaudio   (PyAudio provides microphone access)

import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

try:
    # Open microphone
    with sr.Microphone() as source:
        print("🎤 Speak something...")

        # Adjust microphone according to background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Listen to user's voice
        audio = recognizer.listen(source)

    # Convert speech into text
    print("🔄 Recognizing...")

    text = recognizer.recognize_google(audio)

    print("You said:", text)

# Speech was heard but could not be understood
except sr.UnknownValueError:
    print("❌ Sorry, I couldn't understand your voice.")

# The recognition service could not be reached (check the internet connection)
except sr.RequestError:
    print("❌ Could not connect to Google Speech Recognition service.")

# No microphone available
except OSError:
    print("❌ Microphone not found. Please check your microphone.")

# Any other error
except Exception as e:
    print("❌ Error:", e)
