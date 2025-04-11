import tkinter as tk
from mainFrame import MainFrame
from loginFrame import LoginFrame
import settings as st

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Initialising window
        self.geometry(f'{st.WINDOW_WIDTH}x{st.WINDOW_HEIGHT}')
        self.title(st.WINDOW_TITLE)
        
        self.loginFrame = LoginFrame(self, self.showMainFrame)
        self.mainFrame = MainFrame(self)

        self.loginFrame.pack()

    def showMainFrame(self):
        self.loginFrame.forget()
        self.mainFrame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()