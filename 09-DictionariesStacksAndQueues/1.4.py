person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])
for key, value in person.items():
    print(key, value)

person["surname"] = "Nowak"
person["married"] = False
person["Gender"] = "male"
person["hobby"].append("bicycle")
person["phone"] = {"landline":"123444321","mobile":"777888999", "workphone" : "313131444"}