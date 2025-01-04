
class Ball:
    def __init__(self, game):
        self.game = game
        self.radius = 10
        self.reset()
    
    def reset(self):
        self.x = 50
        self.y = 50
        self.u = 10
        self.v = 5
        self.off_screen = False
        
    def bounce_x(self):
        self.u = -self.u
        
    def bounce_y(self):
        self.v = -self.v
        
    def update(self):
        self.x += self.u
        self.y += self.v
        
        if self.x > self.game.winfo_width():
            self.bounce_x()
            self.x = self.game.winfo_width()
            
        if self.y > self.game.winfo_height():
            self.bounce_y()
            self.y = self.game.winfo_height()
            
        if self.y < 0:
            self.bounce_y()
            self.y = 0
            
        if self.x < 0:
            self.off_screen = True
    
    def draw(self):
        self.game.create_oval((self.x, self.y, self.x + self.radius, self.y + self.radius),
                               fill = 'white')