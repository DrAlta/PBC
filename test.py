from tkinter import *
import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()

root = Tk()

def load_c(lb):
    name=lb.get(ACTIVE)[0]
    print(name)
    if name == 'Random':
        
    else:
        cur.execute('SELECT name FROM characters WHERE name=?', (name,))
        row = cur.fetchone()
    


def get_char():
    top = Toplevel()
    top.title("Select a character to load.")
    char_select = Listbox(top, selectmode='single')
    for row in cur.execute('SELECT name FROM characters'):
        char_select.insert(END, row)
    char_select.insert(END, "Random")
    char_select.pack()
    buttom_frame = Frame(top)
    buttom_frame.pack()
    load_button = Button(buttom_frame, text="load", command=lambda : load_c(char_select))
    load_button.pack(side=LEFT)
    cancel_button = Button(buttom_frame, text="Cancel", command=top.destroy)
    cancel_button.pack(side=RIGHT)

frame = Frame(root)
frame.pack()

load_char = Button(frame, text="Load", command=get_char)
load_char.pack(side=LEFT)
mainloop()

input("\n\nPress the enter key to exit.") #Keep the window open