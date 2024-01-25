from datetime import date
from collections import namedtuple

Match = namedtuple("Match", ["round", "player1", "player2", "winner", "loser"])


class Tournament:
    def __init__(self, name, venue, start_date, end_date, players=[], rounds=4, current_round=1):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.current_round = current_round
        self.matches = []  # List of Match namedtuples for each round
        self.standings = {}  # Dict of player identifiers to points

    def is_active(self):
        return date.today() >= self.start_date and date.today() <= self.end_date

    def is_completed(self):
        return self.current_round > self.rounds

    def register_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def get_matches_for_round(self, round_number):
        return [match for match in self.matches if match.round == round_number]

    def enter_result(self, round_number, player1, player2, winner):
        """
        Enter result for a match and update standings.

        Args:
            round_number (int): Round number of the match.
            player1: Player object for the first player.
            player2: Player object for the second player.
            winner: Player object for the winner (or None for a tie).
        """
        match = next(
            match for match in self.matches if match.round == round_number
            and (match.player1 == player1 or match.player2 == player1)
            and (match.player1 == player2 or match.player2 == player2)
        )

        if not match:
            raise ValueError("Invalid match entered for round {}".format(round_number))

        match = Match(round_number, player1, player2, winner, None if winner else player1 if player1 != winner else player2)
        self.matches.append(match)

        # Update standings
        self.standings.setdefault(player1.identifier, 0)
        self.standings.setdefault(player2.identifier, 0)
        if winner:
            self.standings[winner.identifier] += 1
        else:
            self.standings[player1.identifier] += 0.5
            self.standings[player2.identifier] += 0.5

    def advance_round(self):
        """
        Advance to the next round and generate new pairings.
        """
        if not self.is_completed():
            self.current_round += 1
            self.matches = generate_pairings(self.players, self.current_round, self.standings)

    def generate_report(self):
        """
        Generate a report string with tournament details, standings, and matches.

        (format can be plain text or HTML)
        """
        # Implement report generation logic here
        # You can use template libraries or format strings to create structured reports
        pass

    def __repr__(self):
        return f"Tournament: {self.name}, Dates: {self.start_date}-{self.end_date}, Players: {len(self.players)}, Rounds: {self.rounds}, Current Round: {self.current_round}"

    # Utility method for sorting players by points for standings
    def sorted_players_by_points(self):
        return sorted(self.standings.items(), key=lambda item: item[1], reverse=True)

