from models.model_player import ModelPlayer
from views.view_player import ViewPlayer
from id_database.id_numbers_database import players_id_database
from operator import attrgetter
from tinydb import Query


class ControllerPlayer:

    """A Controller for Player Class.

    The controller can perform the following actions :

    - Check the ID of a player ;
    - Add a player to a tournament ;
    - Print the ranking of a player ;
    - Change the ranking of a player ;
    - Sort the players of a tournament by ranking ;
    - Sort the players of a tournament by last name ;
    - Sort all players by ranking ;
    - Sort all players by last name."""

    def __init__(self, model, view):
        self.model = ModelPlayer
        self.view = ViewPlayer

    def check_id_number():

        """A function to check the ID number of a player.

        If a player has no ID, a new player is generated.

        If an ID number is entered,
        the number is compared to the ID numbers available
        in the models/players_database.json database :

        - If the player is recognized (and not entered yet)
        the player is added to the tournament ;

        - In the absence of matching result
        or if the player has already been entered,
        a new player is generated."""

        id_number_tested = ViewPlayer.get_player_id_number()

        # Player with no ID

        if int(id_number_tested) == 0:
            ViewPlayer.generate_player()
            player = ControllerPlayer.add_player_to_tournament()
            serialized_player = ModelPlayer.serialize_player(player)
            ModelPlayer.save_player_to_database(serialized_player)
            return serialized_player

        Player = Query()
        p_d = ModelPlayer.players_database
        results_p_d = p_d.search(Player.id_number == int(id_number_tested))

        # No matching result with the ID entered

        if len(results_p_d) == 0:
            ViewPlayer.return_unknown_id()
            ViewPlayer.generate_player()
            player = ControllerPlayer.add_player_to_tournament()
            serialized_player = ModelPlayer.serialize_player(player)
            ModelPlayer.save_player_to_database(serialized_player)
            return serialized_player

        # Matching results with the ID entered

        elif len(results_p_d) == 1:
            t_p = ModelPlayer.tournament_players
            results_t_p = t_p.search(Player.id_number == int(id_number_tested))

            # The player is recognized and added to the tournament

            if len(results_t_p) == 0:
                ViewPlayer.return_successful_identification()
                for result in results_p_d:
                    player = ModelPlayer.deserialize_player(result)
                    ViewPlayer.print_player(player)
                    print(ViewPlayer.line)
                    print("\nNext player:\n")                    
                return result

            # The player has already been added to the tournament
            # A new player is generated

            elif len(results_t_p) == 1:
                ViewPlayer.return_player_already_registered()
                ViewPlayer.generate_player()
                player = ControllerPlayer.add_player_to_tournament()
                serialized_player = ModelPlayer.serialize_player(player)
                ModelPlayer.save_player_to_database(serialized_player)
                return serialized_player

    def add_player_to_database():

        """A function to add a new player
        to a JSON database."""

        p_d = ModelPlayer.players_database
        player_features = ViewPlayer.get_player_inputs()
        p_f = player_features
        player_index = len(p_d)
        id_number = players_id_database[player_index]
        player = ModelPlayer(p_f[0], p_f[1], id_number, p_f[2], p_f[3],
                             p_f[4])
        ViewPlayer.print_player(player)
        return player

    def add_player_to_all_players_database():

        """A function to add a new player
        to models/players_database.json"""

        player = ControllerPlayer.add_player_to_database()
        ViewPlayer.confirm_player_addition_to_all_players_database()
        print(ViewPlayer.line)
        return player

    def add_player_to_tournament():

        """A function to add a player to a tournament."""

        player = ControllerPlayer.add_player_to_database()
        ViewPlayer.confirm_player_addition_to_tournament()
        print(ViewPlayer.line)
        return player

    def print_player_ranking():

        """A function to print the ranking of a player."""

        ViewPlayer.get_player_ranking()
        player_name = ViewPlayer.get_player_name()
        p_n = player_name
        for i in range(0, 8):
            if p_n in ModelPlayer.tournament_players[i].last_name:
                player_ranking = ModelPlayer.tournament_players[i].ranking
                p_r = player_ranking
                return ViewPlayer.print_player_ranking(p_n, p_r)

    def announce_new_rankings():

        """A function to announce ranking change for each player
        at the end of a tournament."""

        ViewPlayer.set_new_rankings()

    def recap_ranking(last_name, id_number, ranking):

        """A function to recap the ranking of a player
        before changing it."""

        ViewPlayer.print_player_new_ranking(last_name, id_number, ranking)

    def set_new_rankings(player):

        """A function to change the ranking of a player
        at the end of a tournament. """

        new_ranking = ViewPlayer.change_player_ranking()
        id_number = player["id_number"]
        Player = Query()
        p_d = ModelPlayer.players_database
        p_d.update({'ranking': new_ranking}, Player.id_number == id_number)
        ViewPlayer.confirm_ranking_change()
        return new_ranking

    def change_ranking():

        """A function to change the ranking of a player at any moment.
        To change the ranking of a player at the end of a tournament,
        See set_new_rankings() function above."""

        player = ModelPlayer.get_player()
        if player is not None:
            player = player[0]
            new_ranking = ViewPlayer.change_player_ranking()
            id_number = player["id_number"]
            Player = Query()
            p_d = ModelPlayer.players_database
            p_d.update({'ranking': new_ranking}, Player.id_number == id_number)
            ViewPlayer.confirm_ranking_change()

    def take_fourth(elem):

        """A function to return the third element of a list."""

        return elem[3]

    def slice_results(list_to_slice):

        """A function to split a list into 40 chunks."""

        lts = list_to_slice
        return [lts[i:i + 39] for i in range(0, len(lts), 39)]

    def see_chunks_items(chunked_list):

        """A function to see the items of a list sliced into chunks."""

        if len(chunked_list) <= 40:
            for chunk in chunked_list:
                ViewPlayer.print_sorted_players(chunk)
        elif len(chunked_list) > 40:
            chunks = ControllerPlayer.slice_results(chunked_list)
            for elt in chunks[0]:
                ViewPlayer.print_sorted_players(elt)
            i = 1
            while i < len(chunks):
                see_more = ViewPlayer.see_more_results()
                if see_more in "yY":
                    for elt in (chunks[i]):
                        ViewPlayer.print_sorted_players(elt)
                    i += 1
                elif see_more in "nN":
                    break

    def sort_players_by_ranking(database):

        """A function to sort the players of a tournament by ranking."""

        deserialized_players = []
        for player in database:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(deserialized_players,
                                key=attrgetter("ranking"), reverse=True)
        ControllerPlayer.see_chunks_items(sorted_players)

    def sort_all_players_by_ranking():

        """A function to sort all the players by ranking."""

        ViewPlayer.print_all_players_by_ranking()
        ControllerPlayer.sort_players_by_ranking(ModelPlayer.players_database)

    def sort_players_by_last_name(database):

        """A function to sort the players of a tournament by last name."""

        deserialized_players = []
        for player in database:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(deserialized_players,
                                key=attrgetter("last_name"))
        ControllerPlayer.see_chunks_items(sorted_players)

    def sort_all_players_by_last_name():

        """A function to sort all the players by last name."""

        ViewPlayer.print_all_players_by_last_name()
        database = ModelPlayer.players_database
        ControllerPlayer.sort_players_by_last_name(database)

    def return_search_results(players):

        """A function to return the results of a research in a database
        depending on the content of the result.

        "players" is the output of the research.

        Is players is empty, a message error is printed.
        Is none, the user is asked to select a solution
        among the results of the research.

        The solution is then serialized and returned as the final result."""

        Player = Query()
        p_d = ModelPlayer.players_database

        ViewPlayer.print_number_of_results(players)
        i = 1
        for player in players:
            ViewPlayer.print_players_options()
            i += 1
        player_chosen = ViewPlayer.choose_player()
        searched_player = players[int(player_chosen) - 1]
        s_player = searched_player
        serialized_player = p_d.search(Player.id_number ==
                                       s_player["id_number"])
        deserialized_player = ModelPlayer.deserialize_player(s_player)
        print(deserialized_player)
        return serialized_player

    def search_player_with_last_name():

        """A function to search a player in models/players_database.json
        based on his/her last name."""

        Player = Query()
        p_d = ModelPlayer.players_database

        last_name = ViewPlayer.search_last_name()
        players = p_d.search(Player.last_name == last_name)

        if len(players) == 0:
            ViewPlayer.return_no_player()

        elif len(players) > 0:
            serialized_player = ControllerPlayer.return_search_results(players)
            return serialized_player

    def search_player_with_id_number():

        """A function to search a player in models/players_database.json
        based on his/her ID number."""

        Player = Query()
        p_d = ModelPlayer.players_database

        id_number = ViewPlayer.search_id_number()
        players = p_d.search(Player.id_number == id_number)

        if len(players) == 0:
            ViewPlayer.return_no_player()

        elif len(players) > 0:
            serialized_player = ControllerPlayer.return_search_results(players)
            return serialized_player

    def get_player():

        """A function to retrieve a serialized player
        to players_database.json database.

        The player can be found with his/her last name or ID number."""

        option_number = ViewPlayer.search_player()

        if option_number == "1":
            searched_player = ControllerPlayer.search_player_with_last_name()
            return searched_player

        elif option_number == "2":
            searched_player = ControllerPlayer.search_player_with_id_number()
            return searched_player
