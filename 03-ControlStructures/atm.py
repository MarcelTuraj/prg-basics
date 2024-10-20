###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Change PIN")

    choice = input("Choose an option (1-4): ")
    print()

    if choice == '1':
        is_pin = str(input("Enter your PIN: "))
        if is_pin == pin  :
          print(f"Your current balance is: €{balance}")
        else :
            print("Wrong PIN")
            break
    elif choice == '2':
        is_pin = str(input("Enter your PIN: "))
        if is_pin == pin :
          amount = float(input("Enter the amount to deposit: "))
          balance += amount
          print(f"€{amount} has been deposited. New balance: €{balance}")
        else :
            print("Wrong PIN")
            break
    elif choice == '3':
        is_pin = str(input("Enter your PIN: "))
        if is_pin == pin :
          amount = float(input("Enter the amount to withdraw: "))
          if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
          else:
            print("Insufficient balance.")
        else :
           print("Wrong PIN")
           break
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == "5" :
        is_pin = str(input("Enter your current PIN: "))
        if is_pin == pin :
           newpin = str(input("Enter your new PIN (4 digits) : "))
           if newpin.isdigit() == True :
               pin = newpin
               print("PIN changed successfully")
               continue
           else :
              print("It has to be digits only. ")
              break
                  
    else:
        print("Invalid option. Please try again.")
