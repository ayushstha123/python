import random
import sys
from enum import Enum


def rps(name="PlayerOne"):
    game_count=0
    player_wins=0
    python_wins=0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK=1
            PAPER=2
            SCISSOR=3

        print("")
        playerchoice=input(f"{name}Enter .....\n 1 for Rock \n 2 for Paper \n 3 for Scissors\n\n")
        if(playerchoice not in ["1","2","3"]):
            print(f"{name} please the choice should be 1,2,3")
            return play_rps()
        # player choice string ma huncha so you should make it into integer
        player=int(playerchoice)

        computerchoice = random.choice("123")
        computer=int(computerchoice)

        print(f"{name} choose {str(RPS(player)).replace('RPS.','')}")
        print(f"computer choose {str(RPS(computer)).replace('RPS.','')}")
        print("")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player==1 and computer==3:
                player_wins +=1
                return f"🥴{name}, win"
            elif player==2 and computer==1:
                player_wins +=1
                return f"🥴{name}, win"
            elif player==3 and computer==2:
                player_wins +=1
                return f"🥴{name}, win"
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

        print(f"\n Game Count: {str(game_count)}")
        print(f"\n {name} wins: {str(player_wins)}")
        print(f"\n python wins: {str(python_wins)}")
        

        print("Play again?")

        while(True):
            playagain=input("\n\n To play again press Y for yes and N for no")
            if playagain.lower() not in ["y","n"]:
                return play_rps()
            else:
                break
        if playagain.lower() =='y':
            return play_rps()
        else:
            print(f"BBye {name}")
            sys.exit("BYE BRO")
    return play_rps()

if __name__ == '__main__':

    import argparse

    parser=argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n","--name" , metavar="name",
        required=True,help="The name of the person to playing the game"
    )

    args=parser.parse_args()

    rock_paper_scissors=rps(args.name)
    rock_paper_scissors()