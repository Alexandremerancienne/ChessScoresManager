import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_match import ModelMatch
from models.model_player import ModelPlayer
from views.view_match import ViewMatch
from controllers.controller_player import ControllerPlayer


class ControllerMatch:

    def __init__(self, model, view):
        self.model = ModelMatch
        self.view = ViewMatch

    def start_match(first_player, second_player):
        first_player_name = first_player.surname
        second_player_name = second_player.surname
        return ViewMatch.start_match(first_player_name, second_player_name)

    def print_winner_and_score(first_player, second_player):

        match = ModelMatch("", "", "", "")

        f_p = first_player.surname
        s_p = second_player.surname

        result = ViewMatch.get_match_result(f_p)

        if result in "wW":
            result = ModelMatch.first_player_wins(match)
            first_player.score += 1
            match = ModelMatch(f_p, 1, s_p, 0)
            ViewMatch.print_first_player_wins_and_score(f_p, s_p)

        elif result in "lL":
            result = ModelMatch.second_player_wins(match)
            second_player.score += 1
            match = ModelMatch(f_p, 0, s_p, 1)
            ViewMatch.print_first_player_wins_and_score(s_p, f_p)

        elif result in "dD":
            result = ModelMatch.draw(match)
            first_player.score += 0.5
            second_player.score += 0.5
            match = ModelMatch(f_p, 0.5, s_p, 0.5)
            ViewMatch.print_draw(f_p, s_p)

        return match


if __name__ == "__main__":

    ModelPlayer.tournament_players.truncate()
    for _ in range(1, 3):
        player = ControllerPlayer.add_player_to_tournament()
        serialized_player = ModelPlayer.serialize_player(player)
        ModelPlayer.save_tournament_player(serialized_player)
        ModelPlayer.save_player_to_database(serialized_player)

    for player in ModelPlayer.tournament_players:
        print(player)
"""
    first_player = ModelPlayer.tournament_players[0]
    second_player = ModelPlayer.tournament_players[1]

    ControllerMatch.start_match(first_player, second_player)

    ControllerMatch.print_winner_and_score(first_player, second_player)
"""