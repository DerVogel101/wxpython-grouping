from typing import Optional, Union

from .core.base import GroupCalculatorInterface
from .core.data_models import Round, Rounds, Group, Person


class GroupCalculator(GroupCalculatorInterface):
    def __init__(self, amount_people: int, group_size: int):
        """
        Initialize a new instance of the GroupCalculator class.
        :raises ValidationError: If the amount of people or group size is invalid.
        :raises AmountPeopleError: If the amount of people is less than the group_size.
        :param amount_people:
        :param group_size:
        """
        pass

    def reset_groups(self) -> None:
        """
        Reset the groups and round to be initial.
        :return: None
        """
        pass

    def create_groups(self) -> None:
        """
        Creates the groups, based on the round.
        Avoids usage of the same person in the same group.
        :return: None
        """
        pass

    def visualize_groups(self) -> None:
        """
        Print the groups in a readable format.
        :return: None
        """
        pass

    def can_repeat(self) -> int:
        """
        Calculates the maximum number of unique groups that can be created.
        :return int: The maximum number of unique groups.
        """
        pass

    def get_current_groups(self, pyd: bool = False) -> dict:
        """
        Gets the current groups.
        :return dict: The current groups.
        """
        pass

    def get_all_groups(self, pyd: bool = False) -> dict:
        """
        Gets all the groups.
        :return dict: All the groups.
        """
        pass

    def select_from_csv_file(self, has_header_row: bool, student_firstname_col: Union[int, str],
                             student_lastname_col: Optional[Union[int, str]]) -> None:
        """
        Selects the students from a CSV file.
        :param has_header_row: If the CSV file has a header row.
        :param student_firstname_col: The column index or name of the student first name.
        :param student_lastname_col: The column index or name of the student last name.
        :return: None
        """
        pass

    def select_csv_file(self, file_path: str) -> dict:
        """
        Selects the students from a CSV file.
        :param file_path: The path to the CSV file.
        :return: The column indexes and column names to choose from.
        """
        pass