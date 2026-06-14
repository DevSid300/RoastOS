import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Try different indexes if needed
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 180)

engine.say("Testing Roast O S voice system.")

engine.runAndWait()