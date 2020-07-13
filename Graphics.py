#!/usr/bin/python3

from tkinter import *

root = Tk()
root.title('Connection')
root.iconbitmap('')
root.geometry('850x600')
root['bg'] = 'red'
entry = Entry(root, text="Enter your name", width=40)
entry.pack()
entry.insert(0, "Enter your name")
root.mainloop()
