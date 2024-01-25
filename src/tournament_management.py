from dataclasses import dataclass
from typing import List

from .club_management import Player

@dataclass
class Tournament:
    name: str
    venue: str
    start_date: str
    end_date: str
    rounds: int
    current_round: int
    players: List[Player]
    matches: List[List[Player]]

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_match(self, match):
        self.matches.append(match)

    def remove_match(self, match):
        self.matches.remove(match)