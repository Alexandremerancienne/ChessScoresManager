class View():

    @staticmethod
    def print_player(i, family_name, first_name, birth_date, gender, ranking, score):
        print("**************************************************************")
        print(f"- Player {i}")
        print(f"- Player name : {first_name} {family_name}")
        print(f"- Gender : {gender}")
        print(f"- Date of birth (YYYY-MM-DD) : {birth_date}")
        print(f"- Current ranking : {ranking}")
        print(f"- Score : {score}")
        print("**************************************************************")


    @staticmethod
    def print_player_ranking(family_name, ranking):
        print("**************************************************************")
        print(f"- Player name : {family_name}")
        print(f"- Ranking : {ranking}")
        print("**************************************************************")


    @staticmethod
    def print_player_new_ranking(family_name, new_ranking):
        print("**************************************************************")
        print(f"- Player name : {family_name}")
        print(f"- Ranking : {new_ranking}")
        print("**************************************************************")


    @staticmethod
    def print_tournament_players_by_name(players_list):
        print("**************************************************************")
        print("Tournament players (sorted by name)")
        print(players_list)
        print("**************************************************************")     

    @staticmethod
    def print_tournament_players_by_ranking(players_list):
        print("**************************************************************")
        print("Tournament players (sorted by ranking)")
        print(players_list)
        print("**************************************************************")        

    @staticmethod
    def print_all_players_by_name(players_list):
        print("**************************************************************")
        print("Database players (sorted by name)")
        print(players_list)
        print("**************************************************************")     

    @staticmethod
    def print_all_players_by_ranking(players_list):
        print("**************************************************************")
        print("Database players (sorted by ranking)")
        print(players_list)
        print("**************************************************************")