from turtle import *

# Draw the body
def draw_body():
    t.width(1)
    t.pencolor('red')
    t.fillcolor('red')
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.end_fill()
    
# Go to front wheel location
def go_to_front_wheel():
    t.penup()
    t.setpos(0, 0)
    t.pendown()

# Draw a wheel
def draw_wheel():
    t.pencolor('black')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(wheel_radius)
    t.end_fill()

# Go to back wheel location
def go_to_back_wheel():
    t.penup()
    t.setpos(160, 0)
    t.pendown()

# Draw a wagon
def draw_wagon():
    draw_body()
    go_to_front_wheel()
    draw_wheel()
    go_to_back_wheel()
    draw_wheel()

######### Program starts here ########
# Create the objects
t = Turtle()
s = Screen()
s.title('Red Wagon')
length = 200
height = 50
wheel_radius = 20

draw_wagon()

s.mainloop()
