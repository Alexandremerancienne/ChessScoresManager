from models.model_match import ModelMatch
from models.model_player import ModelPlayer
from models.model_round import ModelRound
from views.view_round import ViewRound
from controllers.controller_player import ControllerPlayer
from controllers.controller_match import ControllerMatch
from datetime import datetime

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.dirname(current_dir))
sys.path.append(root_dir)


class ControllerRound:

    def __init__(self, model, view):
        self.model = ModelRound
        self.view = ViewRound

    def start_round(i):
        ViewRound.start_round(i)
        start_date = datetime.now().replace(microsecond=0)
        return start_date

    def end_round():
        end_date = datetime.now().replace(microsecond=0)
        return end_date

    def print_round_results(i, start_date, end_date, list_of_matches):
        return ViewRound.print_round_results(i, start_date, end_date,
                                             list_of_matches)
