class BankAccount:

    def __init__(self, number, holder, balance = 0):
        self.__holder = holder
        self.__number = number
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount
        print(f'Withdraw of €{amount}')

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposit of €{amount}')

    def get_info(self):
        return f'Bankaccount with number {self.__number} belongs to {self.__holder} has a balance of €{self.__balance}.'


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
    acc2 = BankAccount('NL01ABCD0234567777', 'Guido')

    print(acc1.get_info())
    print(acc2.get_info())

    acc1.deposit(1000)
    acc1.withdraw(100)
    acc1.withdraw(22)

    acc2.deposit(10000)
    acc2.withdraw(1090)
    acc2.withdraw(220)

    print(acc1.get_info())
    print(acc2.get_info())
