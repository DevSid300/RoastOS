import pyttsx3
import threading
import time

def speak(text):

    def run():

        # Sync with typing animation
        time.sleep(0.4)

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)

        engine.setProperty('rate', 170)

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    threading.Thread(
        target=run,
        daemon=True
    ).start()
    