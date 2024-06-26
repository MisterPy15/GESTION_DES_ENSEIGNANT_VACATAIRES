import customtkinter as ct
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error


class Enseignants:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion des Enseignants")
        self.mac.geometry("1000x700+200+0")
        self.mac.resizable(0, 0)
        self.mac.focus_force()
        self.mac.grab_set()

        self.db_connection = self.connect_to_db()  # Connect to the database
        self.Elements_Du_haut()
        self.Formulaire()
        self.tableDetails()
        self.update_table()
        

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',  
                database='vacataire',  
                user='root',  
                password='root', 
                port=8889 
            )
            if connection.is_connected():
                print("Connexion réussie à la base de données")
            return connection
        except Error as e:
            print("Erreur lors de la connexion à MySQL", e)
            return None
  
        
        
    def ajouter_enseignant(self, nom, prenom, email, mot_de_passe):
        if nom == "" or prenom == "" or email == "" or mot_de_passe == "" or self.entryConfirmPasswordEns.get() == "":
            messagebox.showerror("Attention", "Remplissez tous les champs", parent=self.mac)
        elif self.entryConfirmPasswordEns.get() != mot_de_passe:
            messagebox.showerror("Attention", "Les Mots de passe ne correspondent pas", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                query = "INSERT INTO enseignant (Nom, Prenom, Email, Mot_Passe) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (nom, prenom, email, mot_de_passe))
                self.db_connection.commit()
                messagebox.showinfo("Succès", "Ajout Réussi.", parent=self.mac)
                self.update_table()
                self.ViderChamp()
                
            except Exception as es:
                messagebox.showerror("Attention", f"Problème de Connexion {str(es)}", parent=self.mac)



    def ViderChamp(self):
        try:
            self.entryNomEns.delete(0, END)
            self.entryPrenomEns.delete(0, END)
            self.entryEmailEns.delete(0, END)
            self.entryPasswordEns.delete(0, END)
            self.entryConfirmPasswordEns.delete(0, END)
        except AttributeError as e:
            messagebox.showerror("Erreur", f"Un champ d'entrée est introuvable: {str(e)}", parent=self.mac)



    def modifier_enseignant(self, id, nom, prenom, email, mot_de_passe):
        if nom == "" or prenom == "" or email == "" or mot_de_passe == "":
            messagebox.showerror("Attention", "Choisissez un Enseignant à Modifier", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute(
                    "UPDATE enseignant SET Nom = %s, Prenom = %s, Email = %s, Mot_Passe = %s WHERE Id_Enseignant = %s",
                    (nom, prenom, email, mot_de_passe, id)
                )
                self.db_connection.commit()
                messagebox.showinfo("Succès", "Modification réussie.", parent=self.mac)
                self.ViderChamp()
                self.update_table()
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Lors de la Modification {str(es)}", parent=self.mac)




    def modifier_enseignant_callback(self):
        id = self.get_selected_enseignant_id()
        if id:
            nom = self.entryNomEns.get()
            prenom = self.entryPrenomEns.get()
            email = self.entryEmailEns.get()
            mot_de_passe = self.entryPasswordEns.get()
            self.modifier_enseignant(id, nom, prenom, email, mot_de_passe)
        else:
            messagebox.showerror("Attention", "Sélectionnez un enseignant à modifier", parent=self.mac)




    def supprimer_enseignant(self, id):
        
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM enseignant WHERE Id_Enseignant = %s", (id,))
                self.db_connection.commit()
                self.update_table()  # Update the table after deleting an enseignant
                self.ViderChamp()
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Lors de la Suppression {str(es)}", parent=self.mac)



    def supprimer_enseignant_callback(self):
        id = self.get_selected_enseignant_id()
        if id:
            self.supprimer_enseignant(id)
        else:
            messagebox.showerror("Attention", "Sélectionnez un enseignant à supprimer", parent=self.mac)



    def rechercher_enseignant(self, recherche):
        if recherche =="":
            messagebox.showerror("Attention", "Entrez Un Id ou Un Nom", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                query = "SELECT * FROM enseignant WHERE Id_Enseignant = %s OR Nom LIKE %s"
                cursor.execute(query, (recherche, f"%{recherche}%"))
                result = cursor.fetchall()
                self.afficher_enseignants(result)  # Affiche les résultats de la recherche
                if result:
                    self.remplir_champs(result[0])
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Du à {str(es)}", parent=self.mac)



    def rechercher_enseignant_callback(self):
        if self.entryRecherche.get() =="":
            messagebox.showerror("Attention", "Entrez Un Id ou Un Nom", parent=self.mac)
        else:
            recherche = self.entryRecherche.get()
            self.rechercher_enseignant(recherche)


    def remplir_champs(self, enseignant):
        self.selected_enseignant_id = enseignant[0]
        self.entryNomEns.delete(0, END)
        self.entryNomEns.insert(0, enseignant[1])
        self.entryPrenomEns.delete(0, END)
        self.entryPrenomEns.insert(0, enseignant[2])
        self.entryEmailEns.delete(0, END)
        self.entryEmailEns.insert(0, enseignant[3])
        self.entryPasswordEns.delete(0, END)
        self.entryPasswordEns.insert(0, enseignant[4])
        self.entryConfirmPasswordEns.delete(0, END)
        self.entryConfirmPasswordEns.insert(0, enseignant[4])



    def update_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM enseignant")
        enseignants = cursor.fetchall()
        self.afficher_enseignants(enseignants)  # Display all enseignants



    def afficher_enseignants(self, enseignants):
        # Clear the current table
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, enseignant in enumerate(enseignants):
            labelId = ct.CTkLabel(self.scrollable_frame, text=str(enseignant[0]))
            labelId.grid(row=i, column=0, padx=10, pady=10)
            labelNomEns = ct.CTkLabel(self.scrollable_frame, text=enseignant[1])
            labelNomEns.grid(row=i, column=1, padx=30, pady=10)
            labelPrenomEns = ct.CTkLabel(self.scrollable_frame, text=enseignant[2])
            labelPrenomEns.grid(row=i, column=2, padx=30, pady=10)
            labelEmailEns = ct.CTkLabel(self.scrollable_frame, text=enseignant[3])
            labelEmailEns.grid(row=i, column=3, padx=30, pady=10)
            labelPasswordEns = ct.CTkLabel(self.scrollable_frame, text="*")
            labelPasswordEns.grid(row=i, column=4, padx=30, pady=10)



    def Formulaire(self):
        self.frame1 = ct.CTkFrame(self.mac, width=400, height=400, corner_radius=15)
        self.frame1.place(x=10, y=200)

        labelTitre = ct.CTkLabel(self.frame1, text="Gestion Des Enseignants", font=("times new roman", 25, "bold"))
        labelTitre.place(x=10, y=10)

        labelNomEns = ct.CTkLabel(self.frame1, text="Nom", font=("times new roman", 18, "bold"))
        labelNomEns.place(x=10, y=60)

        self.entryNomEns = ct.CTkEntry(self.frame1, placeholder_text="Nom de l'Enseignant",
                                       width=300, font=("times new roman", 15, "bold"))
        self.entryNomEns.place(x=80, y=60)

        labelPrenomEns = ct.CTkLabel(self.frame1, text="Prénom", font=("times new roman", 18, "bold"))
        labelPrenomEns.place(x=10, y=110)

        self.entryPrenomEns = ct.CTkEntry(self.frame1, placeholder_text="Prénom",
                                          width=300, font=("times new roman", 15, "bold"))
        self.entryPrenomEns.place(x=80, y=110)

        labelEmailEns = ct.CTkLabel(self.frame1, text="Email", font=("times new roman", 18, "bold"))
        labelEmailEns.place(x=10, y=160)

        self.entryEmailEns = ct.CTkEntry(self.frame1, placeholder_text="Email",
                                         width=300, font=("times new roman", 15, "bold"))
        self.entryEmailEns.place(x=80, y=160)

        labelPasswordEns = ct.CTkLabel(self.frame1, text="Mot de Passe", font=("times new roman", 18, "bold"))
        labelPasswordEns.place(x=10, y=210)

        self.entryPasswordEns = ct.CTkEntry(self.frame1, placeholder_text="Mot de Passe", show="*",
                                            width=250, font=("times new roman", 15, "bold"))
        self.entryPasswordEns.place(x=125, y=210)

        labelConfirmPasswordEns = ct.CTkLabel(self.frame1, text="Confirmer", font=("times new roman", 18, "bold"))
        labelConfirmPasswordEns.place(x=10, y=260)

        self.entryConfirmPasswordEns = ct.CTkEntry(self.frame1, placeholder_text="Confirmer le Mot de passe", show="*",
                                                   width=280, font=("times new roman", 15, "bold"))
        self.entryConfirmPasswordEns.place(x=100, y=260)

        buttonAjout = ct.CTkButton(self.frame1, text="Ajouter", width=100, fg_color="green",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                   command=self.ajouter_enseignant_callback)
        buttonAjout.place(x=20, y=330)

        buttonModifier = ct.CTkButton(self.frame1, text="Modifier", width=100, fg_color="#305B43",
                                      corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                      command=self.modifier_enseignant_callback)
        buttonModifier.place(x=140, y=330)

        buttonSupprimer = ct.CTkButton(self.frame1, text="Supprimer", width=100, fg_color="red",
                                       corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                       command=self.supprimer_enseignant_callback)
        buttonSupprimer.place(x=260, y=330)



    def ajouter_enseignant_callback(self):
        nom = self.entryNomEns.get()
        prenom = self.entryPrenomEns.get()
        email = self.entryEmailEns.get()
        mot_de_passe = self.entryPasswordEns.get()
        self.ajouter_enseignant(nom, prenom, email, mot_de_passe)




    def get_selected_enseignant_id(self):
        return getattr(self, 'selected_enseignant_id', None)



    def tableDetails(self):
        self.frameGeneral = ct.CTkFrame(self.mac, width=570, height=400)
        self.frameGeneral.place(x=420, y=200)

        self.scrollable_frame = ct.CTkScrollableFrame(self.frameGeneral, label_text="-", height=150, width=520)
        self.scrollable_frame.place(x=17, y=80)

        lblEnseignant = ct.CTkLabel(self.frameGeneral, text="Enseignant", font=("times new roman", 25, "bold"))
        lblEnseignant.place(x=35, y=10)

        self.entryRecherche = ct.CTkEntry(self.frameGeneral, placeholder_text="Recherche", width=200)
        self.entryRecherche.place(x=180, y=10)

        buttonRecherche = ct.CTkButton(self.frameGeneral, text="🔍", corner_radius=30, width=5,
                                       cursor="hand", fg_color="green",
                                       command=self.rechercher_enseignant_callback)
        buttonRecherche.place(x=390, y=10)

        lblID = ct.CTkLabel(self.frameGeneral, text="ID", fg_color="green", text_color="white",
                            corner_radius=10, font=("times new roman", 18, "bold"))
        lblID.place(x=20, y=85)

        lblNomEns = ct.CTkLabel(self.frameGeneral, text="Nom", fg_color="green", text_color="white",
                                corner_radius=10, font=("times new roman", 18, "bold"))
        lblNomEns.place(x=90, y=85)

        lblPrenomEns = ct.CTkLabel(self.frameGeneral, text="Prénom", fg_color="green", text_color="white",
                                   corner_radius=10, font=("times new roman", 18, "bold"))
        lblPrenomEns.place(x=190, y=85)

        lblEmailEns = ct.CTkLabel(self.frameGeneral, text="Email", fg_color="green", text_color="white",
                                  corner_radius=10, font=("times new roman", 18, "bold"))
        lblEmailEns.place(x=370, y=85)

        lblPasswordEns = ct.CTkLabel(self.frameGeneral, text="MDP", fg_color="green", text_color="white",
                                     corner_radius=10, font=("times new roman", 12, "bold"))
        lblPasswordEns.place(x=500, y=85)




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
    obj = Enseignants(Mac)
    Mac.mainloop()
