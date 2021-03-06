import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog
from bridges import IUiBridge
from typing import Tuple

class App:
    def __init__(self, bridge: IUiBridge, image_size: Tuple[int, int] = (500,500)):
        self.bridge = bridge
        self.image_size = image_size

        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title('Meme Generator')

        self.setup_ui()

        tk.mainloop()

    def submit_login(self, username: str, password: str, save_credentials: bool) -> None:
        if self.bridge.try_to_login(username, password, save_credentials):
            self.canvas.destroy()
            self.setup_ui()

    def get_credentials(self) -> None:
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

    def update_image(self, new_image: Image) -> None:
        new_image.thumbnail(self.image_size, Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(new_image)

        self.image_label.configure(image = new_image)
        self.image_label.image = new_image

    def get_new_image(self, new_image_func: Image) -> None:
        self.update_image(new_image_func())

    def filter_images(self, filter_str: str) -> None:
        new_image = self.bridge.filter(filter_str)
        if new_image is None:
            new_image = self.bridge.filter('')
        self.update_image(new_image)

    def compile_image(self, text0: str, text1: str) -> None:
        new_image = self.bridge.compile(text0, text1)
        if new_image is None:
            new_image = self.bridge.filter('')
        self.update_image(new_image)

    def main_view(self) -> None:
        img = self.bridge.rand()
        img.thumbnail(self.image_size, Image.ANTIALIAS)

        image = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self.root, image=image)
        self.image_label.image = image
        self.image_label.grid(columnspan=3, column = 0, row = 0)

        prev_btn = tk.Button(self.root, text='previous', command=lambda: self.get_new_image(self.bridge.prev))
        prev_btn.grid(columnspan=1, row=1, column=0, stick='we')

        rand_btn = tk.Button(self.root, text='random', command=lambda: self.get_new_image(self.bridge.rand))
        rand_btn.grid(columnspan=1, row=1, column=1, stick='we')

        next_btn = tk.Button(self.root, text='next', command=lambda: self.get_new_image(self.bridge.next))
        next_btn.grid(columnspan=1, row=1, column=2, stick='we')

        search_entry = tk.Entry(self.root)
        search_entry.insert(-1, 'template name...')
        search_entry.grid(columnspan=2, row=2, column=0, stick='we')

        search_btn = tk.Button(self.root, text='search', command=lambda: self.filter_images(search_entry.get()))
        search_btn.grid(columnspan=1, row=2, column=2, stick='we')

        text_0 = tk.Entry(self.root)
        text_0.insert(-1, 'Caption 1...')
        text_0.grid(columnspan=3, row=3, column=0, stick='we')

        text_1 = tk.Entry(self.root)
        text_1.insert(-1, 'Caption 2...')
        text_1.grid(columnspan=3, row=4, column=0, stick='we')

        preview_btn = tk.Button(self.root, text='preview', command=lambda: self.compile_image(text_0.get(), text_1.get()))
        preview_btn.grid(columnspan=2, row=5, column=0, stick='we')

        save_btn = tk.Button(self.root, text='save', command=self.bridge.save)
        save_btn.grid(columnspan=1, row=5, column=2, stick='we')

    def setup_ui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.grid(columnspan=3)

        if not self.bridge.is_logged_in():
            self.get_credentials()
        else:
            self.main_view()
