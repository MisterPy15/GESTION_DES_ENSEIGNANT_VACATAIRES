import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk
from Dashboard import Dashboard



class Login:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Login")
        self.mac.geometry("800x600+300+80")
        self.mac.resizable(0,0)
        
        #--------------Les Variables--------------
        self.Email = StringVar()
        self.mdp = StringVar()
 
        # Utilisation d'une seule variable de contrôle pour les boutons radio
        radio_button_var = StringVar(value="")  # Valeur par défaut
        
        
                
        apparenceOption = ct.CTkOptionMenu(self.mac, values=["Dark", "Light",  "System"], corner_radius=20,
                                          command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        
        
        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((450, 120))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)
        
        label_logoUTA = Label(self.mac, image=self.logo_UTA_login, borderwidth=0,
                              width=450, height=120)
        label_logoUTA.place(x=350, y=5)
        
        
        
        logoIcon = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/Icon1 login.png")
        logoIcon = logoIcon.resize((450, 570))
        self.logo_Icon_login = ImageTk.PhotoImage(logoIcon)
        
        label_logoIcon = Label(self.mac, image=self.logo_Icon_login, borderwidth=0,
                               width=450, height=570)
        label_logoIcon.place(x=350, y=125)
        
        
        
        labelConsigne = ct.CTkLabel(self.mac, text="Bienvenue! \n Connectez vous", 
                                    font=("times new roman", 40, "bold"))
        labelConsigne.place(x=15, y=120)
        
        
        
        entryEmail = ct.CTkEntry(self.mac, placeholder_text="Email",
                                 width=250, font=("times new roman", 15, "italic"))
        entryEmail.place(x=15, y=280)
        
        
        
        entryMdp = ct.CTkEntry(self.mac, placeholder_text="Mot de Passe", 
                               width=250, show="*", font=("times new roman", 15, "italic"))
        entryMdp.place(x=15, y=350)
        
        
        
        butonConnection = ct.CTkButton(self.mac, text="Se Connecter", 
                                       font=("times new roman", 18, "italic"), 
                                       fg_color="green",width=250, 
                                       corner_radius=20, command=self.dashB)
        butonConnection.place(x=25, y=400)
        
        
        
        labelOu = ct.CTkLabel(self.mac, text="En tant que", 
                              font=("times new roman", 20, "bold"))
        labelOu.place(x=80, y=450)
        
        
        

        buttonRProf = ct.CTkRadioButton(self.mac, text="Enseignant", variable=radio_button_var, value="Prof")
        buttonRProf.place(x=50, y=500)
        
        
        
        
        buttonRAdmin = ct.CTkRadioButton(self.mac, text="Admin", variable=radio_button_var, value="Admin")
        buttonRAdmin.place(x=150, y=500)



    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)




    def dashB(self):
        self.nouvelle_fenetre = Toplevel(self.mac)
        self.app = Dashboard(self.nouvelle_fenetre)


if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Login(Mac)
    Mac.mainloop()
