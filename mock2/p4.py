
def f(fnc,prods):
    return ",".join(list(map(fnc, prods)))
prods = ["water","cheese","tomato"]
fnc1 = lambda x:(x[0]+x[-1]).upper()
print(f(fnc1,prods))