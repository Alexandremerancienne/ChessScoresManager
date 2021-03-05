from models.model_player import ModelPlayer
from controllers.controller_tournament import ControllerTournament
from controllers.controller_player import ControllerPlayer
from views.view_menu import ViewMenu
from models.model_tournament import ModelTournament

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

    def quit_current_page():

        """A function to quit the program or return to welcome page."""

        return_choice = ViewMenu.quit_current_page()

        # The user returns to welcome page

        if return_choice in "yY":
            ViewMenu.print_welcome_page()
            stay is True

        # The user quits the program

        elif return_choice in "nN":
            ViewMenu.quit_program()
            stay is False

# Welcome page


ViewMenu.print_welcome_page()

stay = True

# While loop as long as the program is used

while stay is True:

    option_choice = ViewMenu.return_first_choice_welcome_page()

    if option_choice == "1":

        # Option 1: Start a new tournament

        ViewMenu.print_first_option()

        ControllerTournament.generate_new_tournament()

        # Once the tournament is played, 
        # return to welcome page or leave the program

        ControllerMenu.quit_current_page()

    elif option_choice == "2":

        # Option 2: Access to players database

        player_search_option = ViewMenu.print_player_search_options()

        if player_search_option == "1":

            # Option 2.1 : See all players

            ranking_or_name = ViewMenu.choose_ranking_or_name()

            if ranking_or_name in "aA":

                # Option 2.1.A : Sort all players by ranking

                ControllerPlayer.sort_all_players_by_ranking()

            elif ranking_or_name in "bB":

                # Option 2.1.B : Sort all players by last name

                ControllerPlayer.sort_all_players_by_last_name()

            # Once the players are sorted,
            # return to welcome page or leave the program

            ControllerMenu.quit_current_page()

        elif player_search_option == "2":

            # Option 2.2 : Change the ranking of a player

            player = ControllerPlayer.change_ranking()

            # Once the change is made,
            # return to welcome page or leave the program

            ControllerMenu.quit_current_page()

        elif player_search_option == "3":

            # Option 2.2 : Add a new player to players database

            new_player = ControllerPlayer.add_player_to_all_players_database()

            serialized_player = ModelPlayer.serialize_player(new_player)

            ModelPlayer.save_player_to_database(serialized_player)

            # Once the new player is added,
            # return to welcome page or leave the program

            ControllerMenu.quit_current_page()

    elif option_choice == "3":

        # Option 3: Access to tournaments database

        tournament_search_option = ViewMenu.print_tournament_search_options()

        if tournament_search_option == "1":

            # Option 3.1: See all tournaments

            ModelTournament.get_all_tournaments()

        elif tournament_search_option == "2":

            # Option 3.2: See details of a tournament

            ModelTournament.get_tournament()

        # Once the tournaments have been displayed,
        # return to welcome page or leave the program

        ControllerMenu.quit_current_page()

    elif option_choice == "4":

        # Option 4: Quit program

        ViewMenu.quit_program()
        break
