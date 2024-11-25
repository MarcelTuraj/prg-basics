###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, encoding='utf-8') as file:
    email = file.read()
    



# regular expression pattern
# for amounts
pattern = r'€\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
# calculate the total purchases

amounts = [int(item.replace("€","")) for item in amounts]

suma = 0
for item in amounts:
    suma += item
print(suma)