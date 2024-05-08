from bank_account import *

Dave=BankAccount(1000,"Dave")
Ayush=BankAccount(2000,"Ayush")

Dave.getBalance()
Ayush.getBalance()

Dave.deposit(2000)

Dave.withdraw(3000)
Dave.withdraw(3000)

Ayush.transfer(1000, Dave)
Dave.getBalance()

Jim=InterestRewardsAccount(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)
Jim.getBalance()

Blaze=SavingsAccount(1000,"Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(100,Ayush)
Blaze.withdraw(100)