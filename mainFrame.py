import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Main label
        label = tk.Label(self, text="Transactions", font=("Arial", 20, "bold"))
        label.pack()

        self.canvas = tk.Canvas(self, background="#ffffff", borderwidth=0) # Create a canvas widget for displaying a frame with content
        self.frame = tk.Frame(self.canvas, background="#ffffff") # Create a frame with the conent
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) # Create a vertical scrollbar for the canvas
        self.canvas.configure(yscrollcommand=self.vsb.set) # Link the scrollbar to the canvas so it controls the vertical view of the canvas
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        # Create a window inside the canvas where the frame will be placed
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.canvas.bind_all("<MouseWheel>", self.onMousewheel)

        self.populate()
    
    def populate(self):
        for row in range(100):
            tk.Button(self.frame, text="%s" % row, width=100, borderwidth="1", relief="solid").grid(row=row, column=0)

    def onFrameConfigure(self, event):
        # Update scrollregion after inserting widgets
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        # Resize the internal frame to match canvas width
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def onMousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units") # Moves the canvas's view

# Create a test figure
#fig = Figure(figsize=(5, 4), dpi=100)
#plot = fig.add_subplot(111)
#plot.plot([1, 2, 3, 4, 5], [1, 4, 2, 3, 7])  # Sample data
# Embed the figure in a canvas
#canvas = FigureCanvasTkAgg(fig, master=self)
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)