# for voice
# LISTEN VOICE FOR GIRL 1 AND FOR BOY 0

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1])
engine.setProperty('voice',voices[1].id)
engine.say("Hi, I am text to speach, Mr shashi kant kumar, in b.tech 3rd year from CSE branch")
engine.runAndWait()