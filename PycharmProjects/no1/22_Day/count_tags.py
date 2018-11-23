from xml.dom import minidom

doc = minidom.parse('py_xml.xml')

id = doc.getElementsByTagName('food')

print('food items count in a menu: ',len(id))



