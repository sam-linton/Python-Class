class Tile:
    def __init__(self, canvas, bounding_box):
        self.canvas = canvas
        self.bounding_box = bounding_box
        self.player = ''
        x, y, xp, yp = bounding_box
        self.canvas.create_rectangle(x, y, xp, yp)
        
    def is_played(self):
        return self.player != ''
        
    def get_player(self):
        return self.player
        
    def contains(self, x, y):
        print(f'{x},{y} bbox: {self.bounding_box}')
        if x < self.bounding_box[0]: return False
        if x > self.bounding_box[2]: return False
        if y < self.bounding_box[1]: return False
        if y > self.bounding_box[3]: return False
        return True
    
    def play(self, player):
        self.player = player
        x = 0.5*(self.bounding_box[0] + self.bounding_box[2])
        y = 0.5*(self.bounding_box[1] + self.bounding_box[3])
        print(f'draw at {x},{y}')
        self.canvas.create_text(x, y,
                                text=f'{self.player}',
                                font=("Arial", 30, "bold"))
    
    