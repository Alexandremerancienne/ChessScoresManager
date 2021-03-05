class ViewMatch():

    line = (100*"-")

    @staticmethod
    def start_match(first_player, second_player):

        """A static method to announce a match."""

        print(f"NEXT MATCH : {first_player[0]} ({first_player[1]})"
              + f" vs {second_player[0]} ({second_player[1]})")

    @staticmethod
    def get_match_result(first_player, first_id):

        """A static method to enter the results of a match."""

        result = input(f"Enter result for {first_player} ({first_id})"
                       + " => W (wins), L (looses), D (draw): ")
        while result not in ("wWlLdD"):
            result = input(f"Enter result for {first_player} ({first_id})"
                           + " => W (wins), L (looses), D (draw): ")
            continue
        return result

    @staticmethod
    def print_first_player_wins_and_score(first_player, first_id,
                                          second_player, second_id):

        """A static method to announce the victory of the first player."""

        print(ViewMatch.line)
        print(f"MATCH RESULT : {first_player} ({first_id}) WINS")
        print(f"{first_player} ({first_id}): 1")
        print(f"{second_player} ({second_id}): 0")
        print(ViewMatch.line)

    @staticmethod
    def print_draw(first_player, first_id, second_player, second_id):

        """A static method to announce a draw."""

        print(ViewMatch.line)
        print("MATCH RESULT : DRAW")
        print(f"{first_player} ({first_id}): 0.5")
        print(f"{second_player} ({second_id}): 0.5")
        print(ViewMatch.line)
