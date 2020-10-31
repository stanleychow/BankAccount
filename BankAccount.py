class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print('Amount Deposited:  $'+'{:.2f}'.format(amount))

    
   
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance -= overdraft_fee
        else:
            self.balance -= amount
            print('Amount Withdrawn:  $'+'{:.2f}'.format(amount))
        pass
   
    def get_balance(self):
        print('Your balance is: $'+'{:.2f}'.format(self.balance))
        return self.balance
        pass
   
    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance += interest
        pass

   
    def print_receipt(self):
        print(self.full_name)
        print("Account No.: ****" + self.account_number[-4:])
        print("Routing No.: " + self.routing_number)
        print('Balance:  $'+'{:.2f}'.format(self.balance))
        pass


stanleyAccount = BankAccount('Stanley Chow','83057123', 'A1B1', 5)
johnAccount = BankAccount('John Doe', '13491124', 'A1B2', 10)
bobAccount = BankAccount('Bob Johnson', '12345678', 'B5O1', 100)

stanleyAccount.deposit(1000)
stanleyAccount.withdraw(3)
stanleyAccount.get_balance()
stanleyAccount.add_interest()
stanleyAccount.print_receipt()

print("----------------")

johnAccount.deposit(10)
johnAccount.withdraw(1)
johnAccount.get_balance()
johnAccount.add_interest()
johnAccount.print_receipt()

print("----------------")

bobAccount.deposit(50)
bobAccount.withdraw(1000)
bobAccount.get_balance()
bobAccount.add_interest()
bobAccount.print_receipt()









