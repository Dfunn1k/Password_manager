import tkinter as tk
from  tkinter import tkk
import tkinter.font as font
import models

class APP(tk.Tk):
    def __init__(self):
        super().__init__()

        self.configure(bg = "black")
        font.nametofont("TkDefaultFont").configure(size=12, underline=True)
        self.title("Password Manager")

        # ventana posicionada centralmente independientemente de los cambios
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # frame container
        main_container = tk.Frame(self, bg = "green")
        main_container.grid( padx=40, pady=50, sticky="nsew")

        # Stored frames
        self.all_frames = dict()

        for f in (models.Add_frame, models.Show_frame):
            frame = f(self, main_container)
            self.all_frames[f] = frame
            frame.grid(row=0, column=0,sticky="nsew")

