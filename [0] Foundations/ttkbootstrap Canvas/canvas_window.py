import ttkbootstrap as ttk

class CanvasWindow(ttk.Window):
    """This is designe to allow students to create a canvas hosted in a window with
    a single command:
    
    canvas = MyWindow().canvas
    """
    
    def __init__(self,
                 title = 'Canvas',
                 geometry = '1000x800',
                 bg = 'black'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self._canvas = ttk.Canvas()
        self._canvas.pack(expand = True, fill = 'both')
        self._canvas.configure(bg = bg)
        self._canvas.create_oval(10, 10, 20, 20, fill = 'white')
        self._canvas.focus_set()
        
        self.mainloop()
        
    @property
    def canvas(self):
        return self._canvas