import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3

playagain=True

while playagain:
    print("")
    playerchoice=input("Enter .....\n 1 for Rock \n 2 for Paper \n 3 for Scissors\n\n")

    # player choice string ma huncha so you should make it into integer
    player=int(playerchoice)
    if player<1 or player>3:
        sys.exit("the choice should be 1,2,3")

    computerchoice = random.choice("123")
    computer=int(computerchoice)

    print("you choose "+ str(RPS(player)).replace("RPS.","") + ".")
    print("computer choose "+ str(RPS(computer)).replace("RPS.","") +".")
    print("")

    if player==1 and computer==3:
        print("🥴you win")
    elif player==2 and computer==1:
        print("🥴you win")
    elif player==3 and computer==2:
        print("🥴you win")
    elif player==computer:
        print("👔 its a tie")
    else:
        print("Python wins the game!!")
        print("")

    playagain=input("\n\n To play again press Y for yes and N for no")
    if playagain.lower() =='y':
        continue
    else:
        print("Bye!")
        playagain=False


