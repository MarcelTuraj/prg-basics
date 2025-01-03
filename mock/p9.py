import csv
def f(value):
    file_name = "employees.csv"
    with open(file_name, "r") as file:
        collection = []
        data = csv.DictReader(file)
        counter = 0
        for row in data:
    
           if float(row["Age"]) >= value:
               collection.append(row["Name"])
    return collection
            

print(f(12))
            
