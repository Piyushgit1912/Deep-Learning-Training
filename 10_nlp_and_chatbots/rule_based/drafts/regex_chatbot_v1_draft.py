# First draft of the regular-expression chatbot (the third chatbot built in the course).
# See ../regex_chatbot_advanced.py for the improved version.

# 3rd chatboy regular expression based chatbbpt 
# re regular expression 
import re
print ('=' * 50)
print ('      Rule Based Chatbot')
print ('=' * 50)
print (' type bye to exit \n')

while True :
    # Normalise the input: lowercase + strip whitespace
    user = input('YOU -: ').lower().strip()

    # greeting 
    # \b = word boundary: matches whole words only
    if re.search(r'\b(hi|hello|hey)\b', user):
        print ( 'Bot:- Hello  how can i help u')

    elif 'your name' in user:
        print ('Bot:-- my name is chatBOT')

    elif 'how old' in user:
        print('bot:  i dont have an age. i was just created ')

    elif 'python' in user:
        print('bot: python is a popular programming language')

    elif 'date' in user:
        from datetime  import datetime
        print ('bot:--', datetime.now().strftime('%d-%m-%y'))

    elif 'time' in user:
        from datetime import datetime
        print ('bot- ', datetime.now().strftime('%I:%M:%S %p'))
    # NOTE: only matches the single word 'thankyou', not 'thank you'
    elif 'thankyou' in user:
        print (' bot:- thanks alot')

    elif user=='bye':
        print('goodbye')
        break
    else:
        print('bot-- sorry i didnt understand that')
