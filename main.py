import tkinter as tk
from mainFrame import MainFrame
from loginFrame import LoginFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        self.title("FinTracker")
        
        self.loginFrame = LoginFrame(self, self.showMainFrame)
        self.mainFrame = MainFrame(self)

        self.loginFrame.pack()

    def showMainFrame(self):
        self.loginFrame.forget()
        self.mainFrame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()