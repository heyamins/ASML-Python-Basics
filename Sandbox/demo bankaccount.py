

class BankAccount:

    __slots__ = ('_number', '_holder', '_balance')
    
    def __init__(self, number, holder, balance = 0):
        self._number = number
        self._holder = holder
        self._balance = balance

    def __repr__(self):
        return f"BankAccount('{self._number}', '{self._holder}', {self._balance})"

    def __str__(self):
        return f"BankAccount nr. {self._number} of {self._holder} has a balance of € {self._balance}"

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


class SavingsAccount(BankAccount):

    __slots__ = ('_interest',)

    def __init__(self, number, holder, balance = 0, interest = 0):
        super().__init__(number, holder, balance)
        self._interest = interest
    
    def __repr__(self):
        return f"Savings Account('{self._number}', '{self._holder}', {self._balance})"

    def __str__(self):
        return f"Savings Account nr. {self._number} of {self._holder} has a balance of € {self._balance}"

    def cash_interest(self):
        self._balance += self._balance * self._interest / 100


        

if __name__ == '__main__':

    acc1 = BankAccount('NL12ACBD0987678987', 'PC Anema')
    print(acc1)

    acc1.deposit(1000)
    acc1.withdraw(25)
    acc1.withdraw(31.50)

    print(acc1)
    
    acc2 = SavingsAccount('NL12ACBD098761312', 'Peter Anema', interest = 2)
    print(acc2)

    acc2.deposit(1000)
    acc2.cash_interest()
    acc2.deposit(1000)
    acc2.cash_interest()
    acc2.deposit(1000)
    acc2.cash_interest()

    print(acc2)
    
