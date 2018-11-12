from xml.dom import minidom

doc = minidom.parse("py_xml.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

foodmenu = doc.getElementsByTagName("food")

for food in foodmenu:
    sid = food.getAttribute("id")
    name = food.getElementsByTagName("name")[0]
    price = food.getElementsByTagName("price")[0]
    calories = food.getElementsByTagName("calories")[0]
    print("id:%s,name of the food:%s,price:%s,calories:%s"
          %(sid,name.firstChild.data,price.firstChild.data,calories.firstChild.data))
