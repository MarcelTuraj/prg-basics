countries = [
{"name":"Poland" ,"population":38000000},
{"name" : "India", "population": 1450000000},
{"name" : "United States" ,"population": 345000000},
{"name" : "Russia", "population": 144000000},
{"name" : "Ethiopia" ,"population": 132000000}
]

for item in countries:
    for key, value in item.items():
        print(key, value)