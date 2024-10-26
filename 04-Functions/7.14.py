### people detector
def detector(enter) :
    counter = 0
    
    for  i in enter :
        if i == "+" :
            counter += 1
        elif i == "-":
            counter -= 1
        if counter == 3 :
            break
    if counter == 3 :
        return True
    else :
        return False

    

enter = "+-++-++-+---"
print(f"{detector(enter)}")


