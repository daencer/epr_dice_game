"""Docstring: A very short sentence explaining the function. < 79 characters.

additional informaion if required
and more infos

"""

import random
from time import sleep
# from numpy import array  #  an aother example
# from meinmodul import test  #  example for your own module

__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
i.e. an other student for his code"
__email__ = "s1539940@stud.uni-frankfurt.de"
# Here are all lists defined:
list_amount_players = []

# Function: Checks if a number is in specific interval
def in_interval(number, start, stop):
    ok = False
    if number >= start and number <= stop:
        ok = True
    return ok

# Function: Roll Dice
def roll_dice(number = 1, faces = 6, seed = None):
    result = ''
    random.seed(seed)
    for i in range(number):
            result += str(random.randint(1, faces))
            if i + 1 < number:
                result += ','
    return result

# Function: Roll Cheating Dice
def roll_cheating_dice(seed = None):
    faces = [1, 2, 3, 3, 4, 5, 6]
    random.seed(seed)
    return str(random.choice(faces))

# Function: Game
def sixteen_is_dead(players):
    print(None)


# Function: amount of Players
def amount_players():
    while True:
        try:
            players = int(input("Geben Sie ihre Spieleranzahl ein: "))
            if players == 'stop':
                quit()
            break
        except(ValueError, IndexError):
            print("Try again must be a number!")
    return players

# Function: Name the players
def name_players():
    member = []

    counter_player = amount_players()
    count = 1
    while count <= counter_player:
        player_name = input("Name eingeben: ")
        member.append(player_name)
        count += 1
        print(member)


# ~~~~~~~~~~~~~~~~ Main Game Frame ~~~~~~~~~~~~~~~~~~~~~

print("########################################")
print("# [1] Play the Dice Game               #")
print("# [2] Settings                         #")
print("# [3] Credits                          #")
print("#                                      #")
print("# What is the correct answer?....      #")
print("########################################")


while True:
    try:
        console_input = int(input("Choose wisely: "))
        if console_input == 1:
            print("Lets start the Game!")
            amount_players()
            name_players()
        break
    except(ValueError, IndexError):
        print("Try again must be a number!")

count = 1
while count >= name_players():

    state = True
    score = []
    while state == True:
        try:
            print("'Enter' to toss the dice!")
            print("'n' to pass this round!")
            console_input = input(">_ ")
            if console_input == "":
                dice_points = roll_dice()
                score.append(int(dice_points))
                print("Your dice:")
                print(sum(score))
            elif console_input == "n":
                print("Your Score was: ", sum(score))
                break
        except(IndexError, ValueError,):
            print("ERROR!!1!11!")



MARKUS