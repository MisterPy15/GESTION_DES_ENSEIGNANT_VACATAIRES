import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog

class Rapport:
    
    
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion des Rapports")
        self.mac.geometry("1040x700+150+0")
        self.mac.resizable(0, 0)

        apparenceOption = ct.CTkOptionMenu(self.mac, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.place(x=750, y=25)

        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.mac, image=self.logo_UTA_login, borderwidth=0, width=200, height=100)
        label_logoUTA.place(x=5, y=15)

        self.frame1 = ct.CTkFrame(self.mac, width=400, height=200, corner_radius=15)
        self.frame1.place(x=10, y=200)

        labelTitre = ct.CTkLabel(self.frame1, text="Gestion Des Rapports", font=("times new roman", 25, "bold"))
        labelTitre.place(x=10, y=10)

        labelIdEns = ct.CTkLabel(self.frame1, text="ID Enseigant", font=("times new roman", 18, "bold"))
        labelIdEns.place(x=10, y=60)

        self.entryNomFil = ct.CTkEntry(self.frame1, placeholder_text="Entrez un Id",
                                       width=200, font=("times new roman", 15, "bold"))
        self.entryNomFil.place(x=120, y=60)

        buttonGenerer = ct.CTkButton(self.frame1, text="Generer", width=120, fg_color="#305A43",
                                     corner_radius=8, cursor="hand", font=("times new roman", 25, "bold"),
                                     command=self.generer_rapport)
        buttonGenerer.place(x=130, y=150)

        self.frameGeneral = ct.CTkFrame(self.mac, width=580, height=550, border_width=2, border_color="green")
        self.frameGeneral.place(x=450, y=90)

        buttonImprimer = ct.CTkButton(self.mac, text="Télécharger", width=200, fg_color="#305A43",
                                      corner_radius=8, cursor="hand", font=("times new roman", 25, "bold"),
                                      command=self.telecharger_pdf)
        buttonImprimer.place(x=650, y=650)


    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)


    def generer_rapport(self):
        id_ens = self.entryNomFil.get()
        rapport_text = f"Rapport pour l'enseignant ID: {id_ens}"
        
        # Affichage dans frameGeneral
        for widget in self.frameGeneral.winfo_children():
            widget.destroy()
        
        labelRapport = ct.CTkLabel(self.frameGeneral, text=rapport_text, font=("times new roman", 20, "bold"))
        labelRapport.place(x=10, y=10)


    def telecharger_pdf(self):
        id_ens = self.entryNomFil.get()
        rapport_text = f"Rapport pour l'enseignant ID: {id_ens}"
        
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filepath:
            c = canvas.Canvas(filepath, pagesize=letter)
            c.drawString(100, 750, rapport_text)
            c.save()



if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Rapport(Mac)
    Mac.mainloop()
