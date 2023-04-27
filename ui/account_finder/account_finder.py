import tkinter as tk
from tkinter import ttk

class AccountFinder(ttk.Labelframe):

    def __init__(self,master):
        super().__init__(master, text = "Affichage de compte")
        self.label = ttk.Label(self,text = "bonjour")
        self.label.pack()
        self.pack()