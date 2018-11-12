import json

mycompounds = [{"name":"fructose","formula":"C6H1206","id":79025,"similarTo":["Hexose","Glucose"]}]
with open("json_file.json","w") as jsonFile:
    json.dump( mycompounds, jsonFile)


with open("json_file.json","r") as jsonFile:
    compounds = json.load(jsonFile)
print("name",compounds[0]["name"])
print("formula",compounds[0]["formula"])