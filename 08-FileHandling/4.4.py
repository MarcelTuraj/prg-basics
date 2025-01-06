def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('it_company.csv')
file_lines = file_content.splitlines()





counter = 0
while counter < len(file_lines):
   user_input = input("Enter key if continue: ")
   if user_input == "" and counter + 5 < len(file_lines):
      for i in range(counter,counter+5):
         print(file_lines[i])
   counter = counter + 5
   


    
    
   
   

   

   
   
   