# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def __str__(self):
        str = f"""
              \n----------------------------------
              \n{self.name}
              \n   {self.description}
              \n{"items: " + ", ".join([item.name for item in self.items])}\n"""
        return str

    def add(self, item):
        self.items.append(item)
