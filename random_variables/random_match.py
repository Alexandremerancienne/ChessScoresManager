import random
from models.model_match import ModelMatch


class RandomMatch:

    """A class to define random matches."""

    def generate_random_match(first_player, second_player):

        """A function to generate a random match
        between two random players."""

        f_p = first_player.last_name
        s_p = second_player.last_name

        match = ModelMatch("", "", "", "")

        score_options = ["W", "L", "D"]

        result = random.choice(score_options)

        if result == "W":
            result = ModelMatch.first_player_wins(match)
            first_player.score += 1
            match = ModelMatch(f_p, 1, s_p, 0)
            return match

        elif result == "L":
            result = ModelMatch.second_player_wins(match)
            second_player.score += 1
            match = ModelMatch(f_p, 0, s_p, 1)
            return match

        elif result == "D":
            result = ModelMatch.draw(match)
            first_player.score += 0.5
            second_player.score += 0.5
            match = ModelMatch(f_p, 0.5, s_p, 0.5)
            return match
