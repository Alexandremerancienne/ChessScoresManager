from MVC.controllers.controller_tournament import ControllerTournament
from MVC.controllers.controller_player import ControllerPlayer
from MVC.views.view_menu import ViewMenu
from MVC.models.model_tournament import ModelTournament

"""Chess Scores Manager Program.

Author : Alexandre MERANCIENNE

This program aims at monitoring the results of a chess tournament.

The matches are defined according to Swiss-pairing algorithm.

The details of the algorithm are developed in models/model_tournament.py file.

The program also saves the results of each tournament for further use."""


class ControllerMenu:

    """A Controller for main page (menu).

    The functions defined encompass all the options
    available from the main page :

    - Generate a new tournament ;
    - See the ranking of a player ;
    - See the results of a previous tournament ;
    - Quit program."""

    def __init__(self, view):
        self.view = ViewMenu

    def choose_option_on_welcome_page():

        """A function to choose an option on the welcome page."""

        return ViewMenu.return_first_choice_welcome_page()

    def quit_current_page():

        """A function to quit the current page."""

        return ViewMenu.quit_current_page()

    def print_welcome_page():

        """A function to print the welcome page."""

        return ViewMenu.print_welcome_page()

    def quit_program():

        """A function to quit the program."""

        return ViewMenu.quit_program()

# Welcome page


ControllerMenu.print_welcome_page()

stay = True

# While loop as long as the program is used

while stay is True:

    option_choice = ControllerMenu.choose_option_on_welcome_page()

    if option_choice == "1":

        # Option 1: Start a new tournament

        ViewMenu.print_first_option()

        ControllerTournament.generate_new_tournament()

        # Once the tournament is played, the user can return to welcome page
        # or leave the program

        return_choice = ControllerMenu.quit_current_page()

        # The user returns to welcome page

        if return_choice in "yY":
            ControllerMenu.print_welcome_page()
            continue

        # The user quits the program

        elif return_choice in "nN":
            ControllerMenu.quit_program()
            break

    elif option_choice == "2":

        # Option 2: Access to players database

        player_search_option = ViewMenu.print_player_search_options()

        if player_search_option == "1":

            # Option 2.1 : See all players

            ranking_or_name = ViewMenu.choose_ranking_or_name()

            if ranking_or_name in "aA":

                # Option 2.1.A : Sort all players by ranking

                ControllerPlayer.sort_all_players_by_ranking()

                # Once the players are sorted,
                # the user can return to welcome page or leave the program

                return_choice = ControllerMenu.quit_current_page()

                # The user returns to welcome page

                if return_choice in "yY":
                    ControllerMenu.print_welcome_page()
                    continue

                # The user quits the program

                elif return_choice in "nN":
                    ControllerMenu.quit_program()
                    break

            elif ranking_or_name in "bB":

                # Option 2.1.B : Sort all players by last name

                ControllerPlayer.sort_all_players_by_last_name()

                # Once the players are sorted,
                # the user can return to welcome page or leave the program

                return_choice = ControllerMenu.quit_current_page()

                # The user returns to welcome page

                if return_choice in "yY":
                    ControllerMenu.print_welcome_page()
                    continue

                # The user quits the program

                elif return_choice in "nN":
                    ControllerMenu.quit_program()
                    break

        elif player_search_option == "2":

            # Option 2.2 : Change the ranking of a player

            player = ControllerPlayer.change_ranking()

            # Once the change is made,
            # the user can return to welcome page or leave the program

        return_choice = ControllerMenu.quit_current_page()

        # The user returns to welcome page

        if return_choice in "yY":
            ControllerMenu.print_welcome_page()
            continue

        # The user quits the program

        elif return_choice in "nN":
            ControllerMenu.quit_program()
            break

    elif option_choice == "3":

        # Option 3: Access to tournaments database

        tournament_search_option = ViewMenu.print_tournament_search_options()

        if tournament_search_option == "1":

            # Option 3.1: See all tournaments

            ModelTournament.get_all_tournaments()

            # Once all tournaments have been displayed,
            # the user can return to welcome page or leave the program

            return_choice = ControllerMenu.quit_current_page()

            # The user returns to welcome page

            if return_choice in "yY":
                ControllerMenu.print_welcome_page()
                continue

            # The user quits the program

            elif return_choice in "nN":
                ControllerMenu.quit_program()
                break

        elif tournament_search_option == "2":

            # Option 3.2: See details of a tournament

            ModelTournament.get_tournament()

            # Once the tournament has been displayed,
            # the user can return to welcome page or leave the program

            return_choice = ControllerMenu.quit_current_page()

            # The user returns to welcome page

            if return_choice in "yY":
                ControllerMenu.print_welcome_page()
                continue

            # The user quits the program

            elif return_choice in "nN":
                ControllerMenu.quit_program()
                break

    elif option_choice == "4":

        # Option 4: Quit program

        ControllerMenu.quit_program()
        break
