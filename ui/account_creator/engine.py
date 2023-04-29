import tkinter as tk
from tkinter import ttk
import tldextract as tld

def create_error(master : ttk.Labelframe, text : str, list : list, position : tuple):
    """
    Creates a label with the given error message and adds it to the given master widget at the specified position.

    Args:
        master: A ttk.Labelframe widget to which the error label will be added.
        text: A string containing the error message to be displayed on the label.
        position: A tuple representing the row and column position of the label in the grid.
        list: list of all the error_widgets

    Returns:
        The ttk.Label widget that was created.
    """
    error_label = ttk.Label(master, text = text, foreground = "red")
    list.append(error_label)
    error_label.grid(row = position[0], column = position[1], columnspan = 2, sticky = "ew")
    return error_label

def create_label(master : ttk.Labelframe, text : str, position : tuple):
    """
    Creates a label with the given text and adds it to the given master widget at the specified position.

    Args:
        master: A ttk.Labelframe widget to which the label will be added.
        text: A string containing the text to be displayed on the label.
        position: A tuple representing the row and column position of the label in the grid.

    Returns:
        The ttk.Label widget that was created.
    """
    label = ttk.Label(master, text = text)
    label.grid(row = position[0], column = position[1], sticky = "ew")
    return label

def create_entry(master : ttk.Labelframe, variable : tk.StringVar, position : tuple):
    """
    Creates an entry widget with the given StringVar and adds it to the given master widget at the specified position.

    Args:
        master: A ttk.Labelframe widget to which the entry will be added.
        position: A tuple representing the row and column position of the entry in the grid.
        variable: A tk.StringVar object to which the entry will be linked.

    Returns:
        The ttk.Entry widget that was created.
    """
    entry = ttk.Entry(master, textvariable = variable)
    entry.grid(row = position[0], column = position[1], sticky = "ew")
    return entry

def create_checkbox(master : ttk.Labelframe, variable : tk.BooleanVar, text : str, command, position : tuple):
    """
    Creates an entry widget with the given StringVar and adds it to the given master widget at the specified position.

    Args:
        master: A ttk.Labelframe widget to which the entry will be added.
        position: A tuple representing the row and column position of the entry in the grid.
        variable: A tk.StringVar object to which the entry will be linked.

    Returns:
        The ttk.Entry widget that was created.
    """
    check_box = ttk.Checkbutton(master, text = text, command = command, variable = variable)
    check_box.grid(row = position[0], column = position[1], sticky = "ew")
    return check_box

def clean_company_name(var:tk.StringVar):
    value = var.get()
    value = tld.extract(value).domain
    return value

def clean_email(var:tk.StringVar):
    value = var.get()
    hebergeur = tld.extract(value).domain
    suffixe = tld.extract(value).suffix
    if hebergeur != "" and suffixe != "":
        value = value.replace(f"@{hebergeur}.{suffixe}","")
        return value