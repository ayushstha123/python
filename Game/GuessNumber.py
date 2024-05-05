
import sys
import random
from enum import Enum

def GN(name="PlayerOne"):
    gamecount=0
    player_wins=0
    python_wins=0
    def playGN():
        class GN(Enum):
            One=1
            Two=2
            Three=3
            nonlocal player_wins
            nonlocal python_wins

        playerChoice=input("Enter a Number Ranging from (1,2 or 3)?")

        if(playerChoice not in ["1","2","3"]):
            print("The input should be 1,2, or 3 \n")
            playGN()
            
        player=int(playerChoice)
        computer=random.choice("123")
        computer=int(computer)
        print(f"you choose {player}")
        print(f"Python choose {computer}")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player==computer:
                print("Python wins")
                python_wins+=1
            else :
                print("Player wins")
                player_wins+=1

        gameResult=decide_winner(player,computer)
        print(gameResult)
        print(f"your score: {player_wins}")
        print(f"python's score: {python_wins}")
        nonlocal gamecount
        gamecount+=1

        print("\n Game Count: " +str(gamecount))

        while(True):
            playagain=input("Do you wanna play again?\n press Y to continue and N to quit")
            if(playagain.lower() not in ['y','n']):
                playGN()
            else:
                break
        if playagain.lower() =='y':
            playGN()
        else:
            sys.exit()
    playGN()


if "__name__"=="__main__":
    import argparse

    parse=argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )
    parse.add_argument(
        "-n","--name",metavar="name"
        required=True,help="The name of the person playing the game"
    )
    args=parse.parse_args()

guess_number=GN(args.name)
guess_number()

