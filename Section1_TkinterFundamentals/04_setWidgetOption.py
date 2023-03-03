# How to set options for a ttk using keyword arguments, dictionary index and config() method
# keyword arguments - at widget creation
# dictionary index - after widget creation
# config() method is used with keyword attributes

import tkinter as tk
from tkinter import ttk

# use keyword arguments
root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()

# use dictionary key
label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

# use config
label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()
