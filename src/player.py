# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move_to(self, location):
        if(location == "n" and self.current_room.n_to != None):
            self.current_room = self.current_room.n_to
        elif(location == "e" and self.current_room.e_to != None):
            self.current_room = self.current_room.e_to
        elif(location == "s" and self.current_room.s_to != None):
            self.current_room = self.current_room.s_to
        elif(location == "w" and self.current_room.w_to != None):
            self.current_room = self.current_room.w_to
        else:
            print("no room in that direciton please try again")
        print(f"\nYou have entered the {self.current_room.name} room\n")
