import ttkbootstrap as ttk

def greet():
    label['text'] = 'Hello ' + entry.get()

# Create the Main Window
window = ttk.Window(themename = 'darkly')
window.title('Better Greeter')

ttk.Label(window, text = 'Enter Name:').pack()

entry = ttk.Entry(window)
entry.pack()

# Button
button = ttk.Button(window, text = 'Greet Me',
                    command = greet)
button.pack()

# Label
label = ttk.Label(window, text = '')
label.pack()

# Run
window.mainloop()


