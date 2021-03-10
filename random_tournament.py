import random
import json
from models.model_tournament import ModelTournament
from models.model_match import ModelMatch
from models.model_round import ModelRound
from id_database.id_numbers_database import players_id_database
from random_variables.random_player import RandomPlayer
from random_variables.random_round import RandomRound
from random_variables.random_match import RandomMatch
from models.model_player import ModelPlayer
from tinydb import Query

"""A script to generate random tournament from random variables
   (Name, location, start date, end date, time control mode)
   then random tournaments for chess_scores_manager program.

    The script uses ControllerTournament.generate_new_tournament() function
    and includes random variables generated with the functions
    defined in random_variables.py

    Before playing tournaments,
    100 random players are generated
    with Random.generate_random_player() function
    then added to ModelPlayer.players_database database of all players."""


class RandomTournament:

    """A class to define random tournaments.

    Attributes:

    - Name;
    - Location;
    - Start date;
    - End date;
    - Time control mode."""

    # Database of tournament names

    tournament_names = ['Grand Tournoi', 'Grand Prix', 'Chess international',
                        'Grand Chess Tour', 'Grand Prix', 'Champ', 'Classic',
                        'Cup', 'Chess Olympiads', 'WCF Tournoi',
                        'Champions tournament', 'Chess cup', 'Chess Tour',
                        'Grand Tour', 'Chess Masters',
                        'Chess Academy Tournament', 'Chess Grand Tour',
                        'WCF Grand Prix', 'WCF Grand Tour', 'Chess Games',
                        'WCF Games']

    # Database of tournament locations

    tournament_locations = ['Riga', 'Helsinki', 'Paris', 'Bilbao', 'Prague',
                            'Moscow', 'Kigali', 'Johannesburg', 'Montreal',
                            'Sofia', 'Dakar', 'Abidjan', 'Brasilia', 'Madrid',
                            'Denver', 'Tokyo', 'Roma', 'Mexico', 'Washington',
                            'Pristina', 'Santiago', 'Bogota', 'Medellin',
                            'London', 'Malibu', 'Chicago', 'Nairobi', 'Oslo',
                            'Gaborone', 'Dubai', 'Tehran', 'Milano',
                            'Riyad', 'Mascate', 'Tbilisi', 'Dushanbe', 'Tunis',
                            ' Cape Town', 'Sao Paulo', 'Rio de Janeiro',
                            'Saint Louis', 'New York']

    # Database of start dates

    random_start_dates = ['2021.03.03 (08:00:00)', '2021.03.15 (08:00:00)',
                          '2021.05.20 (08:00:00)', '2021.06.29 (08:00:00)',
                          '2021.07.01 (08:00:00)', '2021.07.10 (08:00:00)',
                          '2021.08.29 (08:00:00)', '2021.09.07 (08:00:00)',
                          '2021.09.13 (08:00:00)', '2021.10.03 (08:00:00)']

    # Database of end dates

    random_end_dates = ['2021.03.03 (19:00:00)', '2021.03.15 (19:00:00)',
                        '2021.05.20 (19:00:00)', '2021.06.29 (19:00:00)',
                        '2021.07.01 (19:00:00)', '2021.07.10 (19:00:00)',
                        '2021.08.29 (19:00:00)', '2021.09.07 (19:00:00)',
                        '2021.09.13 (19:00:00)', '2021.10.03 (19:00:00)']

    # List of the random start dates already attributed

    random_dates_attributed = []

    # List of the ID numbers already attributed

    time_control_options = ['Blitz', 'Rapid', 'Bullet']

    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = ""

    def generate_random_tournament_inputs():

        """A function to generate random inputs
        for a tournament (name, location, time control, description...)
        based on  the random variables defined above."""

        random_name = random.choice(RandomTournament.tournament_names)
        random_location = random.choice(RandomTournament.tournament_locations)
        time_control = RandomTournament.time_control_options
        random_time_control = random.choice(time_control)
        description = ""

        j = len(RandomTournament.random_dates_attributed)

        random_start_date = RandomTournament.random_start_dates[j]
        random_end_date = RandomTournament.random_end_dates[j]
        RandomTournament.random_dates_attributed.append(random_start_date)

        return(random_name, random_location, random_start_date,
               random_end_date, description, random_time_control)

    def serialize_random_tournament(self):

        """A function to serialize a random tournament.
        A random serialized tournament is defined by the following keys:

        - Name of the tournament ;
        - Location ;
        - Start date ;
        - End date ;
        - Description ;
        - Time control ;
        - List of players;
        - List of rounds."""

        serialized_tournament = {}
        json.dumps(serialized_tournament, default=str)
        serialized_tournament["name"] = self.name
        serialized_tournament["location"] = self.location
        serialized_tournament["start_date"] = self.start_date
        serialized_tournament["end_date"] = self.end_date
        serialized_tournament["description"] = self.description
        serialized_tournament["time_control"] = self.time_control
        serialized_tournament["players_list"] = self.players_list
        serialized_tournament["rounds"] = self.rounds
        return serialized_tournament

    def generate_ten_random_tournaments():

        """A funtion to generate five random tournaments."""

        for i in range(1, 11):

            # Step 1 : Starting a tournament with random details
            # (name, location, start date, end date, description, time control)

            t_i = RandomTournament.generate_random_tournament_inputs()

            # Step 2: Adding 8 random players to the tournament
            # Each player has been previously generated randomly
            # with RandomPlayer.generate_random_player() function
            # and added to ModelPlayer.players_database database
            # of all players.

            ModelPlayer.tournament_players.truncate()

            x = len(ModelPlayer.players_database)
            random_id_numbers = players_id_database[:x]

            tournament_random_id_numbers = random.sample(random_id_numbers, 8)

            for random_id_number in tournament_random_id_numbers:
                random_id = random_id_number
                Player = Query()
                t_d = ModelPlayer.players_database
                results_t_d = t_d.search(Player.id_number == int(random_id))
                print(results_t_d)
                for result in results_t_d:
                    ModelPlayer.save_tournament_player(result)

            ModelTournament.rounds_list = []
            pairs_list = []

            deserialized_players = []
            d_p = deserialized_players

            for player in ModelPlayer.tournament_players:
                deserialized_player = ModelPlayer.deserialize_player(player)
                deserialized_players.append(deserialized_player)

            # Step 3: Starting a loop of 4 rounds

            deserialized_rounds = []

            for j in range(1, 5):

                # Step 4: Starting a round

                random_round = RandomRound.generate_random_round_inputs(j, i)
                start_date = random_round[0]

                # Step 5: Generating matches
                # according to Swiss-pairing algorithm

                if len(ModelTournament.rounds_list) == 0:
                    generate_pairs = ModelTournament.generate_pairs_by_ranking
                    round_pairs = generate_pairs(d_p)
                    pairs_list.extend(round_pairs)

                elif len(ModelTournament.rounds_list) in range(1, 5):
                    gen_pairs = ModelTournament.generate_pairs_by_score
                    round_pairs = gen_pairs(ModelTournament, d_p, pairs_list)
                    pairs_list.extend(round_pairs)

                # Step 6 : Playing the matches of the round

                deserialized_matches = []

                for k in range(0, 4):

                    first_player = round_pairs[k][0]
                    f_p = first_player
                    second_player = round_pairs[k][1]
                    s_p = second_player

                    match = RandomMatch.generate_random_match(f_p, s_p)

                    serialized_match = ModelMatch.serialize_match(match)
                    s_m = serialized_match
                    ModelRound.list_of_matches.append(s_m)

                    deserialized_match = ModelMatch.deserialize_match(s_m)
                    deserialized_matches.append(deserialized_match)

                # Step 7 : Ending the round before starting the next one

                end_date = random_round[1]

                round = ModelRound(deserialized_matches,
                                   start_date, end_date)

                deserialized_rounds.append(round)

                serialized_round = RandomRound.serialize_random_round(round)

                round_serialized_matches = []
                round_deserialized_matches = serialized_round['matches']
                for match in round_deserialized_matches:
                    serialized_match = ModelMatch.serialize_match(match)
                    round_serialized_matches.append(serialized_match)
                serialized_round['matches'] = round_serialized_matches

                ModelTournament.rounds_list.append(serialized_round)

                ModelRound.list_of_matches = []

            # Step 8 : Ending the tournament and printing the results

            tournament_players_names = []

            for player in ModelPlayer.tournament_players:
                new_ranking = player["ranking"] + player["score"]
                player_name = player["last_name"]
                player_id_number = player["id_number"]
                tournament_players_names.append((player_name, player_id_number,
                                                 new_ranking))

            tournament = ModelTournament(t_i[0], t_i[1], t_i[2], t_i[3],
                                         t_i[4], t_i[5],
                                         tournament_players_names)

            tournament.rounds = ModelTournament.rounds_list

            serialize_r = RandomTournament.serialize_random_tournament
            serialized_tournment = serialize_r(tournament)

            s_t = serialized_tournment

            ModelTournament.save_tournament_to_tournaments_database(s_t)


if __name__ == "__main__":

    # We generate 8 random players

    for i in range(1, 51):
        player = RandomPlayer.generate_random_player()
        serialized_player = ModelPlayer.serialize_player(player)
        ModelPlayer.save_player_to_database(serialized_player)

    # We generate a random tournament with these 8 players

    RandomTournament.generate_ten_random_tournaments()
