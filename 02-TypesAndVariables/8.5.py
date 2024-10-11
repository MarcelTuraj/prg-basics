###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km (liters) : '))
total_fuel_consumption = distance * (fuel_consumption / 100)
total_cost = fuel_price * total_fuel_consumption
print(f'For {distance} km, with fuel cost {fuel_price} PLN per liter and consumption {fuel_consumption} per 100 km, total cost is {total_cost} PLN. Total fuel consumption is {total_fuel_consumption} liters. ')
