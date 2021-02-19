from datetime import datetime

class ViewPlayer():

    line = (60*"-")

    @staticmethod
    def get_player_inputs():

        family_name = input("Enter player's family name: ")
        while family_name.isalpha() is False:
            print("Please enter a valid family name.")
            family_name = input("Enter player's family name: ")
            continue

        first_name = input("Enter player's first name: ")
        while first_name.isalpha() is False:
            print("Please enter a valid first name.")
            first_name = input("Enter player's first name: ")
            continue

        year_of_birth = input("Enter player's year of birth (YYYY): ")
        month_of_birth = input("Enter player's month of birth (MM): ")
        day_of_birth = input("Enter player's day of birth (DD): ")
        date = (f"{year_of_birth}-{month_of_birth}-{day_of_birth}")
        while True:
            try:
                birth_date = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Please enter a valid birth date (YYYY-MM-DD)")
                year_of_birth = input("Enter player's year of birth (YYYY): ")
                month_of_birth = input("Enter player's month of birth (MM): ")
                day_of_birth = input("Enter player's day of birth (DD): ")
                date = (f"{year_of_birth}-{month_of_birth}-{day_of_birth}")

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

        return(family_name, first_name, date, gender, ranking, score)


    @staticmethod
    def print_player(i, player):
        print(ViewPlayer.line)
        print(f"Player {i} \n")
        print(f"- Player name : {player.first_name} {player.family_name}")
        print(f"- Gender : {player.gender}")
        print(f"- Date of birth (YYYY-MM-DD) : {player.birth_date}")
        print(f"- Current ranking : {player.ranking}")
        print(f"- Score : {player.score}")
        print(ViewPlayer.line)

    @staticmethod
    def get_player_ranking():
        print("Player's ranking")


    @staticmethod
    def get_player_name():   
        player_name = input("Enter player's family name: ")
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
        player_name = input("Enter player's family name: ")
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
    def print_player_new_ranking(family_name, new_ranking):
        print(ViewPlayer.line)
        print(f"- Player name : {family_name}")
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