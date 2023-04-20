import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton


tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

"""
new_student = ET.Element('enrolle')
new_student.set('id', '5')
new_student.set('price', '500')
a = ET.SubElement(new_student,'Title')
a.text = 'python'
ET.SubElement(new_student,'Author').text = 'asd'
root.append(new_student)

tree.write('лаб 6/1.xml', encoding="UTF-8")
"""
def clicked():
    new_student = ET.Element('enrolle')
    new_student.set('id', str(len(students_names) + 1))
    ET.SubElement(new_student, 'name').text = student_name.get()
    for i in range(len(exam_names)):
        if checkbuttons_state[i].get(): 
            ET.SubElement(new_student, exam_names[i]).text = entryes[i].get()
    root.append(new_student)
    tree.write('лаб 6/1.xml', encoding="UTF-8")

# Window manager
window = Tk()

students_names = list({elem.findtext('name') for elem in root.iter()})
students_names.remove(None)
students_names.sort()

student_name = Entry(window, width = 10)
student_name.grid(column=1, row = 0)
student_name_lbl = Label(window, text = 'student_name').grid(column=0, row=0)


exam_names = list({elem.tag for elem in root.findall('enrolle/*')})
exam_names.remove('name')
exam_names.sort()


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
submit_btn.grid(column=0, row=5)

window.geometry('400x250')
window.mainloop()
