from turtle import *

class Body:
    def __init__(self, x, y, length, height):
        self._x = x
        self._y = y
        self._length = length
        self._height = height
        
    def draw(self):
        t = Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.fillcolor('red')
        t.setpos(self._x, self._y)
        t.pendown()
        t.begin_fill()
        t.forward(self._length)
        t.left(90)
        t.forward(self._height)
        t.left(90)
        t.forward(self._length)
        t.left(90)
        t.forward(self._height)
        t.left(90)
        t.end_fill()
        
# Test Program
if __name__ == '__main__':
    body = Body(0, 0, 100, 20)
    body.draw()
        
