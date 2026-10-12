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

