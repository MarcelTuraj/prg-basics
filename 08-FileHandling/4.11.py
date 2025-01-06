import csv
with open("powers.csv", "w") as file:
    slots = ['number', 'second_power', 'third_power']
    writer = csv.DictWriter(file, fieldnames=slots)
    for i in range(1,101):
        writer.writerow({'number':i,'second_power':i**2,'third_power':i**3})


