from turtle import *
from body import Body
from wheel import Wheel

class Wagon:
    def __init__(self):
        self._body = Body(-10, 10, 100, 20)
        self._front = Wheel(0, 0, 10)
        self._back = Wheel(80, 0, 10)
        
    def __str__(self):
        return 'Little Red Wagon'
        
    def draw(self):
        self._body.draw()
        self._front.draw()
        self._back.draw()
        
        
# Program
wagon = Wagon()
print(wagon)
wagon.draw()
