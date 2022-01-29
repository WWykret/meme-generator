import tkinter as tk
from tkinter import simpledialog
from bridges import IUiBridge

class App:
    def __init__(self, bridge: IUiBridge):
        self.bridge = bridge

        self.root = tk.Tk()

        self.setup_ui()

        tk.mainloop()

    def submit_login(self, username, password, save_credentials):
        if self.bridge.try_to_login(username, password, save_credentials):
            self.canvas.destroy()
            self.setup_ui()

    def get_credentials(self):
        username_label = tk.Label(self.canvas, text="Username:")
        username_label.grid(row=0, column=0, columnspan=1, stick='w', padx=10, pady=10)

        username_entry = tk.Entry(self.canvas)
        username_entry.grid(row=0, column=1, columnspan=2, stick='we', padx=10, pady=10)
        
        password_label = tk.Label(self.canvas, text="Password:")
        password_label.grid(row=1, column=0, columnspan=1, stick='w', padx=10, pady=10)

        password_entry = tk.Entry(self.canvas)
        password_entry.grid(row=1, column=1, columnspan=2, stick='we', padx=10, pady=10)
        
        save_credentials = tk.BooleanVar()
        save_cred_box = tk.Checkbutton(self.canvas, text='Save Credentials', variable=save_credentials, onvalue=True, offvalue=False)
        save_cred_box.grid(column=2, row = 2, columnspan=1, sticky = 'w', padx=10, pady=10)

        login_with_params = lambda: self.submit_login(username_entry.get(), password_entry.get(), save_credentials.get())
        submit_btn = tk.Button(self.canvas, text='Submit', command=login_with_params)
        submit_btn.grid(row=2, column=0, columnspan=2, stick='we', padx=10, pady=10)

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(columnspan=3)

        if not self.bridge.is_logged_in():
            self.get_credentials()
        else:
            print("test")
