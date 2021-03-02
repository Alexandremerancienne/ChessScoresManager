class ViewTournament():

    line = (100*"-")
    star_line = (100*"*")

    @staticmethod
    def get_tournament_inputs():
        name = input("Please enter tournament name: ")
        while not all(x.isalpha() or x.isspace() for x in name) or name == "":
            print("Please enter a valid name.")
            name = input("Please enter tournament name: ")
            continue

        location = input("Please enter tournament location: ")
        while location.isalpha() is False:
            print("Please enter a valid location.")
            location = input("Please enter tournament location: ")
            continue

        description = input("Please enter a description of the tournament: ")

        time_control = input("Enter time control (blitz, bullet, rapid): ")
        while not time_control.lower() in ("blitz", "rapid", "bullet"):
            print("Please enter a valid time control (blitz, bullet, rapid).")
            time_control = input("Enter time control (blitz, bullet, rapid): ")
            continue

        return(name, location, description, time_control)

    @staticmethod
    def start_tournament(tournament_name, tournament_location):
        print(ViewTournament.line)
        print(f"Welcome to the {tournament_name} of {tournament_location}!")
        input("Press Enter to start the tournament")
        print(ViewTournament.line)

    @staticmethod
    def enter_tournament_players():
        print("Number of players: 8")
        print("Please enter each player's details")
        print(ViewTournament.line)

    @staticmethod
    def announce_round_matches():
        print("Next round matches:")

    @staticmethod
    def print_pairs(i, pair):
        print(f"Match {i}: {pair[0]} vs {pair[1]}")

    @staticmethod
    def print_ending_message():
        print("End of the tournament !")
        print(ViewTournament.line)
        print("Tournament recap")

    @staticmethod
    def print_tournament_results(name, location, start_date, end_date,
                                 description, time_control, players_list,
                                 rounds):
        print(f"Tournament name: {name}\n")
        print(f"Location: {location}\n")
        print(f"Dates: from {start_date} to {end_date}\n")
        print(f"Description: {description}\n")
        print(f"Time control: {time_control.capitalize()}\n")
        print("Participants:\n")
        for player in players_list:
            print(player)
        print("Rounds results:")
        print("\n")
        for round_results in rounds:
            print(round_results)
            print("\n")