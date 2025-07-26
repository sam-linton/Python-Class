from canvas_window import CanvasWindow

window = CanvasWindow()
canvas = window.canvas

# Draw the body here
canvas.create_rectangle(50, 50, 250, 100, fill="red")

# Draw the front wheel
canvas.create_oval(50, 75, 100, 125, fill='black', outline="black")

# Draw the back wheel
canvas.create_oval(200, 75, 250, 125, fill='black', outline="black")


window.mainloop()