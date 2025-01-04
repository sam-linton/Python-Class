import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

root = ttk.Window(themename='darkly')

image1 = Image.open("right.png").resize((20,20), Image.LANCZOS)
test = ImageTk.PhotoImage(image1)

b1 = ttk.Button(root, text = "Button", image = test, compound=LEFT)
b1.pack(side=LEFT, padx=25, pady=50)

b2 = ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b2.pack(side=LEFT, padx=25, pady=10)

root.mainloop()