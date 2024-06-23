import customtkinter as ctk
import tkinter as tk
from tkinter import ttk



class GestionEmploiDuTempsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion d'Emplois Du Temps - UTA")
        self.root.geometry("800x700+200+0")
        self.mac.focus_force()
        self.mac.grab_set()

        self.switch_var = ctk.StringVar(value="Light")

        # Configuration de la fenêtre principale
        self.setup_main_frame()
        self.setup_entries()
        self.setup_buttons()
        self.setup_table()

    def change_theme(self):
        if self.switch_var.get() == "Light":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

    def setup_main_frame(self):
        title = ctk.CTkLabel(self.root, text="Gestion D'emploi Du Temps", font=("Arial", 24))
        title.pack(pady=20)

    def setup_entries(self):
        frame_entries = ctk.CTkFrame(self.root)
        frame_entries.pack(pady=10)

        label_enseignant = ctk.CTkLabel(frame_entries, text="Enseignant")
        label_enseignant.grid(row=0, column=0, padx=10, pady=10)
        entry_enseignant = ctk.CTkEntry(frame_entries, placeholder_text="Code de l'Enseignant")
        entry_enseignant.grid(row=0, column=1, padx=10, pady=10)

        label_filiere = ctk.CTkLabel(frame_entries, text="Filière")
        label_filiere.grid(row=0, column=2, padx=10, pady=10)
        entry_filiere = ctk.CTkEntry(frame_entries, placeholder_text="Code de la filière")
        entry_filiere.grid(row=0, column=3, padx=10, pady=10)

        label_cours = ctk.CTkLabel(frame_entries, text="Cours")
        label_cours.grid(row=1, column=0, padx=10, pady=10)
        entry_cours = ctk.CTkEntry(frame_entries, placeholder_text="Nom du cours")
        entry_cours.grid(row=1, column=1, padx=10, pady=10)

        label_niveau = ctk.CTkLabel(frame_entries, text="Niveau")
        label_niveau.grid(row=1, column=2, padx=10, pady=10)
        entry_niveau = ctk.CTkEntry(frame_entries, placeholder_text="Niveau")
        entry_niveau.grid(row=1, column=3, padx=10, pady=10)

    def setup_buttons(self):
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=10)

        btn_modifier = ctk.CTkButton(button_frame, text="Modifier", fg_color="orange")
        btn_modifier.grid(row=0, column=0, padx=10, pady=10)

        btn_ajouter = ctk.CTkButton(button_frame, text="Ajouter", fg_color="green")
        btn_ajouter.grid(row=0, column=1, padx=10, pady=10)

        btn_supprimer = ctk.CTkButton(button_frame, text="Supprimer", fg_color="red")
        btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        switch = ctk.CTkSwitch(self.root, text="Light/Dark Mode", command=self.change_theme, variable=self.switch_var, onvalue="Dark", offvalue="Light")
        switch.pack(pady=20)

    def setup_table(self):
        table_frame = ctk.CTkFrame(self.root, width=120)
        table_frame.pack(pady=20, fill='both', expand=True)

        # Create treeview with scrollbars
        columns = ["Heure", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=24)
        self.tree.pack(side='left', expand=True)
        
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        
        scrollbarx = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        scrollbarx.pack(side='bottom', fill='x')

        self.tree.configure(yscrollcommand=scrollbar.set)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')

        self.populate_table()

    def populate_table(self):
        # Example data, replace with your actual course schedule data
        schedule_data = [
            ("00:00 - 01:00", "", "", "", "", "", "", ""),
            ("01:00 - 02:00", "", "", "", "", "", "", ""),
            ("02:00 - 03:00", "", "", "", "", "", "", ""),
            ("03:00 - 04:00", "", "", "", "", "", "", ""),
            ("04:00 - 05:00", "", "", "", "", "", "", ""),
            ("05:00 - 06:00", "", "", "", "", "", "", ""),
            ("06:00 - 07:00", "", "", "", "", "", "", ""),
            ("07:00 - 08:00", "", "", "", "", "", "", ""),
            ("08:00 - 09:00", "", "", "", "", "", "", ""),
            ("09:00 - 10:00", "PYTHON\nIGL_L2\nDr Soro", "", "", "", "", "", ""),
            ("10:00 - 11:00", "", "AI\nRT_L2 & IGL_L2\nDr Johnson", "", "", "", "", ""),
            ("11:00 - 12:00", "", "", "", "", "", "", ""),
            ("12:00 - 13:00", "", "", "", "", "", "", ""),
            ("13:00 - 14:00", "", "UI\nIGL_L2\nDr Ali", "", "", "", "", ""),
            ("14:00 - 15:00", "", "", "", "", "", "", ""),
            ("15:00 - 16:00", "", "", "", "", "", "", ""),
            ("16:00 - 17:00", "", "", "", "", "", "", ""),
            ("17:00 - 18:00", "", "", "", "", "", "", ""),
            ("18:00 - 19:00", "", "", "", "", "", "", ""),
            ("19:00 - 20:00", "", "", "", "", "", "", ""),
            ("20:00 - 21:00", "", "", "", "", "", "", ""),
            ("21:00 - 22:00", "", "", "", "", "", "", ""),
            ("22:00 - 23:00", "", "", "", "", "", "", ""),
            ("23:00 - 00:00", "", "", "", "", "", "", "")
        ]

        for i, row in enumerate(schedule_data):
            tag = 'odd' if i % 2 == 0 else 'even'
            self.tree.insert('', tk.END, values=row, tags=(tag,))

        self.tree.tag_configure('odd', background='#808080')
        self.tree.tag_configure('even', background='green')

if __name__ == "__main__":
    root = ctk.CTk()
    app = GestionEmploiDuTempsApp(root)
    root.mainloop()
