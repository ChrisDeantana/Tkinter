import tkinter as tk

root = tk.Tk()

# Place a label on the root window
message = tk.Label(root, text="Hello,World!")
message.pack()

try:
    # If you find the text blurry
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    # Keep the window displaying
    root.mainloop()
