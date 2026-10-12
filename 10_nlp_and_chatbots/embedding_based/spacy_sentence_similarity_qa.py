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
print("  Question Answering System using spaCy")
print("=" * 60)
print("Type 'exit' to stop. \n")

# Interactive loop: ask -> find the most similar knowledge sentence -> print it
while True:

    question = input("Ask a Question: ")

    if question.lower() == 'exit':
        print("\nThank You !")
        break

    # Turn the question into a spaCy Doc (this also gives it a vector)
    question_doc = nlp(question)
    # Keep track of the best match found so far
    best_sentance = None
    best_score = 0

    for sentance in sentances:
        # Cosine similarity between question and sentence vectors (higher = more alike)
        score = question_doc.similarity(sentance)

        if score > best_score:
            best_score = score
            best_sentance = sentance

    print("\nAnswer: ")

    # The answer is the highest-scoring sentence
    if best_sentance is not None:
        print(best_sentance.text.strip())
        print(f"Similarity Score: {best_score:.2f}")
    else:
        print("Sorry, I couldn't find a suitable answer.")
        print(f"Similarity Score: {best_score:.2f}")

    print("-" * 60)

