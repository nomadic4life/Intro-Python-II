from room import Room
from player import Player
from items import Items
from game_commands import Game

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Treasure"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Frank", room["outside"])

# Game instance
game = Game(player, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
start = True
while True:

    # user_input = input("press n, w, e, s \n")
    # game.command(input("press n, w, e, s \n"))
    # player.move_to(command_options[user_input])

    # print(command_options[incoming])

    if(start):
        start = False
        print(
            f"\nGreetings {player.name}! Welcome to the {player.current_room.name},\n\n{player.current_room.description}\n")
        user_input = input(
            f"{player.name}, so while your here what action do you choose to embark on your journy? \n>>> ")
    else:
        print(f"\n\nYou have entered the {player.current_room.name} room\n")
        print(f"{player.current_room.description}\n")
        user_input = input(
            f"Alright {player.name} where do you want to go next?\nChoose wisely because it might be your last.\n>>> ")

    game.command(user_input)

    # if (user_input == "n" or user_input == "s" or user_input == "w" or user_input == "e"):
    #     player.move_to(user_input)
    # elif(user_input == "q"):
    #     exit()
    # elif(user_input == "i"):
    #     print(
    #         f"items in {player.current_room.name} {player.current_room.items}")
    # else:
    #     print(">  not sure what you are tring to do with that command but you probably want to choose a better command that makes sense\n>  hint: w go west, e go east, n go north, and s go south, or q to just give up.")
