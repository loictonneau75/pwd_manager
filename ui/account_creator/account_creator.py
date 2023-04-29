import tkinter as tk
from tkinter import ttk

from ui.account_creator.engine import *


class AccountCreator(ttk.Labelframe):

    def __init__(self, master: ttk.Frame):
        super().__init__(master, text = "Création de compte")
        self.create_widget()
        # self.erase_error()
        # self.config_entry()
        self.company.error_no_company.grid_forget()
        self.company.value.trace("w", self.company.check_company_entry_lenght())
        self.pack()

    def create_widget(self):
        self.company = Company(self,0)
        self.email = Email(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.pseudo = Pseudo(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.password = Password(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.create_valid_button()

    def create_valid_button(self):
        """
        Creates the 'Creer un compte' button and assigns its command.
        """
        self.valid_button = ttk.Button(self, text="Valider")
        self.valid_button.configure(command = lambda : print("ok"))
        self.valid_button.grid(row = 13, column = 1, sticky = "e")


class Company():

    def __init__(self, master, start_row):
        self.start_row = start_row
        self.create_widget(master)

    def  create_widget(self, master):
        self.value = tk.StringVar()
        self.label = create_label(master, "Nom de la compagnie :", (self.start_row, 0))
        self.entry = create_entry(master, self.value, (self.start_row, 1))
        self.error_no_company = create_error(master, "Veuillez mettre le nom de la compagnie pour laquelle vous enregistrez un compte", (self.start_row + 1, 0))

    def check_company_entry_lenght(self):
        def _check_company(*args):
            value = self.value.get()
            if self.value.get() == "":
                self.error_no_company.grid(row = self.start_row + 1, column = 0, columnspan = 2)
            else:
                self.error_no_company.grid_forget()
        return _check_company


class Email():

    def __init__(self, master, start_row):
        self.start_row = start_row
        self.create_widget(master)

    def  create_widget(self,master):
        self.value = tk.StringVar()
        self.label = create_label(master, "Email :", (self.start_row, 0))
        self.entry = create_entry(master, self.value, (self.start_row, 1))
        self.error_no_email = create_error(master, "Veuillez mettre l'adresse utilisé pour créer un compte", (self.start_row + 1, 0))
        self.error_incorect_email = create_error(master, "Email incorrecte", (self.start_row + 2, 0) )


class Pseudo():

    def __init__(self, master, start_row):
        self.start_row = start_row
        self.create_widget(master)

    def  create_widget(self, master):
        self.is_necessary = tk.BooleanVar()
        self.is_necessary_checkbox = create_checkbox(master, self.is_necessary, "Avez vous besoin d'un pseudo", 
                                                     lambda: print(self.is_necessary.get()), (self.start_row, 0))
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(master, self.is_already_possessed, "Avez vous deja un pseudo",
                                                             lambda: print(self.is_already_possessed.get()), (self.start_row, 1))
        self.value = tk.StringVar()
        self.label = create_label(master, "Pseudo :", (self.start_row + 1, 0))
        self.entry = create_entry(master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(master,"Veuillez renseigné un pseudo",(self.start_row + 2, 0))


class Password():

    def __init__(self, master, start_row):
        self.start_row = start_row
        self.create_widget(master)

    def  create_widget(self, master):
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(master, self.is_already_possessed, "Avez vous deja un mot de passe",
                                                             lambda: print(self.is_already_possessed.get()), (self.start_row, 0))
        self.value = tk.StringVar()
        self.label = create_label(master, "Mot de passe :", (self.start_row + 1, 0))
        self.entry = create_entry(master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(master,"Veuillez renseigné un mot de passe",(self.start_row + 2, 0))
        self.label = create_label(master, "Répéter le mot de passe :", (self.start_row + 3, 0))
        self.entry = create_entry(master, self.value, (self.start_row + 3, 1))
        self.error_no_pseudo = create_error(master,"Les mots de passe doivent corespondre",(self.start_row + 4, 0))