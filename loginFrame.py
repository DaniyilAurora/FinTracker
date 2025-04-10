import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, master, switchToMain):
        super().__init__(master)
        self.switchToMain = switchToMain

        # Entries for login data
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        loginButton = tk.Button(self, text="Login", command=self.login)

        self.username.pack()
        self.password.pack()
        loginButton.pack()

    def login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Basic login details check
        if username == "1" and password == "1":
            self.switchToMain()