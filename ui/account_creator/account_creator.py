import tkinter as tk
from tkinter import ttk
from ui.account_creator.engine import *


class AccountCreator(ttk.Labelframe):

    def __init__(self, master: tk.Tk):
        super().__init__(master, text = "Création de compte")
        self.widgets_to_hide = []
        self.create_widget()
        self.hide_widgets()
        self.config_entries()
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
        self.valid_button["state"] = "disable"
        self.valid_button.grid(row = 13, column = 1, sticky = "e")

    def hide_widgets(self):
        for widget in self.widgets_to_hide:
            widget.grid_forget()

    def config_entries(self):
        self.company.value.trace("w", self.company.check_company_input())
        self.company.entry.bind("<FocusOut>", self.company.check_company_input())
        self.email.value.trace("w", self.email.check_email_input())


class Company():

    def __init__(self, master : AccountCreator, start_row):
        self.master = master
        self.start_row = start_row
        self.create_widget()
        self.entry.focus()

    def  create_widget(self):
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Nom de la compagnie :", (self.start_row, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row, 1))
        self.error_no_company = create_error(self.master, "Veuillez mettre le nom de la compagnie pour laquelle vous enregistrez un compte", (self.start_row + 1, 0))
        self.master.widgets_to_hide.extend([self.error_no_company])

    def check_company_input(self):
        def _check_company_input(*args):
            value = clean_company_name(self.value)
            if value == "":
                self.error_no_company.grid(row = self.start_row + 1, column = 0, columnspan = 2)
            else:
                self.error_no_company.grid_forget()
        return _check_company_input


class Email():

    def __init__(self, master : AccountCreator, start_row):
        self.master = master
        self.start_row = start_row
        self.create_widget()

    def  create_widget(self):
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Email :", (self.start_row, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row, 1))
        self.error_no_email = create_error(self.master, "Veuillez mettre l'adresse utilisé pour créer un compte", (self.start_row + 1, 0))
        self.error_incorect_email = create_error(self.master, "Email incorrecte", (self.start_row + 2, 0))
        self.master.widgets_to_hide.extend([self.error_no_email,self.error_incorect_email])


    def check_email_input(self):
        def _check_email_input(*args):
            clean_email(self.value)
        return _check_email_input


class Pseudo():

    def __init__(self, master : AccountCreator, start_row):
        self.master = master
        self.start_row = start_row
        self.create_widget()

    def  create_widget(self):
        self.is_necessary = tk.BooleanVar()
        self.is_necessary_checkbox = create_checkbox(self.master, self.is_necessary, "Avez vous besoin d'un pseudo", 
                                                     lambda: print(self.is_necessary.get()), (self.start_row, 0))
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(self.master, self.is_already_possessed, "Avez vous deja un pseudo",
                                                             lambda: print(self.is_already_possessed.get()), (self.start_row, 1))
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Pseudo :", (self.start_row + 1, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(self.master,"Veuillez renseigné un pseudo",(self.start_row + 2, 0))
        self.master.widgets_to_hide.extend([self.is_already_possessed_checkbox,self.label,self.entry,self.error_no_pseudo])


class Password():

    def __init__(self, master : AccountCreator, start_row):
        self.master = master
        self.start_row = start_row
        self.create_widget()

    def  create_widget(self):
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(self.master, self.is_already_possessed, "Avez vous deja un mot de passe",
                                                             lambda: print(self.is_already_possessed.get()), (self.start_row, 0))
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Mot de passe :", (self.start_row + 1, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(self.master,"Veuillez renseigné un mot de passe", (self.start_row + 2, 0))
        self.label_match = create_label(self.master, "Répéter le mot de passe :", (self.start_row + 3, 0))
        self.entry_match = create_entry(self.master, self.value, (self.start_row + 3, 1))
        self.error_pseudo_match = create_error(self.master,"Les mots de passe doivent corespondre",(self.start_row + 4, 0))
        self.master.widgets_to_hide.extend([self.label,self.entry,self.error_no_pseudo,self.label_match,self.entry_match,self.error_pseudo_match])