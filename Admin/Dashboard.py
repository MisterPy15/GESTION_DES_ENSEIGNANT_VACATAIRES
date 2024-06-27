import customtkinter as ct
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GestionFiliere import Filiere
from GestionProf import Enseignants
from GestionRapport import Rapport
import mysql.connector
from GestionEmploiDuTemps import EmploiTemps





class Dashboard:
    def __init__(self, mac, nom, prenom):
        self.mac = mac
        self.mac.title("Dashboard")
        self.mac.geometry("1350x700+0+0")
        
        self.nom = nom
        self.prenom = prenom
        
        
        
        self.conn = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="root",  
                database="vacataire",
                port=8889
            )
        self.cursor = self.conn.cursor()

        
        
    
        self.frameInfo = ct.CTkFrame(self.mac, width=1350, height=110)
        self.frameInfo.place(x=10, y=10)

        logoUTA = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)

        label_logoUTA = Label(self.frameInfo, image=self.logo_UTA_login, borderwidth=0,
                              width=200, height=100)
        label_logoUTA.place(x=10, y=5)

        labeBievenue = ct.CTkLabel(self.frameInfo, text=f"Bon retour Parmi nous Admin: {self.prenom} {self.nom}", 
                                   font=("times new roman", 35, "bold"))
        labeBievenue.place(x=460, y=25)
        
        # labeBievenue = ct.CTkLabel(self.frameInfo, text=f"Bon retour Parmi nous Admin: Py", 
        #                            font=("times new roman", 35, "bold"))
        # labeBievenue.place(x=460, y=25)

        apparenceOption = ct.CTkOptionMenu(self.frameInfo, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.place(x=1200, y=35)
        
        # scaling_optionemenu = ct.CTkOptionMenu(self.frameInfo, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # scaling_optionemenu.place(x=980, y=35) 
 
 



        
        self.frameGestion = ct.CTkFrame(self.mac, width=350, height=650)
        self.frameGestion.place(x=10, y=120)

        labeldash = ct.CTkLabel(self.frameGestion, text="Dashboard", text_color="white", fg_color="green", corner_radius=10,
                                                    width=320,font=("times new roman", 35, "bold"))
        labeldash.place(x=15, y=20)
        
        
        
        
        
        
        btnProf = ct.CTkButton(self.frameGestion, text="Gestion Des Enseignants", fg_color="#2B2B2B", command=self.GestionEnseigant,
                                                        width=320, cursor="hand",font=("times new roman", 22, "bold"))
        btnProf.place(x=25, y=100)
        
        lbl_Logo_Prof = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/Prof.png")
        lbl_Logo_Prof = lbl_Logo_Prof.resize((30, 30))
        self.logo_Prof_lbl = ImageTk.PhotoImage(lbl_Logo_Prof)

        label_logoProf = Label(btnProf, image=self.logo_Prof_lbl, borderwidth=0,
                              width=30, height=30)
        label_logoProf.place(x=5, y=0)
        
        
        
        
        btnFiliere = ct.CTkButton(self.frameGestion, text="Gestion Des Filières", fg_color="#2B2B2B", command=self.GestionFiliere,
                                                        width=320, cursor="hand", font=("times new roman", 22, "bold"))
        btnFiliere.place(x=25, y=180)
        
        lbl_Logo_Fili = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/Fillière.png")
        lbl_Logo_Fili = lbl_Logo_Fili.resize((30, 30))
        self.logo_Fili_lbl = ImageTk.PhotoImage(lbl_Logo_Fili)

        label_logoFiliere = Label(btnFiliere, image=self.logo_Fili_lbl, borderwidth=0,
                              width=30, height=30)
        label_logoFiliere.place(x=5, y=0)
        
        
        
        
        
        
        btnEmploisDuTemps = ct.CTkButton(self.frameGestion, text="Emplois du temps", fg_color="#2B2B2B", command=self.EmploiDutemps,
                                                        width=320, cursor="hand", font=("times new roman", 22, "bold"))
        btnEmploisDuTemps.place(x=25, y=260)
        
        lbl_Logo_Emplois_tmp = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/empl tmps.png")
        lbl_Logo_Emplois_tmp = lbl_Logo_Emplois_tmp.resize((30, 30))
        self.logo_Emplois_tmp_lbl = ImageTk.PhotoImage(lbl_Logo_Emplois_tmp)

        label_logoEmplois_tmp = Label(btnEmploisDuTemps, image=self.logo_Emplois_tmp_lbl, borderwidth=0,
                              width=30, height=30)
        label_logoEmplois_tmp.place(x=5, y=0)
        
        
        
        
        btnRapport = ct.CTkButton(self.frameGestion, text="Gestion Des Rapports", fg_color="#2B2B2B", command=self.GestionRapports,
                                                        width=320, cursor="hand", font=("times new roman", 22, "bold"))
        btnRapport.place(x=25, y=340)
        
        lbl_Logo_Rapport = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/Rapport.png")
        lbl_Logo_Rapport = lbl_Logo_Rapport.resize((30, 30))
        self.logo_Rapport_lbl = ImageTk.PhotoImage(lbl_Logo_Rapport)

        label_logoRapport = Label(btnRapport, image=self.logo_Rapport_lbl, borderwidth=0,
                              width=30, height=30)
        label_logoRapport.place(x=5, y=0)
 
       
        
        
        
   
        btnParametre = ct.CTkButton(self.frameGestion, text="Paramètre", fg_color="#2B2B2B", 
                                                        width=320, cursor="hand", font=("times new roman", 22, "bold"))
        btnParametre.place(x=25, y=420)
        
        lbl_Logo_Parametre = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/Parametre.png")
        lbl_Logo_Parametre = lbl_Logo_Parametre.resize((30, 30))
        self.logo_Parametre_lbl = ImageTk.PhotoImage(lbl_Logo_Parametre)

        label_logoParametre = Label(btnParametre, image=self.logo_Parametre_lbl, borderwidth=0,
                              width=30, height=30)
        label_logoParametre.place(x=5, y=0)
   
   
    


          # create scrollable frame
        
        self.frameGeneral = ct.CTkFrame(self.mac, width=680, height=250)
        self.frameGeneral.place(x=470, y=200)
        
        self.scrollable_frame = ct.CTkScrollableFrame(self.frameGeneral, label_text=".", height=70, width=650)
        self.scrollable_frame.place(x=5 ,y=0)
        
        lblID = ct.CTkLabel(self.frameGeneral, text="ID", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblID.place(x=20, y=35)
        
        
        lblNom = ct.CTkLabel(self.frameGeneral, text="Nom", fg_color="green",text_color="white",corner_radius=10, font=("times new roman", 18, "bold"))
        lblNom.place(x=480, y=35) 
        
       
        
        lblEnseignant = ct.CTkLabel(self.frameGeneral, text="Enseignants", font=("times new roman", 20, "bold"))
        lblEnseignant.place(x=18, y=3)
        
        entryRecherche = ct.CTkEntry(self.frameGeneral, placeholder_text="Recherche", width=200)
        entryRecherche.place(x=200, y=2)
        
        buttonRecherche = ct.CTkButton(self.frameGeneral, text="🔍", corner_radius=30, width=5, fg_color="green",)
        buttonRecherche.place(x=420, y=5)
        
        # self.scrollable_frame_buttonDelete = []  
        self.scrollable_frame_labelId = [] 
        self.scrollable_frame_labelProf = [] 
        
    
        for i in range(5):
            labelId = ct.CTkLabel(self.scrollable_frame, text=f"Id {i+1}")
            labelId.grid(row=i, column=0, padx=10, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelId.append(labelId)
            
            labelProf = ct.CTkLabel(self.scrollable_frame, text=f"NomProf {i+1}")
            labelProf.grid(row=i, column=1, padx=420, pady=10)  # Utilisation de grid() au lieu de place()
            self.scrollable_frame_labelProf.append(labelProf)
            
            
            
            # buttonDelete = ct.CTkButton(self.scrollable_frame, text="Supprimer", fg_color="red")
            # buttonDelete.grid(row=i, column=4, pady=10)  # Utilisation de grid() au lieu de place()
            # self.scrollable_frame_buttonDelete.append(buttonDelete)




    

        
        self.frameNbrProf = ct.CTkFrame(self.mac, width=250, height=70)
        self.frameNbrProf.place(x=570, y=125)
        
        
        IconProf = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/teacher.png")
        IconProf = IconProf.resize((80, 80))
        
        self.Icon_ProfIcon = ImageTk.PhotoImage(IconProf)

        label_IconProf = Label(self.frameNbrProf, image=self.Icon_ProfIcon, borderwidth=0,
                                                    width=80, height=80)
        label_IconProf.place(x=160, y=5)
        
        
        labelPro = ct.CTkLabel(self.frameNbrProf, text="Enseigant", font=("times new roman", 20, "bold"))
        labelPro.place(x=10, y=10)
        
        labelNbrPro = ct.CTkLabel(self.frameNbrProf, text="", font=("times new roman", 25, "bold"))
        labelNbrPro.place(x=10, y=30)
        
        nbr_enseignants = self.get_nbr_enseignants()
        labelNbrPro.configure(text=str(nbr_enseignants))
        
        
        
        
        
        
        self.frameNbrFili = ct.CTkFrame(self.mac, width=250, height=70)
        self.frameNbrFili.place(x=970, y=125)
        
        IconFili = Image.open(r"C:\Users\HP\Desktop\AlsonPersonalFiles\py\GESTION_DES_ENSEIGNANT_VACATAIRES\Img\empl tmps.pngImg/graduation-hat.png")
        IconFili = IconFili.resize((80, 80))
        self.Icon_FiliIcon = ImageTk.PhotoImage(IconFili)
        
        label_IconFili = Label(self.frameNbrFili, image=self.Icon_FiliIcon, borderwidth=0,
                                                    width=80, height=80)
        label_IconFili.place(x=160, y=5)
        
        
        labelFiliere = ct.CTkLabel(self.frameNbrFili, text="Filière", font=("times new roman", 20, "bold"))
        labelFiliere.place(x=10, y=10)
        
        labelNbrFiliere = ct.CTkLabel(self.frameNbrFili, text=f"0", font=("times new roman", 25, "bold"))
        labelNbrFiliere.place(x=10, y=30)
        nbr_filiere = self.get_nbr_filieres()
        
        labelNbrFiliere.configure(text=str(nbr_filiere))
        
        


        # ================Statistique=========
        # Frame pour le graphique
        self.frame_chart = ct.CTkFrame(self.mac, width=980, height=300)
        self.frame_chart.place(x=370, y=460)  # Utilisation de .place au lieu de .pack

        # Données pour le graphique
        Prof = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
        filieres = [55, 65, 75, 85, 95, 80, 115, 125, 135, 145]



        # Création du graphique avec matplotlib
        fig = Figure(figsize=(9.8, 3), dpi=100)
        ax = fig.add_subplot(111)
        
        ax.bar(range(len(Prof)), Prof, width=0.4, label='Enseignants', align='center')
        ax.bar([x + 0.4 for x in range(len(filieres))], filieres, width=0.4, label='Filieres', align='edge')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.set_title('Statistique')
        ax.legend()

        # Intégration du graphique dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame_chart)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    
    
    def get_nbr_enseignants(self):
        self.cursor.execute("SELECT COUNT(*) FROM enseignant")
        result = self.cursor.fetchone()
        return result[0] if result else 0
    
    def get_nbr_filieres(self):
        self.cursor.execute("SELECT COUNT(*) FROM filière")
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    
    
    def GestionFiliere(self):
        self.Fenetre_Filiere = Toplevel(self.mac)
        self.app = Filiere(self.Fenetre_Filiere)


    def GestionEnseigant(self):
        self.Fenetre_Enseigant = Toplevel(self.mac)
        self.app = Enseignants(self.Fenetre_Enseigant)
    
    
    
    def GestionRapports(self):
        self.Fenetre_Rapport = Toplevel(self.mac)
        self.app = Rapport(self.Fenetre_Rapport)
    
    
    
    def EmploiDutemps(self):
        self.Fenetre_EmploiTemps = Toplevel(self.mac)
        self.app = EmploiTemps(self.Fenetre_EmploiTemps)
    




    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Dashboard(Mac)
    Mac.mainloop()
