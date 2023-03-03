import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window - Center")

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# can't be resizeable
root.resizable(False, False)

# when a window is resizable, you can specify the minimun and maximum size using the minsize() and maxsize()
# window.minsize(min_width, min_height)
# window.maxsize(min_height, max_height)

# Transparency
root.attributes('-alpha', 1)
# Place root window on top
root.attributes('-topmost', 1)
# Change the icon
root.iconbitmap('./Section1_TkinterFundamentals/assets/book.ico')

root.mainloop()
