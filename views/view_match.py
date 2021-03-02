class ViewMatch():

    line = (100*"-")

    @staticmethod
    def start_match(first_player, second_player):

        """A static method to announce a match."""

        print(f"NEXT MATCH : {first_player} vs {second_player}")

    @staticmethod
    def get_match_result(first_player):

        """A static method to enter the results of a match."""

        result = input(f"Enter result for {first_player}"
                       + " => W (wins), L (looses), D (draw): ")
        while result not in ("wWlLdD"):
            result = input(f"Enter result for {first_player}"
                           + " => W (wins), L (looses), D (draw): ")
            continue
        return result

    @staticmethod
    def print_first_player_wins_and_score(first_player, second_player):

        """A static method to announce the victory of the first player."""

        print(ViewMatch.line)
        print(f"MATCH RESULT : {first_player} WINS")
        print(f"{first_player} : 1")
        print(f"{second_player} : 0")
        print(ViewMatch.line)

    @staticmethod
    def print_draw(first_player, second_player):

        """A static method to announce a draw."""

        print(ViewMatch.line)
        print("MATCH RESULT : DRAW")
        print(f"{first_player} : 0.5")
        print(f"{second_player} : 0.5")
        print(ViewMatch.line)
