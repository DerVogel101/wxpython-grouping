groupbuilder.core package
=========================

Submodules
----------

groupbuilder.core.algorithm module
----------------------------------

.. automodule:: groupbuilder.core.algorithm
    :members:
    :undoc-members:
    :show-inheritance:

Given
~~~~~
- :math:`P`: Total number of people.
- :math:`G`: Group size.
- :math:`H`: Number of placeholders (added if :math:`P` is not divisible by :math:`G`).
- :math:`T`: Total number of participants (including placeholders).
- :math:`\text{groups_per_round}`: The number of groups formed in a round.
- :math:`\text{numerator}`: The product of binomial coefficients for each group.
- :math:`\text{denominator}`: The factorial of the number of groups.

Formula Steps
~~~~~~~~~~~~~
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


groupbuilder.core.base module
-----------------------------

.. automodule:: groupbuilder.core.base
   :members:
   :undoc-members:
   :show-inheritance:

groupbuilder.core.data\_model\_converter module
-----------------------------------------------

.. automodule:: groupbuilder.core.data_model_converter
   :members:
   :undoc-members:
   :show-inheritance:

groupbuilder.core.data\_models module
-------------------------------------

.. automodule:: groupbuilder.core.data_models
   :members:
   :undoc-members:
   :show-inheritance:

groupbuilder.core.exceptions module
-----------------------------------

.. automodule:: groupbuilder.core.exceptions
   :members:
   :undoc-members:
   :show-inheritance:

groupbuilder.core.logger module
-------------------------------

.. automodule:: groupbuilder.core.logger
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: groupbuilder.core
   :members:
   :undoc-members:
   :show-inheritance:
