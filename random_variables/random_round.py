import json

"""A script to generate random round from random variables
   (start date, end date)"""


class RandomRound:

    """A class to define random rounds.

    Attributes:

    - Start date;
    - End date."""

    # List of the random start dates already attributed

    random_dates_attributed = []

    # Database of start dates

    random_start_dates = ['2021.03.03 (08:30:00)', '2021.03.03 (11:00:00)',
                          '2021.03.03 (15:00:00)', '2021.03.03 (17:30:00)',
                          '2021.03.15 (08:30:00)', '2021.03.15 (11:00:00)',
                          '2021.03.15 (15:00:00)', '2021.03.15 (17:30:00)',
                          '2021.05.20 (08:30:00)', '2021.05.20 (11:00:00)',
                          '2021.05.20 (15:00:00)', '2021.05.20 (17:30:00)',
                          '2021.06.29 (08:30:00)', '2021.06.29 (11:00:00)',
                          '2021.06.29 (15:00:00)', '2021.06.29 (17:30:00)',
                          '2021.07.01 (08:30:00)', '2021.07.01 (11:00:00)',
                          '2021.07.01 (15:00:00)', '2021.07.01 (17:30:00)',
                          '2021.07.10 (08:30:00)', '2021.07.10 (11:00:00)',
                          '2021.07.10 (15:00:00)', '2021.07.10 (17:30:00)',
                          '2021.08.29 (08:30:00)', '2021.08.29 (11:00:00)',
                          '2021.08.29 (15:00:00)', '2021.08.29 (17:30:00)',
                          '2021.09.07 (08:30:00)', '2021.09.07 (11:00:00)',
                          '2021.09.07 (15:00:00)', '2021.09.07 (17:30:00)',
                          '2021.09.13 (08:30:00)', '2021.09.13 (11:00:00)',
                          '2021.09.13 (15:00:00)', '2021.09.13 (17:30:00)',
                          '2021.10.03 (08:30:00)', '2021.10.03 (11:00:00)',
                          '2021.10.03 (15:00:00)', '2021.10.03 (17:30:00)']

    # Database of end dates

    random_end_dates = ['2021.03.03 (10:00:00)', '2021.03.03 (13:00:00)',
                        '2021.03.03 (17:00:00)', '2021.03.03 (19:00:00)',
                        '2021.03.15 (10:00:00)', '2021.03.15 (13:00:00)',
                        '2021.03.15 (17:00:00)', '2021.03.15 (19:00:00)',
                        '2021.05.20 (10:00:00)', '2021.05.20 (13:00:00)',
                        '2021.05.20 (17:00:00)', '2021.05.20 (19:00:00)',
                        '2021.06.29 (10:00:00)', '2021.06.29 (13:00:00)',
                        '2021.06.29 (17:00:00)', '2021.06.29 (19:00:00)',
                        '2021.07.01 (10:00:00)', '2021.07.01 (13:00:00)',
                        '2021.07.01 (17:00:00)', '2021.07.01 (19:00:00)',
                        '2021.07.10 (10:00:00)', '2021.07.10 (13:00:00)',
                        '2021.07.10 (17:00:00)', '2021.07.10 (19:00:00)',
                        '2021.08.29 (10:00:00)', '2021.08.29 (13:00:00)',
                        '2021.08.29 (17:00:00)', '2021.08.29 (19:00:00)',
                        '2021.09.07 (10:00:00)', '2021.09.07 (13:00:00)',
                        '2021.09.07 (17:00:00)', '2021.09.07 (19:00:00)',
                        '2021.09.13 (10:00:00)', '2021.09.13 (13:00:00)',
                        '2021.09.13 (17:00:00)', '2021.09.13 (19:00:00)',
                        '2021.10.03 (10:00:00)', '2021.10.03 (13:00:00)',
                        '2021.10.03 (17:00:00)', '2021.10.03 (19:00:00)']

    def __init__(self, name, location, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def generate_random_round_inputs(j, i):

        """A function to generate random inputs
        for a round (start date, end date)
        based on  the random variables defined above."""

        random_start_date = RandomRound.random_start_dates[j-1+4*(i-1)]
        random_end_date = RandomRound.random_end_dates[j-1+4*(i-1)]
        RandomRound.random_dates_attributed.append(random_start_date)

        return(random_start_date, random_end_date)

    def serialize_random_round(self):

        """A function to serialize a random round.
        A serialized round is defined by the following keys:

        - Matches ;
        - Start date ;
        - End date."""

        serialized_round = {}
        json.dumps(serialized_round, default=str)
        serialized_round["matches"] = self.matches
        serialized_round["start_date"] = self.start_date
        serialized_round["end_date"] = self.end_date
        return serialized_round
