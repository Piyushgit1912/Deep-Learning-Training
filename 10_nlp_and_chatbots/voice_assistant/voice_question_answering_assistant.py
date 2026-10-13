# Voice question-answering assistant: speak a question, get a spoken answer.
#
# Pipeline: microphone -> speech-to-text -> spaCy sentence embedding -> cosine similarity against a small knowledge base
# -> best answer (if similarity >= 0.55) -> text-to-speech.
#
# Setup:  pip install spacy SpeechRecognition pyaudio pyttsx3 numpy ; python -m spacy download en_core_web_md
# Say 'exit', 'quit' or 'bye' to stop.

import spacy
import numpy as np
import speech_recognition as sr
import pyttsx3


# ==========================================
# Load spaCy Model
# ==========================================

nlp = spacy.load("en_core_web_md")


# ==========================================
# Initialize Text-to-Speech
# ==========================================

engine = pyttsx3.init()
# Speaking rate (words per minute)
engine.setProperty("rate", 170)


# Print the text and read it aloud
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ==========================================
# Knowledge Base
# ==========================================

knowledge = [
    "Python is a high-level programming language.",
    "Python was developed by Guido van Rossum.",
    "Python was first released in 1991.",
    "Python is widely used for Artificial Intelligence, Machine Learning, Data Science, Web Development, Automation, and Cyber Security.",
    "NumPy is used for numerical computing.",
    "Pandas is used for data analysis.",
    "The Taj Mahal is located in Agra.",
    "The Earth revolves around the Sun."
]


# ==========================================
# Create Sentence Embeddings
# ==========================================

sentence_vectors = np.array([
    nlp(sentence).vector
    for sentence in knowledge
])


# ==========================================
# Cosine Similarity
# ==========================================

def cosine_similarity(v1, v2):

    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)

    if denominator == 0:
        return 0

    return np.dot(v1, v2) / denominator


# ==========================================
# Speech Recognition
# ==========================================

recognizer = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:

                print("No speech detected.")
                return ""

    except OSError:

        speak("Microphone is not available.")
        return ""


    # ======================================
    # Convert Speech to Text
    # ======================================

    try:

        # Send the audio to Google's Web Speech API and get text back (needs internet)
        command = recognizer.recognize_google(audio).lower()

        print("You:", command)

        return command


    except sr.UnknownValueError:

        speak("Sorry, I could not understand.")
        return ""


    except sr.RequestError:

        speak("Speech recognition service is unavailable.")
        return ""


# ==========================================
# Find Best Answer
# ==========================================

def answer_question(question):

    question_vector = nlp(question).vector

    similarities = []

    for vector in sentence_vectors:

        similarity = cosine_similarity(
            question_vector,
            vector
        )

        similarities.append(similarity)


    similarities = np.array(similarities)

    best_index = np.argmax(similarities)

    best_score = similarities[best_index]


    print("Similarity:", round(float(best_score), 3))


    # Minimum similarity threshold

    if best_score < 0.55:

        return "Sorry, I don't know the answer."


    return knowledge[best_index]


# ==========================================
# Virtual Assistant
# ==========================================

print("=" * 60)
print("             spaCy Virtual Assistant")
print("=" * 60)


speak("Hello. I am your virtual assistant.")
speak("Ask me a question.")


# ==========================================
# Main Loop
# ==========================================

while True:

    question = listen()


    if question == "":
        continue


    # ======================================
    # Exit Commands
    # ======================================

    if (
        "exit" in question
        or "quit" in question
        or "bye" in question
    ):

        speak("Goodbye. Have a nice day.")
        break


    # ======================================
    # Answer Question
    # ======================================

    answer = answer_question(question)

    speak(answer)

    print("Answer:", answer)
