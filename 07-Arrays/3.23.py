text = "An apple a day keeps the doctor away"
def function1(text):
    text = text.split()
    return len(text)

def function2(text):
    text = text.split()
    for i in range(0,len(text)):
        for j in range(0,len(text)- i - 1):
            if len(text[j]) < len(text[j+1]) :
                text[j],text[j+1] = text[j+1],text[j]
    return text

def function3(text):
    text = text.split()
    for i in range(0,len(text)):
        for j in range(0,len(text)-i-1):
            if text[j] > text[j+1]:
                text[j], text[j+1] = text[j+1], text[j]
    return text
            

        

print(function3(text))


        