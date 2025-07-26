from canvas_window import CanvasWindow

window = CanvasWindow()
canvas = window.canvas

wagon_length = 200
wagon_height = 50
wagon_x = 50
wagon_y = 50
wheel_radius = 25

# Draw the body here
canvas.create_rectangle(
    wagon_x, wagon_y,
    wagon_x + wagon_length,
    wagon_y + wagon_height,
    fill="red")

# Draw the front wheel
canvas.create_oval(
    wagon_x, wagon_y + wheel_radius,
    wagon_x + 2 * wheel_radius,
    wagon_y + wagon_height + wheel_radius,
    fill='black', outline="black")

# Draw the back wheel
canvas.create_oval(
    wagon_x + wagon_length - 2 * wheel_radius,
    wagon_y + wheel_radius,
    wagon_x +  wagon_length,
    wagon_y + wagon_height + wheel_radius,
    fill='black', outline="black")

canvas.create_oval(200, 75, 250, 120, fill='black', outline="black")


window.mainloop()
