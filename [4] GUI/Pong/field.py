import ttkbootstrap as ttk
from paddle import Paddle
from ball import Ball

class Game(ttk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.running = False
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bind('<Up>', self.move_down)
        self.bind('<Down>', self.move_up)
        self.focus_set()
        self.configure(bg = 'black')
        
    def start(self):
        self.running  = True
        self.run()
        
    def run(self):
        if self.running:
            self.update()
            self.draw()
            self.after(20, self.run)
        
    def stop(self):
        self.running = False
        
    def move_up(self, _ ):
        self.paddle.move_up()
        self.paddle.draw()
        
    def move_down(self, _ ):
        self.paddle.move_down()
        self.paddle.draw()
        
    def update(self):
        self.paddle.update()
        self.ball.update()
        
        if self.ball.off_screen:
            self.ball.reset()
            self.score_board.lose_life()
            return
        
        if self.ball.y > self.paddle.ymax: return
        if self.ball.y < self.paddle.ymin: return
        if self.ball.x <= self.paddle.x:
            self.ball.bounce_x()
        
    def draw(self):
        self.delete('all')
        self.paddle.draw()
        self.ball.draw()