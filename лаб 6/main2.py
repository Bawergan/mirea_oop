import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton



def main_window():

    radiobuttons = []
    selected = IntVar()
    for i in range(len(students_names)):
        radiobuttons.append(Radiobutton(window, text = students_names[i], value = i, variable=selected))
        radiobuttons[i].grid(column = 0, row = i)

    checkbuttons_a_state = []
    checkbuttons_a = []
    entryes_a = []
    for i in range(len(exam_names)):
        checkbuttons_a_state.append(BooleanVar())
        checkbuttons_a.append(Checkbutton(window, text=exam_names[i], var = checkbuttons_a_state[i]))
        checkbuttons_a[i].grid(column = 1, row = i)

        entryes_a.append(Entry(window, width = 10))
        entryes_a[i].grid(column = 2, row = i)

    submit_btn = Button(window, command=clicked_edit, width=10, text='submit')
    submit_btn.grid(column=0, row=len(students_names))

    add_new_btn = Button(window, command=clicked_add_new_student_window, width=10, text='add new')
    add_new_btn.grid(column=0, row=len(students_names)+1)



def get_names(): 
    global students_names
    global exam_names

    students_names = list({elem.findtext('name') for elem in root.iter()})
    students_names.remove(None)
    students_names.sort()

    exam_names = list({elem.tag for elem in root.findall('enrolle/*')})
    exam_names.remove('name')
    exam_names.sort()    

if __name__ == "__main__":
    
    tree = ET.parse('лаб 6/1.xml')
    root = tree.getroot()

    window = Tk()
    window.geometry('400x250')

    get_names()

    window.mainloop()
    window.update()