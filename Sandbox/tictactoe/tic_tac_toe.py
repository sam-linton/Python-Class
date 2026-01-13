import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

class TicTacToe(ttk.Window):
    def __init__(self):
        super().__init__()
        
        self.title("Local Tic-Tac-Toe — ttkbootstrap")

        self.board = [None] * 9
        self.turn = 'X'

        self.status = ttk.Label(self, text=f"Turn: {self.turn}", font=('Helvetica', 14))
        self.status.pack(pady=10)

        self.canvas = tk.Canvas(self, width=300, height=300, bg='white')
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind('<Button-1>', self.on_click)

        self.draw_grid()
        
        self.mainloop()

    def draw_grid(self):
        self.canvas.delete('all')
        w = h = 300
        # grid lines
        self.canvas.create_line(w/3, 0, w/3, h, width=2)
        self.canvas.create_line(2*w/3, 0, 2*w/3, h, width=2)
        self.canvas.create_line(0, h/3, w, h/3, width=2)
        self.canvas.create_line(0, 2*h/3, w, 2*h/3, width=2)

        # draw symbols
        for i, v in enumerate(self.board):
            if v:
                cx = (i % 3) * (w/3) + (w/6)
                cy = (i // 3) * (h/3) + (h/6)
                r = 40
                if v == 'X':
                    self.canvas.create_line(cx-r, cy-r, cx+r, cy+r, width=4)
                    self.canvas.create_line(cx-r, cy+r, cx+r, cy-r, width=4)
                else:
                    self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=4)

    def on_click(self, event):
        if self.check_winner() is not None:
            return

        cell_w = self.canvas.winfo_width() / 3
        cell_h = self.canvas.winfo_height() / 3
        col = int(event.x // cell_w)
        row = int(event.y // cell_h)
        idx = row * 3 + col

        if self.board[idx] is not None:
            return

        self.board[idx] = self.turn
        self.turn = 'O' if self.turn == 'X' else 'X'

        self.draw_grid()
        winner = self.check_winner()
        if winner:
            self.status.config(text=f"Winner: {winner}")
        elif all(self.board):
            self.status.config(text="Draw — game over")
        else:
            self.status.config(text=f"Turn: {self.turn}")

    def check_winner(self):
        b = self.board
        lines = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b1,c in lines:
            if b[a] and b[a] == b[b1] == b[c]:
                return b[a]
        return None


if __name__ == "__main__":
    TicTacToe()
