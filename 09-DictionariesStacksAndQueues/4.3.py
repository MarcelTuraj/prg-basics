translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input("Enter english word: ")
if word not in translations:
    print("No such word in database")
else:
    print(translations[word])