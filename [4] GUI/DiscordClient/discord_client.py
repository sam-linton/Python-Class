# DiscordClient
#
import ttkbootstrap as ttk
import requests

base_url = "https://discordserver.samuellinton.repl.co/"

class DiscordClient(ttk.Window):
    """ The main window of the Discord Client application."""
    
    def __init__(self)-> None:
        """ Initialize the Discord Client application."""
        super().__init__(themename="darkly")
        self.geometry("400x600")
        self.title("Discord Client")
        
        # Messag History Display
        self.messages_display = ttk.ScrolledText(self)
        self.messages_display.pack(fill="both", expand=True, padx=(10, 10), pady=(10, 10))
        
        # Message Entry Frame
        message_frame = ttk.Frame(self)
        message_frame.pack(fill="x", pady=(0, 10))
        
        self.message_entry = ttk.Entry(
            message_frame,
            style="primary.TEntry")
        self.message_entry.pack(side='left', expand=True, fill='x', padx=(10, 10), pady=(0, 0))
        
        ttk.Button(
            message_frame,
            text="Send",
            style="success.Outline.TButton",
            command=self.send_message).pack(side='left', padx=(0, 10), pady=(0, 0))
        
        self.display_messages()
                   
        self.mainloop()
        
    def send_message(self)-> None:
        """ Send a message to the server."""
        message = self.message_entry.get()
        if message:
            self.message_entry.delete(0, 'end')
            requests.get(base_url + f"send/{message}")
            
    def display_messages(self)-> None:
        """ Display the messages from the server."""
        content = requests.get(base_url).json()
        messages = content["messages"]
        self.messages_display.delete('1.0', 'end')
        for message in messages:
            self.messages_display.insert('end', message + "\n")
        self.after(1000, self.display_messages)
        
            
        
        
if __name__ == "__main__":
    DiscordClient()