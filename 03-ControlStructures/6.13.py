###
# Speed checker
#
car_speed = float(input("Enter car speed"))
speed_limit_min = 40
speed_limit_max = 140
if car_speed < 40 :
    print("Warning. Invalid car speed. ")
elif car_speed >= 40 and car_speed <= 140 :
    print("Car speed ok. ")
elif car_speed > 140 :
    print("Warning. Invalid car speed. ")
