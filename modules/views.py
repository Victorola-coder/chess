class MainScreen:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    def show(self):
        print("Welcome to Castle Chess!")
        if not self.tournaments:
            print("No active tournaments.")
            print("1. Create a new tournament")
            print("2. Quit")
        else:
            print("Active Tournaments:")
            for i, tournament in enumerate(self.tournaments):
                print(f"{i+1}. {tournament}")
            print("3. View/manage a tournament")
            print("4. Create a new tournament")
            print("5. Quit")

        choice = input("\nPlease enter your choice: ")
        return handle_choice(choice, self.tournaments)

def handle_choice(choice, tournaments):
    # Implement logic to handle user input and navigate between screens
    # based on choices (e.g., switch to ViewManageTournament screen)
    # depending on selected tournament or create a new one

class ViewManageTournament:
    def __init__(self, tournament):
        self.tournament = tournament

    def show(self):
        print(f"Tournament: {self.tournament.name}")
        print(f"Dates: {self.tournament.start_date} - {self.tournament.end_date}")
        print(f"Venue: {self.tournament.venue}")
        print(f"Rounds: {self.tournament.rounds}")
        print(f"Current Round: {self.tournament.current_round}")
        print(f"\nPlayers:")
        for player in self.tournament.players:
            print(f"\t- {player}")

        if not self.tournament.is_completed():
            print("\nActions:")
            print("1. Register a player")
            print("2. Enter results for current round")
            print("3. Advance to next round")
            print("4. Generate report")
            print("5. Go back to main menu")
        else:
            print("\nTournament completed!")
            print("1. Generate report")
            print("2. Go back to main menu")

        choice = input("\nPlease enter your choice: ")
        return handle_choice(choice, self.tournament)