import random
from models.model_player import ModelPlayer
from id_database.id_numbers_database import players_id_database

"""A script to generate random players from random variables
   (ID numbers, rankings, gender, first name, last name)"""


class RandomPlayer:

    """A class to define random players.

    Attributes:

    - ID number;
    - Ranking;
    - Gender;
    - First name;
    - Last name."""

    # Database of random rankings.
    # Each player has a unique ranking.

    players_rankings_database = [48.1, 11.1, 61.9, 97.6, 53.8, 22.6, 43.7, 44.9, 79.6, 98.6, 77.5, 18.1, 21.7, 49.9,
                                 45.5, 64.3, 44.7, 80.5, 12.2, 89.2, 27, 22.9, 56.7, 60.6, 68.6, 53.1, 43, 3.4, 66.4,
                                 33.3, 23.7, 39.7, 74.5, 64.3, 32.8, 34.1, 99.7, 61.5, 74.4, 88.6, 80.3, 85.8, 83,
                                 37.4, 96.6, 77.7, 40.1, 43.3, 53.3, 26.1, 81.2, 19.6, 30, 89.8, 44.3, 24.2, 93.1,
                                 92.4, 3.6, 58.3, 65.2, 14.4, 30.5, 92.8, 22.3, 54.4, 51.3, 45.3, 49.7, 46.7, 39.8,
                                 35.1, 50.1, 48.7, 3.7, 26.1, 51.2, 2.3, 23.7, 48.4, 57.1, 41.3, 96.1, 49.4, 43.6,
                                 22.8, 69.6, 50.3, 20.5, 50.2, 27.3, 45.4, 67.9, 38.8, 24, 44.9, 3.5, 51.6, 55.1,
                                 76.2, 50.2, 96.7, 12.2, 37.9, 35.1, 41.4, 41.2, 54.4, 37, 52.8, 15.2, 23.5, 41.3,
                                 52.1, 21.1, 82.2, 81.2, 50.4, 47.8, 8.2, 18.9, 56.7, 24.9, 37.5, 42.7, 59.2, 99.1,
                                 9.4, 46.5, 81.6, 34.6, 77.2, 66.9, 31.1, 53.5, 25.4, 26, 2.9, 45.2, 69.8]

    # Player's gender to be randomly chosen.

    gender = ['M', 'F']

    # Database of male first names.

    male_first_names = ['Pasquale', 'Parker', 'Eldridge', 'Jonathon', 'Hipolito', 'Reuben', 'Zackary', 'Gerard',
                        'Lucius', 'Gregory', 'Anderson', 'John', 'Reggie', 'Randell', 'Ahmad', 'Rex', 'Tracy', 'Robt',
                        'Dean', 'Wally', 'Porter', 'Odell', 'Lawrence', 'Reed', 'Millard', 'Jerrell', 'Steve',
                        'Martin', 'Leslie', 'Issac', 'Mathew', 'Reid', 'Stevie', 'Emory', 'Jewell', 'Chas', 'Carol',
                        'Benedict', 'Huey', 'Tony', 'Matthew', 'Ivan', 'Manuel', 'Hollis', 'Arnold', 'Ian', 'Alphonse',
                        'Geoffrey', 'Rickie', 'Mauro']

    # Database of female first names.

    female_first_names = ['Iris', 'Marti', 'Fernande', 'Audrie', 'Cathi', 'Lindsy', 'Maribeth', 'Kimberely',
                          'Shaquana', 'Ada', 'Krysten', 'Dori', 'Joetta', 'Jana', 'Natividad', 'Carolina', 'Trina',
                          'Elin', 'Grazyna', 'Dionna', 'Zetta', 'Janene', 'Magen', 'Leilani', 'Neely', 'Tammy',
                          'Melinda', 'Rosalina', 'Nicol', 'Rachael', 'Soila', 'Inga', 'Tammi', 'Fumiko', 'Mui',
                          'Sharee', 'Thi', 'Christene', 'Mari', 'Louetta', 'Antonina', 'Dagny', 'Melody', 'Manda',
                          'Erlinda', 'Patti', 'Vicenta', 'Detra', 'Jutta', 'Leticia']

    # Database of last names.

    last_names = ['Moon', 'Bray', 'Mann', 'Banks', 'Roman', 'Walton', 'Neal', 'Keith', 'Bentley', 'Bender', 'Ortiz',
                  'Walter', 'Nash', 'Meyers', 'Good', 'Cabrera', 'Hatfield', 'Buchanan', 'Robinson', 'Russell', 'Haas',
                  'Bush', 'Stokes', 'York', 'Mccall', 'Hodge', 'Lucas', 'Obrien', 'Davidson', 'Watson', 'Wyatt',
                  'Morgan', 'Acevedo', 'House', 'Larson', 'Barnett', 'Mcmillan', 'Christensen', 'Richmond', 'Horne',
                  'Garcia', 'Calhoun', 'Fuentes', 'Berg', 'Hunter', 'Bates', 'Montoya', 'Steele', 'Page', 'Leonard']

    def __init__(self, last_name, first_name, id_number, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.id_number = id_number
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def generate_random_player():

        """A function to generate a random player
        based on  the random variables defined above."""

        random_last_name = random.choice(RandomPlayer.last_names)

        random_gender = random.choice(RandomPlayer.gender)
        if random_gender == 'M':
            random_first_name = random.choice(RandomPlayer.male_first_names)
        elif random_gender == 'F':
            random_first_name = random.choice(RandomPlayer.female_first_names)

        i = len(ModelPlayer.players_database)
        id_number = players_id_database[i]
        random_ranking = RandomPlayer.players_rankings_database[i]

        random_year = random.randrange(1921, 2003)
        random_month = random.randrange(1, 12)
        if random_month in [1, 3, 5, 7, 8, 10, 12]:
            random_day = random.randrange(1, 31)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randrange(1, 30)
        elif random_month == 2:
            random_day = random.randrange(1, 28)
        if len(str(random_month)) == 1:
            random_month = str(random_month).zfill(2)
        if len(str(random_day)) == 1:
            random_day = str(random_day).zfill(2)
        random_birth_date = f'{random_year}.{random_month}.{random_day}'

        random_player = ModelPlayer(random_last_name, random_first_name,
                                    id_number, random_birth_date,
                                    random_gender, random_ranking)

        return random_player


if __name__ == "__main__":

    for i in range(1, 9):
        player = RandomPlayer.generate_random_player()
        serialized_player = ModelPlayer.serialize_player(player)
        ModelPlayer.save_player_to_database(serialized_player)
