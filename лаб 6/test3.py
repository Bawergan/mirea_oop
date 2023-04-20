import xml.etree.ElementTree as ET



tree = ET.parse('лаб 6/1.xml')
root = tree.getroot()

a = list({elem.tag for elem in root.findall('enrolle/*')})
a.remove('name')
print(a)