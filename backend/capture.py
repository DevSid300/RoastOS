import pyautogui
from datetime import datetime
import os


def capture_screen():

    os.makedirs("screenshots", exist_ok=True)

    filename = f"screenshots/{datetime.now().timestamp()}.png"

    screenshot = pyautogui.screenshot()

    screenshot.save(filename)

    return filename