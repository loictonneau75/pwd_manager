import tkinter as tk
from tkinter import ttk

class AccountCreator(ttk.Labelframe):

    def __init__(self,master):
        super().__init__(master, text = "Création de compte")
        self.label = ttk.Label(self,text = "bonjour")
        self.label.pack()
        self.pack()