import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton


tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

def clicked():
    for i in entryes:
        try:
            if 100 <= int(i.get()) >= 0: 
                lbl.configure(text='invalid score')
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

            if checkbuttons_state[i].get(): enrolle.find(exam_names[i]).text = entryes[i].get()

    tree.write('лаб 6/1.xml', encoding="UTF-8")
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

# window manager
window = Tk()

get_names()

radiobuttons = []
selected = IntVar()
for i in range(len(students_names)):
    radiobuttons.append(Radiobutton(window, text = students_names[i], value = i, variable=selected))
    radiobuttons[i].grid(column = 0, row = i)


checkbuttons_state = []
checkbuttons = []
entryes = []
for i in range(len(exam_names)):
    checkbuttons_state.append(BooleanVar())
    checkbuttons.append(Checkbutton(window, text=exam_names[i], var = checkbuttons_state[i]))
    checkbuttons[i].grid(column = 1, row = i)

    entryes.append(Entry(window, width = 10))
    entryes[i].grid(column = 2, row = i)


submit_btn = Button(window, command=clicked, width=10)
submit_btn.grid(column=0, row=len(students_names))


lbl = Label(window,text='waiting input')
lbl.grid(column=0, row=len(students_names)+1)


window.geometry('400x250')
window.mainloop()