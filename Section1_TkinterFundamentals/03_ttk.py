import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()

# The following ttk widgets replace the Tkinkter widgets with the same names:

# Button
# Checkbutton
# Entry
# Frame
# Label
# LabelFrame
# Menubutton
# PanedWindow
# Radiobutton
# Scale
# Scrollbar
# Spinbox
# And the following widgets are new and specific to ttk:

# Combobox
# Notebook
# Progressbar
# Separator
# Sizegrip
# Treeview
