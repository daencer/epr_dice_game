"""Docstring: A very short sentence explaining the function. < 79 characters.

additional informaion if required
and more infos

"""

import random, time

# from numpy import array  #  an aother example
# from meinmodul import test  #  example for your own module

__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
i.e. an other student for his code"
__email__ = "s1539940@stud.uni-frankfurt.de"

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
    loser = []
    lowest_result = 0
    hit_sixteen = False

    # pass through every player
    for i in range(players):
        total = 0
        print('Spieler', i)
        # roll the dice(s) without end
        while True:
            cin = input('Um zu wuerfeln, druecke ENTER... ')
            if cin == 'n':
                # stop if player don't want anymore
                break
            else:
                result = int(roll_dice()) #Function to sum up the String is missing !!!
                total += result
                print('Gewuerfelt:', result, 'Summiert:', total)
                # if player reaches the total of 9
                if total == 9:
                    time.sleep(3)
                    result = int(roll_dice())  # Function to sum up the String is missing !!!
                    total += result
                    break
                # stop if player reaches the total of 16 or higher
                if total >= 16:
                    hit_sixteen = True
                    loser = [i]
                    break
        # assume that player one has the lowest result
        if i == 0:
            lowest_result = total
        # add new loser to others
        if total == lowest_result:
            loser.append(i)
        # define new loser
        if total < lowest_result:
            loser = [i]
            lowest_result = total
        print('schlechteste aktuell:', loser, 'mit', lowest_result)
        if hit_sixteen:
            break
    if hit_sixteen:
        print('Die 16 wurde getroffen')
    else:
        print('Verlierer ist/sind', loser, 'mit nur', lowest_result)

sixteen_is_dead(9)