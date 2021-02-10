from player import Player
from match import Match
from datetime import datetime


class Round:

    """A class to represent a round.

    Attributes:

    - Round matches (presented as a list);
    - Name of the round;
    - Start date (YYY-MM-DD HH:MM:SS);
    - End date (YYY-MM-DD HH:MM:SS);"""

    number_of_rounds = 0

    def __init__(self, matches, start_date, end_date):
        Round.number_of_rounds += 1
        self._matches = matches
        self._round_name = "Round " + str(Round.number_of_rounds)
        self._start_date = start_date
        self._end_date = end_date

    def __repr__(self):
        return(f"{self.round_name} \nDates: from {self.start_date}, to {self.end_date}\
            \nMatches: {self._matches}\n\n")

    def __str__(self):
        return(f"{self.round_name}: \nDates: from {self.start_date}, to {self.end_date}\
            \nMatches: {self._matches}")

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, new_matches):
        if not (isinstance(new_matches, list) and len(new_matches) == 4):
            print("Please enter a valid list of matches.")
        self._matches = new_matches

    @property
    def round_name(self):
        return self._round_name.capitalize()

    @round_name.setter
    def round_name(self, new_name):
        if not isinstance(new_name, int):
            print("Please enter a valid round name.")
        self._first_name = new_name

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD HH:MM:SS).")
        self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD HH:MM:SS).")
        self._end_date = new_date


if __name__ == "__main__":

    """Testing program generating a round.

    The program first generates 8 players from Player class,
    then divides the 8 players into 4 matches from Match class,
    then plays the 4 matches to generate results,
    then creates a round.

    As no pairing algorithm has been defined yet, 
    the matches are defined arbitrarily."""

    #Step 1: Generating 8 players from Player class

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

    #Step 2: Starting the clock to initiate the round

    print("--------------------------------------")
    input("Press Enter to start the round")
    start_date = datetime.now().replace(microsecond=0)

    #Step 3: Dividing the players into 4 matches from Match class

    print("--------------------------------------")
    print("Number of matches : 4")   

    list_of_matches = []

    for i in range(1, 5):

        match = Match("", "", "", "")
        match.first_player = players[2*i-2]
        match.second_player = players[2*i-1]
        print("--------------------------------------")
        print(f"Match {i}: {match.first_player}, {match.second_player}")

        #Step 4: For each loop, playing the match to generate results

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

    print("--------------------------------------")
    print(f"Round results : {list_of_matches}")
   
    #Step 5: Creating a round

    round = Round("", "", "")
    round.matches = list_of_matches
    round.start_date = start_date
    input("Press Enter to finish the round")
    end_date = datetime.now().replace(microsecond=0)
    round.end_date = end_date

    print("--------------------------------------")
    print(round)
