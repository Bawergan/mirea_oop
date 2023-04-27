import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton


tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

def clicked():
    
    if student_name.get() in students_names: 
        lbl.configure(text='student already exists')
        return
    for i in entryes:
        try:
            if 100 <= int(i.get()) >= 0: 
                lbl.configure(text='invalid score')
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
    lbl.configure(text='done')
    

def get_names(): 
    global students_names
    global exam_names

    students_names = list({elem.findtext('name') for elem in root.iter()})
    students_names.remove(None)
    students_names.sort()

    exam_names = list({elem.tag for elem in root.findall('enrolle/*')})
    exam_names.remove('name')
    exam_names.sort()  

# Window manager
window = Tk()

get_names()
student_name = Entry(window, width = 10)
student_name.grid(column=1, row = 0)
student_name_lbl = Label(window, text = 'student_name').grid(column=0, row=0)


checkbuttons_state = []
checkbuttons = []
entryes = []
for i in range(len(exam_names)):
    checkbuttons_state.append(BooleanVar())
    checkbuttons.append(Checkbutton(window, text=exam_names[i], var = checkbuttons_state[i]))
    checkbuttons[i].grid(column = 0, row = i + 2)

    entryes.append(Entry(window, width = 10))
    entryes[i].grid(column = 1, row = i + 2)

submit_btn = Button(window, command=clicked, width=10)
submit_btn.grid(column=0, row=len(exam_names)+2)

lbl = Label (window, text='waiting input')
lbl.grid(column=0, row=len(exam_names)+3)

window.geometry('400x250')
window.mainloop()