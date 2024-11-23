names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
names_letter_counters = []
for item in names:
    names_letter_counters.append(len(item))

biggestname = names[names_letter_counters.index(max(names_letter_counters))]
print(biggestname)



