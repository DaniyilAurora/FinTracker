import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Main label
        label = tk.Label(self, text="Main")
        label.pack()

        # Create a test figure
        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(111)
        plot.plot([1, 2, 3, 4, 5], [1, 4, 2, 3, 7])  # Sample data

        # Embed the figure in a canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)