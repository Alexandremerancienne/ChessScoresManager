from datetime import datetime


class ViewPlayer():

    line = (100*"-")

    @staticmethod
    def get_player_id_number():
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
        print(ViewPlayer.line)
        print("New Player")

        surname = input("Enter player's surname: ")
        while surname.isalpha() is False:
            print("Please enter a valid surname.")
            surname = input("Enter player's surname: ")
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
        return(surname, first_name, birth_date, gender,
               ranking, score)

    @staticmethod
    def print_player(player):
        print(f"Player {player.id_number} \n")
        print(f"- Player name : {player.first_name} {player.surname}")
        print(f"- Gender : {player.gender}")
        print(f"- Date of birth (YYYY.MM.DD) : {player.birth_date}")
        print(f"- Current ranking : {player.ranking}")
        print(f"- Score : {player.score}\n")
        print("Player added to tournament")

    @staticmethod
    def get_player_ranking():
        print("Player's ranking")

    @staticmethod
    def get_player_name():
        player_name = input("Enter player's surname: ")
        return player_name

    @staticmethod
    def print_player_ranking(player_name, ranking):
        print(ViewPlayer.line)
        print(f"- Player name : {player_name}")
        print(f"- Ranking : {ranking}")
        print(ViewPlayer.line)

    @staticmethod
    def change_player_ranking():
        print("Change player's ranking")
        player_name = input("Enter player's surname: ")
        return player_name

    @staticmethod
    def enter_new_ranking():
        new_ranking = input("Enter new ranking: ")
        while isinstance(new_ranking, float) is False:
            try:
                new_ranking = float(new_ranking)
            except Exception:
                print("Please enter a valid ranking (positive float).")
                new_ranking = input("Enter new ranking: ")
                continue
        return new_ranking

    @staticmethod
    def print_player_new_ranking(surname, new_ranking):
        print(ViewPlayer.line)
        print(f"- Player name : {surname}")
        print(f"- Ranking : {new_ranking}")
        print(ViewPlayer.line)

    @staticmethod
    def print_tournament_players_by_name(players_list):
        print(ViewPlayer.line)
        print("Tournament players (sorted by name)")
        print(players_list)
        print(ViewPlayer.line)

    @staticmethod
    def print_tournament_players_by_ranking(players_list):
        print(ViewPlayer.line)
        print("Tournament players (sorted by ranking)")
        print(players_list)
        print(ViewPlayer.line)

    @staticmethod
    def print_all_players_by_name(players_list):
        print(ViewPlayer.line)
        print("Database players (sorted by name)")
        print(players_list)
        print(ViewPlayer.line)

    @staticmethod
    def print_all_players_by_ranking(players_list):
        print(ViewPlayer.line)
        print("Database players (sorted by ranking)")
        print(players_list)
        print(ViewPlayer.line)
