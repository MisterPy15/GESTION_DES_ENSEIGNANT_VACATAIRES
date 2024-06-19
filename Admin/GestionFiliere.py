import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk



class Filiere:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion des Filières")
        self.mac.geometry("850x700+300+0")
        self.mac.resizable(0,0)
        
        
        # self.Elements_Du_haut()
        # self.Formulaire()
        # self.tableDetails()
        
        
        
    # def Formulaire(self):
        
        self.frame1 = ct.CTkFrame(self.mac, width=400, height=200, corner_radius=15)
        self.frame1.place(x=10, y=200)
        
        labelTitre = ct.CTkLabel(self.frame1, text="Gestion Des Filières", font=("times new roman", 25, "bold"))
        labelTitre.place(x=10, y=10)
        
        labelNomFil = ct.CTkLabel(self.frame1, text="Filière", font=("times new roman", 18, "bold"))
        labelNomFil.place(x=10, y=60)
        
        entryNomFil = ct.CTkEntry(self.frame1, placeholder_text="Nom de la filière", 
                                  width=300, font=("times new roman", 15, "bold"))
        entryNomFil.place(x=80, y=60)
        
        
        buttonAjout = ct.CTkButton(self.frame1, text="Ajouter", width=100, fg_color="green",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonAjout.place(x=20, y=150)
        
        
        buttonModifier = ct.CTkButton(self.frame1, text="Modifier", width=100, fg_color="#305B43",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonModifier.place(x=140, y=150)
        
        
        buttonAjout = ct.CTkButton(self.frame1, text="Supprimer", width=100, fg_color="red",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonAjout.place(x=260, y=150)
        
    # def tableDetails(self):
         
        self.frameGeneral = ct.CTkFrame(self.mac, width=380, height=450)
        self.frameGeneral.place(x=420, y=200)
        
        self.scrollable_frame = ct.CTkScrollableFrame(self.frameGeneral, label_text="-", height=150, width=320)
        self.scrollable_frame.place(x=20 ,y=80)
        
        lblFiliere = ct.CTkLabel(self.frameGeneral, text="Filiere", font=("times new roman", 20, "bold"))
        lblFiliere.place(x=18, y=10)
        
        entryRecherche = ct.CTkEntry(self.frameGeneral, placeholder_text="Recherche", width=200)
        entryRecherche.place(x=100, y=10)
        
        buttonRecherche = ct.CTkButton(self.frameGeneral, text="🔍", corner_radius=30, width=5, cursor="hand", fg_color="green",)
        buttonRecherche.place(x=315, y=10)
        
        
        lblID = ct.CTkLabel(self.frameGeneral, text="ID", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblID.place(x=20, y=85)
        
        
        lblNomFil = ct.CTkLabel(self.frameGeneral, text="Filière", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblNomFil.place(x=235, y=85) 
        
        
        self.scrollable_frame_labelId = [] 
        self.scrollable_frame_labelFil = [] 
        
        
        for i in range(5):
            labelId = ct.CTkLabel(self.scrollable_frame, text=f"Id {i+1}")
            labelId.grid(row=i, column=0, padx=10, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelId.append(labelId)
            
            labelFil = ct.CTkLabel(self.scrollable_frame, text=f"Filière {i+1}")
            labelFil.grid(row=i, column=1, padx=170, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelFil.append(labelFil)


    # def Elements_Du_haut(self):
        
        apparenceOption = ct.CTkOptionMenu(self.mac, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.place(x=650, y=45)
        

        
        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.mac, image=self.logo_UTA_login, borderwidth=0,
                              width=200, height=100)
        label_logoUTA.place(x=5, y=15)
        
    
    
    
    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)








if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Filiere(Mac)
    Mac.mainloop()
