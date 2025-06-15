# Advanced AES-256 Encryption Tool with Enhanced GUI

import os
import threading
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from base64 import urlsafe_b64encode, urlsafe_b64decode

backend = default_backend()

# -------------------- Utility Functions --------------------
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_path = file_path + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(salt + iv + ciphertext)
    return encrypted_path

def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    decrypted_path = file_path.replace('.enc', '.dec')
    with open(decrypted_path, 'wb') as f:
        f.write(plaintext)
    return decrypted_path

# -------------------- GUI Setup --------------------
def choose_file():
    filepath = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filepath)

def set_status(msg):
    status_label.config(text=msg)
    root.update_idletasks()

def run_with_progress(task_func, path, password):
    def runner():
        try:
            progress_bar.start(10)
            set_status("Processing...")
            out_path = task_func(path, password)
            set_status("Done: " + out_path)
            messagebox.showinfo("Success", f"Output saved to:\n{out_path}")
        except Exception as e:
            set_status("Error")
            messagebox.showerror("Failed", str(e))
        finally:
            progress_bar.stop()

    threading.Thread(target=runner).start()

def encrypt_action():
    path = entry_file.get()
    password = entry_password.get()
    if not path or not password:
        messagebox.showerror("Error", "Please provide both file and password.")
        return
    run_with_progress(encrypt_file, path, password)

def decrypt_action():
    path = entry_file.get()
    password = entry_password.get()
    if not path or not password:
        messagebox.showerror("Error", "Please provide both file and password.")
        return
    run_with_progress(decrypt_file, path, password)

def on_drop(event):
    file_path = event.data.strip('{}')
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

# -------------------- UI Layout --------------------
root = tk.Tk()
root.title("AES-256 Encryption Tool")
root.geometry("520x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

style_opts = {'bg': '#1e1e1e', 'fg': 'white', 'font': ('Poppins', 10)}

tk.Label(root, text="File Path:", **style_opts).pack(pady=(15, 0))
entry_file = tk.Entry(root, width=60, **style_opts)
entry_file.pack(pady=5)
tk.Button(root, text="Browse", command=choose_file).pack()

# Drag and drop file support (Windows only)
try:
    import tkinterdnd2 as tkdnd
    dnd = tkdnd.TkinterDnD.Tk()
    entry_file.drop_target_register(tkdnd.DND_FILES)
    entry_file.dnd_bind('<<Drop>>', on_drop)
except:
    pass

tk.Label(root, text="Password:", **style_opts).pack(pady=(15, 0))
entry_password = tk.Entry(root, width=60, show='*', **style_opts)
entry_password.pack(pady=5)

tk.Button(root, text="Encrypt File", command=encrypt_action, bg="#3a7bd5", fg="white", width=20).pack(pady=(10, 5))
tk.Button(root, text="Decrypt File", command=decrypt_action, bg="#34a853", fg="white", width=20).pack(pady=5)

progress_bar = ttk.Progressbar(root, mode='indeterminate', length=400)
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="Idle", **style_opts)
status_label.pack()

root.mainloop()
