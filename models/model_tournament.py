from model_player import ModelPlayer
from model_match import ModelMatch
from model_round import ModelRound
from datetime import datetime
from operator import attrgetter
from operator import itemgetter
from tinydb import TinyDB, Query
import json
import re

class ModelTournament:

    """A class to represent a tournament.

    Attributes :

    - Name of the tournament;
    - Location;
    - ID Number (10-digit unique identification number).    
    - Start date (YYYY.MM.DD HH:MM:SS);
    - End date (YYYY.MM.DD HH:MM:SS);
    - Description of the tournament ;
    - Number of rounds (default value 4);
    - List of rounds (tournament starts with an empty list);
    - Time control:
      Rapid (game between 10 and 100 minutes),
      Blitz (game under 10 minutes),
      Bullet (game under 3 minutes) ;
    - List of players."""
    
    tournaments_database = TinyDB("tournaments_database.json")
    number_of_rounds = 0
    rounds_list = []

    def __init__(self, name, location, start_date,
                 end_date, description, time_control, players_list):
        ModelTournament.number_of_rounds += 1
        self._name = name
        self._location = location
        self._start_date = start_date
        self._end_date = end_date
        self._description = description
        self._time_control = time_control
        self._players_list = players_list
        self._rounds = []

    def __str__(self):
        return(f"Tournament name: {self.name}\n\n"
               + f"Location: {self.location} \n\n"
               + f"Dates: from {self.start_date} to {self.end_date} \n\n"
               + f"Description: {self.description}\n\n"
               + f"Time control: {self.time_control}\n\n"
               + f"Participants: {self.players_list[0]}, "
               + f"{self.players_list[1]}, {self.players_list[2]}"
               + f"{self.players_list[3]}, {self.players_list[4]}"
               + f"{self.players_list[5]}, {self.players_list[6]}"
               + f"{self.players_list[7]}\n\n"
               + "Results:"
               + f"{self.rounds[0]}\n"
               + f"{self.rounds[1]}\n"
               + f"{self.rounds[2]}\n"
               + f"{self.rounds[3]}\n")


    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        if not all(x.isalpha() or x.isspace() for x in new_name):
            print("Please enter a valid name of tournament.")
        self._name = new_name

    @property
    def location(self):
        return self._location.capitalize()

    @location.setter
    def location(self, new_location):
        if new_location.isalpha() is False:
            print("Please enter a valid location.")
        self._location = new_location

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y.%m.%d (%H:%M:%S)").date()
        except ValueError:
            print("Please enter a valid start date (YYYY.MM.DD (HH:MM:SS))")
        self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y.%m.%d (%H:%M:%S)").date()
        except ValueError:
            print("Please enter a valid start date (YYYY.MM.DD (HH:MM:SS))")
        self._end_date = new_date

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, new_list):
        if not (isinstance(new_list, list) and len(new_list) == 4):
            print("Please enter a valid list of rounds.")
        self._rounds = new_list

    @property
    def players_list(self):
        return self._players_list

    @players_list.setter
    def players_list(self, new_list):
        if not (isinstance(new_list, list) and len(new_list) == 8):
            print("Please enter a valid list of players.")
        self._players_list = new_list

    @property
    def time_control(self):
        return self._time_control.capitalize()

    @time_control.setter
    def time_control(self, new_time_control):
        if not new_time_control.lower() in ("blitz", "rapid", "bullet"):
            print("Please enter a valid time control (blitz, bullet, rapid).")
        self._time_control = new_time_control

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def generate_pairs_by_ranking(players):

        """A function to generate pairs of players
        before the first round,
        according to Swiss pairing algorithm.

        The players are ranked in descending order:

        [1,2,3,4,5,6,7,8]

        then divided in two groups :

        [1,2,3,4]   [5,6,7,8]
        then paired as follows :

        (1,5) (2,6) (3,7) (4,8)"""

        rankings_to_sort = sorted(players, key=attrgetter("ranking"),
                                  reverse=True)

        first_half = rankings_to_sort[:4]
        second_half = rankings_to_sort[4:]
        ranking_pairs = [(first_half[i], second_half[i]) for i in range(0, 4)]
        return ranking_pairs

    def invert_pair(pair):
        return(pair[1], pair[0])

    def swiss_pair(list1, n, list2, k, i, j):

        """Function to pair list1[n] pair
        with list1[n+k] pair

        input :

                 list1[n]             ...      list1[n+k]         ----->  list1

         (list2[2*n], list2[2*n+1])   ...  (list2[i], list2[j])   ----->  list2
            |______________|____________________|        |
                           |_____________________________|

        output :

                 list1[n]             ...      list1[n+k]           --->  list1

           (list2[2*n], list2[i])   ...   (list2[2*n+1], list2[j])  --->  list2

        In our program, list1 corresponds to the list of matches,
        while list2 correponds to the list of players :

                  match[n]             ...       match[n+k]
        (players[2*n], players[2*n+1])     (players[i], players[j])

        As players[2*n] already played against players[2*n+1], we want to pair
        players[2*n] with players[i], and players[2*n+1] with players[j]
        as follows :

                  match[n]             ...       match[n+k]
          (players[2*n], players[i])     (players[2*n+1], players[j])"""

        list1[n] = (list2[2*n], list2[2*n+i])
        list1[n+k] = (list2[2*n+1], list2[2*n+j])

    def generate_pairs_by_score(self, players, pairs_list):

        """A function to generate pairs of players
        after the first round,
        according to Swiss pairing algorithm.

        The players are sorted by score:

        [1,2,3,4,5,6,7,8]

        then paired as follows :

        (1,2) (3,4) (5,6) (7,8)

        If a match has already been played
        (for instance, 1 and 2 already played each other)
        then 1 plays against 3 (and so on...)

        Note : if player 7 and 8 already played each other,
        the same logic applies backwards :
        7 plays with 6 (and 8 plays with 5)"""

        rankings_sorted = sorted(players, key=attrgetter("ranking"),
                                 reverse=True)
        scores_to_sort = [(player, player.score) for player in rankings_sorted]
        players_by_score = sorted(scores_to_sort, key=itemgetter(1),
                                  reverse=True)
        players_by_score = [pair[0] for pair in players_by_score]
        score_pairs = [(players_by_score[i], players_by_score[i+1])
                       for i in range(0, 7, 2)]
        round_pairs = [players_by_score, score_pairs]

        players_by_score = round_pairs[0]
        pbs = players_by_score
        round_pairs = round_pairs[1]
        r_p = round_pairs

        for pair in round_pairs:
            inverted_pair = ModelTournament.invert_pair(pair)
            pair_index = r_p.index(pair)
            n = pair_index
            if (pair or inverted_pair) in pairs_list:
                print(f"\nRedundant pair: ")
                for elt in pair:
                    print(elt)

                if n in range(0, 2):
                    ModelTournament.swiss_pair(r_p, n, pbs, 1, 2, 3)
                    inverted_pair = ModelTournament.invert_pair(r_p[n])
                    if (r_p[n] or inverted_pair) in pairs_list:
                        print(f"\nRedundant pair: ")
                        for elt in r_p[n]:
                            print(elt)
                        ModelTournament.swiss_pair(r_p, n, pbs, 1, 3, 2)
                        if (r_p[n] or inverted_pair) in pairs_list:
                            print(f"\nRedundant pair: ")
                            for elt in r_p[n]:
                                print(elt)
                            if n in range(0, 2):
                                ModelTournament.swiss_pair(r_p, n, pbs,
                                                           2, 4, 5)
                                r_p[n+1] = (pbs[2*n+2], pbs[2*n+3])
                            elif n == 2:
                                ModelTournament.swiss_pair(r_p, n, pbs,
                                                           -1, -1, -2)
                                r_p[n+1] = (pbs[2*n+2], pbs[2*n+3])

                elif n == 3:
                    ModelTournament.swiss_pair(r_p, n, pbs, -1, -1, -2)
                    inverted_pair = ModelTournament.invert_pair(r_p[n])
                    if (r_p[n] or inverted_pair) in pairs_list:
                        print(f"Redundant pair: {r_p[n]}")
                        ModelTournament.swiss_pair(r_p, n, pbs, -1, -2, -1)
                        if (r_p[n] or inverted_pair) in pairs_list:
                            print(f"Redundant pair: {r_p[n]}")
                            ModelTournament.swiss_pair(r_p, n, pbs, -2, -3, -4)
                            r_p[n-1] = (pbs[4], pbs[5])

        return round_pairs

    def serialize_tournament(self):
        serialized_tournament = {}
        json.dumps(serialized_tournament, default=str)
        serialized_tournament["name"] = self.name
        serialized_tournament["location"] = self.location
        serialized_tournament["start_date"] = self.start_date.strftime("%Y.%m.%d (%H:%M:%S)")
        serialized_tournament["end_date"] = self.end_date.strftime("%Y.%m.%d (%H:%M:%S)")
        serialized_tournament["description"] = self.description
        serialized_tournament["time_control"] = self.time_control
        serialized_tournament["players_list"] = self.players_list
        serialized_tournament["rounds"] = self.rounds
        return serialized_tournament

    def deserialize_tournament(serialized_tournament):
        name = serialized_tournament["name"]
        location = serialized_tournament["location"]
        start_date = serialized_tournament["start_date"]
        end_date = serialized_tournament["end_date"]
        description = serialized_tournament["description"]
        time_control = serialized_tournament["time_control"]
        players_list = serialized_tournament["players_list"]
        rounds = serialized_tournament["rounds"]
        deserialized_tournament = ModelTournament(name=name, location=location, start_date=start_date, end_date = end_date, description=description, time_control=time_control, players_list=players_list)
        deserialized_tournament.rounds = rounds
        return deserialized_tournament    

    def save_tournament_to_tournaments_database(self):
        ModelTournament.tournaments_database.insert(self)

    def search_tournament_with_name():
        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        tournament_name = input("\nEnter tournament name: ")
        tournament_name = tournament_name.title()
        results = t_d.search(Tournament.name == tournament_name)            
        number_of_results = 0
        if len(results) == 0:
            print("\nNo tournament found")
        elif len(results) == 1:
            print(f"\nNumber of results: 1")
            for result in results:
                print(result)
                return result
        elif len(results) > 1:
            serialized_tournaments = []
            for result in results:
                number_of_results +=1
            print(f"\nNumber of results: {number_of_results}\n")
            i = 1
            for result in results:
                print(f"[{i}] {result['name']} of {result['location']}")
                print(f"Start : {result['start_date']}")
                print(f"End : {result['end_date']}\n")
                i +=1
            tournament_choice = input("Choose number to select a tournament\n")
            while not (isinstance(tournament_choice, int) and tournament_choice in range(1, len(results))):
                try: 
                    tournament_choice = int(tournament_choice)
                    break                 
                except Exception:
                    tournament_choice = input("Choose number to select a tournament\n") 
            search_result = results[tournament_choice-1]
            tournament



            return serialized_tournaments



            if sort_players in "aA":
                Tournament = Query()
                t_p = ModelPlayer.tournament_players
                results = t_d.search(Tournament.name == tournament_name)            



                deserialized_tournaments = []
                for serialized_tournament in serialized_tournaments:
                    d_r = ModelTournament.deserialize_tournament(serialized_tournament)
                    deserialized_tournaments.append(d_r)
                for deserialized_tournament in deserialized_tournaments:
                    print(f"Tournament: {deserialized_tournament.name} of {deserialized_tournament.location}")
                    print(f"Date: from {deserialized_tournament.start_date} to {deserialized_tournament.end_date}")
                    tournament_players_list = deserialized_tournament.players_list

                    rankings_to_sort = []
                    for player in tournament_players_list:
                        print(player)
                        player_and_ranking = (player, player.ranking)
                        rankings_to_sort.append(player_and_ranking)           
                    sorted_tournament_players = sorted((rankings_to_sort), key=lambda k:k[1])
                    print("Players sorted by ranking :\n")
                    for sorted_player in sorted_tournament_players:
                        print(f"Player: {sorted_player[0]} - Ranking : {sorted_player[1]}")

            
            elif sort_players in "bB":    
                deserialized_tournaments = []
                for serialized_tournament in serialized_tournaments:
                    d_r = ModelTournament.deserialize_tournament(serialized_tournament)
                    deserialized_tournaments.append(d_r)
                for deserialized_tournament in deserialized_tournaments:
                    print(f"Tournament: {deserialized_tournament.name} of {deserialized_tournament.location}")
                    print(f"Date: from {deserialized_tournament.start_date} to {deserialized_tournament.end_date}")
                    print("Players sorted by last name :\n")
                    sorted_players = sorted((deserialized_tournament.players_list))
                    for sorted_player in sorted_players:
                        print(sorted_player)

    def search_tournament_players_by_location():

        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        location = input("\nEnter tournament location: ")
        location = location.capitalize()
        results = t_d.search(Tournament.location == location)            
        number_of_results = 0
        if len(results) == 0:
            print("No tournament found")
        elif len(results) > 0:
            deserialized_results = []
            for result in results:
                number_of_results += 1
            print(f"Number of results: {number_of_results}")
            sort_players = input("Sort players: \n" 
                                  + "[A] By ranking\n" 
                                  + "[B] By last name")
            while sort_players not in "aAbB":
                sort_players = input("Sort players: \n" 
                                     + "[A] By ranking\n" 
                                     + "[B] By last name")
                continue
            if sort_players in "aA":
                deserialized_result = ModelTournament.deserialize_tournament(deserialized_result)
                d_r = deserialized_result
                deserialized_results.append(d_r)
                for d_r in deserialized_results:
                    sorted_result = sorted(d_r["players_list"], key=attrgetter("ranking"), reverse=True)
                    print(f"Tournament : {sorted_result.name}")
                    print("\nPlayers sorted by ranking :\n")
                    print(sorted_result)         
            
            elif sort_players in "bB":    
                deserialized_result = ModelTournament.deserialize_tournament(deserialized_result)
                d_r = deserialized_result
                deserialized_results.append(d_r)
                for d_r in deserialized_results:
                    sorted_result = sorted(d_r["players_list"], key=attrgetter("last_name"))
                    print(f"Tournament : {sorted_result.name}")
                    print("\nPlayers sorted by last name :\n")
                    print(sorted_result)   

    def search_tournament_players_by_year():

        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        year = input("\nEnter tournament year: ")
        results = t_d.search(Tournament.start_date == year)            
        number_of_results = 0
        if len(results) == 0:
            print("No tournament found")
        elif len(results) > 0:
            deserialized_results = []
            for result in results:
                number_of_results += 1
            print(f"Number of results: {number_of_results}")
            sort_players = input("Sort players: \n" 
                                  + "[A] By ranking\n" 
                                  + "[B] By last name")
            while sort_players not in "aAbB":
                sort_players = input("Sort players: \n" 
                                     + "[A] By ranking\n" 
                                     + "[B] By last name")
                continue
            if sort_players in "aA":
                deserialized_result = ModelTournament.deserialize_tournament(deserialized_result)
                d_r = deserialized_result
                deserialized_results.append(d_r)
                for d_r in deserialized_results:
                    sorted_result = sorted(d_r["players_list"], key=attrgetter("ranking"), reverse=True)
                    print(f"Tournament : {sorted_result.name}")
                    print("\nPlayers sorted by ranking :\n")
                    print(sorted_result)         
            
            elif sort_players in "bB":    
                deserialized_result = ModelTournament.deserialize_tournament(deserialized_result)
                d_r = deserialized_result
                deserialized_results.append(d_r)
                for d_r in deserialized_results:
                    sorted_result = sorted(d_r["players_list"], key=attrgetter("last_name"))
                    print(f"Tournament : {sorted_result.name}")
                    print("\nPlayers sorted by last name :\n")
                    print(sorted_result)


    def print_matching_results(results):

        i = 1
        for result in results:
            print(f"[{i}] {result['name']} of {result['location']}")
            print(f"Start : {result['start_date']}")
            print(f"End : {result['end_date']}\n")
            i +=1
        tournament_choice = input("Choose number to select a tournament\n")
        while not (isinstance(tournament_choice, int) and tournament_choice in range(1, len(results))):
            try: 
                tournament_choice = int(tournament_choice)
                break                 
            except Exception:
                tournament_choice = input("Choose number to select a tournament\n") 
        search_result = results[tournament_choice-1]
        print("\n")
        players_sorted = input("Order tournament players:\n\n" 
                               + "By ranking [A]\n"
                               + "By last name [B]\n")
        print("\n")

        if players_sorted in "bB":
            players_sorted_by_last_name = sorted(search_result["players_list"])
            print("Tournament players sorted by last name")
            for player in players_sorted_by_last_name:
                print(player)



    def get_tournament():

        Tournament = Query()
        t_d = ModelTournament.tournaments_database
        choice = input("\nSearch tournament (Enter option number): \n\n"
                        + "By name [A]\n" 
                        + "By location [B]\n"
                        + "By year [C]\n\n")

        while choice not in "aAbBcC":
            print("Choose a correct number.")
            choice = input("\nSearch tournament (Enter option number): \n\n"
                        + "By name [A]\n" 
                        + "By location [B]\n"
                        + "By year [C]\n\n")
            continue

        if choice in "aA":
            name = input("\nEnter tournament name: ")
            name = name.title()
            results = t_d.search(Tournament.name == name)            
            number_of_results = 0
            if len(results) == 0:
                print("No tournament found")
            elif len(results) > 0:
                for result in results:
                    number_of_results +=1
                print(f"\nNumber of results: {number_of_results}\n")
            ModelTournament.print_matching_results(results)

        elif choice in "bB":
            location = input("\nEnter tournament location: ")
            location = location.capitalize()
            results = t_d.search(Tournament.location == location)
            number_of_results = 0
            if len(results) == 0:
                print("No tournament found\n")
            elif len(results) > 0:
                for result in results:
                    number_of_results +=1
                print(f"Number of results: {number_of_results}\n")
            ModelTournament.print_matching_results(results)

        elif choice in "cC":
            year = input("\nEnter tournament year: ")
            results = []
            number_of_results = 0
            for tournament in t_d:
                if re.match(year, tournament["start_date"]):
                    number_of_results += 1
                    results.append(tournament)
            if number_of_results == 0:
                print("No tournament found\n")
            elif number_of_results > 0:
                print(f"Number of results: {number_of_results}\n") 
            ModelTournament.print_matching_results(results)


    def get_all_tournaments():
        print("\nDatabase of all tournaments\n")
        all_tournaments = ModelTournament.tournaments_database.all()
        i = 1
        for tournament in all_tournaments:
            print(f"[{i}] {tournament['name']} of {tournament['location']}")
            print(f"Start : {tournament['start_date']}")
            print(f"End : {tournament['end_date']}\n")
            i +=1
        tournament_choice = input("Choose a number to see tournament details\n")
        while not (isinstance(tournament_choice, int) and tournament_choice in range(1, len(all_tournaments))):
            try: 
                tournament_choice = int(tournament_choice)
                break                 
            except Exception:
                tournament_choice = input("Choose a number to see tournament details\n") 
        searched_tournament = all_tournaments[tournament_choice-1]

        ModelRound.number_of_rounds = 0
        tournament_rounds = searched_tournament['rounds']
        tournament_deserialized_rounds = []
        for round in tournament_rounds:
            round_matches = round['matches']
            round_deserialized_matches = []
            for match in round_matches:
                deserialized_match = ModelMatch.deserialize_match(match)
                round_deserialized_matches.append(deserialized_match)
            round['matches'] = round_deserialized_matches
            deserialized_round = ModelRound.deserialize_round(round)
            tournament_deserialized_rounds.append(deserialized_round)
        searched_tournament['rounds'] = tournament_deserialized_rounds
        print(f"{searched_tournament['name']} of {searched_tournament['location']}")
        print("\n")
        deserialized_tournament = ModelTournament.deserialize_tournament(searched_tournament)
        print(deserialized_tournament)
