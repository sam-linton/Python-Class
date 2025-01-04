import ttkbootstrap as ttk
from game import Game

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'darkly')
        self.geometry('1000x800')
        self.title('Pong!')
        
        control_bar = ttk.Frame(self)
        control_bar.pack(side = 'top', fill = 'x')
        ttk.Button(control_bar,
                   text = 'Start',
                   width = 15,
                   command = self.start).pack(side = 'left', anchor = 'w', padx = 5, pady = 5)
        ttk.Button(control_bar,
                   text = 'Stop',
                   width = 15,
                   command = self.stop).pack(side = 'left', anchor = 'w', padx = 5, pady = 5)
        self.game = Game(self)
        self.game.pack(expand = True, fill = 'both')
        
        self.mainloop()
        
    def start(self):
        self.game.focus_set()
        self.game.start()
        
    def stop(self):
        print('stop')
        self.game.stop()
    
    
if __name__ == '__main__':
    App()