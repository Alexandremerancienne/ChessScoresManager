import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_player import ModelPlayer
from views.view_player import ViewPlayer
from operator import attrgetter
from tinydb import TinyDB, Query
from id_database.id_numbers_database import id_numbers_database


class ControllerPlayer:

    def __init__(self, model, view):
        self.model = ModelPlayer
        self.view = ViewPlayer

    def check_id_number():
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

        p_d = ModelPlayer.players_database
        player_features = ViewPlayer.get_player_inputs(p_d)
        p_f = player_features
        index = len(ModelPlayer.players_database)
        id_number = id_numbers_database[index]
        player = ModelPlayer(p_f[0], p_f[1], id_number, p_f[2], p_f[3],
                             p_f[4])
        ViewPlayer.print_player(player)
        print(ViewPlayer.line)
        return player

    def print_player_ranking():
        ViewPlayer.get_player_ranking()
        player_name = ViewPlayer.get_player_name()
        p_n = player_name
        for i in range(0, 8):
            if p_n in ModelPlayer.tournament_players[i].surname:
                player_ranking = ModelPlayer.tournament_players[i].ranking
                p_r = player_ranking
                return ViewPlayer.print_player_ranking(p_n, p_r)

    def change_ranking():
        player_name = ViewPlayer.change_player_ranking()
        p_n = player_name
        for i in range(0, 8):
            if p_n in ModelPlayer.tournament_players[i].surname:
                new_ranking = ViewPlayer.enter_new_ranking()
                ModelPlayer.tournament_players[i].ranking = new_ranking
                ViewPlayer.print_player_new_ranking(p_n, new_ranking)

    def sort_tournament_players_by_name():

        names_sorted = sorted(ModelPlayer.tournament_players,
                              key=attrgetter("surname"))
        length = len(names_sorted)
        names_list = [names_sorted[i].surname for i in range(length)]
        ViewPlayer.print_tournament_players_by_name(names_list)

    def sort_tournament_players_by_ranking():

        rankings_sorted = sorted(ModelPlayer.tournament_players,
                                 key=attrgetter("ranking"), reverse=True)
        ViewPlayer.print_tournament_players_by_ranking(rankings_sorted)

    def sort_all_players_by_name():

        names_sorted = sorted(ModelPlayer.database_players,
                              key=attrgetter("surname"))
        length = len(names_sorted)
        names_list = [names_sorted[i].surname for i in range(length)]
        ViewPlayer.print_all_players_by_name(names_list)

    def sort_all_players_by_ranking():

        rankings_sorted = sorted(ModelPlayer.database_players,
                                 key=attrgetter("ranking"), reverse=True)
        ViewPlayer.print_all_players_by_ranking(rankings_sorted)


if __name__ == "__main__":

    ControllerPlayer.search_player()

    ControllerPlayer.print_player_ranking()

    ControllerPlayer.change_ranking()

    ControllerPlayer.sort_tournament_players_by_name()

    ControllerPlayer.sort_tournament_players_by_ranking()

    ControllerPlayer.sort_all_players_by_name()

    ControllerPlayer.sort_all_players_by_ranking()
