import tkinter as tk
from tkinter import ttk

from ui.account_creator.engine import *

class AccountCreator(ttk.Labelframe):

    def __init__(self, master:tk.Tk):
        super().__init__(master, text = "Création de compte")
        self.company = Company(self,len(self.children))
        self.email = Email(self,len(self.children))
        self.pseudo = Pseudo(self,len(self.children))
        # self.password = Password(self,len(self.children))
        self.pack()


class Company():

    def __init__(self, master, start_row):
        self.create_widget(master,start_row)

    def  create_widget(self,master,start_row):
        self.value_var = tk.StringVar()
        self.label = create_label(master,"Nom de la compagnie :",(start_row,0))
        self.entry = create_entry(master,(start_row,1), self.value_var)
        self.error_no_company = create_error(master, "Veuillez mettre le nom de la compagnie pour laquelle vous enregistrez un compte",(start_row+1,0))
    

class Email():

    def __init__(self, master, start_row):
        self.create_widget(master, start_row)

    def  create_widget(self,master,start_row):
        self.value_var = tk.StringVar()
        self.label = create_label(master,"Email :",(start_row,0))
        self.entry = create_entry(master,(start_row,1), self.value_var)
        self.error_no_email = create_error(master, "Veuillez mettre l'adresse utilisé pour créer un compte",(start_row+1,0))
        self.error_incorect_email = create_error(master, "Email incorrecte",(start_row+2,0) )


class Pseudo():

    def __init__(self, master, start_row):
        self.create_widget(master,start_row)

    def  create_widget(self,master,start_row):
        self.is_necessary_var = tk.BooleanVar()
        self.is_necessary_checkbox = create_checkbox(master,self.is_necessary_var,"Avez vous besoin d'un pseudo",lambda: print(self.is_necessary_var.get()),(start_row,0))

    def get_value(self):
        if self.is_necessary_var.get():
            pass


class Password():

    def __init__(self, master, start_row):
        self.create_widget(master,start_row)

    def  create_widget(self,master,start_row):
        pass