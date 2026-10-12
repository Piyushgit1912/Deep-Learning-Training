# Earlier draft of spacy_sentence_similarity_qa.py (same logic; contains spelling differences and an unused numpy import).
# See ../spacy_sentence_similarity_qa.py for the main version.

import spacy
import numpy as np 

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Knowledge Base
Knowledge = """
Python is a high-level Programming language.
Python developed by Guido van Rossum.
Python was first released in 1991.
Python is wildly used for Artifical Intelligence, Machine Learning, Data Science, Web Developmnet, Automation, and Cyber Security.
"""

# Convert Knowledge into a spaCy document
doc = nlp(Knowledge)

# Extract sentence
sentances = list(doc.sents)

print("=" * 60)
print("  Question Answering System using spaCy")
print("=" * 60)
print("Type 'exit' to stop. \n")

# Interactive loop: ask -> find the most similar knowledge sentence -> print it
while True:

    question = input("Ask a Question: ")

    if question.lower() == 'exit':
        print("\nThank You !")
        break

    # Turn the question into a spaCy Doc (gives it a vector)
    question_doc = nlp(question)
    best_sentance = None
    best_score = 0

    for sentance in sentances:
        # Cosine similarity between question and sentence vectors
        score = question_doc.similarity(sentance)

        if score > best_score:
            best_score = score
            best_sentance = sentance

    print("\nAnswer: ")

    if best_sentance is not None:
        print(best_sentance.text.strip())
        print(f"Similarity Score: {best_score:.2f}")
    else:
        print("Sorry, I couldn't find a suitable answer.")
        print(f"Similarity Score: {best_score:.2f}")

    print("-" * 60)
