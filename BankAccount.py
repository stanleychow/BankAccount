import random
class BankAccount:
    '''This class simulates a bank account
    '''
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(100000000,999999999)
        self.routing_number = 123456789
        self.balance = 0
    


    def deposit(self, amount):
        '''Adds 'amount' of money into balance
        '''
        self.balance += amount
        print('Amount Deposited:  $'+'{:.2f}'.format(amount))
    
   
    def withdraw(self, amount):
        '''Subtracts 'amount' of money from balance
        '''
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance -= overdraft_fee
        else:
            self.balance -= amount
            print('Amount Withdrawn:  $'+'{:.2f}'.format(amount))
        
   
    def get_balance(self):
        '''Returns balance
        '''
        print('Your balance is: $'+'{:.2f}'.format(self.balance))
        return self.balance
        
   
    def add_interest(self):
        '''Calculates the interest and adds it to balance
        '''
        interest = self.balance *  0.00083
        self.balance += interest
        

   
    def print_receipt(self):
        '''Prints recept
        '''
        print(self.full_name)
        print("Account No.: ****" + str(self.account_number)[-4:])
        print("Routing No.: " + str(self.routing_number))
        print('Balance:  $'+'{:.2f}'.format(self.balance))
        


stanleyAccount = BankAccount('Stanley Chow')
johnAccount = BankAccount('John Doe')
bobAccount = BankAccount('Bob Johnson')

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









