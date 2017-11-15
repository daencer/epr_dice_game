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

# Function: amount of Players
def amount_players():
    while True:
        try:
            players = int(input('Geben Sie ihre Spieleranzahl ein: '))
            if players == 'stop':
                quit()
            break
        except(ValueError, IndexError):
            print('Try again must be a number!')
    return players

# Function: Name the players
def name_players():
    member = []

    counter_player = amount_players()
    count = 1
    while count <= counter_player:
        player_name = input('Name von Spieler ' + str(count) + ' eingeben: ')
        member.append(player_name)
        count += 1
        #print(member)
    return member

# Function: Game
def sixteen_is_dead(players, members):
    loser = []
    lowest_result = 0
    hit_sixteen = False
    continue_game = True
    # pass through every player
    for i in range(players):
        if continue_game:
            total = 0
            last_turn = False
            print(members[i])
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
    else:
        print('Verlierer ist/sind')
        for i in loser:
            print(i)
        print('mit nur', lowest_result, 'Summenpunkten')

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
        cin = int(input("Choose wisely: "))
        print( "\n")
        if cin == 1:
            member_list = name_players()
            sixteen_is_dead(len(member_list), member_list)
        """
            while count <= len(member_list) - 1:
                try:
                    print("\n")
                    print(member_list[count],"ist am Zug!")
                    user_input = input("Würfeln 'Enter', Aufhören 'n': ")
                    sleep(3)
                    if user_input == "":
                        x = roll_dice()
                        score.append(int(x))
                        z = sum(score)
                        print("Gewürfelt:   " + x )
                        print("Insgesamt:   " + str(z))
    #AB HIER FUNKTIONIERT NOCH NICHTS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                    elif sum(score) == 10:
 #                       user_input = input("Sie müssen nochmal würfeln!")
  #                  elif user_input == "stop":
   #                     print(z)
    #                    quit()
     #               elif sum(score) >= 16 or z == 9:
      #                  print("Sie haben verloren! try again!")
       #                 break
        #            elif user_input == "n":
         #               count += 1
          #              score.append(sum(score))
           #             score = []
            #        else:
             #           print(player_1, "Ihr Ergebnis lautet: ", z)
              #          if z >= 16 or z == 9:
               #             print("Sie haben verloren")
                #            print(toss_2)
                 #           break
                  #      else:
                   #         print(toss_2)
                    #        break
                except(IndexError, ValueError):
                    print("Only 'Enter' or 'n'")
#BIS HIER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        elif cin == 2:
            print("Settings")
        elif cin == 3:
            print("Credits")
        elif cin == 42:
            print("cheat Menu")"""
        break
    except(IndexError, ValueError):
        print("Only numbers!")