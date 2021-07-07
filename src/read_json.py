import json

with open("data.json", "r") as handle:
    data = json.load(handle)

# print(data)

for i in data:
    print(f"{i['id']}\t{i['sequence']}\t{i['species']}")
