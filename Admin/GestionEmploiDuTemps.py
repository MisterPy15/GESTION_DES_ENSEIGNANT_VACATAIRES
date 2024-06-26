import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import mysql.connector


class EmploiTemps:
    def __init__(self, mac):
        # Connexion à la base de données
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="vacataire",
            port=8889
        )
        self.cursor = self.connection.cursor()

        # Initialisation de la fenêtre principale
        self.mac = mac
        self.mac.title("Gestion d'emploi du temps")
        self.mac.geometry("960x700+45+0")
        self.mac.resizable(0, 0)
        self.mac.focus_force()
        self.mac.grab_set()

        # Création des variables
        self.jours = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI"]
        self.heurs = ["08h à 12h", "13h à 17h"]
        self.schedule = [["" for _ in range(8)] for _ in range(11)]

        self.Filiere_var = ctk.StringVar()
        self.Module_var = ctk.StringVar()
        self.jour_var = ctk.StringVar(value=self.jours[0])
        self.heur_var = ctk.StringVar(value=self.heurs[0])
        self.niveau_var = ctk.StringVar()
        self.salle_var = ctk.StringVar()
        self.Enseigant_id_var = ctk.StringVar()

        # Création des champs de saisie
        self.create_widgets()

        # Création d'un tableau pour l'emploi du temps
        self.create_schedule_table()

        # Boucle principale
        self.mac.mainloop()

    def create_widgets(self):
        ctk.CTkLabel(self.mac, text="ID Enseignant:").place(x=35, y=15)
        Enseigant_id_entry = ctk.CTkEntry(self.mac, textvariable=self.Enseigant_id_var)
        Enseigant_id_entry.place(x=130, y=15)

        ctk.CTkLabel(self.mac, text="Module:").place(x=280, y=15)
        Module_entry = ctk.CTkEntry(self.mac, textvariable=self.Module_var)
        Module_entry.place(x=350, y=15)

        ctk.CTkLabel(self.mac, text="Heure:").place(x=510, y=15)
        heur_menu = ctk.CTkOptionMenu(self.mac, variable=self.heur_var, values=self.heurs)
        heur_menu.place(x=570, y=15)

        ctk.CTkLabel(self.mac, text="Filière:").place(x=35, y=90)
        Filiere_entry = ctk.CTkEntry(self.mac, textvariable=self.Filiere_var)
        Filiere_entry.place(x=80, y=90)

        ctk.CTkLabel(self.mac, text="Niveau").place(x=280, y=90)
        Niveau_menu = ctk.CTkEntry(self.mac, textvariable=self.niveau_var)
        Niveau_menu.place(x=350, y=90)

        ctk.CTkLabel(self.mac, text="Jour:").place(x=35, y=180)
        jour_menu = ctk.CTkOptionMenu(self.mac, variable=self.jour_var, values=self.jours)
        jour_menu.place(x=80, y=180)

        ctk.CTkLabel(self.mac, text="Salle:").place(x=280, y=180)
        salle_entry = ctk.CTkEntry(self.mac, textvariable=self.salle_var)
        salle_entry.place(x=350, y=180)

        # Bouton pour enregistrer les informations
        save_button = ctk.CTkButton(self.mac, text="Enregistrer", command=self.save_schedule)
        save_button.place(x=550, y=100)


    
        self.frameTableau = Frame(self.mac, bd=4)
        self.frameTableau.place(x=5, y=215, width=950, height=480)  
    
    
    def create_schedule_table(self):
        self.labels = [[] for _ in range(len(self.heurs))]
        for i, jour in enumerate(["HEURES/JOURS"] + self.jours):
            label = ctk.CTkLabel(self.frameTableau, text=jour, text_color="black", padx=10, pady=5, fg_color="green" if i == 0 else "red")
            label.grid(row=2, column=i, sticky="nsew")

        for i, heur in enumerate(self.heurs):
            label = ctk.CTkLabel(self.frameTableau, text=heur, padx=10, pady=5, fg_color="orange")
            label.grid(row=i + 3, column=0, sticky="nsew")
            for j in range(len(self.jours)):
                cell = ctk.CTkLabel(self.frameTableau, text="", text_color="black", padx=10, pady=5, fg_color="white")
                cell.grid(row=i + 3, column=j + 1, sticky="nsew", padx=5, pady=5)
                self.labels[i].append(cell)

        # Configuration des colonnes et lignes pour le redimensionnement automatique
        for i in range(len(self.jours) + 1):
            self.frameTableau.grid_columnconfigure(i, weight=1)
        for i in range(len(self.heurs) + 3):
            self.frameTableau.grid_rowconfigure(i, weight=1)

    def save_schedule(self):
        Filiere = self.Filiere_var.get()
        Module = self.Module_var.get()
        jour = self.jour_var.get()
        heur = self.heur_var.get()
        niveau = self.niveau_var.get()
        salle = self.salle_var.get()
        Enseigant_id = self.Enseigant_id_var.get()

        if not all([jour, heur, Module, salle, Filiere, Enseigant_id, niveau]):
            messagebox.showwarning("Champ manquant", "Veuillez remplir tous les champs.", parent=self.mac)
            return

        # Enregistrement des informations dans la base de données
        try:
            self.cursor.execute(
                "INSERT INTO emploi_temps (Filière, Module, Date, Heure, Niveau, Salle, Id_Enseignant) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (Filiere, Module, jour, heur, niveau, salle, Enseigant_id)
            )
            self.connection.commit()
            messagebox.showinfo("Succès", "Emploi du temps enregistré avec succès.", parent=self.mac)
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement: {err}",parent=self.mac)
            return

        # Ajout des informations dans le tableau
        row = self.heurs.index(heur) + 1
        column = self.jours.index(jour) + 1
        self.schedule[row][column] = f"{Module}\n{salle}\n{Filiere}\nID: {Enseigant_id}"
        self.update_schedule()

    def update_schedule(self):
        for i in range(len(self.heurs)):
            for j in range(len(self.jours)):
                cell_text = self.schedule[i + 1][j + 1]
                self.labels[i][j].configure(text=cell_text)






if __name__ == "__main__":
    Mac =  ctk.CTk()
    obj = EmploiTemps(Mac)
    Mac.mainloop()
