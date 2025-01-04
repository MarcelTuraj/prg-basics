import re
def f(mnnumbers):
    pattern = r"^[+-]?[A-Da-d1-7]+$"
    counter = 0 
    for item in mnnumbers:
        if re.match(pattern, item):
            counter += 1
    return counter

print(f(["A15","-31","7abC","+D1","-gH"]))
