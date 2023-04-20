import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton


tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

def clicked():
    for enrolle in root.findall(f"enrolle[name='{students_names[selected.get()]}']"):
        #if math_checked.get(): enrolle.find('math').text = math_score.get()
        #if russian_checked.get(): enrolle.find('russian').text = russian_score.get()
        #if informatics_checked.get(): enrolle.find('informatics').text = informatics_score.get()
        for i in range(len(exam_names)):
            if checkbuttons_state[i].get(): enrolle.find(exam_names[i]).text = entryes[i].get()

    tree.write('лаб 6/1.xml', encoding="UTF-8")

# window manager
window = Tk()

students_names = list({elem.findtext('name') for elem in root.iter()})
students_names.remove(None)
students_names.sort()
#for enrolle in root.findall("enrolle"):
#    students_names.append(enrolle.findtext('name'))

radiobuttons = []
selected = IntVar()
for i in range(len(students_names)):
    radiobuttons.append(Radiobutton(window, text = students_names[i], value = i, variable=selected))
    radiobuttons[i].grid(column = 0, row = i)



exam_names = list({elem.tag for elem in root.findall('enrolle/*')})
exam_names.remove('name')
exam_names.sort()
checkbuttons_state = []
checkbuttons = []
entryes = []
for i in range(len(exam_names)):
    checkbuttons_state.append(BooleanVar())
    checkbuttons.append(Checkbutton(window, text=exam_names[i], var = checkbuttons_state[i]))
    checkbuttons[i].grid(column = 1, row = i)

    entryes.append(Entry(window, width = 10))
    entryes[i].grid(column = 2, row = i)
"""
math_checked = BooleanVar()
russian_checked = BooleanVar()
informatics_checked = BooleanVar()

math_check = Checkbutton(window, text='math', var = math_checked)
russian_check = Checkbutton(window, text='russian', var = russian_checked)
informatics_check = Checkbutton(window, text='informatics', var = informatics_checked)
math_check.grid(column=1, row=0)
russian_check.grid(column=1, row=1)
informatics_check.grid(column=1, row=2)

math_score = Entry(window, width = 10)
math_score.grid(column=2, row=0)
russian_score = Entry(window, width = 10)
russian_score.grid(column=2, row=1)
informatics_score = Entry(window, width = 10)
informatics_score.grid(column=2, row=2)
"""
submit_btn = Button(window, command=clicked, width=10)
submit_btn.grid(column=0, row=4,)

window.geometry('400x250')
window.mainloop()