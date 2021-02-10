from datetime import datetime


class Player:

    """A class to represent a player.

    Attributes:

    - Family name;
    - First name;
    - Date of birth (YYYY-MM-DD);
    - Gender (M/F);
    - Ranking (positive float);
    - Score (initial value 0)."""

    def __init__(self, family_name, first_name, birth_date, gender, ranking):
        self._family_name = family_name
        self._first_name = first_name
        self._birth_date = birth_date
        self._gender = gender
        self._ranking = ranking
        self._score = 0

    def __repr__(self):
    	return self.family_name

    def __str__(self):
        return(f"Player: {self.first_name} {self.family_name} \
            \nGender: {self.gender} \
            \nDate of birth (YYYY-MM-DD): {self.birth_date} \
            \nCurrent ranking: {self.ranking} \
            \nScore: {self.score}")

    @property
    def family_name(self):
        return self._family_name.upper()

    @family_name.setter
    def family_name(self, new_family_name):
        if new_family_name.isalpha() is False:
            print("Please enter a valid family name.")
        self._family_name = new_family_name

    @property
    def first_name(self):
        return self._first_name.capitalize()

    @first_name.setter
    def first_name(self, new_first_name):
        if new_first_name.isalpha() is False:
            print("Please enter a valid first name.")
        self._first_name = new_first_name

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y-%m-%d").date()
        except ValueError:
            print("Please enter a valid birth date (YYYY-MM-DD).")
        self._birth_date = new_date

    @property
    def gender(self):
        return self._gender.upper()

    @gender.setter
    def gender(self, new_gender):
        if not str(new_gender) in "mMfF" or new_gender.isalpha() is False:
            print("Please enter a valid gender (M/F).")
        self._gender = new_gender

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, new_ranking):
        if not isinstance(new_ranking, float):
            print("Please enter a valid ranking (positive float).")
        self._ranking = new_ranking

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not isinstance(2*new_score, int):
            print("Please enter a valid score.")
        self._score = new_score


if __name__ == "__main__":

    """Testing program generating 8 players."""

    print("Number of players: 8 \n Please enter each player's details")

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

        print("--------------------------------------")
        print(player)
