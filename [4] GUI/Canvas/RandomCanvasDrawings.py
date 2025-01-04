#
# This program uses a canvas to draw random rectangles and ovals
#
# You may need to use Tkinter instead of tkinter
from tkinter import *
import random

# Create the main window and set some of its properties
window = Tk()
window.geometry("600x400")
window.title("My Canvas")

# Create a canvas and 'pack' it into the window
canvas = Canvas(window, height=400, width=600)
canvas.pack()

# Create an array of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'magenta', 'cyan']

# Draw 1000 rectangles with random coordinates and color
for i in range(1000):
    x1 = random.randint(0, 600)
    y1 = random.randint(0, 400)
    x2 = random.randint(0, 600)
    y2 = random.randint(0, 400)
    index = random.randint(0, len(colors)-1)
    canvas.create_rectangle(x1, y1, x2, y2, outline=colors[index])

# Draw 1000 ovals with random coordinates and colors
for i in range(10000):
    x1 = random.randint(0, 600)
    y1 = random.randint(0, 400)
    index = random.randint(0, len(colors)-1)
    canvas.create_oval(x1, y1, x1+10, y1+10, outline=colors[index])

# Start the window's main loop
window.mainloop()