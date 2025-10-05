from canvas_window import CanvasWindow

window = CanvasWindow()
canvas = window.canvas

wagon_length = 200
wagon_height = 50
wagon_x = 50
wagon_y = 50
wheel_radius = 25


def draw_body():
    canvas.create_rectangle(wagon_x,
                            wagon_y,
                            wagon_y + wagon_length,
                            wagon_y + wagon_height,
                            fill="red")
    

def draw_wheel_1():
    x = wagon_x
    y = wagon_y + wagon_height - wheel_radius
    canvas.create_oval(x,
                       y,
                       x + 2*wheel_radius,
                       y + 2*wheel_radius,
                       fill='black',
                       outline="black")
    

def draw_wheel_2():
    x = wagon_x + wagon_length - 2 * wheel_radius
    y = wagon_y + wagon_height - wheel_radius
    canvas.create_oval(x,
                       y,
                       x + 2*wheel_radius,
                       y + 2*wheel_radius,
                       fill='black',
                       outline="black")

def main():
    draw_body()
    
    draw_wheel_1()
    
    draw_wheel_2()

    window.mainloop()


main()
