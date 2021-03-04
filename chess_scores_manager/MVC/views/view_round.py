class ViewRound():

    line = (100*"*")

    @staticmethod
    def start_round(i):

        """A static method to announce the start of a round."""

        print("\n")
        round_i = (f" ROUND {i} ").center(100, "*")
        print(round_i)
        print("Number of matches : 4")
        input("Press Enter to start the round").center(100, " ")
        print(ViewRound.line)

    @staticmethod
    def print_round_results(i, start_date, end_date, list_of_matches):

        """A static method to print the results of a round."""

        print(f"ROUND {i} RESULTS")
        print(f"Start: {start_date}")
        print(f"End: {end_date}")
        print(f"Matches: {list_of_matches}")
