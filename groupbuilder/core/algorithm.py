import itertools
import math

from typing_extensions import deprecated

from .data_models import GroupConfig

class GroupingAlgorithm:
    def __init__(self, config: GroupConfig):
        self._amount_people: int = config.amount_people
        self._group_size: int = config.group_size

        self.__unique_rounds = set()

        self.__groups_per_round = self.__get_groups_per_round()

        self.__all_combinations = self.__generate_all_possible_combs()

        self._current_round_ind = 0
        self._max_rounds = self._get_max_possibilities()

        self._rounds = {}


    def __get_groups_per_round(self) -> int:
        remainder = self._amount_people % self._group_size
        if remainder != 0:
            return (self._amount_people + (self._group_size - remainder)) // self._group_size
        else:
            return self._amount_people // self._group_size


    def __generate_all_possible_combs(self) -> set:
        people = list(range(self._amount_people))

        # Add placeholders (-1) for missing people to make total divisible by group size
        total_people = self._amount_people
        while total_people % self._group_size != 0:
            people.append(-1)
            total_people += 1

        all_combinations_list = list(itertools.combinations(people, self._group_size))
        return set([frozenset(x) for x in all_combinations_list])

    def get_round(self):
        return self._rounds[self._current_round_ind - 1]

    def generate_next_round(self) -> None:
        """Returns the number of possible unique Round combinations."""
        if self.__all_combinations == set():
            raise StopIteration("No more rounds can be generated.")

        for i, round_combination in enumerate(itertools.permutations(self.__all_combinations, self.__groups_per_round)):

            flat_combination = list(itertools.chain(*round_combination))

            if len(set(flat_combination)) != len(flat_combination):
                continue

            for comb in round_combination:
                self.__all_combinations.remove(comb)

            round_groups = frozenset(round_combination)
            self.__unique_rounds.add(round_groups)
            self._rounds[self._current_round_ind] = round_groups
            self._current_round_ind += 1
            break

    def get_remaining_rounds(self) -> int:
        return self._max_rounds - self._current_round_ind

    def get_max_rounds(self) -> int:
        return self._max_rounds


    def _get_max_possibilities(self) -> int:
        """
        Calculate an upper bound on the number of rounds possible.

        This function computes an approximate maximum number of rounds that can be generated based on the total number of unique groups
        that can be formed and the number of groups per round. The calculation involves adjusting the number of people to ensure that
        it is divisible by the group size by adding placeholders if necessary.

        Let:

        - :math:`P` be the original number of people.
        - :math:`G` be the group size.
        - :math:`P'` be the adjusted number of people defined as:

          .. math::
             P' = P + \left(G - \left(P \mod G\right)\right)

          if :math:`P` is not divisible by :math:`G`, and :math:`P' = P` otherwise.

        - :math:`R` be the number of groups per round:

          .. math::
             R = \frac{P'}{G}

        - The total number of unique groups is given by the combination:

          .. math::
             \binom{P'}{G}

        The maximum number of rounds is then approximated by:

        .. math::
             \max \, \text{Rounds} = \frac{\binom{P'}{G}}{R}

        **Parameters:**

          - **amount_people** (*int*):
            The number of people available.

          - **group_size** (*int*):
            The number of people per group.

        **Returns:**

          - *int*:
        An approximate maximum number of rounds that can be generated.
        """
        # Adjust the number of people to include placeholders if needed.
        P = self._amount_people
        G = self._group_size

        remainder = P % G
        if remainder != 0:
            P_adjusted = P + (G - remainder)
        else:
            P_adjusted = P

        # Calculate groups per round (R)
        R = P_adjusted // G

        # Total number of unique groups (combinations)
        total_groups = math.comb(P_adjusted, G)

        # Upper bound on the number of rounds
        max_rounds = total_groups // R
        return max_rounds

    @deprecated("Use generate_next_round instead and get_round to get the current round.")
    def get_possibilities(self):
        """Returns the number of possible unique Round combinations."""
        people = list(range(self._amount_people))

        # Add placeholders (-1) for missing people to make total divisible by group size
        total_people = self._amount_people
        while total_people % self._group_size != 0:
            people.append(-1)
            total_people += 1

        all_combinations = list(itertools.combinations(people, self._group_size))
        unique_rounds = set()

        groups_per_round = total_people // self._group_size

        for round_combination in itertools.permutations(all_combinations, groups_per_round):
            flat_combination = list(itertools.chain(*round_combination))

            if len(set(flat_combination)) != len(flat_combination):
                continue

            round_groups = frozenset(round_combination)
            unique_rounds.add(round_groups)

        return unique_rounds
