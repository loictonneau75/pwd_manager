import tkinter as tk
from tkinter import ttk

class AccountCreator(ttk.Labelframe):

    def __init__(self, master:tk.Tk):
        super().__init__(master, text = "Création de compte")
        self.company = Company(self)
        self.email = Email(self)
        # self.pseudo = Pseudo(self)
        # self.password = Password(self)

        self.pack() 


class Company(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widget()
        self.pack(fill = "x", expand = True)

    def  create_widget(self):
        self.create_label("Nom de la compagnie")
        self.create_entry()
        self.create_error("Veuillez mettre le nom de la compagnie pour laquelle vous enregistrez un compte",1)
        
    def create_label(self,text):
        self.label = ttk.Label(self, text = text)
        self.label.grid(row = 0, column = 0)

    def create_entry(self):
        self.entry = ttk.Entry(self)
        self.entry.grid(row = 0, column = 1, sticky = "ew")

    def create_error(self, text, row):
        self.error_label = ttk.Label(self, text = text, foreground = "red")
        self.error_label.grid(row = row, column = 0, columnspan = 2)


class Email(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="x")


class Pseudo(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill = "x")



class Password(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)