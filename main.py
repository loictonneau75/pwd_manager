import os
from cryptography.fernet import Fernet
from constant import *
from ui.MainApp import app_choice


def create_repo():
    if REPO_NAME not in os.listdir():
        os.makedirs(REPO_NAME)

def create_key():
    if KEY_FILE_NAME not in os.listdir():
        key = Fernet.generate_key()
        with open(KEY_FILE_NAME, "wb") as f:
            f.write(key)

def main():
    os.chdir(os.path.expanduser("~") + "\AppData\Local")
    create_repo()
    os.chdir(REPO_NAME)
    create_key()
    app_choice.App(REPO_NAME,INTERFACE_SIZE)


if __name__ == "__main__":
    main()