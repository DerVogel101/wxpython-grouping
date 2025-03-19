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

        self._unique_rounds: set = set()

        self.__groups_per_round: int | None = None
        self.__set_groups_per_round()

        self.__all_combinations: set | None = None
        self._max_rounds: int | None = None
        self.__generate_all_possible_combs()

        self._current_round_ind: int = 0


        self._rounds: dict = {}


    def __set_groups_per_round(self) -> None:
        remainder = self._amount_people % self._group_size
        if remainder != 0:
            self.__groups_per_round = (self._amount_people + (self._group_size - remainder)) // self._group_size
        else:
            self.__groups_per_round = self._amount_people // self._group_size


    def __generate_all_possible_combs(self) -> None:
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
        self._max_rounds = len(all_combs_set) // self.__groups_per_round
        self.__all_combinations = all_combs_set

    def get_round(self):
        return self._rounds[self._current_round_ind - 1]

    def get_all_rounds(self):
        return self._rounds

    def generate_next_round(self) -> None:
        """Returns the number of possible unique Round combinations."""
        if self.__all_combinations == set():
            raise StopIteration("No more rounds can be generated.")
        is_reversed = False  # TODO: implement reversed generation for multithreading

        all_person_mask = reduce(or_, (1 << x for x in range(self._amount_people)), 0)

        combs_iter = self.__all_combinations.copy()
        bitmask_cache = {}
        while True:
            for group_comb in combs_iter:
                combs_working = self.__all_combinations.copy()
                current_groups = [group_comb]
                combs_working.remove(group_comb)
                combs_working = list(combs_working)[::-1] if is_reversed else list(combs_working)
                if group_comb not in bitmask_cache:
                    bitmask_cache[group_comb] = reduce(or_, (1 << x for x in group_comb), 0)
                break
            new_group, new_working_set, outcast, not_found = self.__add_next_group(current_groups, combs_working,
                                                                                   [], 2, self.__groups_per_round,
                                                                                   False, bitmask_cache, all_person_mask)

            new_working_set = set(new_working_set)
            new_working_set.update(outcast)
            if not not_found:
                break

            try:
                combs_iter.remove(group_comb)
            except KeyError:
                raise StopIteration("No more rounds can be generated.")
        self.__all_combinations = new_working_set
        self._rounds[self._current_round_ind] = new_group
        self._current_round_ind += 1
        self._unique_rounds.add(frozenset(new_group))

    def __add_next_group(self, old_group: list[frozenset], old_working_set: list[frozenset], outcast: list[frozenset],
                         self_id: int, max_id: int, not_found: bool, bitmask_cache: dict[frozenset, int] = None, all_person_mask: int = None) -> tuple[
        list[frozenset], list[frozenset], list[frozenset], bool]:

        # Initialize bitmask cache if not provided
        if bitmask_cache is None:
            bitmask_cache = {}

        # Use in-place modifications
        working_set = old_working_set
        working_group = old_group


        while working_set:
            group_comb = working_set.pop()  # Efficient O(1) removal instead of iteration

            # Get or compute bitmask for the current group_comb
            if group_comb not in bitmask_cache:
                bitmask_cache[group_comb] = reduce(or_, (1 << x for x in group_comb), 0)
            groupmask = bitmask_cache[group_comb]

            # Check for intersection using cached bitmasks
            if any(groupmask & bitmask_cache[comb] for comb in working_group):
                outcast.append(group_comb)
                continue  # Skip invalid groups

            # Add to group and update precomputed bitmasks
            working_group.append(group_comb)
            bitmask_cache[group_comb] = groupmask
            break
        else:
            raise StopIteration("No more rounds can be generated.")

        # Recursive case
        if self_id != max_id:
            while True:
                try:
                    new_group, new_working_set, outcast, not_found = self.__add_next_group(
                        working_group, working_set, outcast, self_id + 1, max_id, False, bitmask_cache, all_person_mask
                    )
                    if not not_found:
                        return new_group, new_working_set, outcast, False
                except StopIteration:
                    removed_group = working_group.pop()
                    outcast.append(removed_group)
                    bitmask_cache.pop(removed_group, None)  # Remove from cache
                    return old_group, working_set, outcast, True

                working_group, working_set, outcast = new_group, new_working_set, outcast
        
        if not reduce(or_, (1 << x for x in itertools.chain.from_iterable(working_group)), 0) == all_person_mask:
            return working_group, working_set, outcast, True
        
        return working_group, working_set, outcast, False



    def get_remaining_rounds(self) -> int:
        return self._max_rounds - self._current_round_ind

    def get_max_rounds(self) -> int:
        return self._max_rounds

    @staticmethod
    def get_ops_needed(amount_people: int, group_size: int) -> tuple[int, int, int]:
        """
        Calculate an estimate of the number of operations needed to generate all possible
        unique round combinations, along with the number of combinations and an approximate
        amount of RAM needed based on an internal regression model.

        .. note::
            This method calculates the number of operations needed to generate all possible
            unique round combinations based on the total number of people and the group size.
            The calculation involves determining the number of possible combinations, the worst-case
            backtracking scenario, and an estimate of RAM usage.

        **Complexity Formula**

        - :math:`n`: Total number of people.
        - :math:`k`: Group size.

        .. math::
          O\\left(\\binom{n}{k} * 2^{n/k} \\right)
        .. raw:: html

                <div style="text-align: center;">
                    Or
                </div>
        .. math::
            O\\left(\\frac{n!}{k!(n-k)!} * 2^{n/k} \\right)

        **Given**

        - :math:`\\text{amount_people}` : The total number of real people.
        - :math:`\\text{group_size}` : The size of each group.

        **Formula Steps**

        0. **Calculate the Number of People and Group Size**
            .. math::
                n = \\text{amount_people} + (\\text{amount_people} \\mod \\text{group_size})
            .. math::
                k = \\text{group_size}

        1. **Calculate All Possible Combinations**
            .. math::
                \\text{combinations} = \\binom{n}{k}
            .. raw:: html

                <div style="text-align: center;">
                    Or
                </div>
            .. math::
                \\text{combinations} = \\frac{n!}{k!(n-k)!}

        2. **Generating a Round**
            2.1. **Calculate the Number of Groups per Round**
                .. math::
                    \\text{groups_per_round} = \\frac{n}{k}

            2.2. **Calculate the Worst-Case Backtracking Scenario**
                .. math::
                    \\text{back_track_poss} = 2^{\\text{groups_per_round}}

        3. **Calculate the Number of Operations Needed**
            .. math::
                \\text{ops_needed} = \\text{combinations} * \\text{back_track_poss}

        4. **Calculate the Approximate Amount of RAM Needed**
            This estimate is determined by a regression model, based on this `Website <https://de.planetcalc.com/5992/?xstring=12720%2091390%20658008%201581580%202123555%202794155%203921225%206210820%207059052%2010009125%2012082785%2021374050%2045379620&ystring=40%2070%20440%20580%20820%201000%201300%202100%202800%203500%204200%208000%2014000&dolinear=1&doquadratic=0&dopower=0&docubic=0&doexponential=0&dologarithmic=0&dohyperbolic=0&doeexponential=0>`_:

                .. math::
                    \\text{ram_needed} = 0.000315294762088087 \\times \\text{combinations} + 200

            If :math:`\\text{combinations} > 92000`, use the formula above.
            Then round :math:`\\text{ram_needed}` up to the nearest multiple of 10.
            Otherwise, default to 100 MB.

        :param amount_people: The total number of people.
        :param group_size: The size of each group.
        :return: A tuple containing:
            1. The estimated number of operations needed (ops_needed).
            2. The number of combinations.
            3. The approximate amount of RAM needed (in MB).

        """
        # 0. Calculate the number of people and group size
        n = amount_people + (amount_people % group_size)
        k = group_size

        # 1. Calculate all the possible combinations, using binomial coefficient
        combinations = math.comb(n, k)

        # 2. Generating a round
        # 2.1. Calculate the number of groups per round
        groups_per_round = n // k
        # 2.2. Calculate the worst case backtracking scenario
        back_track_poss = 2 ** groups_per_round

        # 3. Calculate the number of operations needed
        ops_needed = combinations * back_track_poss

        # 4. Calculate the approximate amount of RAM needed, using a regression model
        if combinations > 92000:
            ram_needed = 0.000315294762088087 * combinations + 200
            ram_needed *= 1.5  # Increase due to overhead
            ram_needed = (ram_needed + 9) // 10 * 10  # Round up to nearest multiple of 10
        else:
            ram_needed = 200

        return ops_needed, combinations, ram_needed

    @deprecated("This calculation is not accurate anymore.")
    def _get_max_possibilities(self) -> int:
        """
.. note::
  Method is deprecated, because it is not accurate anymore, the cause for this is that it does not take into account that the algorithm is not allowed to generate the same group twice.

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
