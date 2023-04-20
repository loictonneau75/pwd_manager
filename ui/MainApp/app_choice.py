from typing import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, app_name : str, size : Tuple[int,int]):
        super().__init__()
        self.title(app_name)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])

        self.mainloop()
