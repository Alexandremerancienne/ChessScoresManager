class ViewTournament():

    line = (100*"-")
    star_line = (100*"*")

    @staticmethod
    def get_tournament_inputs():

        """A static method to get the inputs of a tournament."""

        name = input("Please enter tournament name: ")
        while not all(x.isalpha() or x.isspace() for x in name) or name == "":
            print("Please enter a valid name.")
            name = input("Please enter tournament name: ")
            continue

        location = input("Please enter tournament location: ")
        while all(x.isalpha() or x.isspace() for x in location) is False:
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

        """A static method to announce the start of a tournament."""

        print(ViewTournament.line)
        print(f"Welcome to the {tournament_name} of {tournament_location}!")
        input("Press Enter to start the tournament")
        print(ViewTournament.line)

    @staticmethod
    def enter_tournament_players():

        """A static method to enter tournament players details."""

        print("Number of players: 8")
        print("Please enter each player's details")
        print(ViewTournament.line)

    @staticmethod
    def announce_round_matches():

        """A static method to announce the matches of the next round."""

        print("Next round matches:")

    @staticmethod
    def print_pairs(i, pair):

        """A static method to print the pairs of a match."""

        print(f"Match {i}: {pair[0][0]} ({pair[0][1]})"
              + f" vs {pair[1][0]} ({pair[1][1]})")

    @staticmethod
    def print_ending_message():

        """A static method to announce the end of a tournament."""
        print("\n")
        end = ("  END OF THE T0URNAMENT !  ").center(100, "*")
        print(end)
        print("\n")

    @staticmethod
    def print_tournament_results(name, location, start_date, end_date,
                                 description, time_control, players_list,
                                 rounds):

        """A static method to print the results of a tournament."""

        print(ViewTournament.line)
        print("TOURNAMENT RECAP\n")
        print(f"Tournament name: {name}")
        print(f"Location: {location}")
        print(f"Dates: from {start_date} to {end_date}")
        print(f"Description: {description}")
        print(f"Time control: {time_control.capitalize()}")
        print("Participants:")
        for player in players_list:
            print(f"{player[0]} ({player[1]})")
        print("\nRounds results:")
        for round_results in rounds:
            print(round_results)

    @staticmethod
    def order_players_by_ranking(players):

        """A static method to present players sorted by ranking."""

        print("Tournament players sorted by ranking\n")

        for player in players:

            print(f"Player {player[1]} : "
                  + f"{player[0]}"
                  + f" - Ranking: {player[2]}")

    @staticmethod
    def order_players_by_last_name(players):

        """A static method to present players sorted by last name."""

        print("Tournament players sorted by last name\n")
        for player in players:
            print(f"Player {player[1]} : "
                  + f"{player[0]}")

    @staticmethod
    def choose_tournament(results):

        """A static method to choose a tournament and see details."""

        tournament_choice = input("Enter tournament number to see players\n")
        while not (isinstance(tournament_choice, int)):
            try:
                tournament_choice = int(tournament_choice)
                while int(tournament_choice) not in range(1, len(results) +1):
                    tournament_choice = input("Choose number to select" 
                                              + " a tournament\n")
                    continue
                break
            except Exception:
                tournament_choice = input("Enter tournament number to see"
                                          + " players\n")
        return tournament_choice

    @staticmethod
    def define_sorting_option():

        """A static method to define a sorting option."""

        players_sorted = input("Sort tournament players:\n\n"
                               + "By ranking [A]\n"
                               + "By last name [B]\n\n")
        while players_sorted not in "aAbB":
            players_sorted = input("Sort tournament players:\n\n"
                                   + "By ranking [A]\n"
                                   + "By last name [B]\n\n")
            continue
        return players_sorted

    @staticmethod
    def return_no_tournament():

        """A static method to indicate no tournament has been found."""

        print("No tournament found\n")

    @staticmethod
    def print_number_of_results(number_of_results):

        """A static method to print the number of results."""

        print(f"Number of results: {number_of_results}\n")

    @staticmethod
    def enter_tournament_name():

        """A static method to enter the name of a tournament."""

        name = input("\nEnter tournament name: ")
        return name

    @staticmethod
    def enter_tournament_location():

        """A static method to enter the location of a tournament."""

        location = input("\nEnter tournament location: ")
        return location

    @staticmethod
    def enter_tournament_year():

        """A static method to enter the year of a tournament."""

        year = input("\nEnter tournament year: ")
        return year

    @staticmethod
    def define_search_criteria():

        """A static method to define search criteria for a tournament."""

        choice = input("\nSearch tournament (Enter option number): \n\n"
                       + "By name [A]\n"
                       + "By location [B]\n"
                       + "By year [C]\n\n")

        while choice not in "aAbBcC":
            print("Choose a correct number.")
            choice = input("\nSearch tournament (Enter option number): \n\n"
                           + "By name [A]\n"
                           + "By location [B]\n"
                           + "By year [C]\n\n")
            continue
        return choice

    @staticmethod
    def print_all_tournaments():

        """A static method to print the database of all tournaments."""

        print("\nDatabase of all tournaments\n")

    @staticmethod
    def print_chunk_tournaments(chunk, i):

        """A static method to print tournaments sliced into chunks."""

        print(f"[{i}] {chunk['name']} of {chunk['location']}")
        print(f"Start : {chunk['start_date']}")
        print(f"End : {chunk['end_date']}\n")

    @staticmethod
    def see_more_results():

        """A function to see the next results of a research."""

        see_more = input("\nSee next results ? (Y/N)\n")
        while see_more not in "yYnN":
            see_more = input("\nSee next results ? (Y/N)\n")
            continue
        return see_more

    @staticmethod
    def see_details_or_not():

        """A static method to choose to see tournament details (or not)."""

        choice = input("\nSee tournament details ? (Y/N)\n")
        while choice not in "yYnN":
            choice = input("\nSee tournament details ? (Y/N)\n")
            continue
        return choice

    @staticmethod
    def see_tournament_details(all_tournaments):

        """A static method to see tournament details."""

        tournament_choice = input("\nChoose a number to see tournament"
                                  + " details\n")
        while not (isinstance(tournament_choice, int)):
            try:
                tournament_choice = int(tournament_choice)
                x = len(all_tournaments)
                while int(tournament_choice) not in range(1, x+1):
                    tournament_choice = input("\nChoose a number to see"
                                              + " tournament details\n")
                    continue
                break
            except Exception:
                tournament_choice = input("\nChoose a number to see"
                                          + " tournament details\n")
        return tournament_choice
