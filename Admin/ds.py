import customtkinter as ct
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Dashboard:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Admin Dashboard")
        self.mac.geometry("1350x700+40+0")
        
        # Header Frame
        frameInfo = ct.CTkFrame(self.mac, width=1350, height=110)
        frameInfo.place(x=10, y=10)
        
        logoUTA = Image.open(r"/Users/misterpy/Desktop/cour_L2/Développement de Projet/Prof Vacataire/Img/logo.jpeg")
        logoUTA = logoUTA.resize((200, 100))
        self.logo_UTA_login = ImageTk.PhotoImage(logoUTA)
        
        label_logoUTA = tk.Label(frameInfo, image=self.logo_UTA_login, borderwidth=0, width=200, height=100)
        label_logoUTA.place(x=10, y=5)
        
        labelBienvenue = ct.CTkLabel(frameInfo, text="Bon retour Parmi nous Admin: ", 
                                     font=("times new roman", 35, "bold"))
        labelBienvenue.place(x=480, y=25)
        
        apparenceOption = ct.CTkOptionMenu(frameInfo, values=["Dark", "Light", "System"], corner_radius=20,
                                           command=self.change_appearance_mode_event, fg_color="green")
        apparenceOption.place(x=1200, y=35)
        
        # Menu Frame
        frameGestion = ct.CTkFrame(self.mac, width=350, height=650)
        frameGestion.place(x=10, y=120)
        
        labeldash = ct.CTkLabel(frameGestion, text="Dashboard", font=("times new roman", 35, "bold"))
        labeldash.place(x=25, y=20)
        
        # Adding Menu Buttons
        self.add_menu_buttons(frameGestion)
        
        # Main Frame
        self.main_frame = ct.CTkFrame(self.mac, width=950, height=650)
        self.main_frame.place(x=370, y=120)
        
        self.add_main_content(self.main_frame)
        

        slider = ct.CTkSlider(self.mac, from_=0, to=100, command=self.slider_event)
        slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def slider_event(value):
        print(value)
        
        
    def add_menu_buttons(self, frame):
        menu_items = [
            ("Dashboard", 70),
            ("Teachers", 120),
            ("Filiere", 170),
            ("Level", 220),
            ("Reports", 270),
            ("Time Table", 320),
            ("Settings", 370)
        ]
        
        for item, y_pos in menu_items:
            button = ct.CTkButton(frame, text=item, width=300, height=50, corner_radius=10, fg_color="green")
            button.place(x=25, y=y_pos)
        
    def add_main_content(self, frame):
        # Example label for Teachers
        labelTeachers = ct.CTkLabel(frame, text="Teachers", font=("times new roman", 25, "bold"))
        labelTeachers.place(x=25, y=20)
        
        # Table
        teachers = [
            ("PRE2209", "John Smith", 1185, "98%"),
            ("PRE1245", "Jolie Hoskins", 1195, "99.5%"),
            ("PRE1625", "Pennington Joy", 1196, "99.6%"),
            ("PRE2516", "Millie Marsden", 1187, "98.2%"),
            ("PRE2209", "John Smith", 1185, "98%")
        ]
        
        columns = ["ID", "Name", "Marks", "Percentage"]
        
        for col, text in enumerate(columns):
            label = ct.CTkLabel(frame, text=text, font=("times new roman", 20, "bold"))
            label.place(x=25 + col*200, y=70)
        
        for row, teacher in enumerate(teachers):
            for col, detail in enumerate(teacher):
                label = ct.CTkLabel(frame, text=str(detail), font=("times new roman", 18))
                label.place(x=25 + col*200, y=110 + row*40)
        
        # Adding a chart (using matplotlib)
        self.add_chart(frame)
        
    def add_chart(self, frame):
        # Dummy data for the chart
        teachers = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
        filieres = [55, 65, 75, 85, 95, 105, 115, 125, 135, 145]
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(range(10), teachers, width=0.4, label='Teachers', align='center')
        ax.bar(range(10), filieres, width=0.4, label='Filiere', align='edge')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Teachers & Filiere')
        ax.legend()
        
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=25, y=300)
        
        
        
    def change_appearance_mode_event(self, new_appearance_mode):
        ct.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Dashboard(Mac)
    Mac.mainloop()
