import functools
from tabulate import tabulate


class party:
    def __init__(self, name, votes, mandates=0):
        self.name = name
        self.votes = votes
        self.mandates = mandates


real_parties = [['מחל', 1115336, 32], ['פה', 847435, 24], ['ט', 516470, 14],
                ['כן', 432482, 12], ['שס', 392964, 11], ['ג', 280194, 7], ['ל', 213687, 6],
                ['עם', 194047, 5], ['ום', 178735, 5], ['אמת', 175992, 4]]
parties = [party('מחל', 1115336), party('פה', 847435), party('ט', 516470), party('כן', 432482),
           party('שס', 392964), party('ג', 280194), party('ל', 213687), party('עם', 194047),
           party('ום', 178735), party('אמת', 175992)]
headers = ['שם', 'קולות', 'מנדטים']


def __divider_system__(parities: list[party], f: functools, seats: int):
    while seats:
        max_remainder = 0
        max_party = None
        for p in parities:
            curr_remainder = p.votes / f(p.mandates)
            if curr_remainder > max_remainder:
                max_remainder = curr_remainder
                max_party = p
        max_party.mandates += 1
        seats -= 1
    return parities


def __print_mandates__(parities: list[party]):
    for p in parities:
        print(p.name + " got " + str(p.mandates) + " mandates")


def Webster(x): return x + 0.5


def Jefferson(x): return x + 1


def show_diff():
    print("Real results:")
    real_parties.insert(0, headers)
    print(tabulate(real_parties, headers='firstrow', tablefmt='fancy_grid'))
    real_parties.pop(0)
    print('\n\n')
    webster_parities = (__divider_system__(parties, Webster, 120))
    table = [[p.name, p.votes, p.mandates] for p in webster_parities]
    table.insert(0, headers)
    print("Webster results:")
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


def reset_mandates():
    for p in parties: p.mandates = 0


def is_the_same(curr_parties: list[party]):
    for j in range(0, len(real_parties) - 1):
        if real_parties[j][2] != curr_parties[j].mandates:
            return False
    return True


def check_y():
    step = 0.001
    y = 0.5  # we can start from 0.5 bc we showed the differences in part A

    def Plus_y(x):
        return x + y

    while True:
        reset_mandates()
        y += step
        curr_parties = (__divider_system__(parties, Plus_y, 120))
        if is_the_same(curr_parties):
            print(y - step)
            return


if __name__ == '__main__':
    # # class examples
    # parities = [party('A', 160), party('B', 340)]
    # print("Class first example")
    # __print_mandates__(__divider_system__(parities, Jefferson, 5))
    #
    # parities = [party('A', 40), party('B', 135), party('C', 325)]
    # print("\n\nClass second example")
    # __print_mandates__(__divider_system__(parities, Jefferson, 5))

    # exercise
    print("\n\nPart A:")
    show_diff()

    print("\n\nPart B:")
    check_y()
