import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)

from models.model_player import Player
from views.view_player import View
from datetime import datetime
from operator import attrgetter

class Controller:

	player_number = 0
	list_of_all_players = []
	tournament_players = []


	def __init__(self, model, view):
		self.model = model_player
		self.view = view_player

	def add_player():

		list_of_players = []

		player = Player("", "", "", "", "")

		family_name = input("Enter player's family name: ")
		while family_name.isalpha() is False:
		    print("Please enter a valid family name.")
		    family_name = input("Enter player's family name: ")
		    continue
		player.family_name = family_name

		first_name = input("Enter player's first name: ")
		while first_name.isalpha() is False:
		    print("Please enter a valid first name.")
		    first_name = input("Enter player's first name: ")
		    continue
		player.first_name = first_name

		year_of_birth = input("Enter player's year of birth (YYYY): ")
		month_of_birth = input("Enter player's month of birth (MM): ")
		day_of_birth = input("Enter player's day of birth (DD): ")
		date = (f"{year_of_birth}-{month_of_birth}-{day_of_birth}")
		while True:
		    try:
		        birth_date = datetime.strptime(date, "%Y-%m-%d").date()
		        break
		    except ValueError:
		        print("Please enter a valid birth date (YYYY-MM-DD)")
		        year_of_birth = input("Enter player's year of birth (YYYY): ")
		        month_of_birth = input("Enter player's month of birth (MM): ")
		        day_of_birth = input("Enter player's day of birth (DD): ")
		        date = (f"{year_of_birth}-{month_of_birth}-{day_of_birth}")
		player.birth_date = birth_date

		gender = input("Enter player's gender (M/F): ")
		while str(gender) not in "mMfF" or gender.isalpha() is False:
		    print("Please enter a valid gender (M/F).")
		    gender = input("Enter player's gender (M/F): ")
		    continue
		player.gender = gender

		ranking = input("Enter player's ranking: ")
		while isinstance(ranking, float) is False:
		    try:
		        ranking = float(ranking)
		        break
		    except Exception:
		        print("Please enter a valid ranking (positive float).")
		        ranking = input("Enter player's ranking: ")
		player.ranking = ranking

		player.score = 0
		score = player.score

		Controller.player_number +=1 
		list_of_players.append(player)
		Controller.tournament_players.extend(list_of_players)
		Controller.list_of_all_players.append(player)

		return View.print_player(Controller.player_number, family_name, first_name, birth_date, gender, ranking, score)

	def print_player_ranking():

		print("Player's ranking")
		player_name = input("Enter player's family name: ")
		for i in range(0,8):
			if player_name in Controller.tournament_players[i].family_name:
				player_ranking = (Controller.tournament_players[i].ranking)
				return View.print_player_ranking(player_name, player_ranking)


	def change_ranking():

		print("Change player's ranking")
		player_name = input("Enter player's family name: ")
		for i in range(0,8):
			if player_name in Controller.tournament_players[i].family_name:
				new_ranking = input("Enter new ranking: ")
				while isinstance(new_ranking, float) is False:
					try:
						new_ranking = float(new_ranking)
					except Exception:
						print("Please enter a valid ranking (positive float).")
						new_ranking = input("Enter new ranking: ")
						continue
				Controller.tournament_players[i].ranking = new_ranking
				return View.print_player_new_ranking(player_name, new_ranking) 


	def sort_tournament_players_by_name():

		names_sorted = sorted(Controller.tournament_players, key=attrgetter("family_name"))
		length = len(names_sorted)
		names_list = [names_sorted[i].family_name for i in range(length)]
		return View.print_tournament_players_by_name(names_list)


	def sort_tournament_players_by_ranking():

		rankings_sorted = sorted(Controller.tournament_players, key=attrgetter("ranking"), reverse = True)
		return View.print_tournament_players_by_ranking(rankings_sorted)


	def sort_all_players_by_name():

		names_sorted = sorted(Controller.list_of_all_players, key=attrgetter("family_name"))
		length = len(names_sorted)
		names_list = [names_sorted[i].family_name for i in range(length)]
		return View.print_all_players_by_name(names_list)


	def sort_all_players_by_ranking():

		rankings_sorted = sorted(Controller.list_of_all_players, key=attrgetter("ranking"), reverse = True)
		return View.print_all_players_by_ranking(rankings_sorted)


if __name__ == "__main__":

	for _ in range(1,4):
		Controller.add_player()

	Controller.print_player_ranking()

	Controller.change_ranking()

	Controller.sort_tournament_players_by_name()

	Controller.sort_tournament_players_by_ranking()

	Controller.sort_all_players_by_name()

	Controller.sort_all_players_by_ranking()



