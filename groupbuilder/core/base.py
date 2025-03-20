"""
Group Builder Base Module
========================

This module defines abstract interfaces for group calculation functionality.

.. inheritance-diagram:: groupbuilder.core.base
   :parts: 1

.. autosummary::
   :toctree: generated/

   GroupCalculatorInterface
"""

from abc import ABC, abstractmethod


class GroupCalculatorInterface(ABC):
    """
    Abstract interface for group calculator implementations.

    This interface defines the core functionality required for any group calculator
    implementation in the system, ensuring consistent behavior across different
    implementations.

    .. inheritance-diagram:: groupbuilder.core.base.GroupCalculatorInterface
       :parts: 1

    .. autosummary::
       :toctree: generated/

       __init__
       reset_groups
       create_groups
       visualize_groups
       can_repeat
       get_current_groups
       get_all_groups
       select_from_csv_file
    """

    @abstractmethod
    def __init__(self, amount_people: int, group_size: int):
        """
        Initialize a new instance of the GroupCalculator class.

        :param amount_people: The total number of people to organize into groups
        :type amount_people: int
        :param group_size: The desired size of each group
        :type group_size: int
        :raises ValidationError: If the amount of people or group size is invalid
        :raises AmountPeopleError: If the amount of people is less than the group_size
        """
        pass

    @abstractmethod
    def reset_groups(self) -> None:
        """
        Reset the groups and round to initial state.

        This method clears any existing group assignments and returns the calculator
        to its initial state.

        :return: None
        """
        pass

    @abstractmethod
    def create_groups(self) -> None:
        """
        Creates the groups, based on the round.

        This method generates new group assignments, ensuring that the same person
        is not placed in the same group multiple times across different rounds.

        :return: None
        """
        pass

    @abstractmethod
    def visualize_groups(self) -> None:
        """
        Print the groups in a readable format.

        This method outputs the current group assignments in a human-readable format,
        typically to the console.

        :return: None
        """
        pass

    @abstractmethod
    def can_repeat(self) -> int:
        """
        Calculates the maximum number of unique groups that can be created.

        This method determines how many rounds of unique group assignments can be
        created given the constraints of the group size and total number of people.

        :return: The maximum number of unique groups
        :rtype: int
        """
        pass

    @abstractmethod
    def get_current_groups(self) -> dict:
        """
        Gets the current groups.

        This method returns the current group assignments for the active round.

        :return: The current groups
        :rtype: dict
        """
        pass

    @abstractmethod
    def get_all_groups(self) -> dict:
        """
        Gets all the groups from all rounds.

        This method returns all group assignments across all rounds that have
        been created.

        :return: All the groups
        :rtype: dict
        """
        pass

    @staticmethod
    @abstractmethod
    def select_from_csv_file(file_path: str) -> list[list[str]]:
        """
        Reads the CSV file and prepares the data for selection.

        This method loads people data from a CSV file to be used in group assignments.

        :param file_path: The path to the CSV file
        :type file_path: str
        :return: CSV data as a list of rows
        :rtype: list[list[str]]
        """
        pass