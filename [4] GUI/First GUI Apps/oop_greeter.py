import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Greeter(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'darkly')
        self.geometry('500x500')
        
        ttk.Label(self, text = 'Name:').pack()
        self._entry = ttk.Entry(self)
        self._entry.pack()
        ttk.Button(self,
                   text = 'Greet',
                   command = self.greet
                   ).pack()
        self._greeting = ttk.Label(self, text = '')
        self._greeting.pack()
        
        self.mainloop()
                   
    def greet(self):
        self._greeting['text'] = 'Hello ' + self._entry.get()
        
    
if __name__ == '__main__':
    Greeter()