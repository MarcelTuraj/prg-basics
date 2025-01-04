def f(x,y,d):
    string1 = ""
    for i in range(x,y+1):
        string1 += f"{str(i)}"
    if f"{d}" in string1:
        return True
    return False

print(f(205,210,"04"))

