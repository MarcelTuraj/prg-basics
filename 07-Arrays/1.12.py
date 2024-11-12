categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive = max(expenses)
category = categories[expenses.index(max(expenses))]
print(most_expensive)
print(category)