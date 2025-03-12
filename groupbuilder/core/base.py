from abc import ABC, abstractmethod


class GroupCalculatorInterface(ABC):

    @abstractmethod
    def __init__(self, amount_people: int, group_size: int):
        """
        Initialize a new instance of the GroupCalculator class.
        :raises ValidationError: If the amount of people or group size is invalid.
        :raises AmountPeopleError: If the amount of people is less than the group_size.
        :param amount_people:
        :param group_size:
        """
        pass

    @abstractmethod
    def reset_groups(self) -> None:
        """
        Reset the groups and round to be initial.
        :return: None
        """
        pass

    @abstractmethod
    def create_groups(self) -> None:
        """
        Creates the groups, based on the round.
        Avoids usage of the same person in the same group.
        :return: None
        """
        pass

    @abstractmethod
    def visualize_groups(self) -> None:
        """
        Print the groups in a readable format.
        :return: None
        """
        pass

    @abstractmethod
    def can_repeat(self) -> int:
        """
        Calculates the maximum number of unique groups that can be created.
        :return int: The maximum number of unique groups.
        """
        pass

    @abstractmethod
    def get_current_groups(self) -> dict:
        """
        Gets the current groups.
        :return dict: The current groups.
        """
        pass

    @abstractmethod
    def get_all_groups(self) -> dict:
        """
        Gets all the groups.
        :return dict: All the groups.
        """
        pass

    @staticmethod
    @abstractmethod
    def select_from_csv_file(file_path: str) -> list[list[str]]:
        """
        Reads the CSV file and prepares the data for selection.
        :param file_path: The path to the CSV file.
        :return: CSV data
        """
        pass