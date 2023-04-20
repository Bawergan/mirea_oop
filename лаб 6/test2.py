import xml.etree.ElementTree as ET



tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()
'''
for enrolle in root.findall(f"enrolle"):
    print(enrolle.tag)
print(list({elem.findtext('name') for elem in root.iter() if elem.findtext('name') is not None}))

'''

exam_names = list({elem.tag for elem in root.findall('enrolle/s')})
#exam_names.remove('name')
print(exam_names)