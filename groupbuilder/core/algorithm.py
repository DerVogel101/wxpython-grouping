import itertools
import math

from .data_models import GroupConfig, Rounds

class GroupingAlgorithm:
    def __init__(self, config: GroupConfig):
        self._amount_people: int = config.amount_people
        self._group_size: int = config.group_size
        self._rounds = Rounds(rounds={})

    def get_possibilities(self):
        """Returns the number of possible unique round combinations using mathematical computation."""
        P = self._amount_people
        G = self._group_size

        # Calculate the number of placeholders required
        if P % G == 0:
            H = 0
        else:
            H = G - (P % G)

        # Total number of participants after adding placeholders
        T = P + H

        # Calculate the total number of unique round combinations
        groups_per_round = T // G
        numerator = 1
        for i in range(groups_per_round):
            numerator *= math.comb(T - i * G, G)

        denominator = math.factorial(groups_per_round)
        unique_rounds = numerator // denominator

        return unique_rounds

