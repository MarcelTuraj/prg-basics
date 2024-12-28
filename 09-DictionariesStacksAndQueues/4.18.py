import json
with open("dogs.json", "r") as file:
    dawg = json.load(file)
younger_dawg = []
for item in dawg:
    if item['age'] < 5 :
        younger_dawg.append(item)
for item in younger_dawg:
    for key, value in item.items():
        print(key, ':', value)
