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
    def get_player_inputs(database):

        """A static method to get all the details of a player."""

        print(ViewPlayer.line)
        print("New Player")

        last_name = input("Enter player's last name: ")
        while last_name.isalpha() is False:
            print("Please enter a valid last name.")
            last_name = input("Enter player's last name: ")
            continue

        first_name = input("Enter player's first name: ")
        while first_name.isalpha() is False:
            print("Please enter a valid first name.")
            first_name = input("Enter player's first name: ")
            continue

        year_of_birth = input("Enter player's year of birth (YYYY): ")
        month_of_birth = input("Enter player's month of birth (MM): ")
        day_of_birth = input("Enter player's day of birth (DD): ")
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

        print("\nRanking successfully changed !")


    @staticmethod
    def print_player_new_ranking(last_name, new_ranking):

        """A static method to print the new ranking of a player."""

        print(ViewPlayer.line)
        print(f"- Player name : {last_name}")
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

        print("Database players (sorted by last name)")

    @staticmethod
    def print_all_players_by_ranking():

        """A static method to print all players sorted by ranking."""

        print("Database players (sorted by ranking)")
