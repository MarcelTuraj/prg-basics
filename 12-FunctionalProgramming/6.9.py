measure = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
filtered_measurement = list(filter(lambda x:x>0, measure.values()))

for key, value in measure.items():
        if value in filtered_measurement:
                print(key)

