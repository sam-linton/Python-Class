import ttkbootstrap as ttk
from tile import Tile

class TicTacToe(ttk.Window):
    def __init__(self):
        super().__init__()
        
        self.x0 = 0
        self.y0 = 0
        self.dx = 100
        self.dy = 100
        
        self.current_player = 'x'
        
        
        self.canvas = ttk.Canvas(self)
        self.canvas.pack(fill='both', expand=True, padx=10, pady=10)
        self.canvas.bind('<Button-1>', self.on_click)

        self.tiles = self.create_tiles()
        
        self.mainloop()
        
    def create_tiles(self):
        tiles = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            y = self.y0 + i*self.dy
            yp = y + self.dy
            for j in range(3):
                x = self.x0 + j*self.dx
                xp = x + self.dx
                tiles[i][j] = Tile(self.canvas, (x, y, xp, yp))
        
        for i in range(3):
            for j in range(3):
                x, y, xp, yp = tiles[i][j].bounding_box
                print(f'{i},{j}: {x},{y}   ', end='')
            print()
        return tiles
        
    def on_click(self, event):
        i = (event.y - self.y0) // self.dy
        j = (event.x - self.x0) // self.dx
        print(f'event at {event.x},{event.y} -> {i},{j}')
        if 0 <= i <= 2 and 0 <= j <= 2:
            tile = self.tiles[i][j]
            if not tile.is_played():
                tile.play(self.current_player)
                self.next_player()
                
    def get_winner(self):
        
        return None
                
    def next_player(self):
        self.current_player = 'o' if self.current_player == 'x' else 'x'
              
if __name__ == '__main__':
    TicTacToe()