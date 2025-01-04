from turtle import *

# Create the objects
t = Turtle()
s = Screen()
s.title('Red Wagon')

# Draw the body
t.width(1)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()

# Go to front wheel location
t.penup()
t.setpos(0, 0)
t.pendown()

# Draw a wheel
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.circle(20)
t.end_fill()

# Go to back wheel location
t.penup()
t.setpos(160, 0)
t.pendown()

# Draw a wheel
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.circle(20)
t.end_fill()


s.mainloop()
