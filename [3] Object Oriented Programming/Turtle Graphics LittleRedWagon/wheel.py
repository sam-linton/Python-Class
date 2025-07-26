from turtle import *

class Wheel:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius
         
    def draw(self):
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.setpos(self._x, self._y)
        t.pendown()
        t.fillcolor('black')
        t.begin_fill()
        t.circle(self._radius)
        t.end_fill()
        
        
if __name__ == '__main__':
    w = Wheel(0, 0, 10)
    w.draw()

