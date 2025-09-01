import webbrowser
import pyperclip
import urllib.parse
import keyboard
from plyer import notification
import time

hotkeys_active = True

def notify(message):
    notification.notify(
        title="Search Anywhere! 💗",
        message=message,
        timeout=1  # seconds
    )

def search_google():
    if hotkeys_active:
        text = pyperclip.paste().strip()
        if text:
            url = "https://www.google.com/search?q=" + urllib.parse.quote(text)
            webbrowser.open(url)
            notify(f"🔍 GOOGLE: {text}")

def search_youtube():
    if hotkeys_active:
        text = pyperclip.paste().strip()
        if text:
            url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(text)
            webbrowser.open(url)
            notify(f"▶️ YOUTUBE: {text}")

def toggle_hotkeys():
    global hotkeys_active
    hotkeys_active = not hotkeys_active
    status = "ON" if hotkeys_active else "OFF"
    notify(f"Hotkeys {status}")

# Register hotkeys to prevent typing letters
keyboard.add_hotkey('ctrl+alt+g', search_google, suppress=True)
keyboard.add_hotkey('ctrl+alt+y', search_youtube, suppress=True)
keyboard.add_hotkey('ctrl+alt+t', toggle_hotkeys, suppress=True)
keyboard.add_hotkey('esc', lambda: exit(), suppress=True)  # Fully exit

# Silent background loop
while True:
    time.sleep(0.1)
