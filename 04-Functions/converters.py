def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_i(n):
    return n*0.393701

def fi_to_cm(f, i):
    f = f*30.48
    i = i*2.54
    result = f"{f+i}"
    return result


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"5'6 in feet and inches is {fi_to_cm(5, 6)} cm. ")
    print(f"167 cm is {cm_to_i(167)} in inches")
