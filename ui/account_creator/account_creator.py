import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ui.account_creator.engine import *


class AccountCreator(ttk.Labelframe):
    """A class for creating a user account with a company, email, pseudonym, and password.

    Args:
        master (tk.Frame): The parent widget.

    Attributes:
        widgets_to_hide (List[tk.Widget]): A list of widgets to hide.

    Methods:
        create_widget(): Create the widgets for the account creator.
        hide_widgets(): Hide the widgets in the list widgets_to_hide.
        handle_validation(): Validates the information entered by the user.
        validate_info(): Validates the information provided by the user.
    """
    def __init__(self, master: tk.Frame) -> None:
        """Initializes an instance of the AccountCreator class.

        Args:
            master (tk.Frame): The parent widget.
        """
        super().__init__(master, text = "Création de compte")
        self.widgets_to_hide = []
        self.create_widget()
        self.hide_widgets()
        self.pack()

    def create_widget(self) -> None:
        #TODO finir la docstring
        """
        Creates the widgets for the account creator.

        Attributes:
            company: A class that contains a label and entry widget for the user's company name, and provides methods for validating and checking the user's input.
            email: 
            pseudo: 
            password: 
            valid_button:
        """
        self.company = Company(self,0)
        self.email = Email(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.pseudo = Pseudo(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.password = Password(self, self.winfo_children()[-1].grid_info()["row"] + 1)
        self.valid_button = ttk.Button(self, text="Valider", command = self.handle_validation)
        self.valid_button.grid(row = 13, column = 1, sticky = "e")

    def hide_widgets(self) -> None:
        """
        Hides the widgets in the list widgets_to_hide
        """
        [widget.grid_forget() for widget in self.widgets_to_hide]

    def handle_validation(self) -> None:
        """
        Validates the information entered by the user and prints "ok" if all the required fields are
        filled in. Otherwise, displays an error message using a messagebox.

        Raises:
            tkinter.TclError: If there is an error with the messagebox.
        """
        if self.validate_info():
            print("ok")
        else:
            try:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            except tk.TclError as e:
                # The error message is displayed in the console if there is a problem with the messagebox.
                print(f"Error displaying messagebox: {e}")

    def validate_info(self):
        """
        Validates the information provided by the user.
        
        Returns:
            bool: True if all information is valid, False otherwise.
        """
        return False


class Company():
    """
    A class that contains a label and entry widget for the user's company name, and provides methods
    for validating and checking the user's input.

    Args:
        master: The AccountCreator object that serves as the master of this widget.
        start_row: The row at which to start placing this widget.

    Attributes:
        master: The AccountCreator object that serves as the master of this widget.
        start_row: The row at which to start placing this widget.
        company_name: The StringVar object that contains the user's input for the company name.
        label: The ttk.Label object that displays the label for the company name entry.
        entry: The ttk.Entry object that allows the user to input their company name.
        error_no_company: The ttk.Label object that displays an error message if the user has not entered a company name.
    """

    def __init__(self, master: AccountCreator, start_row: int) -> None:
        """
        Initializes the Company object with a label and entry widget for the user's company name,
        and methods for validating and checking the user's input.

        Args:
            master: The AccountCreator object that serves as the master of this widget.
            start_row: The row at which to start placing this widget.

        Attributes:
            master: The AccountCreator object that serves as the master of this widget.
            start_row: The row at which to start placing this widget.
            company_name: The StringVar object that contains the user's input for the company name.
            label: The ttk.Label object that displays the label for the company name entry.
            entry: The ttk.Entry object that allows the user to input their company name.
            error_no_company: The ttk.Label object that displays an error message if the user has not entered a company name.
        """
        self.master = master
        self.start_row = start_row
        self.create_widgets()
        self.config_widgets()

    def  create_widgets(self) -> None:
        """
        Creates the label, entry, and error message widgets for the Company object.

        Attributes:
            company_name: The StringVar object that contains the user's input for the company name.
            label: The ttk.Label object that displays the label for the company name entry.
            entry: The ttk.Entry object that allows the user to input their company name.
            error_no_company: The ttk.Label object that displays an error message if the user has not entered a company name.
        """
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Nom de la compagnie :", (self.start_row, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row, 1))
        self.error_no_company = create_error(self.master, "Veuillez mettre le nom de la compagnie pour laquelle vous enregistrez un compte", (self.start_row + 1, 0))
        self.master.widgets_to_hide.extend([self.error_no_company])

    def handle_input(self, *args):
        """
        Checks the user's input for the company name, and displays an error message if the input is
        empty. Otherwise, removes any displayed error messages.
        """
        if clean_company_name(self.value) == "":
            self.error_no_company.grid(row = self.start_row + 1, column = 0, columnspan = 2)
        else:
            self.error_no_company.grid_forget()
    
    def config_widgets(self) -> None:
        """
        Configures the entry widget to call the check_input method when the user inputs data, and
        binds the check_input method to the "<FocusOut>" event.
        """
        self.value.trace_add("write", self.handle_input)
        self.entry.bind("<FocusOut>", self.handle_input)


class Email():

    def __init__(self, master : AccountCreator, start_row) -> None:
        self.master = master
        self.start_row = start_row
        self.create_widget()
        self.config_widgets()

    def  create_widget(self) -> None:
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Email :", (self.start_row, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row, 1))
        self.error_no_email = create_error(self.master, "Veuillez mettre l'adresse utilisé pour créer un compte", (self.start_row + 1, 0))
        self.error_incorrect_email = create_error(self.master, "Email incorrecte", (self.start_row + 2, 0))
        self.master.widgets_to_hide.extend([self.error_no_email,self.error_incorrect_email])

    def handle_change(self,*args) -> bool:
        if self.value.get() == "":
            self.error_no_email.grid(row = self.start_row + 1, column = 0, columnspan = 2)
            self.error_incorrect_email.grid_forget()
            return True
        else:
            self.error_no_email.grid_forget()
            return False

    def handle_focus_out(self, *args) -> None:
            if self.handle_change():
                return
            self._handle_focus_out()

    def _handle_focus_out(self) -> None: 
        if is_email_format_valid(self.value.get()):
            self.error_incorrect_email.grid(row = self.start_row + 2, column = 0, columnspan = 2)
            self.error_no_email.grid_forget()
        else:
            self.error_incorrect_email.grid_forget()

    def handle_key_press(self, *args) -> None:
        self.error_no_email.grid_forget()
        self.error_incorrect_email.grid_forget()

    def config_widgets(self) -> None:
        self.value.trace_add("write", self.handle_change)
        self.entry.bind("<FocusOut>", self.handle_focus_out)
        self.entry.bind("<KeyPress>", self.handle_key_press)


class Pseudo():

    def __init__(self, master : AccountCreator, start_row) -> None:
        self.master = master
        self.start_row = start_row
        self.create_widget()
        self.config_widget()

    def  create_widget(self) -> None:
        self.is_necessary = tk.BooleanVar()
        self.is_necessary_checkbox = create_checkbox(self.master, self.is_necessary, "Avez vous besoin d'un pseudo", (self.start_row, 0))
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(self.master, self.is_already_possessed, "Avez vous deja un pseudo", (self.start_row, 1))
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Pseudo :", (self.start_row + 1, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(self.master,"Veuillez renseigné un pseudo",(self.start_row + 2, 0))
        self.master.widgets_to_hide.extend([self.is_already_possessed_checkbox,self.label,self.entry,self.error_no_pseudo])

    def handle_is_necessary(self, *args) -> None:
        if self.is_necessary.get():
            self.is_already_possessed_checkbox.grid(row = self.start_row, column = 1)
        else :
            self.is_already_possessed_checkbox.grid_forget()
            self.is_already_possessed.set(False)

    def handle_is_already_possessed(self,*args) -> None:
        if self.is_already_possessed.get():
            self.label.grid(row = self.start_row + 1, column = 0)
            self.entry.grid(row = self.start_row + 1, column = 1)
        else :
            self.label.grid_forget()
            self.entry.grid_forget()
            self.error_no_pseudo.grid_forget()

    def handle_input(self,*args) -> None:
        if self.value.get() == "":
            self.error_no_pseudo.grid(row = self.start_row + 2, column = 0)
        else :
            self.error_no_pseudo.grid_forget()

    def config_widget(self) -> None:
        self.is_necessary.trace_add("write", self.handle_is_necessary)
        self.is_already_possessed.trace_add("write", self.handle_is_already_possessed)
        self.value.trace_add("write", self.handle_input)
        self.entry.bind("<FocusOut>", self.handle_input)


class Password():

    def __init__(self, master : AccountCreator, start_row) -> None:
        self.master = master
        self.start_row = start_row
        self.create_widget()

    def  create_widget(self) -> None:
        self.is_already_possessed = tk.BooleanVar()
        self.is_already_possessed_checkbox = create_checkbox(self.master, self.is_already_possessed, "Avez vous deja un mot de passe", (self.start_row, 0))
        self.value = tk.StringVar()
        self.label = create_label(self.master, "Mot de passe :", (self.start_row + 1, 0))
        self.entry = create_entry(self.master, self.value, (self.start_row + 1, 1))
        self.error_no_pseudo = create_error(self.master,"Veuillez renseigné un mot de passe", (self.start_row + 2, 0))
        self.label_match = create_label(self.master, "Répéter le mot de passe :", (self.start_row + 3, 0))
        self.entry_match = create_entry(self.master, self.value, (self.start_row + 3, 1))
        self.error_pseudo_match = create_error(self.master,"Les mots de passe doivent corespondre",(self.start_row + 4, 0))
        self.master.widgets_to_hide.extend([self.label,self.entry,self.error_no_pseudo,self.label_match,self.entry_match,self.error_pseudo_match])