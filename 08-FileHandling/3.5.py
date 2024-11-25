###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = str(input("Enter username: "))
password = str(input("Enter password: "))

# pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^(?=.{8,})([a-zA-Z0-9_]+)$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern, password)


# print results
if password_match and username_match:
   print('both correct')
else:
   print('no')