import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk



class Enseigants:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion des Enseignants")
        self.mac.geometry("1000x700+200+0")
        self.mac.resizable(0,0)
        
        
        self.Elements_Du_haut()
        self.Formulaire()
        self.tableDetails()
        
     
     
        
        
    def Formulaire(self):
        
        self.frame1 = ct.CTkFrame(self.mac, width=400, height=400, corner_radius=15)
        self.frame1.place(x=10, y=200)
        
        labelTitre = ct.CTkLabel(self.frame1, text="Gestion Des Enseigants", font=("times new roman", 25, "bold"))
        labelTitre.place(x=10, y=10)
        
        labelNomEns = ct.CTkLabel(self.frame1, text="Nom", font=("times new roman", 18, "bold"))
        labelNomEns.place(x=10, y=60)
        
        entryNomEns = ct.CTkEntry(self.frame1, placeholder_text="Nom de l'Enseignant", 
                                  width=300, font=("times new roman", 15, "bold"))
        entryNomEns.place(x=80, y=60)
        
        
        labelPrenomEns = ct.CTkLabel(self.frame1, text="Prénom", font=("times new roman", 18, "bold"))
        labelPrenomEns.place(x=10, y=110)
        
        entryPrenomEns = ct.CTkEntry(self.frame1, placeholder_text="Prénom", 
                                  width=300, font=("times new roman", 15, "bold"))
        entryPrenomEns.place(x=80, y=110)
        
        
        labelEmailEns = ct.CTkLabel(self.frame1, text="Email", font=("times new roman", 18, "bold"))
        labelEmailEns.place(x=10, y=160)
        
        entryEmailEns = ct.CTkEntry(self.frame1, placeholder_text="Email", 
                                  width=300, font=("times new roman", 15, "bold"))
        entryEmailEns.place(x=80, y=160)
        
        
        labelPasswordEns = ct.CTkLabel(self.frame1, text="Mot de Passe", font=("times new roman", 18, "bold"))
        labelPasswordEns.place(x=10, y=210)
        
        entryPasswordEns = ct.CTkEntry(self.frame1, placeholder_text="Mot de Passe", show="*",
                                  width=250, font=("times new roman", 15, "bold"))
        entryPasswordEns.place(x=125, y=210)
        
        
        labelConfirmPasswordEns = ct.CTkLabel(self.frame1, text="Confirmer", font=("times new roman", 18, "bold"))
        labelConfirmPasswordEns.place(x=10, y=260)
        
        entryConfirmPasswordEns = ct.CTkEntry(self.frame1, placeholder_text="Confirmer les Mot de passe", show="*", 
                                  width=280, font=("times new roman", 15, "bold"))
        entryConfirmPasswordEns.place(x=100, y=260)
        
        
        
        buttonAjout = ct.CTkButton(self.frame1, text="Ajouter", width=100, fg_color="green",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonAjout.place(x=20, y=330)
        
        
        buttonModifier = ct.CTkButton(self.frame1, text="Modifier", width=100, fg_color="#305B43",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonModifier.place(x=140, y=330)
        
        
        buttonAjout = ct.CTkButton(self.frame1, text="Supprimer", width=100, fg_color="red",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"))
        buttonAjout.place(x=260, y=330)
  
  
        
    def tableDetails(self):
         
        self.frameGeneral = ct.CTkFrame(self.mac, width=570, height=400)
        self.frameGeneral.place(x=420, y=200)
        
        self.scrollable_frame = ct.CTkScrollableFrame(self.frameGeneral, label_text="-", height=150, width=520)
        self.scrollable_frame.place(x=17 ,y=80)
        
        lblEnseigant = ct.CTkLabel(self.frameGeneral, text="Enseigant", font=("times new roman", 25, "bold"))
        lblEnseigant.place(x=35, y=10)
        
        entryRecherche = ct.CTkEntry(self.frameGeneral, placeholder_text="Recherche", width=200)
        entryRecherche.place(x=180, y=10)
        
        buttonRecherche = ct.CTkButton(self.frameGeneral, text="🔍", corner_radius=30, width=5,
                                       cursor="hand", fg_color="green",)
        buttonRecherche.place(x=390, y=10)
        
        
        lblID = ct.CTkLabel(self.frameGeneral, text="ID", fg_color="green",text_color="white",
                            corner_radius=10, font=("times new roman", 18, "bold"))
        lblID.place(x=20, y=85)
        
        
        lblNomEns = ct.CTkLabel(self.frameGeneral, text="Nom", fg_color="green",text_color="white",
                                corner_radius=10, font=("times new roman", 18, "bold"))
        lblNomEns.place(x=90, y=85) 
        
        
        lblPrenomEns = ct.CTkLabel(self.frameGeneral, text="Prénom", fg_color="green",text_color="white",
                                corner_radius=10, font=("times new roman", 18, "bold"))
        lblPrenomEns.place(x=190, y=85) 
        
        
        lblTel = ct.CTkLabel(self.frameGeneral, text="Tel", fg_color="green",text_color="white",
                            corner_radius=10, font=("times new roman", 18, "bold"))
        lblTel.place(x=310, y=85)
        
        
        lblEmailEns = ct.CTkLabel(self.frameGeneral, text="Email", fg_color="green",text_color="white",
                                corner_radius=10, font=("times new roman", 18, "bold"))
        lblEmailEns.place(x=400, y=85) 
        
        
        lblPasswordEns = ct.CTkLabel(self.frameGeneral, text="MDP", fg_color="green",text_color="white",
                                corner_radius=10, font=("times new roman", 12, "bold"))
        lblPasswordEns.place(x=500, y=85) 
        
        
        self.scrollable_frame_labelId = [] 
        self.scrollable_frame_labelNomEns = [] 
        self.scrollable_frame_labelPrenomEns = [] 
        self.scrollable_frame_labelTelEns = [] 
        self.scrollable_frame_labelEmailEns = [] 
        self.scrollable_frame_labelPaswordlEns = [] 
        
        
        for i in range(5):
            labelId = ct.CTkLabel(self.scrollable_frame, text=f"Id {i+1}")
            labelId.grid(row=i, column=0, padx=10, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelId.append(labelId)
            
            labelNomEns = ct.CTkLabel(self.scrollable_frame, text=f"Nom {i+1}")
            labelNomEns.grid(row=i, column=1, padx=30, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelNomEns.append(labelNomEns)
            
            labelPrenomEns = ct.CTkLabel(self.scrollable_frame, text=f"Prénom {i+1}")
            labelPrenomEns.grid(row=i, column=2, padx=30, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelPrenomEns.append(labelPrenomEns)
            
            labelTelEns = ct.CTkLabel(self.scrollable_frame, text=f"Tel {i+1}")
            labelTelEns.grid(row=i, column=3, padx=30, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelTelEns.append(labelTelEns)
            
            labelEmailEns = ct.CTkLabel(self.scrollable_frame, text=f"Email {i+1}")
            labelEmailEns.grid(row=i, column=4, padx=30, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelEmailEns.append(labelEmailEns)
            
            labelPasswordEns = ct.CTkLabel(self.scrollable_frame, text="*")
            labelPasswordEns.grid(row=i, column=5, padx=30, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelPaswordlEns.append(labelEmailEns)



    def Elements_Du_haut(self):
        
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
    obj = Enseigants(Mac)
    Mac.mainloop()
