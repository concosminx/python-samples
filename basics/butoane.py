#display numbers from 1 to 10 in a popup; display pressed number in console

#see https://docs.python.org/3/library/tkinter.html#bindings-and-events
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def display_button(event):
    messagebox.showinfo("Pressed button: ", event.widget['text'])


win = Tk()
win.geometry("750x150")
Label(win, text="Press a button").pack(pady=20)

nr = 0
while nr < 10 :
    nr = nr + 1
    btn = ttk.Button(win, text=str(nr))
    btn.bind('<Button-1>', display_button)
    btn.pack(side=LEFT)

win.mainloop()


