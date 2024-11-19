def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

pettext = read_from_file("pets.txt")
arrpet = pettext.splitlines()
number_of_words = 0
for item in arrpet:
   wordnumber = len(item.split())
   number_of_words += wordnumber
   
print(number_of_words)
