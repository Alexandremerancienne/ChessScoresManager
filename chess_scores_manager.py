import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from controllers.controller_tournament import ControllerTournament
from views.view_menu import ViewMenu
from models.model_player import ModelPlayer
from models.model_tournament import ModelTournament

"""Chess Scores Manager Program.

Author : Alexandre MERANCIENNE

This program aims at monitoring the results of a chess tournament.

The matches are defined according to Swiss-pairing algorithm.

If needed, the details of the algorithm are developed in
models/model_tournament.py file.

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
        return ViewMenu.return_first_choice_welcome_page()

    def quit_current_page():
        return ViewMenu.quit_current_page()

    def print_welcome_page():
        return ViewMenu.print_welcome_page()

    def quit_program():
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

        return_choice = ControllerMenu.quit_current_page()
        if return_choice in "yY":
            ControllerMenu.print_welcome_page()
            continue
        elif return_choice in "nN":
            ControllerMenu.quit_program()
            break

    elif option_choice == "2":

        # Option 2: See the ranking of a player

        ModelPlayer.get_player()

        return_choice = ControllerMenu.quit_current_page()

        if return_choice in "yY":
            ControllerMenu.print_welcome_page()
            continue
        elif return_choice in "nN":
            ControllerMenu.quit_program()
            break

    elif option_choice == "3":

        # Option 3: See the results of a previous tournament

        ModelTournament.get_tournament()

        return_choice = ControllerMenu.quit_current_page()

        if return_choice in "yY":
            ControllerMenu.print_welcome_page()
            continue
        elif return_choice in "nN":
            ControllerMenu.quit_program()
            break

    elif option_choice == "4":

        # Option 4: Quit program

        ControllerMenu.quit_program()
        break
