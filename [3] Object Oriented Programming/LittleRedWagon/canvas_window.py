import ttkbootstrap as ttk

class CanvasWindow(ttk.Window):
    """This is designed to allow students to create a canvas hosted in a window
    very simply:

    from canvas_window import CanvasWindow
    window = CanvasWindow()
    canvas = window.canvas
    
    <Your Code Here>
    
    window.mainloop()
    """
    
    def __init__(self,
                 title = 'Canvas',
                 geometry = '1000x800',
                 bg = 'white'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self._canvas = ttk.Canvas()
        self._canvas.pack(expand = True, fill = 'both')
        self._canvas.configure(bg = bg)
        self._canvas.focus_set()
        

        
    @property
    def canvas(self):
        return self._canvas