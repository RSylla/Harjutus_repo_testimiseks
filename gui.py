from main import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    v.set(csv_file_path)


root = tk.Tk()
tk.Label(root, text='Divide persons into groups').grid(row=0, column=0)
v = tk.StringVar()

entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)

tk.Button(root, text='Load persons from CSV', command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Generate groups', command=lambda: main(v.get())).grid(row=1, column=1)

root.mainloop()
