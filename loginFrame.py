import tkinter as tk
from dataManager import DataManager


class LoginFrame(tk.Frame):
    def __init__(self, master, switchToMain, dm: DataManager):
        super().__init__(master)
        self.switchToMain = switchToMain

        # Entries for login data
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        loginButton = tk.Button(self, text="Login", command=self.login)

        self.username.pack()
        self.password.pack()
        loginButton.pack()

        self.dm = dm

    def login(self):
        inputUsername = self.username.get().strip()
        inputPassword = self.password.get().strip()

        password = self.dm.getPassword(inputUsername)
        # login details check
        if inputPassword == password:
            self.switchToMain(inputUsername)
