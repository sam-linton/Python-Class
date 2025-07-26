from canvas_window import CanvasWindow
from wagon import Wagon

window = CanvasWindow()
canvas = window.canvas

wagon_length = 200
wagon_height = 50
wagon_x = 50
wagon_y = 50
wheel_radius = 25

wagon = Wagon(wagon_x, wagon_y, wagon_length, wagon_height, wheel_radius)
wagon.draw(canvas)


window.mainloop()
