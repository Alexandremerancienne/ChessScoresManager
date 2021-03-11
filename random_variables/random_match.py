import random
from models.model_match import ModelMatch


class RandomMatch:

    """A class to define random matches."""

    def generate_random_match(first_player, second_player):

        """A function to generate a random match
        between two random players."""

        match = ModelMatch("", "", "", "")

        score_options = ["W", "L", "D"]

        result = random.choice(score_options)

        if result == "W":
            result = ModelMatch.first_player_wins(match)
            first_player.score += 1
            match = ModelMatch(first_player.last_name, 1, second_player.last_name, 0)
            return match

        elif result == "L":
            result = ModelMatch.second_player_wins(match)
            second_player.score += 1
            match = ModelMatch(first_player.last_name, 0, second_player.last_name, 1)
            return match

        elif result == "D":
            result = ModelMatch.draw(match)
            first_player.score += 0.5
            second_player.score += 0.5
            match = ModelMatch(first_player.last_name, 0.5, second_player.last_name, 0.5)
            return match
