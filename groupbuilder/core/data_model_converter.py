from groupbuilder.core.data_models import Round, Rounds, Group, Person

def convert_group_to_list(group: Group) -> list:
    """
    Convert a Group object to a list.
    :param group: The Group object to convert.
    :return list: The list representation of the Group object, only retaining the id.
    """
    return list(group.get_ids())

def convert_round_to_dict(round_: Round) -> dict:
    """
    Convert a Round object to a dictionary.
    :param round_: The Round object to convert.
    :return dict: The dictionary representation of the Round object.
    """
    round_to_convert = dict(round_)
    for key, value in round_to_convert.items():
        if isinstance(value, Group):
            round_to_convert[key] = convert_group_to_list(value)
    return round_to_convert

def convert_rounds_to_dict(rounds: Rounds) -> dict:
    """
    Convert a Rounds object to a dictionary.
    :param rounds: The Rounds object to convert.
    :return dict: The dictionary representation of the Rounds object.
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
