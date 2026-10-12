# Incomplete earlier draft of spacy_embedding_qa_cosine_similarity.py.
#
# NOTE: this draft stops right after the 'exit' check - it never embeds the question or prints an answer.
# See ../spacy_embedding_qa_cosine_similarity.py for the complete version.

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
    sentance_vectors.append(doc.vector)

sentance_vectors = np.array(sentance_vectors)

# Cosine Similarity Function

# cosine similarity = (v1 . v2) / (|v1| * |v2|)
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Question Answering Loop

print("=" * 60)
print("  Question Answering System using spaCy  Embeddings")
print("=" * 60)
print("Type 'exit' to stop. \n")

# Question loop (the rest of the logic is missing in this draft)
while True:

    question = input("Ask a Question: ")

    if question.lower() == 'exit':
        print("\nThank You !")
        break

