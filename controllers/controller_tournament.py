import os
import sys
import json

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

    def print_ending_message():
        return ViewTournament.print_ending_message()

    def print_tournament_results(name, location, start_date, end_date,
                                 description, time_control, players_list,
                                 rounds):
        ViewTournament.print_tournament_results(name, location, start_date,
                                                end_date, description,
                                                time_control, players_list,
                                                rounds)

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

        ModelTournament.rounds_list = []
        pairs_list = []

        deserialized_players = []

        for player in ModelPlayer.tournament_players:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)

        # Step3: Starting a loop of 4 rounds

        deserialized_rounds = []

        for i in range(1, 5):

            # Step4: Starting the Round

            start_date = ControllerRound.start_round(i)

            # Step5: Generating pairs according to Swiss-pairing algorithm

            if len(ModelTournament.rounds_list) == 0:
                d_p = deserialized_players
                round_pairs = ModelTournament.generate_pairs_by_ranking(d_p)
                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            elif len(ModelTournament.rounds_list) in range(1, 5):
                gen_pairs_by_score = ModelTournament.generate_pairs_by_score
                round_pairs = gen_pairs_by_score(ModelTournament, d_p,
                                                 pairs_list)
                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            print(ViewTournament.star_line)

            # Step6 : Playing the matches of the round
            
            deserialized_matches = []
            
            for i in range(0, 4):

                first_player = round_pairs[i][0]
                f_p = first_player
                second_player = round_pairs[i][1]
                s_p = second_player

                #match = ModelMatch("", "", "", "")

                ControllerMatch.start_match(f_p, s_p)
                match = ControllerMatch.print_winner_and_score(f_p, s_p)
                print("match")
                print(match)

                serialized_match = ModelMatch.serialize_match(match)
                ModelRound.list_of_matches.append(serialized_match)

                deserialized_match = ModelMatch.deserialize_match(serialized_match)
                deserialized_matches.append(deserialized_match)

                print("deserialized_matches")
                print(deserialized_matches)
                print(deserialized_match)

            # Step7 : Ending the round before iterating to other rounds

            end_date = ControllerRound.end_round()

            ControllerRound.print_round_results(i, start_date, end_date,
                                                deserialized_matches)

            round = ModelRound(deserialized_matches,
                               start_date, end_date)

            deserialized_rounds.append(round)
            print("deserialized_round")
            print(deserialized_rounds)

            round.matches = ModelRound.list_of_matches 
            serialized_round = ModelRound.serialize_round(round)         

            print("serialized_round")
            print(serialized_round)   
            ModelTournament.rounds_list.append(serialized_round)

            ModelRound.list_of_matches = []

        # Step8 : Ending the tournament and printing the results

        end_date = ControllerTournament.end_tournament()
        tournament_players_names = []
        for player in ModelPlayer.tournament_players:
            player_name = player["surname"]
            tournament_players_names.append(player_name)

        ControllerTournament.print_ending_message()

        ControllerTournament.print_tournament_results(t_i[0], t_i[1],
                                                      start_date, end_date,
                                                      t_i[2], t_i[3],
                                                      tournament_players_names,
                                                      deserialized_rounds)
        print("deserialized_rounds")
        print(deserialized_rounds)

        tournament = ModelTournament(t_i[0], t_i[1], start_date, end_date,
                                     t_i[2], t_i[3], tournament_players_names)

        print("TOURNAMENT")
        print(tournament)

        tournament.rounds = ModelTournament.rounds_list
        print("TOURNAMENT ROUNDS")
        print(tournament.rounds)

        serialized_tournament = ModelTournament.serialize_tournament(tournament)
        print("SERIALIZED TOURNAMENT")
        print(serialized_tournament)
        ModelTournament.save_tournament_to_tournaments_database(serialized_tournament)
