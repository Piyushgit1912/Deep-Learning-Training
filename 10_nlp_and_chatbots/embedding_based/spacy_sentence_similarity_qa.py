# Question-answering bot using spaCy sentence similarity.
#
# The knowledge base is a short paragraph. For every question the bot compares the question's vector with the vector
# of each knowledge sentence (spaCy's .similarity() = cosine similarity of averaged word vectors) and answers with
# the most similar sentence.
#
# Setup:  pip install spacy
#         python -m spacy download en_core_web_md     (a model WITH word vectors; the small 'sm' model has none)
# Run: python spacy_sentence_similarity_qa.py     Type 'exit' to stop.

import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Knowledge Base
Knowledge = """
Python is a high-level Programming language.
Python developed by Guido van Rossum.
Python was first released in 1991.
Python is wildly used for Airtifical Intelligence, Machine Learning, Data Science, Web Developmenet, Automation, and Cyber Security.
"""

# Convert Knowledge into a spaCy document
doc = nlp(Knowledge)

# Extract sentence
sentances = list(doc.sents)

print("=" * 60)
