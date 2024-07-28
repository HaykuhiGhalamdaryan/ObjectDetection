class BankAccount:
    
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(f'Deposit: +${amount}')

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(f'Withdraw: -${amount}')
        else:
            raise Exception('No money') 
        
    def transfer(self, other_account, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            other_account.__balance += amount
            self.transactions.append(f'Transfer to {other_account.__account_number} -${amount}')    
            other_account.transactions.append(f'Transfer from {self.__account_number} +${amount}')
        else:
            raise Exception('No money') 
            
    def generate_statement(self):
        return self.transactions
    
    def get_balance(self):
        return self.__balance
    
    def clear_transactions(self):
        self.transactions.clear()
        
user1 = BankAccount('1315 5454 6487 3164',5000)
user2 = BankAccount('6477 1364 4641 3154',2000)
user1.deposit(1000)
user1.withdraw(2000)
user1.transfer(user2, 500)
print(user1.get_balance())
print(user1.generate_statement())
print(user2.get_balance())
print(user2.generate_statement())