def f(word):
    if len(word) == 1:
        return word.upper()
    else :
        word_arr = []
        for i in range(len(word)):
            word_arr.append(word[:i].lower() + word[i].upper() + word[i+1:].lower())

            

            
    return "-".join(word_arr)

print(f("water"))
