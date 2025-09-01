# 🔥 Hotkey Clipboard Search Tool

**Search Google & YouTube instantly using hotkeys!**  

This lightweight Windows tool lets you search **Google** or **YouTube** directly from your clipboard with customizable global hotkeys. Hotkeys can be toggled ON/OFF and show small toast notifications.

---

## ✨ Features

- 🔍 **Google Search** – Ctrl+Alt+G  
- ▶️ **YouTube Search** – Ctrl+Alt+Y  
- ⚡ **Toggle Hotkeys** – Ctrl+Alt+T (ON/OFF with notification)  
- 🛑 **Exit Script** – Esc  
- 🖥️ **Runs silently in background**  
- 🚫 **Suppress keypresses** – prevents letters from being typed while using hotkeys  
- 🪟 **Windows native toast notifications** using [plyer](https://pypi.org/project/plyer/)

---

## 📦 Installation & Usage

1. Clone the repo:

```bash
git clone https://github.com/happyman09/hotkey-clipboard-search.git
cd hotkey-clipboard-search/source
Install dependencies:

pip install keyboard pyperclip plyer


Run the script:

python hotkey_search_final.py

💻 Hotkeys
Hotkey	Action
Ctrl+Alt+G	Google search clipboard text
Ctrl+Alt+Y	YouTube search clipboard text
Ctrl+Alt+T	Toggle hotkeys ON/OFF
Esc	Exit the script completely
🔨 Build Windows Executable
pip install pyinstaller
pyinstaller --onefile --noconsole hotkey_search_final.py


Copy .exe to Shell:startup → starts automatically on Windows login

No terminal window will appear; fully silent in background

📝 Notes

Works on Windows only

Cross-platform toast notifications via plyer

Hotkeys use Ctrl+Alt to reduce clashes, even during games

🤝 Contributions

Want to add Linux or Mac support?

Have ideas for additional search engines or custom hotkeys?

Open a PR or issue — contributions welcome!

📜 License

MIT License


---

If you want, I can **also create the shield badges** (stars, last commit, license, downloads, etc.) for the top of this README to make it **instantly flex-worthy** like your wallpaper-themer repo.  

Do you want me to do that next?
