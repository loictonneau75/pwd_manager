from typing import *
import tkinter as tk
from tkinter import ttk
from constant import *
from ui.account_creator.account_creator import AccountCreator
from ui.account_finder.account_finder import AccountFinder

class Window(tk.Tk):
    """
    Module containing the Window class.

    The Window class represents the main window of the application. It inherits from the Tk class in the tkinter module
    and contains methods to configure the window, create an instance of the AppChoice class, create an exit button,
    and start the main event loop of the window.

    Methods:
    configure_window(): Configures the title and resizable property of the window.
    configure_frame(): Configures the layout of the window frame.
    set_exit_button(): Configures the text and command of the exit button.
    create_exit_button(): Creates an exit button and attaches a command to it.
    change_app(): Changes the current application to a new one.
    start_main_loop(): Starts the main event loop of the window.
    """

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
        self.configure_frame()
        self.change_app(AppChoice)
        self.create_exit_button()
        self.start_main_loop()

    def configure_window(self):
        """
        Configures the title and resizable property of the window.

        Uses the configuration options from the CONFIG dictionary to set the title of the window to the name of the
        repository and to disable resizing of the window.
        """
        self.title(REPO_NAME)
        self.resizable(width = RESIZABLE, height = RESIZABLE)

    def configure_frame(self):
        """
        Configures the layout of the window frame.

        Creates and packs the main label and back button frames in the window.
        """
        self.main_label = ttk.Frame(self)
        self.back_button_frame = ttk.Frame(self)
        self.main_label.pack(side = "top", fill = "both", expand = True, padx = 50, pady = 10)
        self.back_button_frame.pack(side = "bottom", fill = "x", padx = 10, pady = (0, 10))

    def set_button(self, button: ttk.Button, text: str, command):
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
        self.exit_button = ttk.Button(self.back_button_frame)
        self.set_button(self.exit_button, "Quitter", self.destroy)
        self.exit_button.pack(side = "left")

    def change_app(self, new_app, text_exit_button: str = "", command = None):
        """
        Changes the current application to a new one.

        Configures the exit button with the appropriate return function and destroys the current application before 
        creating a new one.

        Args:
        - new_app: A reference to the new application to create.
        - command: A reference to the function to call when the user clicks the exit button.
        - text_exit_button: The text of the button depending of the new app
        """
        if command != None:

            #TODO: a retiré en fin de projet
            if text_exit_button == "":
                raise AttributeError
            
            self.set_button(self.exit_button, text_exit_button, lambda: command())
            self.app.destroy()
        self.app = new_app(self.main_label)

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
        self.pack()

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

    def switch_app(self, new_app):
        """
        Switches to a new application.

        Args:
            new_app: The new application to be displayed.
        """
        self.master.master.change_app(new_app, text_exit_button = "Quitter", command = self.return_to_appchoice)
        self.master.master.change_app(new_app, text_exit_button = "Retour", command = self.return_to_appchoice)

    def return_to_appchoice(self):
        """
        Returns to the AppChoice screen.
        """
        self.master.master.change_app(AppChoice, text_exit_button = "Quitter", command = self.master.master.destroy)





