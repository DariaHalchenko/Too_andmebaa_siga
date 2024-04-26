import json
from tkinter.ttk import Separator
json_data='{"nimi": "Daria Halchenko", "vanus":17, "prillid":true}'
data=json.loads(json_data) 

print(data) 
print(data["nimi"]) 
for id_, dat in enumerate(data):
    print(id_, "-", dat) 

for key, value in data.items():
    print(key, ":", value)

data2={
    "nimi": "Valeria",
    "vanus": 17,
    "abielus": True, 
    "lapsed":("Darja", "Mati"),
    "koduloomad":None,
    "autod":
    [
        {"muudel": "BMW", "varv": "punane", "joud":500, "number": "666MAX"},
        {"muudel": "Audi", "varv": "must", "joud":500, "number": "321ABC"},
        {"muudel": "Ford", "varv": "must", "joud":300, "number": "123ABC"}
        ]
    }
print(json.dumps(data2)) 
print(json.dumps(data2, indent=2,separators=(".","="),sort_keys=True))  

with open ("data_file.json","w") as w_file:
    json.dump(data2,w_file) 

print("Andmed fallist:") 
with open("data_file.json", "r") as r_file:
    data2=json.load(r_file) 

print(data2) 

