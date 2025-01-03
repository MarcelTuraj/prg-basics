import re
def f(array):
    pattern = r"^[a-z0-9_]{4,12}$"
    counter = 0 
    for word in array:
        if re.match(pattern, word):
            counter += 1
    return counter

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
