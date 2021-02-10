from player import Player
from datetime import datetime


class Match:

    """A class to represent a match.

    Attributes:

    - Player 1;
    - Score of player 1: 0 (looses), 0.5 (draw), 1 (wins);
    - Player 2;
    - Score of player 2: 0 (looses), 0.5 (draw), 1 (wins)."""

    def __init__(self, first_player, first_score, second_player, second_score):
        self.first_player = first_player
        self._first_score = first_score
        self.second_player = second_player
        self._second_score = second_score

    def __repr__(self):
    	return(f"[({self.first_player}, {self.first_score}), ({self.second_player}, {self.second_score})]") 

    def __str__(self):
        return(f"Result: [({self.first_player}, {self.first_score}), ({self.second_player}, {self.second_score})]")

    @property
    def first_score(self):
        return self._first_score

    @first_score.setter
    def first_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0   0.5   1).")
        self._first_score = new_score

    @property
    def second_score(self):
        return self._second_score

    @second_score.setter
    def second_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0   0.5   1).")
        self._second_score = new_score

    def first_player_wins(self):
        self.second_score = 0
        self.first_score = 1

    def second_player_wins(self):
        self.second_score = 1
        self.first_score = 0

    def draw(self):
        self.second_score = 0.5
        self.first_score = 0.5

if __name__ == "__main__":

    """Testing program generating 3 matches.

    The program first generates 2 players from Player class,
    then creates 3 matches with the following outcomes:

    - Player 1 wins;
    - Player 2 wins;
    - Draw

    And print the corresponding results."""

    next_match = []
    print("Next Match")

    #Step 1: Generating 2 players

    for i in range(1, 3):

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

        next_match.append(player.family_name)

    #Step 2: Generating a match
    
    match = Match("", "", "", "")

    match.first_player = next_match[0]
    match.second_player = next_match[1]

    print("--------------------------------------")
    print(f"Next match: {match.first_player} vs {match.second_player}")
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