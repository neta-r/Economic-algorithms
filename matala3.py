import functools
from tabulate import tabulate


class party:
    def __init__(self, name, votes, mandates=0):
        self.name = name
        self.votes = votes
        self.mandates = mandates


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
    real_parities = [['שם', 'קולות', 'מנדטים'], ['מחל', 1115336, 32], ['פה', 847435, 24], ['ט', 516470, 14],
                     ['כן', 432482, 12], ['שס', 392964, 11], ['ג', 280194, 7], ['ל', 213687, 6],
                     ['עם', 194047, 5], ['ום', 178735, 5], ['אמת', 175992, 4]]
    print(tabulate(real_parities, headers='firstrow', tablefmt='fancy_grid'))
    print('\n\n')
    webster_parities = (
        __divider_system__([party('מחל', 1115336), party('פה', 847435), party('ט', 516470), party('כן', 432482),
                            party('שס', 392964), party('ג', 280194), party('ל', 213687), party('עם', 194047),
                            party('ום', 178735), party('אמת', 175992)], Webster, 120))
    table = [[p.name, p.votes, p.mandates] for p in webster_parities]
    table.insert(0,['שם', 'קולות', 'מנדטים'] )
    print("Webster results:")
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


if __name__ == '__main__':
    # class examples
    parities = [party('A', 160), party('B', 340)]
    print("Class first example")
    __print_mandates__(__divider_system__(parities, Jefferson, 5))

    parities = [party('A', 40), party('B', 135), party('C', 325)]
    print("\n\nClass second example")
    __print_mandates__(__divider_system__(parities, Jefferson, 5))

    print("\n\n")
    show_diff()
