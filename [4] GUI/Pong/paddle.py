
class Paddle:
    def __init__(self, game):
        self.x = 10
        self.y = 10
        self.width = 10
        self.height = 100
        self.game = game
        
    @property
    def ymax(self):
        return self.y + self.height;
    
    @property
    def ymin(self):
        return self.y
        
    def update(self):
        pass
        
    def draw(self):
        self.game.create_rectangle((self.x, self.y, self.x + self.width, self.y + self.height),
                                    fill = 'white')
        
    def move_up(self):
        self.y += 15
        
    def move_down(self):
        self.y -= 15