from tkinter import *
from tkinter.ttk import Combobox

import matplotlib.pyplot as plt
import numpy as np

def BuildGraph(xmin, xmax, funct): 
    x = np.arange(xmin, xmax, 1)
    if funct == 'x^2': y = x ** 2
    if funct == 'x^3': y = x**3
    if funct == 'x': y = x

    plt.plot(x,y)
    plt.show()
    print (xmin, xmax, funct)

def clicked():
    try:
        xmin = int(xmin_.get())
        xmax = int(xmax_.get())
    except: xmin, xmax = 0, 0
    
    funct = funct_.get()

    BuildGraph(xmin, xmax, funct)


# Window manager
window = Tk()

xmin_ = Entry(window, width = 10)
xmin_.grid(column=1, row=0)
xmax_ = Entry(window, width = 10)
xmax_.grid(column=2, row=0)

funct_ = Combobox(window, values=('x', 'x^2', 'x^3'))
funct_.current(0)
funct_.grid(column = 3, row=0)

xmin_btn = Button(window, command=clicked)
xmin_btn.grid(column=4, row=0)

window.geometry('400x250')
window.mainloop()
