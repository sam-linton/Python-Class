from turtle import *

s = Screen()
t = Turtle()

command = input('Input command: ')
while command != '':
    for c in command:
        if c == 'f':
            t.forward(100)
        elif c == 'b':
            t.backward(100)
        elif c == 'l':
            t.left(90)
        elif c == 'r':
            t.right(90)
    command = input('Input command: ')
