import customtkinter as ct
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

class Filiere:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion des Filières")
        self.mac.geometry("850x700+50+0")
        self.mac.resizable(0, 0)
        self.mac.focus_force()
        self.mac.grab_set()

        self.db_connection = self.connect_to_db()
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




    def ajouter_filiere(self, nom_filiere):
        if nom_filiere == "":
            messagebox.showerror("Attention", "Remplissez tous les champs", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                query = "INSERT INTO filière (Nom_Filière) VALUES (%s)"
                cursor.execute(query, (nom_filiere,))
                self.db_connection.commit()
                messagebox.showinfo("Succès", "Ajout Réussi.", parent=self.mac)
                self.update_table()
                self.ViderChamp()
            except Exception as es:
                messagebox.showerror("Attention", f"Problème de Connexion {str(es)}", parent=self.mac)




    def ViderChamp(self):
        try:
            self.entryNomFil.delete(0, END)
        except AttributeError as e:
            messagebox.showerror("Erreur", f"Un champ d'entrée est introuvable: {str(e)}", parent=self.mac)



    def modifier_filiere(self, id, nom_filiere):
        if nom_filiere == "":
            messagebox.showerror("Attention", "Choisissez une Filière à Modifier", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute(
                    "UPDATE filière SET Nom_Filière = %s WHERE Id_Filière = %s",
                    (nom_filiere, id)
                )
                self.db_connection.commit()
                messagebox.showinfo("Succès", "Modification réussie.", parent=self.mac)
                self.ViderChamp()
                self.update_table()
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Lors de la Modification {str(es)}", parent=self.mac)



    def supprimer_filiere(self, id):
        if self.entryNomFil.get() == "":
            messagebox.showerror("Attention", "Veuillez Entrez Une Filière", parent=self.mac)
        
        else:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM filière WHERE Id_Filière = %s", (id,))
                self.db_connection.commit()
                self.update_table()  # Update the table after deleting a filiere
                self.ViderChamp()
                messagebox.showinfo("Succès", "Suppression réussie.")
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Lors de la Suppression {str(es)}", parent=self.mac)



    def rechercher_filiere(self, recherche):
        if recherche == "":
            messagebox.showerror("Attention", "Entrez un Id ou un Nom", parent=self.mac)
        else:
            try:
                cursor = self.db_connection.cursor()
                query = "SELECT * FROM filière WHERE Id_Filière = %s OR Nom_Filière LIKE %s"
                cursor.execute(query, (recherche, f"%{recherche}%"))
                result = cursor.fetchall()
                self.afficher_filieres(result)  # Affiche les résultats de la recherche
                if result:
                    self.remplir_champs(result[0])
            except Exception as es:
                messagebox.showerror("Attention", f"Erreur Due à {str(es)}", parent=self.mac)



    def update_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM filière")
        filieres = cursor.fetchall()
        self.afficher_filieres(filieres)  # Display all filieres



    def afficher_filieres(self, filieres):
        # Clear the current table
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for i, filiere in enumerate(filieres):
            labelId = ct.CTkLabel(self.scrollable_frame, text=str(filiere[0]))
            labelId.grid(row=i, column=0, padx=10, pady=10)
            labelNomFil = ct.CTkLabel(self.scrollable_frame, text=filiere[1])
            labelNomFil.grid(row=i, column=1, padx=190, pady=10)



    def Formulaire(self):
        self.frame1 = ct.CTkFrame(self.mac, width=400, height=200, corner_radius=15)
        self.frame1.place(x=10, y=200)

        labelTitre = ct.CTkLabel(self.frame1, text="Gestion Des Filières", font=("times new roman", 25, "bold"))
        labelTitre.place(x=10, y=10)

        labelNomFil = ct.CTkLabel(self.frame1, text="Filière", font=("times new roman", 18, "bold"))
        labelNomFil.place(x=10, y=60)

        self.entryNomFil = ct.CTkEntry(self.frame1, placeholder_text="Nom de la filière",
                                       width=300, font=("times new roman", 15, "bold"))
        self.entryNomFil.place(x=80, y=60)

        buttonAjout = ct.CTkButton(self.frame1, text="Ajouter", width=100, fg_color="green",
                                   corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                   command=self.ajouter_filiere_callback)
        buttonAjout.place(x=20, y=150)

        buttonModifier = ct.CTkButton(self.frame1, text="Modifier", width=100, fg_color="#305B43",
                                      corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                      command=self.modifier_filiere_callback)
        buttonModifier.place(x=140, y=150)

        buttonSupprimer = ct.CTkButton(self.frame1, text="Supprimer", width=100, fg_color="red",
                                       corner_radius=8, cursor="hand", font=("times new roman", 20, "bold"),
                                       command=self.supprimer_filiere_callback)
        buttonSupprimer.place(x=260, y=150)



    def ajouter_filiere_callback(self):
        nom_filiere = self.entryNomFil.get()
        self.ajouter_filiere(nom_filiere)



    def get_selected_filiere_id(self):
        return getattr(self, 'selected_filiere_id', None)



    def modifier_filiere_callback(self):
        id = self.get_selected_filiere_id()
        if id:
            nom_filiere = self.entryNomFil.get()
            self.modifier_filiere(id, nom_filiere)
        else:
            messagebox.showerror("Attention", "Sélectionnez une filière à modifier", parent=self.mac)



    def supprimer_filiere_callback(self):
        id = self.get_selected_filiere_id()
        if id:
            self.supprimer_filiere(id)
        else:
            messagebox.showerror("Attention", "Sélectionnez une filière à supprimer", parent=self.mac)



    def rechercher_filiere_callback(self):
        if self.entryRecherche.get() == "":
            messagebox.showerror("Attention", "Entrez un Id ou un Nom", parent=self.mac)
        else:
            recherche = self.entryRecherche.get()
            self.rechercher_filiere(recherche)



    def remplir_champs(self, filiere):
        self.selected_filiere_id = filiere[0]
        self.entryNomFil.delete(0, END)
        self.entryNomFil.insert(0, filiere[1])



    def tableDetails(self):
        self.frameGeneral = ct.CTkFrame(self.mac, width=380, height=450)
        self.frameGeneral.place(x=420, y=200)

        self.scrollable_frame = ct.CTkScrollableFrame(self.frameGeneral, label_text="-", height=150, width=320)
        self.scrollable_frame.place(x=20, y=80)
        
        lblFiliere = ct.CTkLabel(self.frameGeneral, text="Filiere", font=("times new roman", 20, "bold"))
        lblFiliere.place(x=18, y=10)
        
        self.entryRecherche = ct.CTkEntry(self.frameGeneral, placeholder_text="Recherche", width=200)
        self.entryRecherche.place(x=100, y=10)
        
        
        
        buttonRecherche = ct.CTkButton(self.frameGeneral, text="🔍", corner_radius=30, width=5, command=self.rechercher_filiere_callback,
                                       cursor="hand", fg_color="green",)
        buttonRecherche.place(x=315, y=10)
        
        
          
        lblID = ct.CTkLabel(self.frameGeneral, text="ID", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblID.place(x=20, y=85)
        
        
        lblNomFil = ct.CTkLabel(self.frameGeneral, text="Filière", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblNomFil.place(x=235, y=85) 
        



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
    obj = Filiere(Mac)
    Mac.mainloop()

