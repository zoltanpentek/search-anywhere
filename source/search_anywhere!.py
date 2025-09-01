import webbrowser
import pyperclip
import urllib.parse
import keyboard
import time

hotkeys_active = True

def search_google():
    if hotkeys_active:
        text = pyperclip.paste().strip()
        if text:
            url = "https://www.google.com/search?q=" + urllib.parse.quote(text)
            webbrowser.open(url)

def search_youtube():
    if hotkeys_active:
        text = pyperclip.paste().strip()
        if text:
            url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(text)
            webbrowser.open(url)

def toggle_hotkeys():
    global hotkeys_active
    hotkeys_active = not hotkeys_active

# Register hotkeys (suppress typing)
keyboard.add_hotkey('ctrl+alt+g', search_google, suppress=True)
keyboard.add_hotkey('ctrl+alt+y', search_youtube, suppress=True)
keyboard.add_hotkey('ctrl+alt+t', toggle_hotkeys, suppress=True)
keyboard.add_hotkey('esc', lambda: exit(), suppress=True)  # Fully exit

keyboard.wait()
