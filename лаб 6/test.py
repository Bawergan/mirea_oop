from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()



buttons = {}
names = ['aa','bb','cc']
selected = IntVar()
for i in range (len(names)):
    buttons[i] = Radiobutton(window, text = names[i], value = i, variable=selected)
    buttons[i].grid(column = 0, row = i)

window.geometry('400x250')
window.mainloop()