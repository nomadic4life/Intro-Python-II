# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def move_to(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if(new_room):
            self.current_room = new_room
        else:
            self.dialog(type="no room")

    def dialog(self, type=None):
        if(type == "no room"):
            print(f"doesn't appear to be anything in that direction")
        else:
            print(self.current_room)

    def check_inventory(self, user_input):
        print(
            f"""\n{"inventory: " + ", ".join([item.name for item in self.inventory])}\n""")

    def pickup_item(self, user_input):
        if len(self.current_room.items) > 0:
            self.inventory.append(self.current_room.items[0])
            self.current_room.items.pop(0)
        else:
            print("no items to pick up")
