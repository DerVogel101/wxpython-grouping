import itertools
import math
from functools import reduce
from operator import or_

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
        all_combs_set = set()
        for comb in all_combinations_list:
            comb_set = set(comb)
            if -1 in comb_set:
                comb_set.remove(-1)
            all_combs_set.add(frozenset(comb_set))
        return all_combs_set

    def get_round(self):
        return self._rounds[self._current_round_ind - 1]

    def generate_next_round(self) -> None:
        """Returns the number of possible unique Round combinations."""
        if self.__all_combinations == set():
            raise StopIteration("No more rounds can be generated.")

        combs_iter = self.__all_combinations.copy()
        while True:
            for group_comb in combs_iter:
                combs_working = self.__all_combinations.copy()
                current_groups = [group_comb]
                combs_working.remove(group_comb)
                break
            new_group, new_working_set, outcast, not_found = self.__add_next_group(current_groups, combs_working, [], 2, self.__groups_per_round, False)

            new_working_set.update(outcast)
            if not not_found:
                break
            combs_iter.remove(group_comb)
        self.__all_combinations = new_working_set
        self._rounds[self._current_round_ind] = new_group
        self._current_round_ind += 1


    def __add_next_group(self, old_group: list[frozenset], old_working_set: set[frozenset], outcast: list[frozenset],
                         self_id: int, max_id: int, not_found: bool) -> tuple[list[frozenset], set[frozenset], list[frozenset], bool]:
        # Use the provided objects directly so that changes are in place.
        working_set = old_working_set
        working_group = old_group
        reject = False

        # Iterate over a snapshot of the set to avoid modifying the set during iteration.
        for group_comb in list(working_set):
            for comb in working_group:
                groupmask = reduce(or_, (1 << x for x in group_comb), 0)
                combmask = reduce(or_, (1 << x for x in comb), 0)
                if groupmask & combmask:
                    reject = True
                    break
                # if not group_comb.isdisjoint(comb):
                #     reject = True
                #     break
            if reject:
                reject = False
                continue
            working_group.append(group_comb)
            working_set.remove(group_comb)
            break
        else:
            raise StopIteration("No more rounds can be generated.")

        if self_id != max_id:
            while True:
                try:
                    new_group, new_working_set, outcast, not_found = self.__add_next_group(
                        working_group, working_set, outcast, self_id + 1, max_id, False
                    )
                    if not not_found:
                        return new_group, new_working_set, outcast, False
                except StopIteration:
                    outcast.append(working_group.pop())
                    return old_group, working_set, outcast, True
                # Update the in-place variables for the next iteration.
                working_group, working_set, outcast = new_group, new_working_set, outcast

        return working_group, working_set, outcast, False



    def get_remaining_rounds(self) -> int:
        return self._max_rounds - self._current_round_ind

    def get_max_rounds(self) -> int:
        return self._max_rounds


    def _get_max_possibilities(self) -> int:
        """
Calculate an upper bound on the number of rounds possible.

This method computes an approximate maximum number of rounds that can be generated based on the total number of unique groups
that can be formed and the number of groups per round. The calculation involves adjusting the number of people to ensure that
it is divisible by the group size by adding placeholders if necessary.

Given
~~~~~
- :math:`P`: Total number of people.
- :math:`G`: Group size.
- :math:`\\text{remainder}`: Number of placeholders (added if :math:`P` is not divisible by :math:`G`).
- :math:`P_{adjusted}`: Total number of participants (including placeholders).
- :math:`R`: The number of groups formed in a round.
- :math:`\\text{total_groups}`: The product of binomial coefficients for each group.

Formula Steps
~~~~~~~~~~~~~
1. **Adjustment of the Number of People**

  - Calculate the remainder when the number of people is divided by the group size:
      .. math::
        \\text{remainder} = P \\mod G
  - If the remainder is not zero, increase the number of people by the missing value to allow even group division:
      .. math::
        P_{adjusted} = P + (G - \\text{remainder}) \\quad \\text{if } \\text{remainder} \\neq 0
    If there is no remainder, the number of people remains unchanged:
      .. math::
        P_{adjusted} = P

2. **Calculation of Groups per Round**

  - The number of groups per round is given by:
      .. math::
        R = \\frac{P_{adjusted}}{G}

3. **Total Number of Unique Groups (Combinations)**

  - The number of possible unique groups is given by the binomial coefficient:
      .. math::
        \\text{total_groups} = \\binom{P_{adjusted}}{G}

4. **Maximum Number of Rounds**

  - The upper bound for the number of rounds is given by:
      .. math::
        \\text{max_rounds} = \\frac{\\text{total_groups}}{R}

This formula calculates the total number of unique round combinations based on the number of participants and the group size, taking into account any necessary placeholders.
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
