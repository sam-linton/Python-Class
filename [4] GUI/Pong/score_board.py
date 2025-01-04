class ScoreBoard:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.lives = 3
        
    def add_to_score(self, points):
        self.score += points
        
    def draw(self):
        x = self.game.winfo_width() / 2
        y = 50
        self.game.create_text((x, y),
                              text = f'Score: {self.score}\t Lives: {self.lives}',
                              fill = 'white',
                              font = ('Arial', 20))
#         self.game.create_text((x, y + 50),
#                               text = f'Lives: {self.lives}',
#                               fill = 'white',
#                               font = ('Arial', 20))
        
    def lose_life(self):
        self.lives -= 1
        
        
    