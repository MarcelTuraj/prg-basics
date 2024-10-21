###
# printer
#
for i in range(1,31) :
    if i%3 == 0 and i%5 != 0 :
        i = str("THREE")
    elif i%3 != 0 and i%5 == 0 :
        i = str("FIVE")
    elif i%5 == 0 and i%3 == 0 :
        i = str("BINGO")
    print(i)