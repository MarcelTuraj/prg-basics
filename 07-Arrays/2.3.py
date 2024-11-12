# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food_expenses = 0
for row in monthly_expenses:
    food_expenses += row[0]



transport_exp = 0
for rows in monthly_expenses:
    transport_exp += rows[1]

utility_exp = 0
for rowss in monthly_expenses:
    utility_exp += rowss[2]

week1 = 0
row_index = 0
for item in monthly_expenses[row_index]:
    week1 += item


week2 = 0
row_index = 1
for item in monthly_expenses[row_index]:
    week2 += item


week3 = 0
row_index = 2
for item in monthly_expenses[row_index]:
    week3 += item


week4 = 0
row_index = 3
for item in monthly_expenses[row_index]:
    week4 += item

total = 0
for row in monthly_expenses :
    for item in row:
        total += item


# Calculates expenses
# Use loop statements


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food:', {food_expenses})
print(f'Transport:{transport_exp}')
print(f'Utilities: {utility_exp}')
print(f'Week 1: {week1}')
print(f'Week 2: {week2}')
print(f'Week 3: {week3}')
print(f'Week 4: {week4}')
print('---------------')
print(f'TOTAL: {total}')