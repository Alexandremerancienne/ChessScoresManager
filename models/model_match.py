import os
import sys
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


class ModelMatch:

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
        return(f"[({self.first_player}, {self.first_score}),"
               + f"({self.second_player}, {self.second_score})]")

    def __str__(self):
        return(f"Result: [({self.first_player}, {self.first_score}),"
               + f"({self.second_player}, {self.second_score})]")

    @property
    def first_score(self):
        return self._first_score

    @first_score.setter
    def first_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0 - 0.5 - 1).")
        self._first_score = new_score

    @property
    def second_score(self):
        return self._second_score

    @second_score.setter
    def second_score(self, new_score):
        if new_score not in [0, 0.5, 1]:
            print("Please enter a valid score (0 - 0.5 - 1).")
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

    def serialize_match(self):

        """A function to serialize a match.
        A serialized match is defined by the following keys:

        - First player ;
        - First score ;
        - Second player ;
        - Second score."""

        serialized_match = {}
        json.dumps(serialized_match, default=str)
        serialized_match["first_player"] = self.first_player
        serialized_match["first_score"] = self.first_score
        serialized_match["second_player"] = self.second_player
        serialized_match["second_score"] = self.second_score
        return serialized_match

    def deserialize_match(serialized_match):

        """A function to deserialize a match."""

        first_player = serialized_match["first_player"]
        first_score = serialized_match["first_score"]
        second_player = serialized_match["second_player"]
        second_score = serialized_match["second_score"]
        deserialized_match = ModelMatch(first_player=first_player,
                                        first_score=first_score,
                                        second_player=second_player,
                                        second_score=second_score)
        return deserialized_match
