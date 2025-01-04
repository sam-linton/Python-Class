import ttkbootstrap as ttk

def greet():
    print('press')
    label['text'] = 'Hello'
    button['state'] = 'disabled'

# Create the Main Window
window = ttk.Window(themename = 'darkly')
window.title('Better Greeter')

# Button
button = ttk.Button(window, text = 'Greet Me',
                    command = greet)
button.pack()

# Label
label = ttk.Label(window, text = '')
label.pack()

# Run
window.mainloop()


