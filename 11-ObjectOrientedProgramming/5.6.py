from Bank import Account
def main():
    new_account = Account("12 3456 5555 9090 1111 0000 7722")
    new_account.show_status()
    new_account.depo(25.30)
    new_account.show_status()
    new_account.withdrawal(31.70)
    new_account.show_status()
    new_account.withdrawal(14)
    new_account.show_status()

if __name__ == "__main__":
    main()