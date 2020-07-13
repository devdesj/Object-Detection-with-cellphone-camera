from tkinter import *
import tkinter.messagebox as msg


def do_nothing():
    print("Ok I won't")


def laugh():
    print("Ja Ja AJ")


root = Tk()
root.geometry('300x200')
root['bg'] = '#E4C1BB'
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Connect", command=do_nothing)
submenu.add_separator()
submenu.add_command(label="Laugh", command=laugh)

edit_sub_menu = Menu(menu)
menu.add_cascade(label="Connection", menu=edit_sub_menu)
edit_sub_menu.add_radiobutton(label="output")

#       ****** Toolbar ******
toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="Basic Button", command=laugh)
insertButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#       ****** Status bar ******

status_bar = Label(root, text="Waiting...", bd=1, relief=FLAT, anchor=W, bg="#CFB8B3")
status_bar.pack(side=BOTTOM, fill=X)

msg.showinfo('Error', 'Monkeys can live baby')
answer = msg.askquestion('Question', 'Do YOU want to die')

if answer == 'yes':
    print("You survived")
else:
    print("Death is for you")

root.mainloop()
""" 
top_frame = Frame(root)
top_frame.pack(side=TOP)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Click me!", fg="red")
button2 = Button(top_frame, text="Click moi!", fg="blue")
button3 = Button(top_frame, text="Click me sir!", fg="green")
button4 = Button(bottom_frame, text="Yeh, Click me!", fg="yellow")

button_list = [button1, button2, button3, button4]

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)
"""

"""
one = Label(root, text="One", bg="black", fg="red")
two = Label(root, text="two", bg="white", fg="red")
three = Label(root, text="three", bg="yellow", fg="red")

one.pack()
two.pack(fill=X)
three.pack(fill=Y, side=LEFT)
"""
"""
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check_box = Checkbutton(root, text="Keep me signed in")
check_box.grid(columnspan=2)
"""
"""

def print_right(event):
    print("Right btn")


def print_left(event):
    print("Left btn")


def print_center(event):
    print("center btn")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", print_left)
frame.bind("<Button-2>", print_center)
frame.bind("<Button-3>", print_right)
frame.pack()

# button_1 = Button(root, text="Click to print a name")
# button_1.bind("<Button-1>", print_right)
# button_1.pack()
"""
"""
a = 12  # Aca se declara la variable
if a > 10:  # verificamos si a (que es 12) es mayor a 10
    print(" a es mayor a 10")  # Como a es mayor a 10 se ejecuta esta linea de código
print("¿Esto se imprime igual?")  # Esta linea de código se ejecuta independientemente de si a es mayor a 10
                                  # porque no está indentada debajo del if, está a la misma altura
                                  
                                  
"""
"""

class JoaquiBtns:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Print Message", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="click me to exit!", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    @staticmethod
    def print_message():
        print("Hi")



root = Tk()
joaquiFrm = JoaquiBtns(root)
root.mainloop()
"""
