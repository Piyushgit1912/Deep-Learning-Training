# Rule-based chatbot: if/elif rules with a few regular expressions.
#
# No machine learning here - the bot replies only to inputs that match a hand-written rule.
# That makes it predictable but unable to understand anything outside the rules.
#
# Run: python rule_based_chatbot.py     Type 'bye' to exit.

import  re

print("=" *50 )
print("   Rule-Based Chatbot")
print("="*50)
print("Type 'bye' to exit.\n")

# Chat loop: read input -> match a rule -> reply, until the user types 'bye'
while True:
    # Normalise the input (lowercase + strip) so matching is case-insensitive
    user = input('You: ').lower().strip()

    # Greeting
    # \b is a word boundary, so 'hi' matches the word 'hi' but not 'this'
    if re.search(r"\b(hi|hello|hey)\b", user):
        print( 'Bot : Hello How can I Help you?')

    # Name
    # NOTE: `user` is already lowercased, so 'Your name' (capital Y) can never match; use 'your name'
    elif "Your name" in user:
        print("Bot: My name is Chatbot.")

    # Age
    elif "how old" in user:
        print("Bot: I don't have an age. I was just created!")

    # Python
    elif "python" in user:
        print("Bot: Python is a populer programming langrage.")

    # Time
    elif "time" in user:
        from datetime import datetime
        print("Bot : ", datetime.now().strftime("%I:%M:%S %p"))

    # Date
    elif "date" in user:
        from datetime import datetime
        print(" Bot :", datetime.now().strftime("%d-%m-%Y"))

    # Thanks
    elif "thank" in user:
        print("Bot : You're welcome!")

    # Exit
    elif user == 'bye':
        print("Bot : Goodbye! Have a nice day")
        break

    # unKnown
    else:
        print("Bot : Sorry, I don't understand that.")
    
    

