import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("PDFExtract")
root.iconbitmap('logo.ico')


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
# logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# select page
options = ["1", "2", "3", "4", "5"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.grid(column=1, row=2)


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[
                       ("Pdf file", "*.pdf")])
    print(file.name)
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[int(selected_option.get())-1]
        page_content = page.extract_text()

        # text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=4)

        # open file for writing
        with open("example.txt", "w", encoding='utf-8') as file:
            # write to file
            file.write(page_content)

        browse_text.set("Browse")


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
