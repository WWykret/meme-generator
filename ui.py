import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.setup_ui()

        tk.mainloop()

    def setup_ui(self):
        canvas = tk.Canvas(self.root, width=400, height=400)
        canvas.pack()
