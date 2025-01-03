def f(player1,player2):
    def counter(expression):
        symbols = ["A", "K", "J", "Q", "T"]

        counter = 0
        for char in expression :
            if char in symbols:
                counter += 10
            else :
                counter += int(char)
        return counter
    return counter(player1) >= counter(player2)
    

print(f("AJ972","AQT72"))
print(f("9532","K8"))
            