import re

from models.model_match import ModelMatch
from models.model_player import ModelPlayer
from models.model_round import ModelRound
from models.model_tournament import ModelTournament
from views.view_tournament import ViewTournament
from controllers.controller_player import ControllerPlayer
from controllers.controller_match import ControllerMatch
from controllers.controller_round import ControllerRound
from datetime import datetime
from tinydb import Query


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
            first_id = round_pairs[i-1][0].id_number
            second_player = round_pairs[i-1][1].last_name
            second_id = round_pairs[i-1][1].id_number
            ViewTournament.print_pairs(i, ((first_player, first_id),
                                       (second_player, second_id)))
            i += 1

    def end_tournament():

        """A function to end a tournament."""

        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_ending_message():

        """A function to print the ending message of a tournament."""

        return ViewTournament.print_ending_message()

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

                # Optional section to print the round pairs
                # And visualize the functioning of Swiss-pairing algorithm

                print("Round pairs\n")
                print(round_pairs)
                print("\n")

                # End of section

                ControllerTournament.generate_pairs(round_pairs)
                pairs_list.extend(round_pairs)

            elif len(ModelTournament.rounds_list) in range(1, 5):
                gen_pairs_by_score = ModelTournament.generate_pairs_by_score
                round_pairs = gen_pairs_by_score(ModelTournament, d_p,
                                                 pairs_list)

                # Optional section to print the round pairs
                # And visualize the functioning of Swiss-pairing algorithm

                print("Round pairs\n")
                print(round_pairs)
                print("\n")

                # End of section

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

        ControllerTournament.print_ending_message()

        ControllerPlayer.announce_new_rankings()

        for player in ModelPlayer.tournament_players:
            ControllerPlayer.recap_ranking(player["last_name"],
                                           player["id_number"],
                                           player["ranking"])
            new_ranking = ControllerPlayer.set_new_rankings(player)
            player_name = player["last_name"]
            player_id_number = player["id_number"]
            tournament_players_names.append((player_name, player_id_number,
                                             new_ranking))

        ViewTournament.print_tournament_results(t_i[0], t_i[1],
                                                start_date, end_date,
                                                t_i[2], t_i[3],
                                                tournament_players_names,
                                                deserialized_rounds)

        tournament = ModelTournament(t_i[0], t_i[1], start_date, end_date,
                                     t_i[2], t_i[3], tournament_players_names)

        tournament.rounds = ModelTournament.rounds_list

        serialized_tournment = ModelTournament.serialize_tournament(tournament)

        s_t = serialized_tournment

        ModelTournament.save_tournament_to_tournaments_database(s_t)

    def take_third(elem):

        """A function to return the third element of a list."""

        return elem[2]

    def order_players_by_ranking(database):

        """A function to order the players of a tournament database
        by ranking."""

        players_to_sort = database["players_list"]
        players_sorted_by_ranking = sorted(players_to_sort,
                                           key=ControllerTournament.take_third,
                                           reverse=True)
        ViewTournament.order_players_by_ranking(players_sorted_by_ranking)

    def order_players_by_last_name(database):

        """A function to order the players of a tournament database
        by last name."""

        players_sorted_by_last_name = sorted(database["players_list"])
        ViewTournament.order_players_by_last_name(players_sorted_by_last_name)

    def print_matching_results(results):

        """A function to print the results of a research in a database
        depending on the option chosen by the user."""

        # The user selects a tournament among the matching tournaments

        if len(results) == 1:
            search_result = results[0]

        elif len(results) > 1:
            tournament_choice = ViewTournament.choose_tournament(results)
            search_result = results[tournament_choice-1]
            print("\n")

        # The user can print the player of the tournament selected.
        # The players can be ordered by ranking or by last name.

        players_sorted = ViewTournament.define_sorting_option()

        # The players are ordered by ranking

        if players_sorted in "aA":
            ControllerTournament.order_players_by_ranking(search_result)

        # The players are ordered by last name

        elif players_sorted in "bB":
            ControllerTournament.order_players_by_last_name(search_result)

    def search_tournament_by_name():

        """A function to search a tournament
        in models/tournaments_database.json database
        based on its name."""

        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        name = ViewTournament.enter_tournament_name()
        name = name.title()
        results = t_d.search(Tournament.name == name)
        if len(results) == 0:
            ViewTournament.return_no_tournament()
        elif len(results) > 0:
            ViewTournament.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def search_tournament_by_location():

        """A function to search a tournament
        in models/tournaments_database.json database
        based on its location."""

        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        location = ViewTournament.enter_tournament_location()
        location = location.capitalize()
        results = t_d.search(Tournament.location == location)
        if len(results) == 0:
            ViewTournament.return_no_tournament()
        elif len(results) > 0:
            ViewTournament.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def search_tournament_by_year():

        """A function to search a tournament
        in models/tournaments_database.json database
        based on its year."""

        t_d = ModelTournament.tournaments_database
        year = ViewTournament.enter_tournament_year()
        results = []
        number_of_results = 0
        for tournament in t_d:
            if re.match(year, tournament["start_date"]):
                number_of_results += 1
                results.append(tournament)
        if number_of_results == 0:
            ViewTournament.return_no_tournament()
        elif number_of_results > 0:
            ViewTournament.print_number_of_results(len(results))
            ControllerTournament.see_chunks_items(results)
            ControllerTournament.print_matching_results(results)

    def get_tournament():

        """A function to retrieve a tournament
        in models/tournaments_database.json database.

        The research can be based on the name,
        the location or the year of the tournament."""

        choice = ViewTournament.define_search_criteria()

        if choice in "aA":
            ControllerTournament.search_tournament_by_name()

        elif choice in "bB":
            ControllerTournament.search_tournament_by_location()

        elif choice in "cC":
            ControllerTournament.search_tournament_by_year()

    def slice_results(list_to_slice):

        """A function to split a list into 40 chunks."""

        lts = list_to_slice
        return [lts[i:i + 9] for i in range(0, len(lts), 9)]

    def see_chunks_items(chunked_list):

        """A function to see the items of a list sliced into chunks."""

        if len(chunked_list) == 0:
            ViewTournament.return_no_tournament()

        elif len(chunked_list) > 0 and len(chunked_list) <= 9:
            i = 1
            for chunk in chunked_list:
                ViewTournament.print_chunk_tournaments(chunk, i)
                i += 1

        elif len(chunked_list) > 9:
            i = 1
            chunks = ControllerTournament.slice_results(chunked_list)
            for elt in chunks[0]:
                ViewTournament.print_chunk_tournaments(elt, i)
                i += 1
            j = 1
            while j < len(chunks):
                see_more = ViewTournament.see_more_results()
                if see_more in "yY":
                    print("\n")
                    for elt in (chunks[j]):
                        ViewTournament.print_chunk_tournaments(elt, i+j-1)
                        j += 1
                elif see_more in "nN":
                    break

            return len(chunked_list)

    def get_all_tournaments():

        """A function to retrieve all the tournaments
        available in models/tournaments_database.json database."""

        ViewTournament.print_all_tournaments()

        all_tournaments = ModelTournament.tournaments_database.all()

        chunks = ControllerTournament.see_chunks_items(all_tournaments)

        if chunks is None:
            pass

        else:
            see_details_or_not = ViewTournament.see_details_or_not()

            if see_details_or_not in "yY":

                see_tournament_details = ViewTournament.see_tournament_details

                tournament_choice = see_tournament_details(all_tournaments)

                searched_tournament = all_tournaments[int(tournament_choice)-1]

                s_t = searched_tournament
                ModelTournament.deserialize_matches_and_rounds(s_t)

            elif see_details_or_not in "nN":
                pass
