from models.model_round import ModelRound
from views.view_round import ViewRound
from datetime import datetime


class ControllerRound:

    """A Controller for Round Class.

    The controller can perform the following actions :

    - Start a round ;
    - End a round ;
    - Print the results of a round."""

    def __init__(self, model, view):
        self.model = ModelRound
        self.view = ViewRound

    def start_round(i):

        """A function to start a round."""

        ViewRound.start_round(i)
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def end_round():

        """A function to end a round."""

        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_round_results(i, start_date, end_date, list_of_matches):

        """A function to print the results of a round."""

        return ViewRound.print_round_results(i, start_date, end_date, list_of_matches)
