from model_player import ModelPlayer
from model_match import ModelMatch
from model_round import ModelRound
from datetime import datetime
from operator import attrgetter
from operator import itemgetter

class ModelTournament:

    """A class to represent a tournament.

    Attributes :

    - Name of the tournament;
    - Location;
    - Start date (YYY-MM-DD HH:MM:SS);
    - End date (YYY-MM-DD HH:MM:SS);
    - Number of rounds (default value 4); 
    - List of rounds (tournament starts with an empty list);
    - List of players;
    - Time control: Rapid (game between 10 and 100 minutes), Blitz (game under 10 minutes), Bullet (game under 3 minutes); 
    - Description of the tournament."""

    number_of_rounds = 0

    def __init__(self, name, location, start_date, end_date, players_list, time_control, description):
        ModelTournament.number_of_rounds +=1
        self._name = name
        self._location = location
        self._start_date = start_date
        self._end_date = end_date
        self._players_list = players_list
        self._time_control = time_control
        self._description = description
        self._rounds_list = []

    def __str__(self):
        return(f"End of {self.name} of {self.location}!\n\nDates: from {self.start_date} to {self.end_date} \n\nDescription: {self.description} \n\nParticipants: {self.players_list} \n\nTime control: {self.time_control} \n\nResults: \n\n{self.rounds_list}")

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        if not all (x.isalpha() or x.isspace() for x in new_name):
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
            new_date: datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S").date()
        except ValueError:
            print("Please enter a valid start date (YYYY-MM-DD HH:MM:SS).")
        self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S").date()
        except ValueError:
            print("Please enter a valid start date (YYYY-MM-DD HH:MM:SS).")
        self._end_date = new_date

    @property
    def rounds_list(self):
        return self._rounds_list

    @rounds_list.setter
    def rounds_list(self, new_list):
        if not (isinstance(new_list, list) and len(new_list) == 4):
            print("Please enter a valid list of rounds.")
        self._rounds_list = new_list

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

    def generate_pairs_by_ranking():

        """A function to generate pairs of players 
        before the first round, 
        according to Swiss pairing algorithm.

        The players are ranked in descending order:

        [1,2,3,4,5,6,7,8]
        
        then divided in two groups : 

        [1,2,3,4]   [5,6,7,8]
        then paired as follows :

        (1,5) (2,6) (3,7) (4,8)""" 

        rankings_to_sort = sorted(players, key=attrgetter("ranking"), reverse=True)
        first_half = rankings_to_sort[:4]
        second_half = rankings_to_sort[4:]
        ranking_pairs = [(first_half[i], second_half[i]) for i in range(0,4)]
        return ranking_pairs


    def invert_pair(pair):
        return(pair[1], pair[0])


    def pair_with_other_pair(list1, n, list2, k,i,j):

        """Function to pair list1[n] pair
        with list1[n+k] pair

        input :

                 list1[n]             ...      list1[n+k]         ----->  list1

         (list2[2*n], list2[2*n+1])   ...  (list2[i], list2[j])   ----->  list2
            |______________|____________________|        |
                           |_____________________________|

        output : 

                 list1[n]             ...      list1[n+k]           --->  list1

           (list2[2*n], list2[i])   ...   (list2[2*n+1], list2[j])  --->  list2"""

        list1[n] = (list2[2*n], list2[2*n+i])
        list1[n+k] = (list2[2*n+1], list2[2*n+j])

    def generate_pairs_by_score(self):	

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

        rankings_sorted = sorted(players, key=attrgetter("ranking"), reverse=True)
        scores_to_sort = [(player, player.score) for player in rankings_sorted]
        players_by_score = sorted(scores_to_sort, key=itemgetter(1), reverse = True)
        players_by_score = [pair[0] for pair in players_by_score]
        score_pairs = [(players_by_score[i], players_by_score[i+1]) for i in range(0,7,2)]
        round_pairs = [players_by_score, score_pairs]

        players_by_score = round_pairs[0]
        round_pairs = round_pairs[1]

        for pair in round_pairs:
            inverted_pair = ModelTournament.invert_pair(pair)
            pair_index = round_pairs.index(pair)
            n = pair_index
            if (pair or inverted_pair) in pairs_list:
                print(f"Redundant pair: {pair}")

                if n in range(0,2):
                    ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, 1, 2, 3)
                    inverted_pair = ModelTournament.invert_pair(round_pairs[n])
                    if (round_pairs[n] or inverted_pair) in pairs_list:
                        print(f"Redundant pair: {round_pairs[n]}")
                        ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, 1, 3, 2)
                        if (round_pairs[n] or inverted_pair) in pairs_list:
                            print(f"Redundant pair: {round_pairs[n]}")
                            if n in range(0,2):
                                ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, 2, 4, 5)
                                round_pairs[n+1] = (players_by_score[2*n+2], players_by_score[2*n+3])
                            elif n == 2:
                                ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, -1, -1, -2)   
                                round_pairs[n+1] = (players_by_score[2*n+2], players_by_score[2*n+3])

                elif n == 3:
                    ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, -1, -1, -2)          
                    inverted_pair = Tournament.invert_pair(round_pairs[n])
                    if (round_pairs[n] or inverted_pair) in pairs_list:
                        print(f"Redundant pair: {round_pairs[n]}")
                        ModelTournament.pair_with_other_pair(round_pairs, n, players_by_score, -1, -2, -1)          
                        if (round_pairs[n] or inverted_pair) in pairs_list:
                            print(f"Redundant pair: {round_pairs[n]}")
                            ModelTournament.pair_with_other_pair(round_pairs, n,players_by_score, -2, -3, -4)   
                            round_pairs[n-1] = (players_by_score[4], players_by_score[5])

        return round_pairs


if __name__ == "__main__":

    """Testing program generating a tournament.

    The program first generates 8 players from Player class,
    then divides the 8 players into 4 matches from Match class,
    then plays the 4 matches to generate results,
    then creates a round from Round class.

	The program finally repeats the above steps to generate 4 rounds. 

    For each round, the matches are defined according to Swiss pairing algorithm.

    Before the first round, 
    the players are ranked in descending order:

    [1,2,3,4,5,6,7,8]
    
    then divided in two groups : 

    [1,2,3,4]   [5,6,7,8]

    then paired as follows :

    (1,5) (2,6) (3,7) (4,8)

    After the first round, 
    the players are sorted by score:

    [1,2,3,4,5,6,7,8]
    
    then paired as follows :

    (1,2) (3,4) (5,6) (7,8)

    If a match has already been played 
    (for instance, 1 and 2 already played each other)
    then 1 plays against 3 (and so on...)"""


    #Step 1: Creating the tournament

    tournament = ModelTournament("", "", "", "", "", "", "")

    name = input("Please enter the name of the tournament: ")
    while not all (x.isalpha() or x.isspace() for x in name):
        print("Please enter a valid name of tournament.")
        name = input("Please enter the name of the tournament: ")
        continue
    tournament.name = name

    location = input("Please enter the location of the tournament: ")
    while location.isalpha() is False:
	    print("Please enter a valid location.")        
	    location = input("Please enter the location of the tournament: ")
	    continue
    tournament.location = location

    print(f"Welcome to the {tournament.name} of {tournament.location}!")
    input(f"Press Enter to start the tournament")
    start_date = datetime.now().date()
    tournament.start_date = start_date

    description = input("Please enter a description of the tournament: ")
    tournament.description = description

    time_control = input("Choose time control (blitz, bullet, rapid): ")
    while not time_control.lower() in ("blitz", "rapid", "bullet"):
        print("Please enter a valid time control (blitz, bullet, rapid).")
        time_control = input("Choose time control (blitz, bullet, rapid): ")
        continue
    tournament.time_control = time_control

    #Step 2: Generating 8 players from Player class

    print("Number of players: 8 \n Please enter each player's details")

    players = []

    for i in range(1, 9):
        print("--------------------------------------")
        print(f"Player {i}")

        player = ModelPlayer("", "", "", "", "")
        players.append(player)

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

    tournament.players_list = players

    #Step 3: Generating a loop of 4 rounds

    rounds_list = []
    pairs_list = []

    for i in range(1,5):
        
        round = ModelRound("", "", "")

        #Step 4: For each round, starting the clock to initiate the round

        print("--------------------------------------")
        input(f"Press Enter to start Round {i}")
        start_date = datetime.now().replace(microsecond=0)
        print("--------------------------------------")

        #Step 5: For each round, generating new pairs of players 
        #according to Swiss pairing algorithm :

        #Before first round

        if len(rounds_list) == 0:
            round_pairs = ModelTournament.generate_pairs_by_ranking()
            print(f"List of matches: {round_pairs}")
            pairs_list.extend(round_pairs)

        #After first round

        elif len(rounds_list) in range(1,5):
            round_pairs = ModelTournament.generate_pairs_by_score(tournament)
            print(f"List of matches: {round_pairs}")
            pairs_list.extend(round_pairs)

        #Step 6: Dividing the players into 4 matches from Match class
        #on the basis of the pairs previously defined
        
        list_of_matches = []
        print("--------------------------------------")
        print("Number of matches : 4")   

        for i in range(1,5):

            match = ModelMatch("", "", "", "")
            match.first_player = round_pairs[i-1][0].family_name
            match.second_player = round_pairs[i-1][1].family_name
            print("--------------------------------------")
            print(f"Match {i}: {match.first_player}, {match.second_player}")

            #Step 7: Playing each match of the round

            result = input(f"Enter result for {match.first_player} - W (wins), L (loose), D (draw): ")
            while str(result) not in "wWlLdD" or result.isalpha() is False:
                print("Please enter a result (W/L/D).")
                result = input(f"Enter result for {match.first_player} - W (wins), L (loose), D (draw): ")
                continue
            print("--------------------------------------")
		    
            if result in "wW":
                result = ModelMatch.first_player_wins(match)
                print(f"{match.first_player} wins")
                round_pairs[i-1][0].score +=1

            elif result in "lL":
                result = ModelMatch.second_player_wins(match)
                print(f"{match.second_player} wins")
                round_pairs[i-1][1].score +=1

            elif result in "dD":
                result = ModelMatch.draw(match)
                print(f"Draw")
                round_pairs[i-1][0].score +=0.5
                round_pairs[i-1][1].score +=0.5

            print(match)

            list_of_matches.append(match)
        
        #Step 8: Ending the round

        print("--------------------------------------")
        print(f"Round results : {list_of_matches}")

        round.matches = list_of_matches
        round.start_date = start_date
        end_date = datetime.now().replace(microsecond=0)
        round.end_date = end_date
        rounds_list.append(round)

    #Step 9: Printing the tournament

    tournament.rounds_list = rounds_list

    print("--------------------------------------")
    input(f"Press Enter to end the tournament")
    end_date = datetime.now().date()
    tournament.end_date = end_date

    print("--------------------------------------")
    print(tournament)