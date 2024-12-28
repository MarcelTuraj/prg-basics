import json
with open("reservations.json", "r") as file:
    info = json.load(file)

def number_of_rooms(info): 
    return len(info["reservations"])



def paid_reservations(info) :
    counter = 0
    for item in info["reservations"]:
        if item["paid"] == True :
            counter += 1
    return counter

def unpaid(info) :
    counter = 0
    for item in info["reservations"]:
        if item["paid"] == False :
            counter += 1
    return counter

def paid_value(info):
    total = 0
    for item in info["reservations"]:
        if item["paid"] == True :
            total += item["price_per_night"]*item["nights"]
    return total

def unpaid_value(info):
    total = 0
    for item in info["reservations"]:
        if item["paid"] == False :
            total += item["price_per_night"]*item["nights"]
    return total





print(paid_value(info))
print(unpaid_value(info))