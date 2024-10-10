###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print('Title in capital letters: ', movie.upper())

# display title in small letters
print('Title in lowercase letters: ', movie.lower())
# display how many times the vowel "e" appears in the title
print('Number of occurances of the letter "e" in title: ', movie.count("e"))

# display where in the text is the word "Lord"
print("The position of the 'Lord' word: ", movie.find("Lord"))

# display where in the text is the word "dragon"
print("The position of the word Dragon: ", movie.find("dragon"))