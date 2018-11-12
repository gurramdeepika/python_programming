from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class FoodMenu(ContentHandler):
    def startElement(self, name, attrs):
        if(name == "food"):
            self.name = attrs.get("id")
    def endElement(self, name):
        if(name == "food"):
            print("%-8s " %(self.name))

food = FoodMenu()
saxparser = make_parser()
saxparser.setContentHandler(food)
datasource = open("py_xml.xml","r")
saxparser.parse(datasource)
datasource.close()