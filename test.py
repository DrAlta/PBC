from tkinter import *

root = Tk()

def get_char():
    top = Toplevel()
    top.title("Select a character to load.")
    char_select = Spinbox(top, values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    char_select.pack()
    buttom_frame = Frame(top)
    buttom_frame.pack()
    load_button = Button(buttom_frame, text="load", command=top.destroy)
    load_button.pack(side=LEFT)
    cancel_button = Button(buttom_frame, text="Cancel", command=top.destroy)
    cancel_button.pack(side=RIGHT)

frame = Frame(root)
frame.pack()

load_char = Button(frame, text="Load", command=get_char)
load_char.pack(side=LEFT)
mainloop()

input("\n\nPress the enter key to exit.") #Keep the window open