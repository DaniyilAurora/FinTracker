import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Main")
        label.pack()