from turtle import *

class SuperTurtle(Turtle):
    def __init__(self):
        super().__init__()
        
    def square(self):
        self.speed(0)
        for i in range(4):
            self.forward(100)
            self.left(90)
        self.penup()
        
            
    def forward(self, distance):
        super().forward(2 * distance)


s = SuperTurtle()
t = Turtle()
t.left(90)

t.forward(100)
s.forward(100)