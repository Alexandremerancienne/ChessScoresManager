from datetime import datetime
from tinydb import TinyDB, Query
import json


class ModelPlayer:

    """A class to represent a player.

    Attributes:

    - Surname;
    - First name;
    - Date of birth (YYYY.MM.DD);
    - Gender (M/F);
    - Ranking (positive float);
    - Score (initial value 0) ;
    - ID Number (6-digit unique identification number)."""

    players_database = TinyDB("players_database.json")
    tournament_players = TinyDB("tournament_players.json")

    def __init__(self, surname, first_name, id_number, birth_date, gender, ranking):
        self._surname = surname
        self._first_name = first_name
        self._id_number = id_number
        self._birth_date = birth_date
        self._gender = gender
        self._ranking = ranking
        self._score = 0

    def __repr__(self):
        return(f"(Player {self.id_number}: " 
               + f"{self.first_name} {self.surname}"
               + f", Gender: {self.gender}" 
               + f", Date of birth: {self.birth_date}"
               + f", Ranking: {self.ranking}"
               + f", Score: {self.score})")

    def __str__(self):
        return(f"\nPlayer {self.id_number}: "
               + f"{self.first_name} {self.surname}"
               + f", Gender: {self.gender}"
               + f", Date of birth (YYYY.MM.DD): {self.birth_date}" 
               + f",Current ranking: {self.ranking}"
               + f", Score: {self.score}")

    @property
    def surname(self):
        return self._surname.upper()

    @surname.setter
    def surname(self, new_surname):
        if new_surname.isalpha() is False:
            print("Please enter a valid surname.")
        self._surname = new_surname

    @property
    def first_name(self):
        return self._first_name.capitalize()

    @first_name.setter
    def first_name(self, new_first_name):
        if new_first_name.isalpha() is False:
            print("Please enter a valid first name.")
        self._first_name = new_first_name

    @property
    def id_number(self):
        return self._id_number

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, new_date):
        try:
            new_date: datetime.strptime(new_date, "%Y.%m.%d").date()
        except ValueError:
            print("Please enter a valid birth date (YYYY.MM.DD).")
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
        if not new_score % 0.5 == 0:
            print("Please enter a valid score.")
        self._score = new_score

    def serialize_player(self):
        serialized_player = {}
        json.dumps(serialized_player, default=str)
        serialized_player["surname"] = self.surname
        serialized_player["first_name"] = self.first_name
        serialized_player["id_number"] = self.id_number
        serialized_player["birth_date"] = self.birth_date
        serialized_player["gender"] = self.gender
        serialized_player["ranking"] = self.ranking
        serialized_player["score"] = self.score
        return serialized_player

    def deserialize_player(serialized_player):
        surname = serialized_player["surname"]
        first_name = serialized_player["first_name"]
        id_number = serialized_player["id_number"]
        birth_date = serialized_player["birth_date"]
        gender = serialized_player["gender"]
        ranking = serialized_player["ranking"]
        score = serialized_player["score"]
        deserialized_player = ModelPlayer(surname=surname, first_name=first_name, id_number=id_number, birth_date = birth_date, gender=gender, ranking=ranking)
        return deserialized_player        

    def save_tournament_player(self):
        ModelPlayer.tournament_players.insert(self)

    def save_player_to_database(self):
        ModelPlayer.players_database.insert(self)

    def get_player():
        Player = Query()
        p_d = ModelPlayer.players_database
        choice = input("\nSearch player (Enter option number): \n\n"
                        + "By surname [1]\n" 
                        + "By ID number [2]\n\n")

        while choice not in "12":
            print("Choose a correct number.")
            choice = input("Search player (Enter option number): \n\n" 
                            + "By surname [1]\n"
                            + "By ID number [2]\n")
            continue

        if choice == "1":
            surname = input("Enter player surname: ")
            results = p_d.search(Player.surname == surname)
            number_of_results = 0
            if len(results) == 0:
                print("No player found")
            elif len(results) > 0:
                for result in results:
                    number_of_results +=1
                print(f"Number of results: {number_of_results}")
                for result in results:
                    print(result)

        elif choice == "2":
            id_number = input("Enter player ID number: ")
            results = p_d.search(Player.id_number == int(id_number))
            number_of_results = 0
            if len(results) == 0:
                print("No player found\n")
            elif len(results) > 0:
                for result in results:
                    number_of_results +=1
                print(f"Number of results: {number_of_results}\n")           
                for result in results:
                    print(result)

    def get_tournament_players():
        print(ModelPlayer.tournament_players.all())

    def get_all_players():
        print(ModelPlayer.players_database.all())
