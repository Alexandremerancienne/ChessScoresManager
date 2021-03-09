from datetime import datetime


class ViewPlayer():

    line = (100*"-")

    @staticmethod
    def get_player_id_number():

        """A static method to get the ID of a player."""

        id_number = input("Enter player's ID number (if None, enter 0): ")
        while isinstance(id_number, int) is False:
            try:
                id_number = int(id_number)
                break
            except Exception:
                print("Please enter a valid ID number.")
                id_number = input("Enter player's ID number"
                                  + "(if None, enter 0): ")
        return id_number

    @staticmethod
    def get_player_inputs():

        """A static method to get all the details of a player."""

        print(ViewPlayer.line)
        print("New Player\n")

        last_name = input("Enter player's last name: ")
        while all(x.isalpha() or x.isspace() for x in last_name) is False:
            print("Please enter a valid last name.")
            last_name = input("Enter player's last name: ")
            continue

        first_name = input("Enter player's first name: ")
        while all(x.isalpha() or x.isspace() for x in first_name) is False:
            print("Please enter a valid first name.")
            first_name = input("Enter player's first name: ")
            continue

        year_of_birth = input("Enter player's year of birth (YYYY): ")
        current_year = datetime.now().year
        if year_of_birth.isdigit() is True:
            while (100 > current_year - int(year_of_birth) > 18) is False:
                print("Enter a valid date of birth")
                year_of_birth = input("Enter player's year of birth (YYYY): ")
                if year_of_birth.isdigit() is True:
                    continue
                else:
                    break
        year_of_birth = str(year_of_birth)
        month_of_birth = input("Enter player's month of birth (MM): ")
        if len(month_of_birth) == 1:
            month_of_birth = "0" + month_of_birth
        day_of_birth = input("Enter player's day of birth (DD): ")
        if len(day_of_birth) == 1:
            day_of_birth = "0" + day_of_birth
        birth_date = (f"{year_of_birth}-{month_of_birth}-{day_of_birth}")
        while True:
            try:
                birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Please enter a valid birth date (YYYY.MM.DD)")
                year_of_birth = input("Enter player's year of birth (YYYY): ")
                month_of_birth = input("Enter player's month of birth (MM): ")
                day_of_birth = input("Enter player's day of birth (DD): ")
                birth_date = (f"{year_of_birth}-{month_of_birth}-"
                              + f"{day_of_birth}")
        date_tuple = (year_of_birth, month_of_birth, day_of_birth)
        birth_date = ".".join(date_tuple)

        gender = input("Enter player's gender (M/F): ")
        while str(gender) not in "mMfF" or gender.isalpha() is False:
            print("Please enter a valid gender (M/F).")
            gender = input("Enter player's gender (M/F): ")
            continue

        ranking = input("Enter player's ranking: ")
        while isinstance(ranking, float) is False:
            try:
                ranking = float(ranking)
                break
            except Exception:
                print("Please enter a valid ranking (positive float).")
                ranking = input("Enter player's ranking: ")

        score = 0

        print(ViewPlayer.line)
        return(last_name, first_name, birth_date, gender,
               ranking, score)

    @staticmethod
    def generate_player():

        """A static method to announce the creation of a player."""

        print("Generating new player...\n")

    @staticmethod
    def return_unknown_id():

        """A static method to indicate an ID number has not been recognized."""

        print("ID number not recognized")

    @staticmethod
    def return_successful_identification():

        """A static method to indicate an identification is successful."""

        print("\nIdentification successful")
        print("\nPlayer details:\n")

    @staticmethod
    def return_player_already_registered():

        """A static method to indicate a player has already been registered
        to a tournament."""

        print("Player already registered in tournament")

    @staticmethod
    def announce_next_player():

        """A static method to indicate a player has already been registered
        to a tournament."""

        print("\nNext player:\n")

    @staticmethod
    def print_player(player):

        """A static method to print a player."""

        print(f"Player {player.id_number} \n")
        print(f"- Player name : {player.first_name} {player.last_name}")
        print(f"- Gender : {player.gender}")
        print(f"- Date of birth (YYYY.MM.DD) : {player.birth_date}")
        print(f"- Current ranking : {player.ranking}")
        print(f"- Score : {player.score}\n")

    @staticmethod
    def confirm_player_addition_to_all_players_database():

        """A static method to confirm
        a player has been added to the players_database.json database."""

        print("Player added to players database")

    @staticmethod
    def confirm_player_addition_to_tournament():

        """A static method to confirm
        a player has been added to a tournament."""

        print("Player added to tournament")

    @staticmethod
    def set_new_rankings():

        """A static method to set the new rankings of all players
        at the end of a tournament."""

        print("NEW RANKINGS\n")
        print("Set new ranking for each player")

    @staticmethod
    def change_player_ranking():

        """A static method to enter the ranking of a player."""

        new_ranking = input("\nEnter new ranking: ")
        while isinstance(new_ranking, float) is False:
            try:
                new_ranking = float(new_ranking)
            except Exception:
                print("Please enter a valid ranking (positive float).")
                new_ranking = input("\nEnter new ranking: ")
                continue
        return new_ranking

    @staticmethod
    def confirm_ranking_change():

        """A static method to confirm the ranking of a player
        has been changed."""

        print("\nRanking successfully changed !\n")

    @staticmethod
    def print_player_new_ranking(last_name, id_number, new_ranking):

        """A static method to print the new ranking of a player."""

        print(ViewPlayer.line)
        print(f"- Player {id_number} : {last_name}")
        print(f"- Ranking : {new_ranking}")
        print(ViewPlayer.line)

    @staticmethod
    def print_tournament_players_by_last_name():

        """A static method to print tournament players sorted by last name."""

        print("Tournament players (sorted by last name)")

    @staticmethod
    def print_tournament_players_by_ranking():

        """A static method to print tournament players sorted by ranking."""

        print("Tournament players (sorted by ranking)")

    @staticmethod
    def print_all_players_by_last_name():

        """A static method to print all players sorted by last name."""

        print("Database players (sorted by last name)\n")

    @staticmethod
    def print_sorted_players(player):

        """A static method to print a sorted player."""

        print(f"Player {player.id_number} : "
              + f"{player.first_name} {player.last_name}"
              + f" - Ranking: {player.ranking}")

    @staticmethod
    def see_more_results():

        """A function to see the next results of a research."""

        see_more = input("\nSee next results ? (Y/N)\n")
        while see_more not in "yYnN" or see_more in "":
            see_more = input("\nSee next results ? (Y/N)\n")
            continue
        return see_more

    @staticmethod
    def print_all_players_by_ranking():

        """A static method to print all players sorted by ranking."""

        print("Database players (sorted by ranking)\n")

    @staticmethod
    def print_number_of_results(results):

        """A static method to print the number of results from a research."""

        print(f"\nNumber of results: {len(results)}\n")

    @staticmethod
    def print_players_options(player, i):

        """A static method to print all the players with an option number
        associated to each player."""

        print(f"[{i}] Player {player['id_number']} :"
              + f" {player['first_name']} {player['last_name']}")

    @staticmethod
    def choose_player(players):

        """A static method to choose a player among the options proposed."""

        player_chosen = input("\nChoose number to select a player\n")
        while not isinstance(player_chosen, int):
            try:
                player_chosen = int(player_chosen)
                while player_chosen not in range(1, len(players) + 1):
                    player_chosen = input("Choose number to select a player\n")
                    continue
                break
            except Exception:
                player_chosen = input("\nChoose number to select a"
                                      + " player\n")
        return int(player_chosen)

    @staticmethod
    def search_last_name():

        """A static method to search the last name of a player."""

        last_name = input("\nEnter player last name: ")
        while not last_name.isalpha() is True:
            print("Value Error.")
            last_name = input("\nEnter player last name: ")
            continue
        return last_name

    @staticmethod
    def search_id_number():

        """A static method to search the ID number of a player."""

        id_number = input("\nEnter player ID number: ")
        while not isinstance(id_number, int):
            try:
                id_number = int(id_number)
                break
            except Exception:
                id_number = input("\nEnter player ID (positive number): ")
                continue
        return id_number

    @staticmethod
    def return_no_player():

        """A static method to indicate no player has been found."""

        print("\nNo player found\n")

    @staticmethod
    def search_player():

        """A static method to search a player by last name or ID number."""

        option_number = input("\nSearch player (Enter option number): \n\n"
                              + "By last name [1]\n"
                              + "By ID number [2]\n\n")
        while option_number not in "12" or option_number in "":
            option_number = input("Search player (Enter option number): \n\n"
                                  + "By last name [1]\n"
                                  + "By ID number [2]\n")
            continue
        return option_number
