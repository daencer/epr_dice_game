"""Docstring: Sixteen-is-Dead Game with fabulous, additional Functions
"""
import random
from time import sleep
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "nobody"
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

# Function: Sum up from String
def sum_from_string(s):
    total = 0
    for i in s.split(','):
        total += int(i)
    return total

# Function: Game
def sixteen_is_dead(players):
    loser = []
    lowest_result = 0
    hit_sixteen = False
    continue_game = True
    # pass through every player
    for i in range(players):
        if continue_game:
            total = 0
            last_turn = False
            print('Spieler', i)
            # roll the dice(s) without end
            while True:
                cin = input('Um zu wuerfeln, druecke ENTER... ')
                if cin == 'n':
                    # stop if player don't want anymore
                    break
                if cin == 'q':
                    continue_game = False
                    break
                result = sum_from_string(roll_dice())
                total += result
                print('Gewuerfelt:', result, 'Summiert:', total)
                # if player reaches the total of 9
                if total == 9:
                    print('9 erreicht. Du darfst nicht mehr würfeln.')
                    last_turn = True
                # if player reaches the total of 10
                if total == 10:
                    print('10 erreicht. Letztes Mal wuerfeln...')
                    sleep(3)
                    result = sum_from_string(roll_dice())
                    total += result
                    print('Gewuerfelt:', result, 'Summiert:', total)
                    last_turn = True
                # player reaches the total of 16 or higher
                if total >= 16:
                    loser = [i]
                    hit_sixteen = True
                # stop if player hit sixteen or his last turn
                if hit_sixteen or last_turn:
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
            #print('schlechteste aktuell:', loser, 'mit', lowest_result)
            if hit_sixteen:
                break
        else:
            print('Das Spiel wurde waehrend des Ablaufs per Hand beendet.')
            break
    if hit_sixteen:
        print('Die 16 wurde getroffen.')
    else:
        print('Verlierer ist/sind', loser, 'mit nur', lowest_result)

sixteen_is_dead(9)