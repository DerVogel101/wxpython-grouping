from pydantic import ValidationError
from typing_extensions import deprecated

from .core.exceptions import AmountPeopleError
from .core.base import GroupCalculatorInterface
from .core.data_models import GroupConfig
from .core.algorithm import GroupingAlgorithm
from .utility.number_to_text import number_to_column
from .utility.csv_read import detect_csv_separator_and_load


class GroupCalculator(GroupCalculatorInterface):
    def __init__(self, amount_people: int, group_size: int, usable_indexes: bool = False):
        """
        Initialize a new instance of the GroupCalculator class.
        :raises AmountPeopleError: If the amount of people or group size is invalid.
        :raises AmountPeopleError: If the amount of people is less than the group_size.
        :param amount_people: The amount of people.
        :param group_size: The group size.
        """
        try:
            self.__group_config = GroupConfig(amount_people=amount_people, group_size=group_size)
        except ValidationError as e:
            raise AmountPeopleError from e
        self.__algorithm = GroupingAlgorithm(self.__group_config)
        self.__ui = usable_indexes

    def reset_groups(self) -> None:
        """
        Reset the groups and round to be initial.
        :return: None
        """
        self.__algorithm = GroupingAlgorithm(self.__group_config)

    def create_groups(self) -> None:
        """
        Creates the groups, based on the round.
        Avoids usage of the same person in the same group.
        :return: None
        """
        self.__algorithm.generate_next_round()

    def visualize_groups(self) -> None:
        """
        Print the groups in a readable format.
        :return: None
        """
        groups = self.get_all_groups()
        for rnd in groups:
            for i, g in groups[rnd].items():
                print(f"Gruppe {rnd+1}{i}: {g}")


    def can_repeat(self) -> int:
        """
        Calculates the maximum number of unique groups that can be created.
        :return int: The maximum number of unique groups.
        """
        return self.__algorithm.get_max_rounds()

    def get_current_groups(self) -> dict:
        """
        Gets the current groups.
        :return dict: The current groups.
        """
        return {i if self.__ui else number_to_column(i+1): [p for p in g] for i, g in enumerate(self.__algorithm.get_round())}

    def get_all_groups(self) -> dict:
        """
        Gets all the groups.
        :return dict: All the groups.
        """
        data = self.__algorithm.get_all_rounds()
        return {rnd: {i if self.__ui else number_to_column(i+1): [p for p in g] for i, g in enumerate(data[rnd])} for rnd in data}

    @staticmethod
    @deprecated("Use the 'detect_csv_separator_and_load' function from the 'csv_read' module instead")
    def select_from_csv_file(file_path: str) -> list[list[str]]:
        """
        Reads the CSV file and prepares the data for selection.
        :param file_path: The path to the CSV file.
        :return: CSV data
        """
        data, _, _ = detect_csv_separator_and_load(file_path)
        return data
