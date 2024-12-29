class Account:
    def __init__(self, acc_no):
        self.acc_no = acc_no
        self.account_balance = 0
    def depo(self, depo_value):
        self.account_balance += depo_value
    def withdrawal(self, with_value):
        if with_value <= self.account_balance:
            self.account_balance -= with_value
        else :
            print("No funds. ")
    def show_status(self):
        print(f"balance : {self.account_balance}")
        print(f"account number: {self.acc_no}")

    
        