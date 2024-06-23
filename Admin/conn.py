import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Créer la base de données et la table des utilisateurs si elles n'existent pas
def initialize_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Ajouter un utilisateur pour le test
def add_test_user():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "password123"))
    conn.commit()
    conn.close()




# Vérifier les informations d'identification de l'utilisateur
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Initialiser l'application CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x200")
app.title("Teraface Login")

# Fonction de connexion
def login():
    username = entry_username.get()
    password = entry_password.get()
    user = check_credentials(username, password)
    if user:
        messagebox.showinfo("Success", "Bienvenue!")
    else:
        messagebox.showerror("Error", "Nom d'utilisateur ou mot de passe incorrect")

# Création des widgets de l'interface
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry_username = ctk.CTkEntry(master=frame, placeholder_text="Nom d'utilisateur")
entry_username.pack(pady=12, padx=10)

entry_password = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
entry_password.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

# Initialiser la base de données et ajouter un utilisateur de test
initialize_db()
add_test_user()

# Lancer l'application
app.mainloop()
