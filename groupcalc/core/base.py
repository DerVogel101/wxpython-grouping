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
    def reset_groups(self):
        """
        Reset the groups and round to be initial.
        """
        pass