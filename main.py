import tkinter as tk
from mainFrame import MainFrame
from loginFrame import LoginFrame
from dataManager import DataManager
import settings as st


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialising Data Manager
        dm = DataManager()

        # Initialising window
        self.geometry(f'{st.WINDOW_WIDTH}x{st.WINDOW_HEIGHT}')
        self.title(st.WINDOW_TITLE)
        self.state('zoomed')

        self.loginFrame = LoginFrame(self, self.showMainFrame, dm)
        self.mainFrame = MainFrame(self, dm)

        self.loginFrame.pack()

    def showMainFrame(self):
        self.loginFrame.forget()
        self.mainFrame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
