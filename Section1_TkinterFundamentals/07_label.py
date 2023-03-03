import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# show the label here
label = ttk.Label(
    root,
    text='A Label with the Helvetica font',
    font=("Helvetica", 14))

# photo = tk.PhotoImage(file='./Section1_TkinterFundamentals/assets/rabbit.png')
# image_label = ttk.Label(
#     root,
#     image=photo,
#     padding=5
# )

label.pack(ipadx=10, ipady=10)
# image_label.pack()

photo = tk.PhotoImage(file='./Section1_TkinterFundamentals/assets/rabbit.png')
image_label = ttk.Label(
    root,
    image=photo,
    text='Python',
    compound='bottom'
)
image_label.pack()

root.mainloop()
