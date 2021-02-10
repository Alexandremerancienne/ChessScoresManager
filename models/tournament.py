from player import Player
from match import Match
from round import Round
from datetime import datetime

class Tournament:

    """A class to represent a tournament.

    Attributes :

    - Name of the tournament;
    - Location;
    - Start date (YYY-MM-DD HH:MM:SS);
    - End date (YYY-MM-DD HH:MM:SS);
    - Number of rounds (default value 4); 
    - List of rounds;
    - List of players;
    - Time control: Rapid (game between 10 and 60 minutes), Blitz (game under 10 minutes), Bullet (game under 3 minutes); 
    - Description of the tournament."""

    number_of_rounds = 0

    def __init__(self, name, location, start_date, end_date, rounds_list, players_list, time_control, description):
        Tournament.number_of_rounds +=1
        self._name = name
        self._location = location
        self._start_date = start_date
        self._end_date = end_date
        self._rounds_list = rounds_list
        self._players_list = players_list
        self._time_control = time_control
        self._description = description

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
        return self._time_control

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


if __name__ == "__main__":

    """Testing program generating a tournament.

    The program first generates 8 players from Player class,
    then divides the 8 players into 4 matches from Match class,
    then plays the 4 matches to generate results,
    then creates a round from Round class.

	The program finally repeats the above steps to generate 4 rounds. 

    As no pairing algorithm has been defined yet, 
    the matches are defined arbitrarily."""


    #Step 1: Creating the tournament

    tournament = Tournament("", "", "", "", "", "", "", "")

    name = input("Please enter the name of the tournament: ")
    while not all (x.isalpha() or x.isspace() for x in name):
        print("Please enter a valid name of tournament.")
        name = input("Please enter the name of the tournament.")
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

        players.append(player.family_name)

    #Step 3: Generating a loop of 4 rounds

    rounds_list = []

    for i in range(1,5):
    
        round = Round("", "", "")

        #Step 4: For each round, starting the clock to initiate the round

        print("--------------------------------------")
        input(f"Press Enter to start Round {i}")
        start_date = datetime.now().replace(microsecond=0)

        #Step 5: Dividing the players into 4 matches from Match class

        print("--------------------------------------")
        print("Number of matches : 4")   

        list_of_matches = []

        for i in range(1, 5):

            match = Match("", "", "", "")
            match.first_player = players[2*i-2]
            match.second_player = players[2*i-1]
            print("--------------------------------------")
            print(f"Match {i}: {match.first_player}, {match.second_player}")

            #Step 6: For each loop of matches, playing the match

            result = input(f"Enter result for {match.first_player} - W (wins), L (loose), D (draw): ")
            while str(result) not in "wWlLdD" or result.isalpha() is False:
                print("Please enter a result (W/L/D).")
                result = input(f"Enter result for {match.first_player} - W (wins), L (loose), D (draw): ")
                continue
            print("--------------------------------------")
		    
            if result in "wW":
                result = Match.first_player_wins(match)
                print(f"{match.first_player} wins")

            elif result in "lL":
                result = Match.second_player_wins(match)
                print(f"{match.second_player} wins")

            elif result in "dD":
                result = Match.draw(match)
                print(f"Draw")

            print(match)

            list_of_matches.append(match)

        #Step 7: Mixing the list of players for the next loop 

        players.insert(0,players.pop())
        
        #Step 8: Printing the round

        print("--------------------------------------")
        print(f"Round results : {list_of_matches}")

        round.matches = list_of_matches
        round.start_date = start_date
        input("Press Enter to end the round")
        end_date = datetime.now().replace(microsecond=0)
        round.end_date = end_date
        rounds_list.append(round)

    #Step 9: Printing the tournament

    tournament.rounds_list = rounds_list
    tournament.players_list = players

    print("--------------------------------------")
    input(f"Press Enter to end the tournament")
    end_date = datetime.now().date()
    tournament.end_date = end_date

    print("--------------------------------------")
    print(tournament)