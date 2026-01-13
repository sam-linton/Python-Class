#
#
class Bird():
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.v = 0
        self.g = 1
        
        self.id = self.canvas.create_rectangle(
            x, y,
            x + self.width, y + self.height,
            fill='yellow')     
    
    def update(self):
        self.v = min(10, self.v + self.g)
        self.canvas.move(self.id, 0, self.v)
        
    def flap(self, event=None):
        self.v = max(-20, self.v-15)
        
    def hit_ground(self):
        coords = self.canvas.coords(self.id)
        ground_level = self.canvas.winfo_height()
        return ground_level > 1 and coords[3] >= ground_level
         
    def get_bounding_box(self):
        return self.canvas.bbox(self.id)