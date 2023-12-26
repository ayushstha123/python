#Rock paper sissors
import sys
import random
from enum import Enum
 

class RPS(Enum):
    ROCK = 1
    PAPPER=2
    SCISSORS=3

print(RPS(2))
print("")
playerChoice=input("Enter....\n 1 for Rock \n 2 for Paper \n 3 for Sissors: \n\n")
computerChoice=random.choice("123")
computer=int(computerChoice)

player=int(playerChoice)

if player < 1 or player > 3 :
    sys.exit("you must enter 1,2,3")
print("")

if player == 1 and computer ==3:
    print("you win! 👦")
elif player== 2 and computer==1:
    print("You win 👦!")
elif player == 3 and computer==2:
    print("You win! 👦")
elif player== computer:
    print("🥴 Its a tie!")
else:
    print("🐍 Python wins")
print("you choose" + str(RPS(player)).replace('RPS.',' ') + ".")
print("Python choose"+ str(RPS(computer)).replace('RPS.',' ') + ".")

