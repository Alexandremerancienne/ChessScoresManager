import pyfiglet


class ViewMenu:

    line = (100*":")

    @staticmethod
    def print_welcome_page():

        """A static method to print the welcome page."""

        welcome_message = pyfiglet.figlet_format("CHESS SCORES MANAGER")
        print(welcome_message)
        print(ViewMenu.line)
        print("AUTHOR : ALEXANDRE MERANCIENNE")
        print(ViewMenu.line)
        print("\nCHOOSE OPTION NUMBER:\n")

    @staticmethod
    def return_first_choice_welcome_page():

        """A static method to return the first choice on the welcome page."""

        option_choice = input(("Generate Tournament [1]    Players Database [2]    Tournaments Database [3]"
                              + "    Quit Program [4]\n\n").center(80))
        while str(option_choice) not in "1234" or str(option_choice) in "":
            print("Choose a number between 1 and 4\n")
            option_choice = input(("Generate Tournament [1]    Players Database [2]    Tournaments Database [3]"
                                  + "    Quit Program [4]\n\n").center(80))
            continue
        return option_choice

    @staticmethod
    def print_first_option():

        """A static method to announce the creation of a new tournament."""

        start_tournament = pyfiglet.figlet_format("NEW TOURNAMENT", font="digital")
        print(start_tournament)

    @staticmethod
    def print_player_search_options():

        """A static method to print the search options for a player."""

        print("\nPlayers Database\n")
        option_choice = input("See all players [1]    Change player ranking [2]    Add new player [3]\n\n")
        while str(option_choice) not in "123" or str(option_choice) in "":
            print("Choose a number between 1 and 3\n")
            option_choice = input("See all players [1]    Change Player Ranking [2]    Add new player [3]\n\n")

            continue
        return option_choice

    @staticmethod
    def print_tournament_search_options():

        """A static method to print the search options for a tournament."""

        print("\nTournaments database\n")
        option_choice = input("See all tournaments [1]    See tournament players [2]\n\n")
        while str(option_choice) not in "12" or str(option_choice) in "":
            print("Choose a number between 1 and 2\n")
            option_choice = input("See all tournaments [1]    See tournament players [2]\n\n")
            continue
        return option_choice

    @staticmethod
    def quit_current_page():

        """A static method to propose to quit the current page."""

        quit_current_page = input("\nReturn to Main Page ? (Y/N)\n")
        while quit_current_page not in "yYnN" or quit_current_page in "":
            quit_current_page = input("Return to Main Page ? (Y/N)\n")
            continue
        return quit_current_page

    @staticmethod
    def search_tournament():

        """A static method to filter the search for a tournament."""

        choice = input("\nSearch tournament (Enter option number): \n\n"
                       + "By name [A]\n"
                       + "By location [B]\n"
                       + "By year [C]\n\n")

        while choice not in "aAbBcC" or choice in "":
            print("Choose a correct number.")
            choice = input("\nSearch tournament (Enter option number): \n\n"
                           + "By name [A]\n"
                           + "By location [B]\n"
                           + "By year [C]\n\n")
            continue

        return choice

    @staticmethod
    def choose_ranking_or_name():

        """A static method to propose to sort players by ranking
        or by last name."""

        print("\nSort players:\n")
        option_choice = input("By ranking [A]"
                              + "    By last name [B]\n\n")
        while str(option_choice) not in "aAbB" or str(option_choice) in "":
            print("Choose a letter between A and B\n")
            option_choice = input("By ranking [A]"
                                  + "    By last name [B]\n\n")
            continue
        return option_choice

    @staticmethod
    def quit_program():

        """A static method to print the end of the program."""

        print("\nThank you for using Chess Scores Manager !")
