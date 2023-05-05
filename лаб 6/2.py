from tkinter import *
from tkinter.ttk import Combobox

import matplotlib.pyplot as plt
import numpy as np

def BuildGraph(xmin, xmax, funct): 
    x = np.arange(xmin, xmax, round((xmax-xmin)/100, 2))
    
    match funct:
        case "x": y = x
        case 'x^2': y = x**2
        case "x**2 - 8*x + 15": y = x**2 - 8*x + 15
        case '(x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1)': y = (x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1)

    plt.plot(x,y)
    plt.show()
    print (xmin, xmax, funct)

def clicked():
    try: xmin = int(xmin_.get())
    except: xmin = 0
    try: xmax = int(xmax_.get())
    except: xmax = 0
    
    funct = funct_.get()

    BuildGraph(xmin, xmax, funct)


# Window manager
window = Tk()

xmin_ = Entry(window, width = 10)
xmin_.grid(column=1, row=0)
xmax_ = Entry(window, width = 10)
xmax_.grid(column=2, row=0)

funct_ = Combobox(window, values=('x', 'x^2', 'x**2 - 8*x + 15', '(x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1)'))
funct_.current(0)
funct_.grid(column = 3, row=0)

xmin_btn = Button(window, command=clicked)
xmin_btn.grid(column=4, row=0)

window.geometry('400x250')
window.mainloop()