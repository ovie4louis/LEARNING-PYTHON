import sys
import random
from enum import Enum

def play_rps():


    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter...\n1. Rock\n2. Paper\n3. Scissors\n\n")


    if playerchoice not in ["1", "2", "3"]:
        print("you must enter 1, 2, 0r 3.")
        return play_rps()

    player = int(playerchoice)


    computerchoice = random.choice("123")
    computer = int(computerchoice)

    
    print("\nyou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("🎉you win!")
    elif player == 2 and computer == 1:
        print("🎉you win!")
    elif player == 3 and computer == 2:
        print("🎉you win!")
    elif player == computer:
        print("😲Tie game")
    else:
        print("🐍python wins!")

    print("\nPlay again?")

    while True:
    
     playagain = input(" \nY for Yes or \nQ to quit \n")

     if playagain.lower() not in ["y", "q"]:
         continue
     else:
         break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing")
        sys.exit("Bye 👋")
        

play_rps()
