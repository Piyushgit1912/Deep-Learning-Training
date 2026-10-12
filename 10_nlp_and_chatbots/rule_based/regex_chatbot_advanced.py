# Regular-expression chatbot (advanced rule-based version).
#
# Every intent (greeting, name, age, topics, date, time, ...) is detected with a regex using word boundaries (\b)
# and several keyword alternatives, so it is more flexible than the plain if/elif version in rule_based_chatbot.py.
#
# Run: python regex_chatbot_advanced.py     Type 'bye' or 'exit' to quit.

import re
# datetime provides the current date and time for those intents
from datetime import datetime

print("=" * 60)
print("          Regular Expression Based Chatbot")
print("=" * 60)
print("Type 'bye' to exit.\n")

# Chat loop. Order matters: the first matching rule wins, so 'exit' is checked first and the default reply is last
while True:
    # Normalise the input: lowercase + strip whitespace
    user = input("You: ").lower().strip()

    # Exit
    if re.search(r"\b(bye|goodbye|exit|quit)\b", user):
        print("Bot: Goodbye! Have a wonderful day!")
        break

    # Greeting
    elif re.search(r"\b(hi|hello|hey|good morning|good evening)\b", user):
        print("Bot: Hello! How can I help you today?")

    # Name
    elif re.search(r"\b(your name|who are you|what is your name)\b", user):
        print("Bot: I am a Regex-based Chatbot.")

    # Age
    elif re.search(r"\b(how old|your age)\b", user):
        print("Bot: I don't have an age like humans.")

    # Python
    elif re.search(r"\bpython\b", user):
        print(
            "Bot: Python is a popular programming language "
            "used in AI, ML, Data Science, and Web Development."
        )

    # Machine Learning
    elif re.search(r"\b(machine learning|ml)\b", user):
        print(
            "Bot: Machine Learning enables computers to learn "
            "from data without explicit programming."
        )

    # Artificial Intelligence
    elif re.search(r"\b(artificial intelligence|ai)\b", user):
        print(
            "Bot: Artificial Intelligence is the field of creating "
            "machines that can perform tasks requiring human-like intelligence."
        )

    # Data Science
    elif re.search(r"\b(data science|data scientist)\b", user):
        print(
            "Bot: Data Science combines programming, statistics, "
            "and data analysis to extract useful insights from data."
        )

    # NumPy
    elif re.search(r"\b(numpy|num py)\b", user):
        print(
            "Bot: NumPy is a Python library used for numerical "
            "computing and working with arrays."
        )

    # Pandas
    elif re.search(r"\bpandas\b", user):
        print(
            "Bot: Pandas is a Python library used for data "
            "manipulation and data analysis."
        )

    # Thanks
    elif re.search(r"\b(thank you|thanks|thankx|thx)\b", user):
        print("Bot: You're welcome!")

    # Help
    elif re.search(r"\bhelp\b", user):
        print(
            "Bot: You can ask me about Python, AI, ML, Data Science, "
            "NumPy, Pandas, Date, and Time."
        )

    # Date
    elif re.search(r"\b(date|today|today's date)\b", user):
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}.")

    # Time
    elif re.search(r"\b(time|current time|what time is it)\b", user):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: The current time is {current_time}.")

    # Default Response
    else:
        print("Bot: Sorry, I don't understand your question.")