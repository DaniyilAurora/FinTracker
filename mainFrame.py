import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Main Frame
        mainFrame = tk.Frame(self, bg="white")
        mainFrame.pack(fill=tk.BOTH, expand=True)

        # Left side frame
        analyticsFrame = tk.Frame(mainFrame, bg="lightgray")
        analyticsFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

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
        leftLabel = tk.Label(analyticsFrame, text="Analytics", bg="lightgray", font=("Arial", 14))
        leftLabel.pack(padx=10, pady=10)

        # Transaction Section (Right Panel)
        self.transactionCanvas = tk.Canvas(transactionFrame, bg="#666666", highlightthickness=0)
        scrollbar = tk.Scrollbar(transactionFrame, orient="vertical", command=self.transactionCanvas.yview)
        scrollableFrame = tk.Frame(self.transactionCanvas, bg="#666666")

        scrollableFrame.bind("<Configure>", lambda e: self.transactionCanvas.configure(scrollregion=self.transactionCanvas.bbox("all")))
        self.transactionCanvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
        self.transactionCanvas.configure(yscrollcommand=scrollbar.set)

        # Information Section (Bottom Panel)
        bottomLabel = tk.Label(informationFrame, text="Information", bg="#666666", font=("Arial", 14))
        bottomLabel.pack(padx=10, pady=10)

        # Layout of canvas and scrollbar
        self.transactionCanvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mouse movement to scrolling
        self.transactionCanvas.bind("<Enter>", lambda e: self.transactionCanvas.bind_all("<MouseWheel>", self.onMousewheel))
        self.transactionCanvas.bind("<Leave>", lambda e: self.transactionCanvas.unbind_all("<MouseWheel>"))

        # TEST DATA, TODO: REMOVE LATER
        for i in range(100):
            tk.Label(scrollableFrame, text=f"Transaction {i+1}", bg="#888888", fg="white").pack(fill="x", padx=5, pady=2)

    def onMousewheel(self, event):
        self.transactionCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
