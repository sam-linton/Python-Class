import ttkbootstrap as ttk

'''
Issue: key event is called before value of entry is updated
'''
class EmailApp(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'darkly')
        self.geometry('400x400')
        
        ttk.Label(self, text = 'First Name:').pack()
        self._first_entry = ttk.Entry(self)
        self._first_entry.bind('<Return>', self.show_email)
        self._first_entry.bind('<Tab>', self.show_email)
        self._first_entry.bind('<FocusOut>', self.show_email)
        self._first_entry.pack()
        
        ttk.Label(self, text = 'Last Name:').pack()
        self._last_entry = ttk.Entry(self)
        self._last_entry.bind('<Return>', self.show_email)
        self._last_entry.bind('<Tab>', self.show_email)
        self._last_entry.bind('<FocusOut>', self.show_email)
        self._last_entry.pack()
        
        ttk.Label(self, text = 'Graduation Year:').pack()
        self._grad_entry = ttk.Entry(self)
        self._grad_entry.bind('<Return>', self.show_email)
        self._grad_entry.bind('<Tab>', self.show_email)
        self._grad_entry.bind('<FocusOut>', self.show_email)
        self._grad_entry.pack()
        
        self._email_label = ttk.Label(
            self, text = '',)
        self._email_label.pack()
        
        button = ttk.Button(
            self,
            text = 'Show Email',
            command = self.show_email)
        button.pack()
        
        self.mainloop()
        
    def show_email(self, event = None):
        first = self._first_entry.get()
        print(event)
        if len(self._last_entry.get()) > 0:
            last_initial = self._last_entry.get()[0]
        else:
            last_initial = ''
        grad_date = self._grad_entry.get()[-2:]
        domain = '@students.harker.org'
        self._email_label['text'] = grad_date + first + last_initial + domain
        
if __name__ == '__main__':
    EmailApp()