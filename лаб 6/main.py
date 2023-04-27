import xml.etree.ElementTree as ET

from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton

def clicked_edit():
    for i in entryes_a:
        try:
            if 0 >= int(i.get()) >= 100: pass
        except: pass
    
    for enrolle in root.findall(f"enrolle[name='{students_names[selected.get()]}']"):
        for i in range(len(exam_names)):

            try: 
                enrolle.find(exam_names[i]).text
            except:
                new_exam = ET.Element(exam_names[i])
                root.find(f"enrolle[name='{students_names[selected.get()]}']").append(new_exam)
                tree.write('лаб 6/1.xml', encoding="UTF-8")

            if checkbuttons_a_state[i].get(): enrolle.find(exam_names[i]).text = entryes_a[i].get()

    tree.write('лаб 6/1.xml', encoding="UTF-8")

def clicked_add_new_student():
    if student_name.get() in students_names: return
    for i in entryes:
        try:
            if 0 >= int(i.get()) <= 100: return
        except: pass    


    new_student = ET.Element('enrolle')
    new_student.set('id', str(len(students_names) + 1))
    ET.SubElement(new_student, 'name').text = student_name.get()
    for i in range(len(exam_names)):
        if checkbuttons_state[i].get(): 
            ET.SubElement(new_student, exam_names[i]).text = entryes[i].get()
        print (checkbuttons_state[i].get())
    root.append(new_student)
    tree.write('лаб 6/1.xml', encoding="UTF-8")
    get_names()   

def clicked_add_new_student_window ():
    global window_add_student
    window_add_student = Tk()

    global student_name
    student_name = Entry(window_add_student, width = 10)
    student_name.grid(column=1, row = 0)
    student_name_lbl = Label(window_add_student, text = 'student_name').grid(column=0, row=0)

    global checkbuttons_state, entryes
    checkbuttons_state = []
    checkbuttons = []
    entryes = []
    for i in range(len(exam_names)):
        checkbuttons_state.append(BooleanVar())
        checkbuttons.append(Checkbutton(window_add_student, text=exam_names[i], var = checkbuttons_state[i]))
        checkbuttons[i].grid(column = 0, row = i + 2)

        entryes.append(Entry(window_add_student, width = 10))
        entryes[i].grid(column = 1, row = i + 2)

    submit_btn = Button(window_add_student, command=clicked_add_new_student, width=10)
    submit_btn.grid(column=0, row=5)
    window_add_student.geometry('400x250')
    window_add_student.mainloop()

def main_window():

    global window
    window = Tk()

    radiobuttons = []
    global selected
    selected = IntVar()
    for i in range(len(students_names)):
        radiobuttons.append(Radiobutton(window, text = students_names[i], value = i, variable=selected))
        radiobuttons[i].grid(column = 0, row = i)

    global checkbuttons_a_state, entryes_a
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

    window.geometry('400x250')
    window.mainloop()

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

    get_names()

    main_window()


#TODO 
#refresh page
#do not allow invalid score
