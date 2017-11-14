from random import randint
import pygame
running = True
while running:
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dice Game!!11!!1")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 60)
    screen.fill((0, 0, 0))

for event in pygame.event.get():
    # Spiel beenden, wenn wir ein QUIT-Event finden.

    if event.type == pygame.QUIT:
        running = False

    # Wir interessieren uns auch für "Taste gedrückt"-Events.

    if event.type == pygame.KEYDOWN:

        # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.

        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        if event.key == pygame.K_ESCAPE:
            running = False
            print("W")

        if event.key == pygame.K_a:
            print("A")

        if event.key == pygame.K_s:
            print("S")

        if event.key == pygame.K_d:
            print("D")

# Inhalt von screen anzeigen.

pygame.display.flip()

print("Spiel beginnt")


# Function: Roll Dice
def roll_dice(number = 1, faces = 6, seed = None):
    result = ''
    random.seed(seed)
    for i in range(number):
            result += str(random.randint(1, faces))
            if i + 1 < number:
                result += ','
    return result


def players():
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

member = []

counter_player = players()
count = 1
while count <= counter_player:
    player_name = input("Name eingeben: ")
    member.append(player_name)
    count += 1

print()





'''
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
        x = roll_dice()
        list_2.append(x)
        z = sum(list_2)
        print(x)
        print("Die Summe ihrer Würfe ist: ", z)
    elif sum(list_2) == 10:
        t_player_1 = input("Sie müssen nochmal würfeln!")
    elif t_player_1 == "stop":
        print(z)
        quit()
    elif sum(list_2) >= 16 or sum(list_2) == 9:
        print("Sie haben verloren! try again!")
        break
    elif t_player_1 == "n":
        index_list += 1
        scoreboard.append(sum(list_2))
        list_2 = []

print(list_3)
print(scoreboard)
print("Spiel ist vorbei!!")
'''