# QR Code generator
# Libraries used pyqrcode,pillow


from tkinter import *
import pyqrcode
from PIL import ImageTk, Image


def generate_qr():
    link_name = name_entry.get()
    link = link_entry.get()
    filename = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(filename, scale=5)
    im = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(image=im)
    image_label.image = im
    canvas.create_window(200, 300, window=image_label)


root = Tk()
canvas = Canvas(root, width=400, height=500)
canvas.pack()
app_label = Label(root, text="QR Code Generator", fg='Blue', font=("Calibri", 20), relief='raised', anchor='center')
canvas.create_window(200, 50, window=app_label)
name_label = Label(root, text="Link Name", font=('Arial', 15))
link_label = Label(root, text="Link", font=('Arial', 15))
name_entry = Entry(root)
link_entry = Entry(root)
button = Button(root, text="Generate", command=generate_qr)

canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 150, window=link_label)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)
canvas.create_window(200, 250, window=button)

root.mainloop()
