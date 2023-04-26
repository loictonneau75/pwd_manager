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
    set_exit_button(): Configures the text and command of the exit button.
    create_exit_button(): Creates an exit button and attaches a command to it.
    change_app(): Changes the current application to a new one.
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
        self.app = AppChoice(master = self)
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

    def set_button(self, button : ttk.Button, text : str, command):
        """
        Configures the text and command of abutton.

        Configures the text of a button to the specified value and attaches the given command to it.

        Args:
        - button: A reference to the ttk.Button widget to configure.
        - text: The text to display on the button.
        - command: A reference to the function to call when the user clicks the button.
        """
        button["text"] = text
        button.configure(command = command)

    def create_exit_button(self):
        """
        Creates an exit button and attaches a command to it.

        Initializes an exit button using the ttk.Button widget and calls the set_exit_button method to configure the
        text and command of the button.
        """
        self.exit_button = ttk.Button(self)
        self.set_button(self.exit_button, "Quitter", self.destroy)
        self.exit_button.pack(side="left", padx=10, pady=(0, 10))

    def change_app(self, new_app, return_to, text_exit_button : str):
        """
        Changes the current application to a new one.

        Configures the exit button with the appropriate return function and destroys the current application before 
        creating a new one.

        Args:
        - new_app: A reference to the new application to create.
        - return_to: A reference to the function to call when the user clicks the exit button.
        - text_exit_button: The text of the button depending of the new app
        """
        self.set_button(self.exit_button, text_exit_button, lambda: return_to())
        self.app.destroy()
        self.app = new_app(self)

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
        switch_app() : Switches to a new application.
        return_to_appchoice() : Returns to the AppChoice screen.
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
        self.create_button.configure(command = lambda : self.switch_app(AccountCreator))
        self.create_button.pack(padx=20, pady=(20, 5))

    def create_get_button(self):
        """
        Creates the 'Afficher un compte' button and assigns its command.
        """
        self.get_button = ttk.Button(self, text="Afficher un compte")
        self.get_button.configure(command =  lambda : self.switch_app(AccountFinder))
        self.get_button.pack(padx=20, pady=(0, 20))

    def place_labelframe(self):
        """
        Places the AppChoice object in the master window.
        """
        self.pack(padx=50, pady=10)
    
    def switch_app(self, new_app):
        """
        Switches to a new application.

        Args:
            new_app: The new application to be displayed.
        """
        self.master.change_app(new_app, self.return_to_appchoice, "Retour")
        self.master.change_app(new_app, self.return_to_appchoice, "Retour")

    def return_to_appchoice(self):
        """
        Returns to the AppChoice screen.
        """
        self.master.change_app(AppChoice, self.master.destroy,"Quitter")


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