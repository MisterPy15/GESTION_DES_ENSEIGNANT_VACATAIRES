import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk

class DashboardProf:
    def __init__(self, mac, nom, prenom):
        self.mac = mac
        self.mac.title("Dashboard Enseignant")
        self.mac.geometry("1350x700+0+0")

        # -------------- Frame d'Information --------------
        self.frameInfo = ct.CTkFrame(self.mac, width=1350, height=110)
        self.frameInfo.place(x=10, y=10)

        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.frameInfo, image=self.logo_UTA_login, borderwidth=0,
                              width=200, height=100)
        label_logoUTA.place(x=10, y=5)

        labeBienvenue = ct.CTkLabel(self.frameInfo, text=f"Bienvenue {prenom} {nom}",
                                   font=("times new roman", 35, "bold"))
        labeBienvenue.place(x=480, y=25)

        # -------------- Contenu Principal --------------
        self.mainFrame = ct.CTkFrame(self.mac, width=1320, height=560)
        self.mainFrame.place(x=10, y=130)

        # Exemples de contenu pour le dashboard enseignant :
        # Ajoutez des widgets spécifiques aux fonctionnalités pour les enseignants
        self.labelDashboard = ct.CTkLabel(self.mainFrame, text="Dashboard Enseignant", font=("times new roman", 30, "bold"))
        self.labelDashboard.place(x=550, y=20)

        self.labelInfo = ct.CTkLabel(self.mainFrame, text="Informations sur l'enseignant", font=("times new roman", 25, "italic"))
        self.labelInfo.place(x=50, y=100)

        self.labelSchedule = ct.CTkLabel(self.mainFrame, text="Emploi du Temps", font=("times new roman", 25, "italic"))
        self.labelSchedule.place(x=50, y=200)

        # Ajoutez d'autres widgets selon vos besoins (Tableaux, Graphiques, Boutons, etc.)



if __name__ == "__main__":
    root = ct.CTk()
    app = DashboardProf(root, "John", "Doe")
    root.mainloop()
