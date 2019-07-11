class Game:
    # command dict for user input

    def __init__(self, player, room):
        self.player = player
        self.mam = room
        self.command_options = {
            'w': {
                'type': 'player_action',
                'method': 'move_to'
            },
            'e': {
                'type': 'player_action',
                'method': 'move_to'
            },
            'n': {
                'type': 'player_action',
                'method': 'move_to'
            },
            's': {
                'type': 'player_action',
                'method': 'move_to'
            },
            'q': {
                'type': 'quit'
            },
        }

    def command(self, user_input):
        execute = self.__command_type__(user_input, 'type')
        execute(user_input)

    def quit(self, user_input):
        exit()

    def player_action(self, user_input):
        action = self.__command_type__(user_input, 'method')
        action(user_input)

    def invalid_input(self, user_input):
        print(f"{user_input} is an invalid input")

    def game_prompt(self):
        self.player.dialog()

    def __command_type__(self, user_input, command_type):
        command_input = self.command_options[user_input]
        if command_type == 'type':
            obj = self
        else:
            obj = self.player
        return getattr(obj, command_input[command_type], "invalid_input")
