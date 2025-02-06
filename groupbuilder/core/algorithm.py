import itertools
import math

from .data_models import GroupConfig, Rounds

class GroupingAlgorithm:
    def __init__(self, config: GroupConfig):
        self._amount_people: int = config.amount_people
        self._group_size: int = config.group_size
        self._rounds = Rounds(rounds={})

    def get_possibilities(self) -> int:
        """
        Calculates the number of possible unique round combinations in a scenario where people are divided into groups of a specified size.

        **Parameters**:

        - :math:`P`: Total number of people.
        - :math:`G`: Group size.
        - :math:`H`: Number of placeholders (added if :math:`P` is not divisible by :math:`G`).
        - :math:`T`: Total number of participants (including placeholders).
        - :math:`\text{groups_per_round}`: The number of groups formed in a round.
        - :math:`\text{numerator}`: The product of binomial coefficients for each group.
        - :math:`\text{denominator}`: The factorial of the number of groups.

        **Formula Steps**:

        1. Calculate placeholders :math:`H` (if necessary):
            .. math::
                H =
                \begin{cases}
                0 & \text{if } P \mod G = 0 \\
                G - (P \mod G) & \text{if } P \mod G \neq 0
                \end{cases}
        2. Total participants :math:`T`:
            .. math::
                T = P + H
        3. Groups per round :math:`\text{groups_per_round}`:
            .. math::
                \text{groups_per_round} = \frac{T}{G}
        4. Numerator: The product of the binomial coefficients:
            .. math::
                \text{numerator} = \prod_{i=0}^{\text{groups_per_round}-1} \binom{T - i \cdot G}{G}
        5. Denominator: The factorial of the number of groups:
            .. math::
                \text{denominator} = (\text{groups_per_round})!
        6. Unique rounds: The total number of unique round combinations:
            .. math::
                \text{unique_rounds} = \frac{\text{numerator}}{\text{denominator}}

        This formula calculates the total number of unique round combinations based on the number of participants and the group size, taking into account any necessary placeholders.

        **Returns**:
            - : The number of possible unique round combinations.
        """

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

