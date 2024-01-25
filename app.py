from views import MainScreen, ViewManageTournament, RegisterPlayer, EnterResults, AdvanceToNextRound, GenerateReport

def main():
    # Load clubs and tournaments from JSON files
    clubs = load_clubs_from_json()
    tournaments = load_tournaments_from_json()

    # Display main screen
    current_screen = MainScreen(tournaments)
    while True:
        # Render current screen and get user choice
        next_screen, tournament = current_screen.show()

        # Handle choice and switch to corresponding screen
        if next_screen == ViewManageTournament:
            current_screen = ViewManageTournament(tournament)
        elif next_screen == RegisterPlayer:
            current_screen = RegisterPlayer(tournament, clubs)
        elif next_screen == EnterResults:
            current_screen = EnterResults(tournament)
        elif next_screen == AdvanceToNextRound:
            current_screen = AdvanceToNextRound(tournament)
        elif next_screen == GenerateReport:
            current_screen = GenerateReport(tournament)
        elif next_screen == "Quit":
            break

        # Save updated tournament data after specific actions
        if next_screen in [ViewManageTournament, RegisterPlayer, EnterResults, AdvanceToNextRound]:
            save_tournaments_to_json(tournaments)

    # Save clubs and tournaments before exiting
    save_clubs_to_json(clubs)
    save_tournaments_to_json(tournaments)


if __name__ == "__main__":
    main()