import xml.etree.ElementTree as ET


tree = ET.parse('лаб 3/2.xml')
root = tree.getroot()

d = {}
names = []
full_names = []

for student in root.findall('student'):
    names.append(student.get('name').split(' ')[0])
    full_names.append(student.get('name'))

for i in set(names): 
    d[i] = names.count(i) - 1 

for student in full_names:
    print(student, '; Однофамильцев:', d[student.split(' ')[0]])