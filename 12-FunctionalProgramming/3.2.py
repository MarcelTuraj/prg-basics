stri = "I completely agree with you"
sets = stri.split()
len_words = list(map(lambda x:(len(x)), sets))
print(len_words)