import json
from datetime import datetime
from tinydb import TinyDB, Query


class ModelPlayer:

    """A class to represent a player.

    Attributes:

    - Last name;
    - First name;
    - Date of birth (YYYY.MM.DD);
    - Gender (M/F);
    - Ranking (positive float);
    - Score (initial value 0) ;
    - ID Number (6-digit unique identification number)."""

    players_database = TinyDB("players_database.json")
    tournament_players = TinyDB("tournament_players.json")

    def __init__(self, last_name, first_name, id_number, birth_date,
                 gender, ranking):
        self._last_name = last_name
        self._first_name = first_name
        self._id_number = id_number
        self._birth_date = birth_date
        self._gender = gender
        self._ranking = ranking
        self._score = 0

    def __repr__(self):
        return(f"(Player {self.id_number}: "
               + f"{self.first_name} {self.last_name}"
               + f", Gender: {self.gender}"
               + f", Date of birth: {self.birth_date}"
               + f", Ranking: {self.ranking}"
               + f", Score: {self.score})")

    def __str__(self):
        return(f"\nPlayer {self.id_number}: "
               + f"{self.first_name} {self.last_name}\n"
               + f"Gender: {self.gender}\n"
               + f"Date of birth (YYYY.MM.DD): {self.birth_date}\n"
               + f"Current ranking: {self.ranking}\n"
               + f"Score: {self.score}")

    @property
    def last_name(self):
        return self._last_name.upper()

    @last_name.setter
    def last_name(self, new_last_name):
        if new_last_name.isalpha() is False:
            print("Please enter a valid last name.")
        self._last_name = new_last_name

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
            new_date = datetime.strptime(new_date, "%Y.%m.%d").date()
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

        """A function to serialize a player.
        A serialized player is defined by the following keys:

        - Last name ;
        - First name ;
        - ID number ;
        - Birth Date ;
        - Gender ;
        - Ranking ;
        - Score."""

        serialized_player = {}
        json.dumps(serialized_player, default=str)
        serialized_player["last_name"] = self.last_name
        serialized_player["first_name"] = self.first_name
        serialized_player["id_number"] = self.id_number
        serialized_player["birth_date"] = self.birth_date
        serialized_player["gender"] = self.gender
        serialized_player["ranking"] = self.ranking
        serialized_player["score"] = self.score
        return serialized_player

    def deserialize_player(serialized_player):

        """A function to deserialize a player."""

        last_name = serialized_player["last_name"]
        first_name = serialized_player["first_name"]
        id_number = serialized_player["id_number"]
        birth_date = serialized_player["birth_date"]
        gender = serialized_player["gender"]
        ranking = serialized_player["ranking"]
        score = serialized_player["score"]
        deserialized_player = ModelPlayer(last_name=last_name,
                                          first_name=first_name,
                                          id_number=id_number,
                                          birth_date=birth_date,
                                          gender=gender, ranking=ranking)
        deserialized_player.score = score
        return deserialized_player

    def save_tournament_player(self):

        """A function to save a serialized player from a tournament
        to tournament_players.json database."""

        ModelPlayer.tournament_players.insert(self)

    def save_player_to_database(self):

        """A function to save a serialized player
        to players_database.json database, registering all players."""

        ModelPlayer.players_database.insert(self)

    def search_player_according_to_criteria(database, criteria):

        """A function to search a player in a database
        according to a defined criteria"""


        results = database.search(Player.criteria == criteria)
        number_of_results = 0
        if len(results) == 0:
            print("No player found\n")
        elif len(results) > 0:
            for result in results:
                number_of_results += 1
            print(f"Number of results: {number_of_results}")


    def get_player():

        """A function to retrieve a serialized player
        to players_database.json database.
        The player can be found with his/her last name or ID number."""

        Player = Query()
        p_d = ModelPlayer.players_database
        choice = input("\nSearch player (Enter option number): \n\n"
                       + "By last name [1]\n"
                       + "By ID number [2]\n\n")

        while choice not in "12":
            print("Choose a correct number.")
            choice = input("Search player (Enter option number): \n\n"
                           + "By last name [1]\n"
                           + "By ID number [2]\n")
            continue

        if choice == "1":
            last_name = input("Enter player last name: ")
            results = p_d.search(Player.last_name == last_name)
            number_of_results = 0
            if len(results) == 0:
                print("No player found\n")
            elif len(results) > 0:
                i = 1
                for result in results:
                    number_of_results += 1
                print(f"Number of results: {number_of_results}")
                for result in results:
                    print(f"\n[{i}] Player {result['id_number']} : {result['first_name']} {result['last_name']}\n")
                    i +=1
                    player_choice = input("Choose number to select a player\n")
                    while not (isinstance(player_choice, int) and player_choice in range(1, len(results))):
                        try: 
                            player_choice = int(player_choice)
                            break                 
                        except Exception:
                            player_choice = input("Choose number to select a tournament\n") 
                    search_result = results[player_choice-1]
                    deserialized_result = ModelPlayer.deserialize_player(search_result)
                    print(deserialized_result)
                    player_searched = p_d.search(Player.id_number == search_result["id_number"])
                    return player_searched

        elif choice == "2":
            id_number = input("Enter player ID number: ")
            while not isinstance(id_number, int):
                try:
                    id_number = int(id_number)
                    break
                except Exception:
                    id_number = input("Enter player ID (positive number): ")
                    continue
            results = p_d.search(Player.id_number == id_number)
            number_of_results = 0
            if len(results) == 0:
                print("No player found\n")
            elif len(results) > 0:
                for result in results:
                    number_of_results += 1
                print(f"Number of results: {number_of_results}")
                for result in results:
                    deserialized_result = ModelPlayer.deserialize_player(result)
                    print(deserialized_result)
                    player_searched = p_d.search(Player.id_number == search_result["id_number"])
                    return player_searched

    def get_tournament_players():

        """A function to retrieve all the serialized players
        from a tournament
        saved in tournament_players.json database"""

        print(ModelPlayer.tournament_players.all())

    def get_all_players():

        """A function to retrieve all the serialized players
        saved in players_database.json database"""

        return ModelPlayer.players_database.all()
