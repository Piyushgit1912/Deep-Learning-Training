# Text-to-speech: read a piece of text aloud.
#
# pyttsx3 works offline and uses the speech engine of the operating system.
# Requires: pip install pyttsx3

import pyttsx3

# Initialise the offline text-to-speech engine
engine = pyttsx3.init()

# Queue the text to be spoken
engine.say("Hello, I am your Poojar0n My ideal person is MS Dhoni. He is one of the most successful and respected cricketers and leaders in India. I have always admired him, not only because of his achievements in cricket, but also because of his personality and the way he handles different situations in life.")
# Speak the queued text and wait until it has finished
engine.runAndWait()