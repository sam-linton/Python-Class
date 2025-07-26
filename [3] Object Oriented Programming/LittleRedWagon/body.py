
class Body:
    def __init__(self, x, y, length, height):
        self._x = x
        self._y = y
        self._length = length
        self._height = height
    
    def draw(self, canvas):
        canvas.create_rectangle(
            self._x, self._y,
            self._x + self._length,
            self._y + self._height,
            fill="red")