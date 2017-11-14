from random import randint

# Aufgabe 3.2 a)

# def sixteen_is_dead(players):
print("Spiel beginnt")


def roll_dice():
    randint(1, 6)
    return


roll_dice()


def numb_players():
    while True:
        try:
            players = int(input("Geben Sie ihre Spieleranzahl ein: "))
            if players == 'stop':
                quit()
                # else:
                # players_new = input("Bitte eine Zahl eingeben: ")
            break
        except(ValueError, IndexError):
            print("Try again must be a number!")
    return players


value = numb_players()
print(value)
import random

liste_1 = [1, 2, 3, 4, 5, 6]
list_2 = []
list_3 = []
list_4 = []
scoreboard = []
count = 1
while count <= value:
    player_name = input("Name eingeben: ")
    list_4.append(player_name)
    count += 1
    print(list_4)

index_list = 0
while index_list <= value - 1:
    print(list_4[index_list], " ist am Zug!")
    t_player_1 = input("Weiter würfeln: Enter, Aufhören: n: ")
    if t_player_1 == "":
        x = int(random.choice(liste_1))
        list_2.append(x)
        z = sum(list_2)
        print(x)
        print("Die Summe ihrer Würfe ist: ", z)
    elif z == 10:
        t_player_1 = input("Sie müssen nochmal würfeln!")
    elif t_player_1 == "stop":
        print(z)
        quit()
    elif z >= 16 or z == 9:
        print("Sie haben verloren! try again!")
        break
    elif t_player_1 == "n":
        index_list += 1
        scoreboard.append(sum(list_2))
        list_2 = []
    else:
        print(player_1, "Ihr Ergebnis lautet: ", z)
        if z >= 16 or z == 9:
            print("Sie haben verloren")
            print(toss_2)
            break
        else:
            print(toss_2)
            break
print(list_3)
print(scoreboard)

'''
while True:
    t_player_2 = input("Weiter würfeln: Enter, Aufhören: n: ")
    if t_player_2 == "":
        v = int(random.choice(liste_1))
        list_3.append(v)
        q = sum(list_3)
        print(v)
        print("Die Summe ihrer Würfe ist: ",q)
    elif t_player_1 == "stop":
        print(q)
        quit()
    else:
        print(player_2, "Ihr Ergebnis lautet: ", q)
        if q >= 16 or z == 9:
            print("Sie haben leider verloren")
        else:
            break
        break
'''
print("Spiel ist vorbei")


# Spieler am Zug
# while bedingung einbauen wenn die eingabe nicht enter ist ->
# sixteen ist dead soll komplettes programm aufbauen
