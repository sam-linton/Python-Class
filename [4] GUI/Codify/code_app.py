import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
from codec import Codec
from text_file import TextFile


class CodeApp(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'darkly')
        self.title('Codify')
        self.geometry('1100x800')
        
        self._codec = Codec()
        self._codec.pass_phrase = 'Hello'
        self._text_file = TextFile()
        
        # Toolbar
        toolbar = ttk.Frame(self)
        toolbar.pack(fill = 'x', padx = 10, pady = 10)
        
        ttk.Label(toolbar, text = 'Passphrase:').pack(
            side = 'left',
            padx = (0, 10))
        self._pass_phrase_entry = ttk.Entry(
            toolbar,
            width = 30)
        self._pass_phrase_entry.pack(
            side = 'left',
            padx = (0, 10))
                
        ttk.Button(
            toolbar,
            text = 'Encode',
            width = 12,
            command = self.encode).pack(side = 'left', padx = (0, 10))
                
        ttk.Button(
            toolbar,
            text = 'Decode',
            width = 12,
            command = self.decode).pack(side = 'left', padx = (0, 10))
        
        ttk.Button(
            toolbar,
            text = 'Save...',
            width = 12,
            command = self._save).pack(side = 'left', padx = (0, 10))
         
        ttk.Button(
            toolbar,
            text = 'Open...',
            width = 12,
            command = self._open).pack(side = 'left', padx = (0, 10))
        
        self._text = ttk.Text(self, foreground = 'white')
        self._text.delete('1.0', 'end')
        self._text.pack(expand = True, fill = 'both')
        
        self.mainloop()
    
    def _open(self):
        print('open')
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        filename = filedialog.askopenfile(filetypes = filetypes).name
        print(filename)
        self._text_file.read_from(filename)
        self._text.delete('1.0', 'end')
        print(self._text_file.text)
        self._text.insert('end', self._text_file.text)
        
    def _save(self):
        print('save')
        self._text_file.text = self._text.get('1.0', 'end-1c')
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        filename = filedialog.asksaveasfile(filetypes = filetypes).name
        self._text_file.save_to(filename)
        
    def encode(self):
        print('\n\nEncode')
        self._codec.pass_phrase = self._pass_phrase_entry.get()
        text = self._text.get('1.0', 'end-1c')
        code = self._codec.encode(text)
        self._text.delete('1.0', 'end')
        self._text.insert('end', code)

    def decode(self):
        print('\n\nDecode')
        self._codec.pass_phrase = self._pass_phrase_entry.get()
        text = self._text.get('1.0', 'end-1c')
        code = self._codec.decode(text)
        self._text.delete('1.0', END)
        self._text.insert('end', code)
        
if __name__ == '__main__':
    CodeApp()