import keyboard

from capture import capture_screen
from ocr import extract_text
from ai import roast_user
from window_detector import get_active_window
from overlay import show_roast
from voice import speak

print("\n🤖 RoastOS is running...")
print("Press F8 to roast current window.")
print("Press F9 to quit.\n")

while True:

    # Wait for F8 key
    keyboard.wait("F8")

    try:

        print("\n" + "=" * 50)
        print("🔥 ROASTING CURRENT WINDOW")
        print("=" * 50)

        # Detect active window
        window = get_active_window()

        # Capture screenshot
        image_path = capture_screen()

        # OCR
        text = extract_text(image_path)

        # Activity context
        activity = f"""
        CURRENT WINDOW:
        {window}

        SCREEN TEXT:
        {text[:300]}
        """

        # Smart app-specific roasts
        if "YouTube" in window:
            roast = "YouTube open again. Productivity filed a missing person report."

        elif "Spotify" in window:
            roast = "Spotify carrying this entire work session emotionally."

        elif "Discord" in window:
            roast = "Discord detected. Focus officially left the building."

        else:
            roast = roast_user(activity)

        speak(roast)
        show_roast(roast)

    except Exception as e:

        print("\n❌ ERROR:")
        print(e)

    # Quit app
    if keyboard.is_pressed("F9"):
        print("\n👋 Exiting RoastOS...")
        break