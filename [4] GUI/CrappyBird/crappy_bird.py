import ttkbootstrap as ttk
from bird import Bird
from wall import Wall

class CrappyBird(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly')
        self.title('Crappy Bird')
        self.geometry('1000x800')
        
        # Create the canvas
        self.canvas = ttk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)
        
        # Create the bird
        self.bird = Bird(self.canvas, 500, 10, 20, 20)
        
        # Create walls
        self.walls = []
        for _ in range(4):
            self.walls.append(Wall(self.canvas, 1990, 100, 700))
        
        # Handle user events
        self.bind("<space>", self.bird.flap)
        
        # Start the updating
        self.update()
        
        self.mainloop()
        
    def update(self):
        self.bird.update()
        if self.bird.hit_ground():
            self.end_game()
            return
        
        for wall in self.walls:
            if self.collision(self.bird, wall):
                self.end_game()
                return
            wall.update()
        
        self.after(20, self.update)
        
    def collision(self, bird, wall):
        ax1, ay1, ax2, ay2 = bird.get_bounding_box()
        bx1, by1, bx2, by2 = wall.get_bounding_box()
        
        if ax1 > bx2: return False
        if ax2 < bx1: return False
        if ay1 > by2: return False
        if ay2 < by1: return False
        return True
            
    def end_game(self):
        print('End Game!')
        
        
if __name__ == "__main__":
    CrappyBird()