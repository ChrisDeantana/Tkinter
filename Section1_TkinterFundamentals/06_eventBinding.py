import tkinter as tk
from tkinter import ttk

# link - https://www.pythontutorial.net/tkinter/tkinter-event-binding/


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


def paste(event):
    text = "A"
    event.widget.configure(text=text)


root = tk.Tk()

# Class level binding
root.bind_class('Button', '<KeyPress-A>', paste)

# Instance level binding
btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)
# btn.bind('<Return>', log, add='+')

btn.focus()
btn.pack(expand=True)


root.mainloop()
