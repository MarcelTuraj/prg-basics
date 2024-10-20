###
# Parking fee calculator
#
time = float(input("Enter parking time in hours: "))
if time < 1 :
    print("Parking free!")
elif time >= 1 and time >= 2 :
    print("Parking fee: 5 PLN. ")
elif time > 2 and time <= 6 :
    print("Parking fee: 15 PLN. ")
elif time > 6 :
    print("Parking fee: 20 PLN. ")