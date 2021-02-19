class ViewMatch():

    line = (60*"-")
    match_result = (" MATCH RESULT ").center(60,"-")

    @staticmethod
    def start_match(first_player, second_player):
        next_match = (" NEXT MATCH ").center(60,"-")
        print(next_match)
        print(f"{first_player} vs {second_player}".center(60, ' '))
        print(ViewMatch.line)

    @staticmethod
    def get_match_result(first_player):
        result = input(f"Enter result for {first_player} - W (wins), L (looses), D (draw): ")
        while result not in ("wWlLdD"):
            print(f"Enter result for {first_player} - W (wins), L (looses), D (draw): ")
            continue
        return result

    @staticmethod
    def print_first_player_wins_and_score(first_player, second_player):
        print("\n" + ViewMatch.match_result)
        print(f"{first_player} WINS".center(60, ' '))
        print(f"{first_player}:1 - {second_player}:0".center(60, ' '))
        print(ViewMatch.line)


    @staticmethod
    def print_draw(first_player, second_player):
        print(ViewMatch.match_result)
        print("DRAW".center(60, ' '))
        print(f"{first_player}:0.5 - {second_player}:0.5".center(60, ' '))
        print(ViewMatch.line)
