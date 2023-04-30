import os
from cryptography.fernet import Fernet
from constant import *
from ui.main_window.main_window import Window


def create_repo() -> None:
    """
    Creates a new directory with the name specified by the REPO_NAME constant
    if it does not already exist.

    Returns:
        None
    """
    # Check if directory with REPO_NAME already exists in the current directory
    if REPO_NAME not in os.listdir():
        # Create new directory with the name specified by REPO_NAME constant
        os.makedirs(REPO_NAME)

def create_key() -> None:
    """
    Generates a new key using the Fernet encryption algorithm and saves it to
    a file with the name specified by the KEY_FILE_NAME constant if the file
    does not already exist.

    Returns:
        None
    """
    # Check if file with KEY_FILE_NAME already exists in the current directory
    if KEY_FILE_NAME not in os.listdir():
        # Generate new key using Fernet encryption algorithm
        key = Fernet.generate_key()
        # Save key to a file with the name specified by the KEY_FILE_NAME constant
        with open(KEY_FILE_NAME, "wb") as f:
            f.write(key)

def main() -> None:
    """
    The main function of the program that sets the current directory, creates
    a new directory and generates a new key if necessary, and creates a new
    instance of the main_window.Window class.

    Returns:
        None
    """
    # Change the current directory to the AppData\Local directory
    os.chdir(os.path.expanduser("~") + "\AppData\Local")
    # Create a new directory with the name specified by the REPO_NAME constant
    create_repo()
    # Change the current directory to the newly created directory
    os.chdir(REPO_NAME)
    # Generate a new key and save it to a file if necessary
    create_key()
    # Create a new instance of the main_window.Window
    Window()


if __name__ == "__main__":
    main()