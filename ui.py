import tkinter as tk
from tkinter import simpledialog

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.setup_ui()

        tk.mainloop()

    def get_credentials(self):
        username_label = tk.Label(self.root, text="Username:")
        username_label.grid(row=0, column=0, columnspan=1, stick='w', padx=10, pady=10)

        username_entry = tk.Entry(self.root)
        username_entry.grid(row=0, column=1, columnspan=2, stick='we', padx=10, pady=10)
        
        password_label = tk.Label(self.root, text="Password:")
        password_label.grid(row=1, column=0, columnspan=1, stick='w', padx=10, pady=10)

        password_entry = tk.Entry(self.root)
        password_entry.grid(row=1, column=1, columnspan=2, stick='we', padx=10, pady=10)
        
        com = lambda: print(f'u: {username_entry.get()}; p: {password_entry.get()}')
        submit_btn = tk.Button(self.root, text='Submit', command=com)
        submit_btn.grid(row=3, column=0, columnspan=3, stick='we', padx=10, pady=10)
        # com()

    def setup_ui(self):
        canvas = tk.Canvas(self.root)
        canvas.grid(columnspan=3)

        self.get_credentials()
