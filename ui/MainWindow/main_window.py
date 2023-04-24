from typing import *
import tkinter as tk
from tkinter import ttk
from constant import *

class Window(tk.Tk):
    """
    Module containing the Window class.

    The Window class represents the main window of the application. It inherits from the Tk class in the tkinter module
    and contains methods to configure the window, create an instance of the AppChoice class, create an exit button,
    and start the main event loop of the window.

    Attributes:
    CONFIG (dict): A dictionary containing configuration options for the Window class.

    Methods:
    configure_window(): Configures the title and resizable property of the window.
    create_app_choice(): Creates an instance of the AppChoice class.
    create_exit_button(): Creates an exit button and attaches a command to it.
    start_main_loop(): Starts the main event loop of the window.
    """
    CONFIG = {
        "title": REPO_NAME,
        "resizable": False,
    }

    def __init__(self):
        """
        Initializes a new instance of the Window class.

        Creates the main window of the application and configures it by calling the configure_window method. 
        Then, creates an instance of the AppChoice class and an exit button by calling the create_app_choice and 
        create_exit_button methods respectively. Finally, starts the main event loop of the window by calling the 
        start_main_loop method.
        """
        super().__init__()
        self.configure_window()
        self.create_app_choice()
        self.create_exit_button()
        self.start_main_loop()

    def configure_window(self):
        """
        Configures the title and resizable property of the window.

        Uses the configuration options from the CONFIG dictionary to set the title of the window to the name of the
        repository and to disable resizing of the window.
        """
        self.title(Window.CONFIG["title"])
        self.resizable(width=Window.CONFIG["resizable"], height=Window.CONFIG["resizable"])

    def create_app_choice(self):
        """
        Creates an instance of the AppChoice class.

        Initializes an instance of the AppChoice class and stores it in the app attribute of the Window object.
        """
        self.app = AppChoice(master = self)

    def create_exit_button(self):
        """
        Creates an exit button and attaches a command to it.

        Initializes an instance of the ttk.Button class and sets its text to "Quitter". Then, attaches the destroy 
        method of the Window object as the command of the button, which will close the main window of the application
        when the button is clicked. Finally, packs the button to the left side of the window and sets padding using
        the padx and pady arguments.
        """
        self.exit_button = ttk.Button(self, text="Quitter")
        self.exit_button.configure(command=self.destroy)
        self.exit_button.pack(side="left", padx=10, pady=(0, 10))

    def start_main_loop(self):
        """
        Starts the main event loop of the window.

        Calls the mainloop method of the Window object to start the main event loop of the window, which handles 
        user input and updates the graphical interface of the application.
        """
        self.mainloop()

class AppChoice(ttk.Labelframe):
    """
    A class representing the app choice label frame.

    Attributes:
        master (tk.Tk): The master window.
    
    Methods:
        create_widget() : Creates the widgets for the AppChoice object.
        create_new_button() : Creates the 'Creer un compte' button and assigns its command.
        create_get_button() : Creates the 'Afficher un compte' button and assigns its command.
        place_labelframe() : Places the AppChoice object in the master window.
        create_account() : Forgets the current frame and launches the AccountCreator object.
        get_account() : Forgets the current frame and launches the AccountFinder object.
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the AppChoice object.

        Args:
            master (tk.Tk): The master window.
        """
        super().__init__(master, text="Choix de l'application")
        self.create_widget()
        self.place_labelframe()

    def create_widget(self):
        """
        Creates the widgets for the AppChoice object.
        """
        self.create_new_button()
        self.create_get_button()

    def create_new_button(self):
        """
        Creates the 'Creer un compte' button and assigns its command.
        """
        self.create_button = ttk.Button(self, text="Creer un compte")
        self.create_button.configure(command = lambda : self.changer_label_frame(AccountCreator))
        self.create_button.pack(padx=20, pady=(20, 5))

    def create_get_button(self):
        """
        Creates the 'Afficher un compte' button and assigns its command.
        """
        self.get_button = ttk.Button(self, text="Afficher un compte")
        self.get_button.configure(command =  lambda : self.changer_label_frame(AccountFinder))
        self.get_button.pack(padx=20, pady=(0, 20))

    def place_labelframe(self):
        """
        Places the AppChoice object in the master window.
        """
        self.pack(padx=50, pady=10)
    
    def changer_label_frame(self, new_class):
        """
        Changes the label frame to a new class.

        Args:
            new_class: The new class to be used for the label frame.
        """
        self.destroy()
        nouvelle_classe = new_class(self.master)
        nouvelle_classe.pack()


class AccountCreator(ttk.Labelframe):

    def __init__(self,master):
        super().__init__(master, text = "Création de compte")
        self.label = ttk.Label(self,text = "bonjour")
        self.label.pack()
        self.pack()


class AccountFinder(ttk.Labelframe):

    def __init__(self,master):
        super().__init__(master, text = "Affichage de compte")
        self.label = ttk.Label(self,text = "bonjour")
        self.label.pack()
        self.pack()