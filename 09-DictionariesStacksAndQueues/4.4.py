
winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

hours = 0
for value in winter_semester.values():
    hours += value

print(f"The total number of hours in the winter semester is {hours}")