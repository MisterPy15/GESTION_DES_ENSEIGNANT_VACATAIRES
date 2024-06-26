import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector


class DashboardProf:
    def __init__(self, mac, nom, prenom, enseignant_id):
        self.mac = mac
        self.mac.title("Dashboard")
        self.mac.geometry("1350x700+0+0")

        self.nom = nom
        self.prenom = prenom
        self.enseignant_id = enseignant_id

        self.frameInfo = ct.CTkFrame(self.mac, width=1350, height=110)
        self.frameInfo.place(x=10, y=10)

        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.frameInfo, image=self.logo_UTA_login, borderwidth=0,
                              width=200, height=100)
        label_logoUTA.place(x=10, y=5)

        labeBievenue = ct.CTkLabel(self.frameInfo, text=f"Bon retour Parmi nous Dr: {self.prenom} {self.nom}", 
                                   font=("times new roman", 25, "bold"))
        labeBievenue.place(x=440, y=25)

        apparenceOption = ct.CTkOptionMenu(self.frameInfo, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.place(x=1200, y=35)

        self.frameGestion = ct.CTkFrame(self.mac, width=350, height=650)
        self.frameGestion.place(x=10, y=120)

        labeldash = ct.CTkLabel(self.frameGestion, text="Dashboard Enseignant", text_color="white", fg_color="green", corner_radius=10,
                                                    width=310, font=("times new roman", 25, "bold"))
        labeldash.place(x=15, y=20)


        # Frame pour le tableau de l'emploi du temps
        self.frameTableau = Frame(self.mac, bd=4)
        self.frameTableau.place(x=380, y=150, width=950, height=600)  
        
        # Création du tableau pour l'emploi du temps
        self.create_schedule_table()
        self.load_schedule()

    def create_schedule_table(self):
        self.jours = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI"]
        self.heures = ["08h à 12h", "13h à 17h"]
        self.schedule_labels = [[] for _ in range(len(self.heures))]

        for i, jour in enumerate(["HEURES/JOURS"] + self.jours):
            label = ct.CTkLabel(self.frameTableau, text=jour, text_color="black", padx=10, pady=5, fg_color="green" if i == 0 else "red")
            label.grid(row=2, column=i, sticky="nsew")

        for i, heure in enumerate(self.heures):
            label = ct.CTkLabel(self.frameTableau, text=heure, padx=10, pady=5, fg_color="orange")
            label.grid(row=i + 3, column=0, sticky="nsew")
            for j in range(len(self.jours)):
                cell = ct.CTkLabel(self.frameTableau, text="", text_color="black", padx=10, pady=5, fg_color="white")
                cell.grid(row=i + 3, column=j + 1, sticky="nsew", padx=5, pady=5)
                self.schedule_labels[i].append(cell)

        # Ajustement de la taille des colonnes
        for i in range(len(self.jours) + 1):
            self.frameTableau.grid_columnconfigure(i, weight=1)
        for i in range(len(self.heures) + 3):
            self.frameTableau.grid_rowconfigure(i, weight=1)

    def load_schedule(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="vacataire",
            port=8889
        )
        cursor = connection.cursor()

        query = "SELECT Filière, Module, Date, Heure, Niveau, Salle FROM emploi_temps WHERE Id_Enseignant = %s"
        cursor.execute(query, (self.enseignant_id,))
        emploi_du_temps = cursor.fetchall()

        for row in emploi_du_temps:
            filiere, module, date, heure, niveau, salle = row
            jour_index = self.jours.index(date)
            heure_index = self.heures.index(heure)
            cell_text = f"{module}\n{salle}\n{filiere}\n{niveau}"
            self.schedule_labels[heure_index][jour_index].configure(text=cell_text)

        cursor.close()
        connection.close()

    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    Mac = ct.CTk()
    obj = DashboardProf(Mac, "Nom", "Prenom", "ID")
    Mac.mainloop()
