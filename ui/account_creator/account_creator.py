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
        ttk.Label(self,background = "red").pack(expand = True, fill = "both")

        #self.create_widget()
        self.pack(fill = "x", expand = True)

    def  create_widget(self):
        ttk.Label(self,background = "red").grid(row = 0, column = 0, sticky = "nswe")
        ttk.Label(self,background = "pink").grid(row = 0, column = 1, sticky = "nswe")
        # self.create_label()
        # self.create_entry()
        # self.create_error()
        
    def create_label(self):
        self.label = ttk.Label(self, text = "Nom de la compagnie")
        self.label.grid(row = 0, column = 0)

    def create_entry(self):
        self.entry = ttk.Entry(self)
        self.entry.grid(row = 0, column = 1)

    def create_error(self):
        self.error_no_label = ttk.Label(self, text = "Veuillez mettre le nom de la compagnie \n pour laquelle vous enregistrez un compte", foreground = "red", background="blue")
        self.error_no_label.grid(row = 1, column = 0, columnspan = 2)


class Email(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self,background = "pink").pack(expand = True, fill = "both")
        self.pack(fill="x")


class Pseudo(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill = "x")



class Password(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)