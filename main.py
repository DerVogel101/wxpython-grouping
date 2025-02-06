from groupbuilder.groupcalculator import GroupCalculator
from groupbuilder import GroupingAlgorithm
from groupbuilder.core.data_models import GroupConfig


if __name__ == "__main__":
    # print(GroupingAlgorithm(GroupConfig(amount_people=4, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=4, group_size=2)).get_possibilities())

    conf1 = GroupingAlgorithm(GroupConfig(amount_people=13, group_size=4))
    print(conf1.get_max_rounds())
    for _ in range(conf1.get_remaining_rounds()):
        conf1.generate_next_round()
        print(conf1.get_round())

    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_possibilities())
    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=3)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=13, group_size=4)).get_max_rounds())