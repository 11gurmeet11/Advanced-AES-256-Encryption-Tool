# 🚀 Advanced AES‑256 Encryption Tool

A cross‑platform, GUI‑based file encryption and decryption application that leverages industry‑standard **AES‑256‑CBC** to keep your data safe. Built with Python 3, `cryptography`, and `Tkinter`.

---

## ✨ Key Features

| Feature                  | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| 🔒 AES‑256 Encryption    | Secure files using 256‑bit keys derived via PBKDF2‑HMAC‑SHA‑256. |
| 📂 Drag‑and‑Drop         | Drop any file onto the app window—no file dialog needed.         |
| 📊 Progress Bar          | Real‑time visual feedback during long operations.                |
| 📢 Status Messages       | Live status updates (Idle ▸ Processing ▸ Done!).                 |
| 🌓 Dark Theme            | Sleek, modern glass‑morphism dark UI (Poppins font).             |
| 🖥 Portable EXE          | One‑click build for Windows using PyInstaller.                   |
| 🐧 macOS / Linux Support | Works everywhere Python 3 and `cryptography` are available.      |



---

## 📦 Requirements

```text
Python >= 3.8
cryptography >= 42.0
Tkinter (bundled with CPython on Windows/macOS; install `python3-tk` on Debian/Ubuntu.)
```

Install dependencies:

```bash
pip install -r requirements.txt
```

*`requirements.txt`*

```
cryptography>=42.0
```

---

## 🚀 Quick Start (Source)

```bash
# 1. Clone the repo
$ git clone https://github.com/<your‑username>/aes‑encryption‑tool.git
$ cd aes‑encryption‑tool

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Run the app
$ python aes_gui_tool.py
```

---

## 🏗 Building a Portable .exe (Windows)

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```
2. Build single‑file executable:

   ```bash
   pyinstaller --onefile --noconsole --icon=lock.ico aes_gui_tool.py
   ```
3. Your standalone executable will be at `dist/aes_gui_tool.exe`.

> **Tip:** Use [`auto‑py‑to‑exe`](https://github.com/brentvollebregt/auto-py-to-exe) for a graphical build wizard.

---

## 🐧 macOS & Linux Notes

* Ensure Tkinter is available: [https://tkdocs.com/tutorial/install.html](https://tkdocs.com/tutorial/install.html)
* Build a macOS `.app` bundle with [`py2app`](https://py2app.readthedocs.io/) or a universal binary with [`briefcase`](https://briefcase.readthedocs.io/).
* On Linux, create an AppImage using [`appimagetool`](https://appimage.org/) or package via Snap/Flatpak.

---

## 🔑 Security Considerations

* **Passwords are never stored**—keys are derived in‑memory only.
* A unique 16‑byte salt + IV are generated per file.
* Output format: `[salt|iv|ciphertext]` so each encrypted file is self‑contained.
* **Warning:** Losing your password means losing access to the data; there is no back‑door recovery.

---

## 🛠 Roadmap

* [ ] Multithreaded chunked encryption for very large files.
* [ ] Optional authenticated encryption (AES‑GCM).
* [ ] Native drag‑and‑drop for macOS/Linux via `tkinterdnd2` fallback.
* [ ] Localization (English, Hindi …).

Feel free to open issues or suggest features!

---

## 🤝 Contributing

1. Fork the repo & create your branch: `git checkout -b feature/awesome`
2. Commit your changes: `git commit -m 'Add awesome feature'`
3. Push to the branch: `git push origin feature/awesome`
4. Open a Pull Request.

### Coding Style

* Keep code **PEP 8** compliant.
* Use type hints where practical.
* Write concise docstrings.

---

## 🪪 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Gurmeet Kaur

> *If you use this tool for academic or professional work, please star ⭐ the repository and give credit!*
