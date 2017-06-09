from operator import itemgetter
import random

# Player setup
players = input('How many PCs? ')
players = int(players)
player_names = []
for i in range(0, players):
    name = input('PC ' + str(i + 1) + ' name: ')
    player_names.append(name)

# New encounter
new_fight = True

while new_fight is True:

    # Type in each player's initiative total
    player_init = []
    for i in range(0, players):
        pinit = input(player_names[i] + ' initiative total: ')
        player_init.append(pinit)

    # Combines the PC names with their initiative rolls in pairs in a list
    player_list = [None] * players
    for i in range(0, players):
        player_list[i] = ('- ' + player_names[i]), player_init[i]

    # How many enemies do we have?
    enemies = input('How many Monsters? ')
    enemies = int(enemies)

    # Type in each enemy's initiative modifier
    enemy_init = []
    for i in range(0, enemies):
        einit = input('Monster ' + str(i + 1) + ' initiative modifier? ')
        enemy_init.append(int(einit))

    # Rolls each enemy's initiative, adding their modifier, adds these rolls
    # into a list with the enemy names, in pairs
    monster_list = []
    for i in range(0, enemies):
        init_roll = random.randint(1, (20 + enemy_init[i]))
        monster_list.append(['- Monster ' + str(i + 1), init_roll])

    # Combines the list and sorts by initiative roll
    init_list = map(list, zip(*sorted(zip(monster_list, player_list), reverse=True)))

    print("\n")
    print("--- Initiative list ---")

    # Prints the list in readable strings without brackets/commas etc
    for entry in init_list:
        print(str(entry).strip("[]()").replace("'", "").replace(",", ":"))

    # Choice to start a new battle with the same group of PCs, or quit
    print("\n")
    again = input('Hit the enter key to start a new battle, or "n" to exit...')
    if again == "n":
        new_fight = False
