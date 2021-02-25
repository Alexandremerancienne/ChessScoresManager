import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_match import ModelMatch
from models.model_player import ModelPlayer
from models.model_round import ModelRound
from models.model_tournament import ModelTournament
from views.view_tournament import ViewTournament
from controllers.controller_player import ControllerPlayer
from controllers.controller_match import ControllerMatch
from controllers.controller_round import ControllerRound
from datetime import datetime


class ControllerTournament:

    def __init__(self, model, view):
        self.model = ModelTournament
        self.view = ViewTournament

    def print_tournament_inputs():
        tournament_inputs = ViewTournament.get_tournament_inputs()
        t_i = tournament_inputs
        ViewTournament.start_tournament(t_i[0], t_i[1])
        return tournament_inputs

    def start_tournament():
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def introduce_players():
        return ViewTournament.enter_tournament_players()

    def generate_pairs(round_pairs):
        ViewTournament.announce_round_matches()
        i = 1
        while i < 5:
            first_player = round_pairs[i-1][0].surname
            second_player = round_pairs[i-1][1].surname
            ViewTournament.print_pairs(i, (first_player, second_player))
            i += 1

    def end_tournament():
        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_tournament_results(name, location, start_date, end_date,
                                 description, time_control, players_list,
                                 rounds_list):
        ViewTournament.print_tournament_results(name, location, start_date,
                                                end_date, description,
                                                time_control, players_list,
                                                rounds_list)

    def generate_new_tournament():

        """Funtion to generate a new tournament.

        The function summarizes the results of the work
        previously done to build an MVC model
        for the chess tournament."""

        # Step1 : Initiate tournament

        tournament_inputs = ControllerTournament.print_tournament_inputs()
        t_i = tournament_inputs
        start_date = ControllerTournament.start_tournament()

        # Step2: Adding 8 players to the tournament

        ControllerTournament.introduce_players()

        ModelPlayer.tournament_players.truncate()
        #ModelPlayer.players_database.truncate()

        for _ in range(1, 9):
            player = ControllerPlayer.check_id_number()            
            ModelPlayer.save_tournament_player(player)

            print("DATABASE")
            for player in ModelPlayer.players_database:
                print(player)
            print("TOURNAMENT")
            for player in ModelPlayer.tournament_players:
                print(player)

        rounds_list = []
        pairs_list = []

        deserialized_players = []

        for player in ModelPlayer.tournament_players:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)

        # Step3: Starting a loop of 4 rounds

        for i in range(1, 5):

            # Step4: Starting the Round

            start_date = ControllerRound.start_round(i)

            # Step5: Generating pairs according to Swiss-pairing algorithm

            if len(rounds_list) == 0:
                d_p = deserialized_players
                round_pairs = ModelTournament.generate_pairs_by_ranking(d_p)
                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            elif len(rounds_list) in range(1, 5):
                gen_pairs_by_score = ModelTournament.generate_pairs_by_score
                round_pairs = gen_pairs_by_score(ModelTournament, d_p,
                                                 pairs_list)
                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            print(ViewTournament.star_line)

            # Step6 : Playing the matches of the round

            for i in range(0, 4):

                first_player = round_pairs[i][0]
                f_p = first_player
                second_player = round_pairs[i][1]
                s_p = second_player

                match = ModelMatch("", "", "", "")

                ControllerMatch.start_match(f_p, s_p)
                match = ControllerMatch.print_winner_and_score(f_p, s_p)

                ModelRound.list_of_matches.append(match)

            # Step7 : Ending the round before iterating to other rounds

            end_date = ControllerRound.end_round()

            ControllerRound.print_round_results(i, start_date, end_date,
                                                ModelRound.list_of_matches)

            round = ModelRound(ModelRound.list_of_matches,
                               start_date, end_date)
            rounds_list.append(round)
            ModelRound.list_of_matches = []

        # Step8 : Ending the tournament and printing the results

        end_date = ControllerTournament.end_tournament()
        tournament_players_names = []
        for player in ModelPlayer.tournament_players:
            player_name = player["surname"]
            tournament_players_names.append(player_name)
        ModelTournament.rounds_list = rounds_list

        ControllerTournament.print_tournament_results(t_i[0], t_i[1],
                                                      start_date, end_date,
                                                      t_i[2], t_i[3],
                                                      tournament_players_names,
                                                      rounds_list)

if __name__ == "__main__":

    # Step1: Starting the tournament

    tournament_inputs = ControllerTournament.print_tournament_inputs()
    t_i = tournament_inputs

    start_date = ControllerTournament.start_tournament()

    # Step2: Adding 8 players to the tournament

    ControllerTournament.introduce_players()

    for i in range(1, 9):
        ControllerPlayer.add_player_to_tournament(i)

    rounds_list = []
    pairs_list = []

    # Step3: Starting a loop of 4 rounds

    for i in range(1, 5):

        # Step4: Starting the Round

        start_date = ControllerRound.start_round(i)

        # Step5: Generating pairs according to Swiss-pairing algorithm

        if len(rounds_list) == 0:
            t_p = ModelPlayer.tournament_players
            round_pairs = ModelTournament.generate_pairs_by_ranking(t_p)
            ControllerTournament.generate_pairs(round_pairs)
            pairs_list.extend(round_pairs)

        elif len(rounds_list) in range(1, 5):
            gen_pairs_by_score = ModelTournament.generate_pairs_by_score
            round_pairs = gen_pairs_by_score(ModelTournament, t_p,
                                             pairs_list)
            ControllerTournament.generate_pairs(round_pairs)
            pairs_list.extend(round_pairs)

        print(ViewTournament.star_line)

        # Step6 : Playing the matches of the round

        for i in range(0, 4):

            first_player = round_pairs[i][0]
            f_p = first_player
            second_player = round_pairs[i][1]
            s_p = second_player

            match = ModelMatch("", "", "", "")

            ControllerMatch.start_match(f_p, s_p)
            match = ControllerMatch.print_winner_and_score(f_p, s_p)

            ModelRound.list_of_matches.append(match)

        # Step7 : Ending the round before iterating to other rounds

        end_date = ControllerRound.end_round()

        ControllerRound.print_round_results(i, start_date, end_date,
                                            ModelRound.list_of_matches)

        round = ModelRound(ModelRound.list_of_matches, start_date, end_date)
        rounds_list.append(round)
        ModelRound.list_of_matches = []

    # Step8 : Ending the tournament and printing the results

    end_date = ControllerTournament.end_tournament()
    tournament_players_names = []
    for i in range(0, 8):
        player = ModelPlayer.tournament_players[i].surname
        tournament_players_names.append(player)
    ModelTournament.rounds_list = rounds_list

    tournament = ModelTournament(t_i[0], t_i[1], start_date, end_date, t_i[2],
                                 t_i[3], tournament_players_names)

    ControllerTournament.print_tournament_results(t_i[0], t_i[1], start_date,
                                                  end_date, t_i[2], t_i[3],
                                                  tournament_players_names,
                                                  rounds_list)
