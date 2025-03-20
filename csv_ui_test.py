from groupbuilder import GroupingAlgorithm
from groupbuilder.core.data_models import GroupConfig
import cProfile
from groupbuilder.groupcalculator import GroupCalculator
import pprint

# calc = GroupCalculator(4, 2)
# calc.create_groups()
# print(calc.get_current_groups())
# calc.create_groups()
# print(calc.get_current_groups())
# pprint.pprint(calc.get_all_groups())
# calc.visualize_groups()

if __name__ == "__main__":
    # print(GroupingAlgorithm(GroupConfig(amount_people=4, group_size=2)).get_max_rounds())
    def main():
        am, gs = 1, 1
        while True:
            print(GroupingAlgorithm.get_ops_needed(am, gs))
            conf1 = GroupingAlgorithm(GroupConfig(amount_people=am, group_size=gs))
            print(f"Amount of people: {am}, Group size: {gs}")
            try:
                for _ in range(conf1.get_remaining_rounds() + 1):
                    conf1.generate_next_round()
                    # print(conf1.get_round())
            except StopIteration:
                print(f"Total rounds: {len(conf1._rounds)} / {conf1.get_max_rounds()}")
                print(f"Total groups: {len(conf1._rounds)} / {len(conf1._unique_rounds)}")
                if not len(conf1._rounds) == len(conf1._unique_rounds):
                    break
                if am == 25:
                    gs += 1
                    am = gs
                am += 1
                pass
    cProfile.run('main()')

    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=5, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=2)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=6, group_size=3)).get_max_rounds())
    # print(GroupingAlgorithm(GroupConfig(amount_people=13, group_size=4)).get_max_rounds())
