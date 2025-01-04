#
# Use the arrow keys to increase / decrease the
# object's speed in the x- and y-directions

# you may need to use Tkinter instead of tkinter
from tkinter import *
import time

# Create the window and set some of its properties
window = Tk()
window.geometry("600x400")
window.title("My Canvas")

# Create the canvas and 'pack' it into the window
canvas = Canvas(window, height=400, width=600)
canvas.pack()

# Create the rectangle
rectangleId = canvas.create_rectangle(10, 10, 20, 20)
print(rectangleId)

# Initialize the x- and y-velocities
u = v = 0

# Up arrow increases the (negative) y-velocity
def onKeyPressUp(event):
    global v
    v = v - 5

# Down arrow decreases the (negative) y-velocity
def onKeyPressDown(event):
    global v
    v = v + 5

# Left arrow decreases the x-velocity
def onKeyPressLeft(event):
    global u
    u = u - 5

# Right arrow increases the x-velocity
def onKeyPressRight(event):
    global u
    u = u + 5

# Bind the key presses to the appropriate functions
canvas.bind_all('<KeyPress-Up>', onKeyPressUp)
canvas.bind_all('<KeyPress-Down>', onKeyPressDown)
canvas.bind_all('<KeyPress-Left>', onKeyPressLeft)
canvas.bind_all('<KeyPress-Right>', onKeyPressRight)

# Animate
while True:
    canvas.move(rectangleId, u, v)
    time.sleep(0.1)
    window.update()

# Start the window's main loop
window.mainloop()