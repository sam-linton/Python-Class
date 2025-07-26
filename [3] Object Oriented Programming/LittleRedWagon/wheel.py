
class Wheel:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius
        
    def draw(self, canvas):
        canvas.create_oval(
            self._x, self._y,
            self._x + 2*self._radius,
            self._y + 2*self._radius,
            fill='black', outline="black")
