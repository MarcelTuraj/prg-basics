###
# Program that simulates the operation of an electronic thermometer.
# 33, 30, 8, 0, -2
temperature = -2
if temperature > 35:
    print(f"It is extermely hot, temp is {temperature}. ")
elif temperature > 30 and temperature <= 35 :
    print(f"It is hot, temp is {temperature}. ")
elif temperature >= 15 and temperature >= 30 :
    print(f"It is warm, temp is {temperature}. ")
elif temperature >= 0 and temperature < 15 :
    print(f"It is cold, temp is {temperature}. ")
else :
    print(f"WARNING! FROSTBIT INCOMING! ")