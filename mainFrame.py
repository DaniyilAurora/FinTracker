import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from dataManager import DataManager


class MainFrame(tk.Frame):
    def __init__(self, master, dm: DataManager, username: str):
        super().__init__(master)

        self.username = username

        self.dm = dm

        # Main Frame
        mainFrame = tk.Frame(self, bg="white")
        mainFrame.pack(fill=tk.BOTH, expand=True)

        # Left side frame
        self.analyticsFrame = tk.Frame(mainFrame, bg="white")
        self.analyticsFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Right side frame
        transactionFrame = tk.Frame(mainFrame, bg="#F0F0F0")
        transactionFrame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=5, pady=5)
        transactionFrame.config(width=50)

        # Bottom-left frame
        informationFrame = tk.Frame(mainFrame, bg="#666666")
        informationFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Configuring grid weights for resizing
        mainFrame.grid_rowconfigure(0, weight=2)
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(0, weight=4)
        mainFrame.grid_columnconfigure(1, weight=1)

        # Analytics Section (Top Left Panel)
        leftLabel = tk.Label(self.analyticsFrame, text="Analytics", bg="white", font=("Arial", 30))
        leftLabel.pack(padx=10, pady=15)

        # Create a transaction figure
        xdata = []
        ydata = []
        transactions = self.dm.getTransactions(self.username)
        balance = 0
        for i, transaction in enumerate(transactions):
            balance += transaction[3]
            xdata.append(i + 1)
            ydata.append(balance)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.fig.add_subplot(111)
        l = self.plot.fill_between(xdata, ydata)
        l.set_facecolors([[.5,.5,.8,.3]])
        self.plot.plot(xdata, ydata)  # Sample data
        self.plot.set_xlabel("Transactions")
        self.plot.set_ylabel("Account Balance")
        self.plot.margins(x=0, y=0)

        # Embed the figure in a canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.analyticsFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Transaction Section (Right Panel)
        self.transactionCanvas = tk.Canvas(transactionFrame, bg="#666666", highlightthickness=0)
        scrollbar = tk.Scrollbar(transactionFrame, orient="vertical", command=self.transactionCanvas.yview)
        self.scrollableFrame = tk.Frame(self.transactionCanvas, bg="#666666")

        self.scrollableFrame.bind("<Configure>", lambda e: self.transactionCanvas.configure(scrollregion=self.transactionCanvas.bbox("all")))
        self.transactionCanvas.create_window((0, 0), window=self.scrollableFrame, anchor="nw")
        self.transactionCanvas.configure(yscrollcommand=scrollbar.set)

        # Information Section (Bottom Panel)
        bottomLabel = tk.Label(informationFrame, text="Information", bg="#666666", font=("Arial", 14))
        bottomLabel.pack(padx=10, pady=10)
        balanceLabel = tk.Label(informationFrame, text=f"Balance ${round(balance, 2)}", bg="#666666", font=("Arial", 14))
        balanceLabel.pack(padx=10, pady=10)
        inputButton = tk.Button(informationFrame, text="Input Window", command=self.createInputWindow)
        inputButton.pack(padx=10, pady=10)

        # Layout of canvas and scrollbar
        self.transactionCanvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mouse movement to scrolling
        self.transactionCanvas.bind("<Enter>", lambda e: self.transactionCanvas.bind_all("<MouseWheel>", self.onMousewheel))
        self.transactionCanvas.bind("<Leave>", lambda e: self.transactionCanvas.unbind_all("<MouseWheel>"))

        for i, transaction in enumerate(transactions):
            tk.Label(self.scrollableFrame, text=f"Transaction for {transaction[2]} for {transaction[3]}", bg="#888888", fg="white").pack(fill="x", padx=5, pady=2)

    def onMousewheel(self, event):
        self.transactionCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def createInputWindow(self):
        inputWindow = tk.Toplevel(self)
        inputWindow.title = "Input Window"
        inputWindow.geometry("400x300")
        inputWindow.resizable(False, False)
        
        title = tk.Label(inputWindow, text="Input Window", font=("Arial", 14))
        title.pack()

        self.inputType = tk.Entry(inputWindow)
        self.inputType.pack()
        self.inputAmount = tk.Entry(inputWindow)
        self.inputAmount.pack()
        submitButton = tk.Button(inputWindow, text="Add", command=self.addNewTransaction)
        submitButton.pack()

    def addNewTransaction(self):
        newTransaction = self.dm.addTransaction(self.username, self.inputType.get().strip(), float(self.inputAmount.get().strip()))

        if newTransaction:
            self.updateInformation(self.inputType.get().strip(), float(self.inputAmount.get().strip()))
    
    def updateInformation(self, type: str, amount: float):
        # Update transaction list
        tk.Label(self.scrollableFrame, text=f"Transaction for {type} for {amount}", bg="#888888", fg="white").pack(fill="x", padx=5, pady=2)

        # Update graph
        self.plot.clear()

        # Get updated data
        transactions = self.dm.getTransactions(self.username)
        xdata = []
        ydata = []
        balance = 0
        for i, transaction in enumerate(transactions):
            balance += transaction[3]
            xdata.append(i + 1)
            ydata.append(balance)

        # Plot again
        self.plot.fill_between(xdata, ydata, facecolor=(.5, .5, .8, .3))
        self.plot.plot(xdata, ydata)
        self.plot.set_xlabel("Transactions")
        self.plot.set_ylabel("Account Balance")
        self.plot.margins(x=0, y=0)

        self.canvas.draw()