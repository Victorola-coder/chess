from dataclasses import dataclass

@dataclass
class Player:
    name: str
    email: str
    chess_id: str
    birthdate: str

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
