#bank account 
class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\n Account :{self.name} created . \n Balance: Rs{self.balance}")

    def getBalance(self):
        print(f"Account {self.name} \n Balance = Rs{self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposit Completed \n")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >=amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry ,account {self.name} only has a balance of Rs{self.balance:.2f}"
            )
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)    
            self.balance=self.balance-amount
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\n withdraw interrupted : {error}")
    def transfer(self,amount,account):
        try:
            print("\n ********* \n\n Beginning Transfer....🧑‍🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("*******\nTransfer Complete")
        except BalanceException as error:
            print(f"Transfer interrupted . ❌ {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance +(amount*1.05)
        print("\nDeposit complete")
        self.getBalance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("Withdraw Completed !")
            self.getBalance()
        except Exception as error:
            print(f"Withdraw interrupted ❌ :{error}")