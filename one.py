import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

print("")

playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
)

player = int(playerchoice)

if player <1 or player >3:
    sys.exit("You must enter 1, 2 or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")

print("You chose " +str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " +str(RPS(computer)).replace('RPS.', '') + ".")

print("")

if player ==1 and computer ==3:
    print("🎉You Win!")
elif player == 2 and computer ==1:
    print("🎉You Win!")
elif player == 3 and computer ==2:
    print("🎉You Win!")
elif player == computer:
    print("😯Tie game!")
else:
    print("🐉Python wins!")

'''
    
Enter...
1 for Rock,
2 for Paper, or
3 for Scissors:

2

You chose Paper.
Python chose Paper.

😯Tie game!

    '''


