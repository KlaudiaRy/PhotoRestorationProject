from tkinter import *
from PIL import Image
from tkinter import filedialog
import numpy as np
import tkinter as tk

def pick_photo():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="images", title="Select picture", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    image_name= root.filename
    root.destroy()
    img=Image.open(root.filename)
    img2= img
    img = img.save('tmp/tmp_img.png', "PNG")
    img2 = img2.save('tmp/tmp_img_modified.png', "PNG")
    return 'tmp/tmp_img.png'

def display_info():
    root = tk.Tk()
    T = tk.Text(root, height=50, width=150)
    T.pack()
    f = open("information.txt", "r")
    text=f.read()
    T.insert(tk.END, text)
    f.close()
    tk.mainloop()

def save_photo():
    root = Tk()
    img= Image.open('tmp/tmp_img_modified.png')
    if (not img):
        img = Image.open('tmp/tmp_img.png')
    filename = filedialog.asksaveasfilename(filetypes=[("Plik png", "*.png")], defaultextension="*.png")
    if filename:
        img.save(filename, "PNG")
        print(filename)
        return filename
    root.destroy()

