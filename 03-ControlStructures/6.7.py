###
# Age checker
#
age = int(input("Enter age: "))
if age >= 0 and age < 13 :
    print("Child")
elif age >= 13 and age <= 19 :
    print("Teen")
elif age > 19 and age < 65 :
    print("Adult")
elif age >= 65 :
    print("Senior")
