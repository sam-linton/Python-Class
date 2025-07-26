from canvas_window import CanvasWindow

def draw_body(canvas, x, y, width, height):
    print('draw_body')
    canvas.create_rectangle(x, y, x + width, y + height, fill="red")
    

def draw_wheel(canvas, x, y, r):
    canvas.create_oval(x, y, x + 2*r, y + 2*r, fill='black', outline="black")


def main():
    window = CanvasWindow()
    canvas = window.canvas
    
    wagon_length = 200
    wagon_height = 50
    wagon_x = 50
    wagon_y = 50
    wheel_radius = 5

    draw_body(canvas, wagon_x, wagon_y, wagon_length, wagon_height)
    
    wheel_x = wagon_x
    wheel_y = wagon_y + wagon_height - wheel_radius
    draw_wheel(canvas, wheel_x, wheel_y, wheel_radius)
    
    wheel_x = wagon_x + wagon_length - 2 * wheel_radius
    draw_wheel(canvas, wheel_x, wheel_y, wheel_radius)

    window.mainloop()


main()