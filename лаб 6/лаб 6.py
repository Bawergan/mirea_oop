from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton

import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np


def Debug():
    print('works!')

window = Tk()

#tabs
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.add(tab3, text ='Tab 3')

tabControl.pack(expand = 1, fill ="both")


#2222222222222222222222222222222222222

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

xmin_ = Entry(tab1, width = 10)
xmin_.grid(column=1, row=0)
xmax_ = Entry(tab1, width = 10)
xmax_.grid(column=2, row=0)

funct_ = Combobox(tab1, values=('x', 'x^2', 'x**2 - 8*x + 15', '(x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1)'))
funct_.current(0)
funct_.grid(column = 3, row=0)

xmin_btn = Button(tab1, command=clicked)
xmin_btn.grid(column=4, row=0)


#3333333333333333333333333333333333333

tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

def EditStudent():
    for i in entryesOnEdit:
        try:
            if int(i.get()) < 0 or int(i.get()) > 100: 
                lblOnEdit.configure(text='invalid score')
                return
        except: pass  

    for enrolle in root.findall(f"enrolle[name='{students_names[selected.get()]}']"):
        for i in range(len(exam_names)):

            try: 
                enrolle.find(exam_names[i]).text
            except:
                new_exam = ET.Element(exam_names[i])
                root.find(f"enrolle[name='{students_names[selected.get()]}']").append(new_exam)
                tree.write('лаб 6/1.xml', encoding="UTF-8")

            if checkbuttons_stateOnEdit[i].get(): enrolle.find(exam_names[i]).text = entryesOnEdit[i].get()

    tree.write('лаб 6/1.xml', encoding="UTF-8")
    lblOnEdit.configure(text='done')

def get_names(): 
    global students_names
    global exam_names

    students_names = list({elem.findtext('name') for elem in root.iter()})
    students_names.remove(None)
    students_names.sort()

    exam_names = list({elem.tag for elem in root.findall('enrolle/*')})
    exam_names.remove('name')
    exam_names.sort()  

get_names()

radiobuttonsOnEdit = []
selected = IntVar()
for i in range(len(students_names)):
    radiobuttonsOnEdit.append(Radiobutton(tab2, text = students_names[i], value = i, variable=selected))
    radiobuttonsOnEdit[i].grid(column = 0, row = i)

checkbuttons_stateOnEdit = []
checkbuttonsOnEdit = []
entryesOnEdit = []
for i in range(len(exam_names)):
    checkbuttons_stateOnEdit.append(BooleanVar())
    checkbuttonsOnEdit.append(Checkbutton(tab2, text=exam_names[i], var = checkbuttons_stateOnEdit[i]))
    checkbuttonsOnEdit[i].grid(column = 1, row = i)

    entryesOnEdit.append(Entry(tab2, width = 10))
    entryesOnEdit[i].grid(column = 2, row = i)

submit_btn = Button(tab2, command=EditStudent, width=10)
submit_btn.grid(column=0, row=len(students_names))

lblOnEdit = Label(tab2,text='waiting input')
lblOnEdit.grid(column=0, row=len(students_names)+1)


#4444444444444444444444444444444444444
def AddStudent():
    
    if student_name.get() in students_names: 
        lblOnAdd.configure(text='student already exists')
        return
    for i in entryes:
        try:
            if int(i.get()) < 0 or int(i.get()) > 100: 
                lblOnAdd.configure(text='invalid score')
                return
        except: pass    

    new_student = ET.Element('enrolle')
    new_student.set('id', str(len(students_names) + 1))
    ET.SubElement(new_student, 'name').text = student_name.get()
    for i in range(len(exam_names)):
        if checkbuttons_state[i].get(): 
            print("works")
            ET.SubElement(new_student, exam_names[i]).text = entryes[i].get()
    root.append(new_student)
    tree.write('лаб 6/1.xml', encoding="UTF-8")
    get_names()
    lblOnAdd.configure(text='done')

get_names()

student_name = Entry(tab3, width = 10)
student_name.grid(column=1, row = 0)
student_name_lbl = Label(tab3, text = 'student_name').grid(column=0, row=0)

checkbuttons_state = []
checkbuttons = []
entryes = []
for i in range(len(exam_names)):
    checkbuttons_state.append(BooleanVar())
    checkbuttons.append(Checkbutton(tab3, text=exam_names[i], var = checkbuttons_state[i]))
    checkbuttons[i].grid(column = 0, row = i + 2)

    entryes.append(Entry(tab3, width = 10))
    entryes[i].grid(column = 1, row = i + 2)

submit_btn = Button(tab3, command=AddStudent, width=10)
submit_btn.grid(column=0, row=len(exam_names)+2)

lblOnAdd = Label (tab3, text='waiting input')
lblOnAdd.grid(column=0, row=len(exam_names)+3)


#draw window
window.geometry('400x250')
window.mainloop()