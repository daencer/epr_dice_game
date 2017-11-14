"""Docstring: A very short sentence explaining the function. < 79 characters.

additional informaion if required
and more infos

"""

import random


from time import sleep
# from numpy import array  #  an aother example
# from meinmodul import test  #  example for your own module

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

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
        player_name = input("Name von Spieler " + str(count) + " eingeben: ")
        member.append(player_name)
        count += 1
        #print(member)
    return member

# Function: Game
def sixteen_is_dead(players):
    loser = []
    lowest_result = 0
    hit_sixteen = False

    # pass through every player
    for i in range(players):
        total = 0
        print("\n")
        print(member_list[i], "ist am Zug!")
        # roll the dice(s) without end
        while True:
            cin = input("Würfeln 'Enter', Aufhören 'n'")
            if cin == 'n':
                # stop if player don't want anymore
                break
            else:
                result = int(roll_dice()) #Function to sum up the String is missing !!!
                total += result
                print('Gewuerfelt:', result, 'Summiert:', total)
                # if player reaches the total of 9
                if total == 9:
                    sleep(3)
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
        console = int(input("Choose wisely: "))
        print( "\n")
        if console == 1:
            #name_players() starts the amount_players() and the return of name_players() is safed in member_list
            member_list = name_players()
            count = 0
            score = []
            dice_eyes = []
            sixteen_is_dead(len(member_list))

 #           while count <= len(member_list) - 1:
  #              try:
   #                 print("\n")
    #                print(member_list[count],"ist am Zug!")
     #               user_input = input("Würfeln 'Enter', Aufhören 'n': ")
      #              sleep(3)
       #             if user_input == "":
        #                x = roll_dice()
         #               score.append(int(x))
          #              z = sum(score)
           #             print("Gewürfelt:   " + x )
            #            print("Insgesamt:   " + str(z))
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
            #    except(IndexError, ValueError):
             #       print("Only 'Enter' or 'n'")
#BIS HIER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

        elif console == 2:
            print("Settings")
        elif console == 3:
            print("Credits")
        elif console == 42:
            print("cheat Menu")
        break
    except(IndexError, ValueError):
        print("Only numbers!")