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

    """A Controller for Tournament Class.

    The controller can perform the following actions :

    - Print the inputs of a tournament ;
    - Start a tournament ;
    - Enter the players of a tournament ;
    - Generate the pairs of a tournament ;
    - End a tournament ;
    - Print the ending message ;
    - Print the results of a tournament."""

    def __init__(self, model, view):
        self.model = ModelTournament
        self.view = ViewTournament

    def print_tournament_inputs():

        """A function to print the inputs of a tournament."""

        tournament_inputs = ViewTournament.get_tournament_inputs()
        t_i = tournament_inputs
        ViewTournament.start_tournament(t_i[0], t_i[1])
        return tournament_inputs

    def start_tournament():

        """A function to start a tournament."""

        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def introduce_players():

        """A function to enter the players of a tournament."""

        return ViewTournament.enter_tournament_players()

    def generate_pairs(round_pairs):

        """A function to generate the pairs of a tournament."""

        ViewTournament.announce_round_matches()
        i = 1
        while i < 5:
            first_player = round_pairs[i-1][0].last_name
            second_player = round_pairs[i-1][1].last_name
            ViewTournament.print_pairs(i, (first_player, second_player))
            i += 1

    def end_tournament():

        """A function to end a tournament."""

        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_ending_message():

        """A function to print the ending message of a tournament."""

        return ViewTournament.print_ending_message()

    def print_tournament_results(name, location, start_date, end_date,
                                 description, time_control, players_list,
                                 rounds):

        """A function to print the results of a tournament."""

        ViewTournament.print_tournament_results(name, location, start_date,
                                                end_date, description,
                                                time_control, players_list,
                                                rounds)

    def generate_new_tournament():

        """A funtion to generate a new tournament."""

        # Step 1 : Starting a tournament

        tournament_inputs = ControllerTournament.print_tournament_inputs()
        t_i = tournament_inputs
        start_date = ControllerTournament.start_tournament()

        # Step 2: Adding 8 players to the tournament

        ControllerTournament.introduce_players()

        ModelPlayer.tournament_players.truncate()

        for _ in range(1, 9):
            player = ControllerPlayer.check_id_number()
            ModelPlayer.save_tournament_player(player)

        ModelTournament.rounds_list = []
        pairs_list = []

        deserialized_players = []

        for player in ModelPlayer.tournament_players:
            print(player)
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)

        # Step 3: Starting a loop of 4 rounds

        deserialized_rounds = []

        for i in range(1, 5):

            # Step 4: Starting a round

            start_date = ControllerRound.start_round(i)

            # Step 5: Generating matches according to Swiss-pairing algorithm

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

            # Step 6 : Playing the matches of the round

            deserialized_matches = []

            for i in range(0, 4):

                first_player = round_pairs[i][0]
                f_p = first_player
                second_player = round_pairs[i][1]
                s_p = second_player

                ControllerMatch.start_match(f_p, s_p)
                match = ControllerMatch.print_winner_and_score(f_p, s_p)

                serialized_match = ModelMatch.serialize_match(match)
                s_m = serialized_match
                ModelRound.list_of_matches.append(s_m)

                deserialized_match = ModelMatch.deserialize_match(s_m)
                deserialized_matches.append(deserialized_match)

            # Step 7 : Ending the round before starting the next one

            end_date = ControllerRound.end_round()

            ControllerRound.print_round_results(i, start_date, end_date,
                                                deserialized_matches)

            round = ModelRound(deserialized_matches,
                               start_date, end_date)

            deserialized_rounds.append(round)

            serialized_round = ModelRound.serialize_round(round)

            round_serialized_matches = []
            round_deserialized_matches = serialized_round['matches']
            for match in round_deserialized_matches:
                serialized_match = ModelMatch.serialize_match(match)
                round_serialized_matches.append(serialized_match)
            serialized_round['matches'] = round_serialized_matches

            ModelTournament.rounds_list.append(serialized_round)

            ModelRound.list_of_matches = []

        # Step 8 : Ending the tournament and printing the results

        end_date = ControllerTournament.end_tournament()
        tournament_players_names = []
        for player in ModelPlayer.tournament_players:
            player_name = player["last_name"]
            tournament_players_names.append(player_name)

        ControllerTournament.print_ending_message()

        ControllerTournament.print_tournament_results(t_i[0], t_i[1],
                                                      start_date, end_date,
                                                      t_i[2], t_i[3],
                                                      tournament_players_names,
                                                      deserialized_rounds)

        tournament = ModelTournament(t_i[0], t_i[1], start_date, end_date,
                                     t_i[2], t_i[3], tournament_players_names)

        ModelPlayer.tournament_players.insert({"tournament_name": t_i[0]})
        ModelPlayer.tournament_players.insert({"tournament_location": t_i[1]})
        start_date_string = start_date.strftime("%Y.%m.%d (%H:%M:%S)")
        s_d_s = start_date_string
        ModelPlayer.tournament_players.insert({"tournament_year": s_d_s[:4]})

        tournament.rounds = ModelTournament.rounds_list

        serialized_tournment = ModelTournament.serialize_tournament(tournament)

        s_t = serialized_tournment

        ModelTournament.save_tournament_to_tournaments_database(s_t)
