from body import Body
from wheel import Wheel

class Wagon:
    def __init__(self, x, y, length, height, wheel_radius):
        self._body = Body(x, y, length, height)
        self._front_wheel = Wheel(
            x,
            y + height - wheel_radius,
            wheel_radius)
        
        self._back_wheel = Wheel(
            x + length - 2 * wheel_radius,
            y + height - wheel_radius,
            wheel_radius)
    
    def draw(self, canvas):
        self._body.draw(canvas)
        self._front_wheel.draw(canvas)
        self._back_wheel.draw(canvas)