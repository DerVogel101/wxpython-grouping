"""
    Data Model Converter Module
    ===========================

    This module provides utility functions for converting custom data model objects to
    standard Python dictionaries and lists.

    .. inheritance-diagram:: groupbuilder.core.data_model_converter
       :parts: 1

    .. autosummary::
       :toctree: generated/

       convert_group_to_list
       convert_round_to_dict
       convert_rounds_to_dict
    """

from groupbuilder.core.data_models import Round, Rounds, Group, Person


def convert_group_to_list(group: Group) -> list:
    """
    Convert a Group object to a list.

    This function extracts the IDs from a Group object and returns them as a list.

    :param group: The Group object to convert
    :type group: Group
    :return: The list representation of the Group object, only retaining the ids
    :rtype: list

    .. autosummary::
       :toctree: generated/
    """
    return list(group.get_ids())


def convert_round_to_dict(round_: Round) -> dict:
    """
    Convert a Round object to a dictionary.

    This function converts a Round object to a dictionary, and handles nested Group
    objects by converting them to lists.

    :param round_: The Round object to convert
    :type round_: Round
    :return: The dictionary representation of the Round object
    :rtype: dict

    .. autosummary::
       :toctree: generated/
    """
    round_to_convert = dict(round_)
    for key, value in round_to_convert.items():
        if isinstance(value, Group):
            round_to_convert[key] = convert_group_to_list(value)
    return round_to_convert


def convert_rounds_to_dict(rounds: Rounds) -> dict:
    """
    Convert a Rounds object to a dictionary.

    This function converts a Rounds object to a dictionary, and handles nested Round
    objects by converting them to dictionaries.

    :param rounds: The Rounds object to convert
    :type rounds: Rounds
    :return: The dictionary representation of the Rounds object
    :rtype: dict

    .. autosummary::
       :toctree: generated/
    """
    rounds_to_convert = dict(rounds)
    for key, value in rounds_to_convert.items():
        rounds_to_convert[key] = convert_round_to_dict(value)
    return rounds_to_convert


if __name__ == "__main__":
    person = Person(id_=1)
    person2 = Person(id_=2)
    person3 = Person(id_=3)

    rounds = Rounds(rounds={
        1: Round(round_={
            "a": Group(items=[person, person2]),
            "b": Group(items=[person3])
        }),
        2: Round(round_={
            "a": Group(items=[person, person2]),
            "b": Group(items=[person3])
        })
    })

    print(convert_round_to_dict(rounds[2]))
    print(convert_rounds_to_dict(rounds))