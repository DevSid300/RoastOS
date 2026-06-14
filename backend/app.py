from capture import capture_screen
from ocr import read_text
from ai import generate_roast


print("🔥 RoastOS Ready 🔥")


while True:

    input("\nPress ENTER to roast your current screen...")

    print("\nCapturing screen...")

    image_path = capture_screen()

    print("Reading screen text...")

    text = read_text(image_path)

    if text.strip() == "":
        print("No text detected.")
        continue

    print("\nDetected Text:\n")
    print(text)

    roast = generate_roast(text)

    print("\n🔥 AI Roast:\n")
    print(roast)

    print("\n-----------------------------")