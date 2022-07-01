import json

sources = []
groups = []

json1 = input("Coleccion base: ")
json2 = input("Coleccion a añadir: ")

with open(json1) as file:
    data = json.load(file)
    for source in data['sources']:
        sources.append(source)
    for group in data['groups']:
        groups.append(group)

with open(json2) as file:
    data2 = json.load(file)
    for source in data2['sources']:
        sources.append(source)
    for group in data2['groups']:
        groups.append(group)


with open(json1, 'w') as file:
    data['sources'] = sources
    data['groups'] = groups
    json.dump(data, file)




