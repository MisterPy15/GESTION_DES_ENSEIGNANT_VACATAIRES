import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk
from DashboardProf import DashboardProf
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

class LoginEnseignant:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Login")
        self.mac.geometry("800x600+300+80")
        self.mac.resizable(0, 0)

        #--------------Les Variables--------------
        self.Email = StringVar()
        self.mdp = StringVar()
        self.radio_button_var = StringVar(value="")

        apparenceOption = ct.CTkOptionMenu(self.mac, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((450, 120))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.mac, image=self.logo_UTA_login, borderwidth=0, width=450, height=120)
        label_logoUTA.place(x=350, y=5)

        logoIcon = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/Icon1 login.png")
        logoIcon = logoIcon.resize((450, 570))
        self.logo_Icon_login = ImageTk.PhotoImage(logoIcon)

        label_logoIcon = Label(self.mac, image=self.logo_Icon_login, borderwidth=0, width=450, height=570)
        label_logoIcon.place(x=350, y=125)

        labelConsigne = ct.CTkLabel(self.mac, text="Bienvenue! \n Connectez vous", 
                                    font=("times new roman", 40, "bold"))
        labelConsigne.place(x=15, y=120)

        self.entryEmail = ct.CTkEntry(self.mac, placeholder_text="Email", width=250, font=("times new roman", 15, "italic"))
        self.entryEmail.place(x=15, y=280)

        self.entryMdp = ct.CTkEntry(self.mac, placeholder_text="Mot de Passe", width=250, show="*", font=("times new roman", 15, "italic"))
        self.entryMdp.place(x=15, y=350)

        butonConnection = ct.CTkButton(self.mac, text="Se Connecter", 
                                       font=("times new roman", 18, "italic"), 
                                       fg_color="green", width=250, 
                                       corner_radius=20, command=self.connection)
        butonConnection.place(x=25, y=400)

    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)

    def connection(self):
        if self.entryEmail.get() == "" or self.entryMdp.get() == "":
            messagebox.showerror("Attention", "Veuillez Remplir tout les champs", parent=self.mac)
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="vacataire",
                    port=8889  
                )
                cur = connection.cursor()
                query = "SELECT Id_Enseignant, Nom, Prenom FROM enseignant WHERE Email=%s AND Mot_Passe=%s"
                cur.execute(query, (self.entryEmail.get(), self.entryMdp.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Attention", "Email ou Mot de passe Invalide", parent=self.mac)
                else:
                    enseignant_id, nom, prenom = row
                    messagebox.showinfo("Succès", f"Bienvenue {prenom} {nom}", parent=self.mac)
                    self.mac.withdraw()
                    DashboardProf_window = Toplevel(self.mac)
                    DashboardProf(DashboardProf_window, nom, prenom, enseignant_id) 
                connection.close()
                
            except Error as ex:
                messagebox.showerror("Attention", f"Problème de Connection: {str(ex)}", parent=self.mac)

    def mdpOublier(self):
        if self.entryEmail.get() == "":
            messagebox.showerror("Attention", "Entrez Un mail", parent=self.mac)
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="vacataire",
                    port=8889 
                )
                cur = connection.cursor()
                query = "SELECT * FROM enseignant WHERE Email=%s"
                cur.execute(query, (self.entryEmail.get(),))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Attention", "Email Inconnue", parent=self.mac)
                else:
                    connection.close()
                    self.mac2 = Toplevel()
                    self.mac2.title("Mdp Oublier")
                    self.mac2.geometry("400x400+600+200")
                    self.mac2.resizable(0, 0)
                    self.mac2.focus_force()
                    self.mac2.grab_set()
                    
                    title = ct.CTkLabel(self.mac2, text="Mot de passe Oublier", font=("times new roman", 15, "bold"))
                    title.place(x=100, y=20)

                    aff_question = ct.CTkLabel(self.mac2, text="Sélectionnez une Question", font=("times new roman", 15, "bold"))
                    aff_question.place(x=70, y=50)
                    self.ecri_question = ct.CTkOptionMenu(self.mac2, font=("times new roman", 15), state="readonly", width=250,
                                                          values=["Ton surnom", "Lieu de naissance", "Meilleur ami", "Film préféré"])
                    self.ecri_question.place(x=70, y=100)
                    
                    aff_rps_lbl = ct.CTkLabel(self.mac2, text="Répondez", font=("times new roman", 15, "bold"))
                    aff_rps_lbl.place(x=70, y=150)
                    self.aff_rpsEntry = ct.CTkEntry(self.mac2, placeholder_text="Écrivez la réponse",
                                                    font=("times new roman", 15, "italic"), width=250)
                    self.aff_rpsEntry.place(x=70, y=200)
                    
                    aff_NewMdp_lbl = ct.CTkLabel(self.mac2, text="Nouveau mot de Passe", 
                                                 font=("times new roman", 15, "bold"))
                    aff_NewMdp_lbl.place(x=70, y=250)
                    self.aff_NewMdpEntry = ct.CTkEntry(self.mac2, placeholder_text="Entrez le nouveau mot de passe",
                                                       font=("times new roman", 15, "italic"), width=250)
                    self.aff_NewMdpEntry.place(x=70, y=300)
                    
                    aff_NewMdp_confirm_lbl = ct.CTkLabel(self.mac2, text="Confirmez", 
                                                         font=("times new roman", 15, "bold"))
                    aff_NewMdp_confirm_lbl.place(x=70, y=350)
                    self.aff_New_Mdp_confirm_Entry = ct.CTkEntry(self.mac2, placeholder_text="Confirmez",
                                                                 font=("times new roman", 15, "italic"), width=250)
                    self.aff_New_Mdp_confirm_Entry.place(x=70, y=400)
                    
                    btnModifMdp = ct.CTkButton(self.mac2, text="Valider", font=("times new roman", 15, "bold"),
                                               command=self.ModifierMdp)
                    btnModifMdp.place(x=160, y=450)
                
            except Error as ex:
                messagebox.showerror("Attention", f"Erreur de Connection: {str(ex)}", parent=self.mac)        

    def ModifierMdp(self):
        pass

if __name__ == "__main__":
    Mac = ct.CTk()
    obj = LoginEnseignant(Mac)
    Mac.mainloop()
