###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    arrfile = file.readlines()
    for i in range(0, len(arrfile)) :
        print(f"{i+1}, {arrfile[i]}", end= "")
    