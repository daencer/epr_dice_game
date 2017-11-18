"""Docstring
Sixteen-is-Dead Game with fabulous, additional Functions
from EPR-Job No.3
"""
import random
from time import sleep
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

def in_interval(number, start, stop):
    """Docstring
    Checks if a number is in specific interval
    """
    ok = False
    if number >= start and number <= stop:
        ok = True
    return ok

def roll_dice(number = 1, faces = 6, seed = None):
    """Docstring
    Roll Dice
    """
    result = ''
    random.seed(seed)
    for i in range(number):
            result += str(random.randint(1, faces))
            if i + 1 < number:
                result += ','
    return result

def roll_cheating_dice(seed = None):
    """Docstring
    Roll Cheating Dice
    """
    faces = [1, 2, 3, 3, 4, 5, 6]
    random.seed(seed)
    return str(random.choice(faces))

def sum_from_string(s):
    """Docstring
    Sum up from the String
    """
    total = 0
    for i in s.split(','):
        total += int(i)
    return total

def amount_players():
    """Docstring
    Amount of Players
    """
    while True:
        try:
            players = int(input('Geben Sie ihre Spieleranzahl ein: '))
            if players == 'stop':
                quit()
            break
        except(ValueError, IndexError):
            print('Try again must be a number!')
    return players

def name_players():
    """Docstring
    Name the players
    """
    member = []

    counter_player = amount_players()
    count = 1
    while count <= counter_player:
        player_name = input('Name von Spieler ' + str(count) + ' eingeben: ')
        member.append(player_name)
        count += 1
        #print(member)
    return member

def help_screen():
    """Docstring
    Helpscreen / Manfile
    """
    print("~~~~~~~~~~~~~~~~~~~")
    print("Eingaben:")
    print("")
    print(" Next Player:  'n'")
    print(" Roll again:   'Enter'")
    print(" Quit:         'q'")
    print("~~~~~~~~~~~~~~~~~~~")

def team_blue(x):
    """Docstring
    Credits aka Team_blue
    """
    if x == 1:
        print("Credits")
    else:
        print("############################")
        print("# Authors are:             #")
        print("#                          #")
        print("#      Markus Kalusche     #")
        print("#           and            #")
        print("#       Tobias Denzer      #")
        print("#                          #")
        print("############################")
        print("\n")

def sixteen_is_dead(players, members):
    """Docstring
    Game procedure
    """
    loser = []
    lowest_result = 0
    hit_sixteen = False
    continue_game = True
    # pass through every player
    print("\n")
    help_screen()
    for i in range(players):
        if continue_game:
            total = 0
            last_turn = False
            print("\n")
            print(members[i] + " ist am Zug!")
            # roll the dice(s) without end
            while True:
                    cin = input('Make your choice:')
                    if cin == 'n':
                        # stop if player don't want anymore
                        break
                    if cin == 'q':
                        continue_game = False
                        break
                    if cin == "":
                        result = sum_from_string(roll_dice())
                        total += result
                        print('Gewuerfelt:', result)
                        print('Summiert:  ', total)
                    else:
                        help_screen()

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
                        loser = [members[i]]
                        hit_sixteen = True
                    # stop if player hit sixteen or his last turn
                    if hit_sixteen or last_turn:
                        break

            # assume that player one has the lowest result
            if i == 0:
                lowest_result = total
            # add new loser to others
            if total == lowest_result:
                loser.append(members[i])
            # define new loser
            if total < lowest_result:
                loser = [members[i]]
                lowest_result = total
            #print('schlechteste aktuell:', loser, 'mit', lowest_result)
            if hit_sixteen:
                break
        else:
            print('Das Spiel wurde waehrend des Ablaufs per Hand beendet.')
            break
    if hit_sixteen:
        print('Die 16 wurde getroffen.')
        print("LOOSER!!")
    else:
        print("\n")
        print('Verlierer ist/sind')
        for i in loser:
            print(i)
        print('mit nur', lowest_result, 'Summenpunkten')

def main():
    """Docstring
    Main Game Frame
    """
    print("########################################")
    print("# [1] Play the Dice Game               #")
    print("# [2] Credits                          #")
    print("#                                      #")
    print("# What is the correct answer?....      #")
    print("########################################")

    while True:
        try:
            cin = int(input("Choose wisely: "))

            print( "\n")
            if cin == 1:
                member_list = name_players()
                sixteen_is_dead(len(member_list), member_list)

            if cin == 2:
                team_blue(2)
            main()
            break
        except(IndexError, ValueError):
            print("Only numbers!")

main()
