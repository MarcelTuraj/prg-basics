def acro(sent) :
    acro = ""
    text = sent
    bag = text.split()
    for word in bag :
        first_letter = word[0]
        acro += first_letter
    return acro
    
sent = "god save the queen"
print(f"{acro(sent)}")