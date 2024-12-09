import csv
with open("vehicle.txt" , "r") as file:
    records = file.readlines()
province_dictionary = {}
with open("province.csv", mode="r", encoding="utf-8") as file :
    province = csv.DictReader(file)
    for row in province:
        key = row["Letter"]
        value = row["Name"]
    
        province_dictionary[key] = value



occurances = {}
for item in records:
    if item[0] not in occurances:
        occurances[item[0]] = 1
    elif item[0] in occurances :
        occurances[item[0]] += 1

names_and_occurances = {}

for key, value in province_dictionary.items():
    names_and_occurances[value] = occurances[key]

for key, value in names_and_occurances.items():
    print(key, value)


