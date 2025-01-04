import tkinter as tk
import ttkbootstrap as ttk

# Create the Main Window
window = ttk.Window(themename = 'darkly')
window.title('Greeting')
window.geometry('1000x800')

label = ttk.Label(window, text = 'Hello, World!')
label.pack()

# Run
window.mainloop()
