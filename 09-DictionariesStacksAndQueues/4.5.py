paragraph = "cat dog mouse cat rat cat mouse"
word_amounts = {}
words_in = paragraph.split()
for word in words_in:
    if word not in word_amounts:
        word_amounts[word] = 1
    elif word in word_amounts :
        word_amounts[word] += 1

for key, value in word_amounts.items():
    print(key, value)


