from random import randint

class Wall:
    def __init__(self, canvas, x, ymin, ymax):

        self.canvas = canvas
        self.u = -randint(5, 10)
        
        # Create random shape
        width = randint(20, 50)
        height = randint(20, 50)
        y = randint(ymin, ymax+1)
        
        self.id = self.canvas.create_rectangle(
            x,
            y,
            x + width,
            y + height,
            fill='green')
        
    def update(self):
        self.canvas.move(self.id, self.u, 0)
        
    def get_bounding_box(self):
        return self.canvas.bbox(self.id)