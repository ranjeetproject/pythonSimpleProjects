
class BankAccount:

    # class attribute
    balance = 0
    previousTransaction = 0
    customerName = ''
    customerId = ''

    # Instance attribute
    def __init__(self, cname, cid):
        self.customerName = cname
        self.customerId = cid

    def deposit(self, amount):
        if amount != 0:
            self.balance = self.balance + amount
            self.previousTransaction = amount

    def withdraw(self, amount):
        if amount != 0:
            self.balance = self.balance - amount
            self.previousTransaction = -amount

    def getPreviousTransaction(self):

        if self.previousTransaction > 0:
            print(f"Deposit: {self.previousTransaction}.")
        elif self.previousTransaction < 0:
            print(f"Withdraw: {abs(self.previousTransaction)}.")
        else:
            print(f"No Transaction Occured")

    def showMenu(self):

        self.option = ''

        print(f"Welcome {self.customerName}")
        print(f"Your ID is {self.customerId}")
        print(f"A. Check Balance")
        print(f"B. Deposit")
        print(f"C. Withdraw")
        print(f"D. Previous Transaction")
        print(f"E. Exit")
        while self.option != 'E':
            print(f"===============================")
            self.option = input(f"Enter an option")
            print(f"===============================")
            print(f"You Select {self.option}")

            if self.option == 'A':
                print(f"----------------------")
                print(f"Balance {self.balance}")
                print(f"----------------------")

            if self.option == 'B':
                print(f"----------------------")
                self.dep = int(input(f"Enter a Amount to Deposit"))
                print(f"----------------------")
                self.deposit(self.dep)

            if self.option == 'C':
                print(f"----------------------")
                self.with_dr = int(input(f"Enter a Withdraw Amount"))
                print(f"----------------------")
                self.withdraw(self.with_dr)

            if self.option == 'D':
                print(f"----------------------")
                self.getPreviousTransaction()
                print(f"----------------------")

        if self.option == 'E':
            print(f"*****************************")
            print(f"Thanku you for useing our service")


# Driver code
# Object instantiation
bankAcccount = BankAccount("Rodger", "#BFX234")
# Accessing class methods
bankAcccount.showMenu()
