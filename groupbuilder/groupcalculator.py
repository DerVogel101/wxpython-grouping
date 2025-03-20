from pydantic import ValidationError
from typing_extensions import deprecated

from .core.exceptions import AmountPeopleError
from .core.base import GroupCalculatorInterface
from .core.data_models import GroupConfig
from .core.algorithm import GroupingAlgorithm
from .utility.number_to_text import number_to_column
from .utility.csv_read import detect_csv_separator_and_load


class GroupCalculator(GroupCalculatorInterface):
    """
    A calculator for creating and managing groups of people.

    This class implements the GroupCalculatorInterface and provides functionality
    for creating groups based on a specified amount of people and group size.

    :param amount_people: The total number of people to be divided into groups
    :type amount_people: int
    :param group_size: The size of each group
    :type group_size: int
    :param usable_indexes: Whether to use indexing based on numbers instead of column letters, defaults to False
    :type usable_indexes: bool, optional
    :raises AmountPeopleError: If the amount of people or group size is invalid
    :raises AmountPeopleError: If the amount of people is less than the group_size
    """
    def __init__(self, amount_people: int, group_size: int, usable_indexes: bool = False):
        """
        Initialize a new instance of the GroupCalculator class.

        :param amount_people: The total number of people to be divided into groups
        :type amount_people: int
        :param group_size: The size of each group
        :type group_size: int
        :param usable_indexes: Whether to use indexing based on numbers instead of column letters, defaults to False
        :type usable_indexes: bool, optional
        :raises AmountPeopleError: If the amount of people or group size is invalid
        :raises AmountPeopleError: If the amount of people is less than the group_size
        """
        try:
            self.__group_config = GroupConfig(amount_people=amount_people, group_size=group_size)
        except ValidationError as e:
            raise AmountPeopleError from e
        self.__algorithm = GroupingAlgorithm(self.__group_config)
        self.__ui = usable_indexes

    def reset_groups(self) -> None:
        """
        Reset the groups and round to their initial state.

        Creates a new GroupingAlgorithm instance with the current configuration.

        :return: None
        """
        self.__algorithm = GroupingAlgorithm(self.__group_config)

    def create_groups(self) -> None:
        """
        Creates the groups for the next round.

        Uses the algorithm to generate the next round of groups,
        avoiding placing the same person in the same group.

        :return: None
        """
        self.__algorithm.generate_next_round()

    def visualize_groups(self) -> None:
        """
        Print the groups in a readable format to the console.

        Displays all groups from all rounds.

        :return: None
        """
        groups = self.get_all_groups()
        for rnd in groups:
            for i, g in groups[rnd].items():
                print(f"Gruppe {rnd+1}{i}: {g}")

    def can_repeat(self) -> int:
        """
        Calculates the maximum number of unique groups that can be created.

        :return: The maximum number of unique rounds
        :rtype: int
        """
        return self.__algorithm.get_max_rounds()

    def get_current_groups(self) -> dict:
        """
        Gets the groups from the current round.

        :return: A dictionary where keys are group identifiers (column letters or indices)
                 and values are lists of people in each group
        :rtype: dict
        """
        return {i if self.__ui else number_to_column(i+1): [p for p in g] for i, g in enumerate(self.__algorithm.get_round())}

    def get_all_groups(self) -> dict:
        """
        Gets all groups from all rounds.

        :return: A nested dictionary where the first level keys are round numbers,
                 second level keys are group identifiers, and values are lists of
                 people in each group
        :rtype: dict
        """
        data = self.__algorithm.get_all_rounds()
        return {rnd: {i if self.__ui else number_to_column(i+1): [p for p in g] for i, g in enumerate(data[rnd])} for rnd in data}

    @staticmethod
    @deprecated("Use the 'detect_csv_separator_and_load' function from the 'csv_read' module instead")
    def select_from_csv_file(file_path: str) -> list[list[str]]:
        """
        Reads the CSV file and prepares the data for selection.

        .. deprecated:: Use the 'detect_csv_separator_and_load' function from the 'csv_read' module instead

        :param file_path: The path to the CSV file
        :type file_path: str
        :return: A list of lists containing the CSV data
        :rtype: list[list[str]]
        """
        data, _, _ = detect_csv_separator_and_load(file_path)
        return data