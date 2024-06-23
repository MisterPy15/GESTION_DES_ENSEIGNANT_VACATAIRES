import customtkinter as ct
from tkinter import *
from tkinter import ttk, messagebox
import PIL



class mdpOublier:
    def __init__(self, mac):
        # self.mac = Toplevel()
        self.mac.title("Rénitialiser")
        self.mac.geometry("400x400+600+200")
        self.mac.resizable(0,0)
        self.mac.focus_force()
        self.mac.grab_set()
        
    
    

if __name__ == "__main__":
    Mac = ct.CTk()
    Obj = mdpOublier(Mac)
    Mac.mainloop()