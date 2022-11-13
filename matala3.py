import functools
from tabulate import tabulate


class party:
    def __init__(self, name, votes, mandates=0):
        self.name = name
        self.votes = votes
        self.copy = votes
        self.mandates = mandates


parties = [party('מחל', 1115336), party('פה', 847435), party('ט', 516470), party('כן', 432482),
           party('שס', 392964), party('ג', 280194), party('ל', 213687), party('עם', 194047),
           party('ום', 178735), party('אמת', 175992)]
headers = ['שם', 'קולות', 'מנדטים']


def __divider_system__(parities: list[party], f: functools, seats: int):
    while seats:
        max_remainder = 0
        max_party = None
        for p in parities:
            curr_remainder = p.copy / f(p.mandates)
            if curr_remainder > max_remainder:
                max_remainder = curr_remainder
                max_party = p
        max_party.mandates += 1
        seats -= 1
    return parities


def Webster(x): return x + 0.5


def Jefferson(x): return x + 1


def show_diff(real_parties: list[party], parties: list[party]):
    print("Real results:")
    real_table = [[p.name, p.votes, p.mandates] for p in real_parties]
    real_table.insert(0, headers)
    print(tabulate(real_table, headers='firstrow', tablefmt='fancy_grid'))
    print('\n\n')
    webster_parities = (__divider_system__(parties, Webster, 120))
    table = [[p.name, p.votes, p.mandates] for p in webster_parities]
    table.insert(0, headers)
    print("Webster results:")
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


def reset_mandates():
    for p in parties: p.mandates = 0
    for p in parties: p.copy = p.votes


def is_the_same(curr_parties: list[party]):
    for j in range(0, len(parties) - 1):
        if real_parties[j].mandates != curr_parties[j].mandates:
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


def __print_mandates__(parities: list[party]):
    for p in parities:
        print(p.name + " got " + str(p.mandates) + " mandates")


if __name__ == '__main__':
    # class examples
    parities = [party('A', 160), party('B', 340)]
    print("Class first example")
    __print_mandates__(__divider_system__(parities, Jefferson, 5))

    parities = [party('A', 40), party('B', 135), party('C', 325)]
    print("\n\nClass second example")
    __print_mandates__(__divider_system__(parities, Jefferson, 5))

    # exercise
    real_parties = [party('מחל', 1115336), party('פה', 847435), party('ט', 516470), party('כן', 432482),
                    party('שס', 392964), party('ג', 280194), party('ל', 213687), party('עם', 194047),
                    party('ום', 178735), party('אמת', 175992)]
    real_parties = (__divider_system__(real_parties, Jefferson, 120))
    print("\n\nPart A:")
    show_diff(real_parties, parties)

    print("\n\nPart B:")
    check_y()
