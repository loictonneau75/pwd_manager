import tkinter as tk
from tkinter import ttk
from ui.account_creator.account_creator import AccountCreator
from ui.account_finder.account_finder import AccountFinder

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

    def __init__(self, master: tk.Tk) -> None:
        """
        Initializes the AppChoice object.

        Args:
            master (tk.Tk): The master window.
        """
        super().__init__(master, text="Choix de l'application")
        self.create_widget()
        self.pack()

    def create_widget(self) -> None:
        """
        Creates the widgets for the AppChoice object.
        """
        self.create_new_button()
        self.create_get_button()

    def create_new_button(self) -> None:
        """
        Creates the 'Creer un compte' button and assigns its command.
        """
        self.create_button = ttk.Button(self, text="Creer un compte")
        self.create_button.configure(command = lambda : self.switch_app(AccountCreator))
        self.create_button.pack(padx=20, pady=(20, 5))

    def create_get_button(self) -> None:
        """
        Creates the 'Afficher un compte' button and assigns its command.
        """
        self.get_button = ttk.Button(self, text="Afficher un compte")
        self.get_button.configure(command =  lambda : self.switch_app(AccountFinder))
        self.get_button.pack(padx=20, pady=(0, 20))

    def switch_app(self, next_application = None) -> None:
        """
        Switches to a new application.

        Args:
            next_application: The next application to be displayed.
        """
        main_window = self.master.master
        if next_application:
            main_window.change_app(
                next_application,
                exit_button_text="Retour",
                exit_button_command=self.switch_app
            )
        else:
            main_window.change_app(
                AppChoice,
                exit_button_text="Quitter",
                exit_button_command=main_window.destroy
            )