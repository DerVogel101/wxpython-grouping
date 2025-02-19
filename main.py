from groupbuilder.groupcalculator import GroupCalculator
from groupbuilder import GroupingAlgorithm
from groupbuilder.core.data_models import GroupConfig
import cProfile
import math


if __name__ == "__main__":
    # print(GroupingAlgorithm(GroupConfig(amount_people=4, group_size=2)).get_max_rounds())
    def main():
        am, gs = 40, 2
        print(GroupingAlgorithm.get_ops_needed(am, gs))
        conf1 = GroupingAlgorithm(GroupConfig(amount_people=am, group_size=gs))
        print(conf1.get_max_rounds())
        try:
            for _ in range(conf1.get_remaining_rounds() + 1):
                conf1.generate_next_round()
                print(conf1.get_round())
        except StopIteration:
            print(len(conf1._rounds))
            pass
    cProfile.run('main()')

    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=3)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=13, group_size=4)).get_max_rounds())