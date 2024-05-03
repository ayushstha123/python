import random
import sys
from enum import Enum


def rps():
    game_count=0
    player_wins=0
    python_wins=0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK=1
            PAPER=2
            SCISSOR=3

        print("")
        playerchoice=input("Enter .....\n 1 for Rock \n 2 for Paper \n 3 for Scissors\n\n")
        if(playerchoice not in ["1","2","3"]):
            print("the choice should be 1,2,3")
            return play_rps()
        # player choice string ma huncha so you should make it into integer
        player=int(playerchoice)

        computerchoice = random.choice("123")
        computer=int(computerchoice)

        print("you choose "+ str(RPS(player)).replace("RPS.","") + ".")
        print("computer choose "+ str(RPS(computer)).replace("RPS.","") +".")
        print("")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins

            if player==1 and computer==3:
                player_wins +=1
                return "🥴you win"
            elif player==2 and computer==1:
                player_wins +=1
                return "🥴you win"
            elif player==3 and computer==2:
                player_wins +=1
                return "🥴you win"
            elif player==computer:
                 return "👔 its a tie"
            else:
                python_wins+=1
                print("Python wins the game!!")
            print("")
        game_result=decide_winner(player,computer)
        print(game_result)

        nonlocal game_count
        game_count+=1

        print("\n Game Count: " +str(game_count))
        print("\n player wins: " +str(player_wins))
        print("\n python wins: " +str(python_wins))
        

        print("Play again?")

        while(True):
            playagain=input("\n\n To play again press Y for yes and N for no")
            if playagain.lower() not in ["y","q"]:
                return play_rps()
            else:
                break
        if playagain.lower() =='y':
            return play_rps()
        else:
            print("BBye")
            sys.exit("BYE BRO")
    return play_rps()

rps()


