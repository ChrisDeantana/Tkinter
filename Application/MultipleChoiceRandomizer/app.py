import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()
root.title("MultipleChoiceRandomizer")
root.iconbitmap('Application\MultipleChoiceRandomizer\logo.ico')
root.resizable(False, False)


canvas = tk.Canvas(root, width=800, height=300)
canvas.grid(columnspan=4, rowspan=9)

# logo
logo = Image.open('Application\MultipleChoiceRandomizer\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
# logo_label.image = logo
logo_label.grid(columnspan=2, column=1, row=0)

# difficulty
instructions = tk.Label(root, text="Difficulty", font="Raleway")
instructions.grid(column=1, row=1, sticky="e", padx=10, pady=5)
# category
Category = tk.Label(root, text="Category", font="Raleway")
Category.grid(column=1, row=2, sticky="e", padx=10, pady=5)
# type
Type = tk.Label(root, text="Type", font="Raleway")
Type.grid(column=1, row=3, sticky="e", padx=10, pady=5)
# N of Questions
N_of_Questions = tk.Label(root, text="N of Questions", font="Raleway")
N_of_Questions.grid(column=1, row=4, sticky="e", padx=10, pady=5)
# N of Sheets
N_of_Sheets = tk.Label(root, text="N of Sheets", font="Raleway")
N_of_Sheets.grid(column=1, row=5, sticky="e", padx=10, pady=5)

# difficulty selection
difficulty_options = ["A(Easy)", "B(Medium)", "C(Hard)"]
selecteddiff_option = tk.StringVar(root)
selecteddiff_option.set(difficulty_options[0])
option_menu = tk.OptionMenu(root, selecteddiff_option, *difficulty_options)
option_menu.grid(column=2, row=1, sticky="w", padx=10, pady=5)
# category selection
category_options = ["A", "B"]
selectedcat_option = tk.StringVar(root)
selectedcat_option.set(category_options[0])
option_menu = tk.OptionMenu(root, selectedcat_option, *category_options)
option_menu.grid(column=2, row=2, sticky="w", padx=10, pady=5)
# type selection
type_options = ["M", "MM"]
selectedtype_option = tk.StringVar(root)
selectedtype_option.set(type_options[0])
option_menu = tk.OptionMenu(root, selectedtype_option, *type_options)
option_menu.grid(column=2, row=3, sticky="w", padx=10, pady=5)
# N_of_Questions
N_of_Questions_text_box = tk.Text(root, height=1, width=5)
N_of_Questions_text_box.grid(column=2, row=4, sticky="w", padx=10, pady=5)
# N_of_Sheets
N_of_Sheets_text_box = tk.Text(root, height=1, width=5)
N_of_Sheets_text_box.grid(column=2, row=5, sticky="w", padx=10, pady=5)


# def open_file():
#     browse_text.set("loading...")
#     file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[
#                        ("Pdf file", "*.pdf")])
#     print(file.name)
#     if file:
#         read_pdf = PyPDF2.PdfReader(file)
#         page = read_pdf.pages[int(selected_option.get())-1]
#         page_content = page.extract_text()

#         # text box
#         text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
#         text_box.insert(1.0, page_content)
#         text_box.tag_configure("center", justify="center")
#         text_box.tag_add("center", 1.0, "end")
#         text_box.grid(column=1, row=4)

#         # open file for writing
#         with open("example.txt", "w", encoding='utf-8') as file:
#             # write to file
#             file.write(page_content)

#         browse_text.set("Browse")

def open_file():
    desktop_path = os.path.join(os.path.join(
        os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop_path, "examples.txt")
    if (os.path.exists(file_path)):
        print("file exist")
    else:
        print(file_path)
        print("file doesn't exist")


# instructions
instructions = tk.Label(root, text="Select your data", font="Raleway")
instructions.grid(columnspan=2, column=1, row=6, pady=(15, 0))

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       font="Raleway", bg="#8fc649", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(columnspan=2, column=1, row=7, sticky="N")

canvas = tk.Canvas(root, width=600, height=200)
canvas.grid(columnspan=3)

root.mainloop()
