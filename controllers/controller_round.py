import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_match import ModelMatch
from models.model_player import ModelPlayer
from models.model_round import ModelRound
from views.view_match import ViewMatch
from views.view_round import ViewRound
from controller_player import ControllerPlayer
from controller_match import ControllerMatch
from datetime import datetime
from operator import attrgetter

class ControllerRound:

    def __init__(self, model, view):
        self.model = model_match
        self.view = view_match

    def start_round(i):
        ViewRound.start_round(i)
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def end_round():
        ViewRound.end_round()
        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_round_results(i, start_date, end_date, list_of_matches):
    	return ViewRound.print_round_results(i, start_date, end_date, list_of_matches)


if __name__ == "__main__":

    round = ModelRound("", "", "")

    start_date = ControllerRound.start_round(1)

    for i in range(1,9):
        ControllerPlayer.add_player_to_tournament(i)

    round_players = ControllerPlayer.sort_tournament_players_by_ranking()

    for i in range(0,4):
        first_player = ModelPlayer.tournament_players[i]
        f_p = first_player
        second_player = ModelPlayer.tournament_players[i+4]
        s_p = second_player

        match = ModelMatch("", "", "", "")

        ControllerMatch.start_match(f_p, s_p)
        match = ControllerMatch.print_winner_and_score(f_p, s_p)

        ModelRound.list_of_matches.append(match)


    end_date = ControllerRound.end_round()

    ControllerRound.print_round_results(1, start_date, end_date, ModelRound.list_of_matches)