# Question-answering bot using sentence embeddings and a hand-written cosine similarity.
#
# Each knowledge sentence is converted to a vector once (doc.vector = average of its word vectors). For every question the
# bot embeds the question, computes cosine similarity against all sentence vectors and returns the best match.
# This is the core idea behind semantic search and retrieval systems.
#
# Setup:  pip install spacy numpy ;  python -m spacy download en_core_web_md
# Run: python spacy_embedding_qa_cosine_similarity.py     Type 'exit' to quit.

import spacy
import numpy as np

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Knowledge Base
Knowledge = [
    "Python is a high-level Programming language.",
    "Python developed by Guido van Rossum.",
    "Python was first released in 1991.",
    "Python is wildly used for Airtifical Intelligence, Machine Learning, Data Science, Web Developmenet, Automation, and Cyber Security.",
    " Numpy is used for Numerical computing.",
    "Pandas is used for Data Analysis",
    "The Taj Mahal is located in Agra",
    "The Earth revolves around the sun."
]

# Create Embedding for Knowledge Base
sentance_vectors = []

for sentance in Knowledge:
    doc = nlp(sentance)
    # doc.vector is the average of the word vectors (300 values for en_core_web_md)
    sentance_vectors.append(doc.vector)

sentance_vectors = np.array(sentance_vectors)

# Cosine Similarity Function

# cosine similarity = (v1 . v2) / (|v1| * |v2|): compares the direction of two vectors and ignores their length
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Question Answering Loop

print("=" * 60)
print("  Question Answering System using spaCy  Embeddings")
print("=" * 60)

while True:

    question = input("\n Ask a Question (Type 'exit' to quit): ")

    if question.lower() == 'exit':
        print("\nThank You !")
        break

    # Question embedding
    question_vector = nlp(question).vector
    similarities = []

    # Compare with every sentance
    for vector in sentance_vectors:
        score = cosine_similarity(question_vector, vector)
        similarities.append(score)

    similarities = np.array(similarities)
    # Index of the most similar knowledge sentence
    best_index = np.argmax(similarities)

    print("\nAnswer: ")
    print(Knowledge[best_index])
    print("Similarity Score: ", round(similarities[best_index], 3))