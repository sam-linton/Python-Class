import ttkbootstrap as ttk
from tkinter.scrolledtext import ScrolledText
import requests

class Diskord(ttk.Window):
    API_BASE = "https://d090f7f1-56b3-4bd7-8828-2e9834c1ef7b-00-2zsmfmg1qaj4x.picard.replit.dev/"   # <--- change this once
    
    def __init__(self):
        super().__init__(themename="darkly")
        self.title('Diskord')
        self.geometry('800x500')
        
        # Chat display
        self.text = ttk.ScrolledText(self, wrap='word', height=12)
        self.text.pack(fill='both', expand=True, padx=10, pady=10)
#         self.text.configure(state='disabled')
        
        # Entry area
        self.entry_area = ttk.Frame(self)
        self.entry_area.pack(fill='x', padx=10, pady=(0, 10))
        self.message_entry = ttk.Entry(self.entry_area)
        self.message_entry.pack(side='left', fill='x', expand=True)
        
        self.send_button = ttk.Button(
            self.entry_area,
            width=8,
            text='Send',
            bootstyle='primary',
            command=self.send_message)
        self.send_button.pack(side='left', padx=(5, 5))
        
        self.refresh_button = ttk.Button(
            self.entry_area,
            width=8,
            text='Refresh',
            bootstyle='danger',
            command=self.read_and_display_messages)
        self.refresh_button.pack(side='left')
        
        self.update()
        self.mainloop()
        
    def update(self):
        self.read_and_display_messages()
        self.after(2000, self.update)
        
    def send_message(self):
        message = self.message_entry.get().strip()
        if len(message) == 0: return
        self.message_entry.delete(0, 'end')
        url = f'{Diskord.API_BASE}/message/{message}'
        response = requests.get(url)
    
    def read_and_display_messages(self):
        print('read and display')
        response = requests.get(Diskord.API_BASE)
        messages = response.json()
        print(messages)
        self.display_messages(messages)
    
    def display_messages(self, messages):
#         self.text.configure(state='normal')
        self.text.delete('1.0', 'end')

        for message in messages:
            self.text.insert('end', message + "\n")

#         self.message.see('end')
#         self.chat.configure(state='disabled')
        
        
if __name__ == "__main__":
    Diskord()