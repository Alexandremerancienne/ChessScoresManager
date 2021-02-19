import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_player import ModelPlayer
from views.view_player import ViewPlayer
from datetime import datetime
from operator import attrgetter

class ControllerPlayer:

	def __init__(self, model, view):
		self.model = model_player
		self.view = view_player

	def add_player_to_tournament():

		player_features = ViewPlayer.get_player_inputs()
		p_f = player_features
		player = ModelPlayer(p_f[0], p_f[1], p_f[2], p_f[3], p_f[4])
		ModelPlayer.tournament_players.append(player)
		return ViewPlayer.print_player(ModelPlayer.p_nb, player)

	def print_player_ranking():
		ViewPlayer.get_player_ranking()
		player_name = ViewPlayer.get_player_name()
		p_n = player_name
		for i in range(0,8):
			if p_n in ModelPlayer.tournament_players[i].family_name:
				player_ranking = ModelPlayer.tournament_players[i].ranking
				p_r = player_ranking
				return ViewPlayer.print_player_ranking(p_n, p_r)

	def change_ranking():
		player_name = View.change_player_ranking()
		p_n = player_name
		for i in range(0,8):
			if p_n in ModelPlayer.tournament_players[i].family_name:
				new_ranking = View.enter_new_ranking()
				ModelPlayer.tournament_players[i].ranking = new_ranking
				return ViewPlayer.print_player_new_ranking(p_n, new_ranking) 

	def sort_tournament_players_by_name():

		names_sorted = sorted(ModelPlayer.tournament_players, key=attrgetter("family_name"))
		length = len(names_sorted)
		names_list = [names_sorted[i].family_name for i in range(length)]
		return ViewPlayer.print_tournament_players_by_name(names_list)


	def sort_tournament_players_by_ranking():

		rankings_sorted = sorted(ModelPlayer.tournament_players, key=attrgetter("ranking"), reverse = True)
		return ViewPlayer.print_tournament_players_by_ranking(rankings_sorted)


	def sort_all_players_by_name():

		names_sorted = sorted(ModelPlayer.database_players, key=attrgetter("family_name"))
		length = len(names_sorted)
		names_list = [names_sorted[i].family_name for i in range(length)]
		return ViewPlayer.print_all_players_by_name(names_list)


	def sort_all_players_by_ranking():

		rankings_sorted = sorted(ModelPlayer.database_players, key=attrgetter("ranking"), reverse = True)
		return ViewPlayer.print_all_players_by_ranking(rankings_sorted)


if __name__ == "__main__":

	for _ in range(1,4):
		ControllerPlayer.add_player_to_tournament()

	ControllerPlayer.print_player_ranking()

	ControllerPlayer.change_ranking()

	ControllerPlayer.sort_tournament_players_by_name()

	ControllerPlayer.sort_tournament_players_by_ranking()

	ControllerPlayer.sort_all_players_by_name()

	ControllerPlayer.sort_all_players_by_ranking()



