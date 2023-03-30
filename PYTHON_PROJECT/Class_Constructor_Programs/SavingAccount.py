class Account:

    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.balance = balance
        print(f"account created successfully {self.name}")

    def showBalance(self):
        print(f"Account Holder: {self.name} Balance: {self.balance}")

    def depositeAmount(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is deposited successfully")
            print(f"Your Total Balance is {self.balance}")
        else:
            print("Amount should be greater than zero ")

    def withdrawAmount(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn successfully")
            print(f"Your Total Balance is {self.balance}")
        else:
            print("Insufficient Balance ")
            print(self.balance)


p1 = Account("Sheela", "Bangalore", 15000)
p1.showBalance()
p1.depositeAmount(-32)
p1.depositeAmount(500)
p1.withdrawAmount(20000)
p1.withdrawAmount(1500)


class Canara(Account):  # Single level inheritance

    def showBalance(self):  # Method overriding
        print(f"Account Holder: {self.name} Balance: {self.balance} Address{self.address}")


p3 = Canara("managa", "Delhi", 5000)


class Hdfc(Canara):  # Multilevel inheritance
    pass


p4 = Hdfc("Dinga", "Mumbai", 1000)


class Icici(Account):  # Hyrical Inheritance
    pass


p5 = Icici("Dingi", "Bhubaneswar", 3000)


class Sbi(Account, Canara, Hdfc):  # Multiple inheritance
    pass
