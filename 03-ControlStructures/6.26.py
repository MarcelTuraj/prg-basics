###
# PIN
# 
pin = "0805"
user = str(input("Enter PIN: "))
user1 = 0 
user2 = 0 
if user == pin : 
    print("PIN correct. ")
else : 
    user1 = str(input("Enter PIN 2 attempts remaining: "))
    if user1 == pin : 
        print("PIN correct. ")
    else : user2 = str(input("Enter PIN 1 attempt remaining: "))
    if user2 == pin :
               print("PIN correct. ")
    else :
                print("Sorry, your payment card has been blocked.")



    