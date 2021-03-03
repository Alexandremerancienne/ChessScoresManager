from models.model_player import ModelPlayer
from views.view_player import ViewPlayer
from operator import attrgetter
from tinydb import Query
from id_database.id_numbers_database import players_id_database


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

        """A function to check the ID number of a player."""

        id_number_tested = ViewPlayer.get_player_id_number()
        if int(id_number_tested) == 0:
            print("Generating new player...\n")
            player = ControllerPlayer.add_player_to_tournament()
            serialized_player = ModelPlayer.serialize_player(player)
            ModelPlayer.save_player_to_database(serialized_player)
            return serialized_player
        Player = Query()
        p_d = ModelPlayer.players_database
        results_p_d = p_d.search(Player.id_number == int(id_number_tested))
        if len(results_p_d) == 0:
            print("ID number not recognized")
            print("Generating new player...\n")
            player = ControllerPlayer.add_player_to_tournament()
            serialized_player = ModelPlayer.serialize_player(player)
            ModelPlayer.save_player_to_database(serialized_player)
            return serialized_player
        elif len(results_p_d) == 1:
            t_p = ModelPlayer.tournament_players
            results_t_p = t_p.search(Player.id_number == int(id_number_tested))
            if len(results_t_p) == 0:
                print("\nIdentification successful")
                print("\nPlayer details:\n")
                for result in results_p_d:
                    player = ModelPlayer.deserialize_player(result)
                    ViewPlayer.print_player(player)
                return result
            elif len(results_t_p) == 1:
                print("Player already registered in tournament")
                print("Generating new player...\n")
                player = ControllerPlayer.add_player_to_tournament()
                serialized_player = ModelPlayer.serialize_player(player)
                ModelPlayer.save_player_to_database(serialized_player)
                return serialized_player

    def add_player_to_tournament():

        """A function to add a player to a tournament."""

        p_d = ModelPlayer.players_database
        player_features = ViewPlayer.get_player_inputs(p_d)
        p_f = player_features
        index = len(ModelPlayer.players_database)
        id_number = players_id_database[index]
        player = ModelPlayer(p_f[0], p_f[1], id_number, p_f[2], p_f[3],
                             p_f[4])
        ViewPlayer.print_player(player)
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

    def change_ranking():

        """A function to change the ranking of a player."""

        player = ModelPlayer.get_player()[0]
        new_ranking = ViewPlayer.change_player_ranking()
        id_number = player["id_number"]
        Player = Query()
        p_d = ModelPlayer.players_database
        result = p_d.search(Player.id_number == id_number)
        p_d.update({'ranking': new_ranking}, Player.id_number == id_number)
        ViewPlayer.confirm_ranking_change()

        
    def sort_players_by_ranking(database):

        """A function to sort the players of a tournament by ranking."""

        deserialized_players = []
        for player in database:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(deserialized_players,
                                key=attrgetter("ranking"), reverse=True)
        for sorted_player in sorted_players:
            print(f"Player {sorted_player.id_number} : "
                  + f"{sorted_player.first_name} {sorted_player.last_name}"
                  + f" - Ranking: {sorted_player.ranking}")

    def sort_players_by_last_name(database):

        """A function to sort the players of a tournament by last name."""

        deserialized_players = []
        for player in database:
            deserialized_player = ModelPlayer.deserialize_player(player)
            deserialized_players.append(deserialized_player)
        sorted_players = sorted(deserialized_players,
                                key=attrgetter("last_name"))
        for sorted_player in sorted_players:
            print(f"Player {sorted_player.id_number} : "
                  + f"{sorted_player.first_name} {sorted_player.last_name}")

    def sort_all_players_by_ranking():

        """A function to sort all the players by ranking."""

        ViewPlayer.print_all_players_by_ranking()
        ControllerPlayer.sort_players_by_ranking(ModelPlayer.players_database)

    def sort_all_players_by_last_name():

        """A function to sort all the players by last name."""

        ViewPlayer.print_all_players_by_last_name()
        database = ModelPlayer.players_database
        ControllerPlayer.sort_players_by_last_name(database)
