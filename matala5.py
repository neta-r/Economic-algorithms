

def sort_object_according_to_ratio(a: list[float], b: list[float], ratio: list[float]):
    newA = [0.0] * len(a)
    newB = [0.0] * len(b)
    for i in range(0, len(ratio)):
        for j in range(0, len(ratio)):
            if a[i] / b[i] == ratio[j]:
                newA[j] = a[i]
                newB[j] = b[i]
                break
    return newA, newB


def adjusted_winner(a: list[float], b: list[float]):
    if len(a) != len(b) or sum(a) != 100 or sum(b) != 100:
        return None
    ratio = []
    for i in range(0, len(a)):
        ratio.append(a[i] / b[i])
    ratio.sort()
    a, b = sort_object_according_to_ratio(a, b, ratio)
    divA = [1] * len(b)  # deep copy of a
    sumA = 100
    divB = [0] * len(b)
    sumB = 0
    for i in range(0, len(ratio)):
        if sumA - a[i] < sumB - b[i]:
            x = (sumA - sumB) / (a[i] + b[i])
            divA[i] = 1 - x
            divB[i] = x
            return divA, divB, a, b
        divA[i] = 0
        sumA -= a[i]
        divB[i] = 1
        sumB += b[i]


def calc_real_bin_val(a: list[float], divA: list[float]):
    sumA = 0.0
    for i in range(0, len(a)):
        sumA += divA[i] * a[i]
    return sumA


def manipulate(other_players_values: list[float], our_real_vals: list[float]):
    if len(other_players_values) != len(our_real_vals):
        return None
    fake_vals = [0] * len(our_real_vals)
    return fake_vals


if __name__ == '__main__':
    Ivana = [40, 25, 30, 5]
    Donald = [15, 15, 40, 30]
    realDivDonald, realDivIvana, Donald, Ivana = adjusted_winner(Donald, Ivana)
    print(calc_real_bin_val(Ivana, realDivIvana))
    fakeDivDonald, fakeDivIvana, Donald, Ivana = adjusted_winner(Donald, [44, 25, 30, 1])
    print(calc_real_bin_val(Ivana, fakeDivIvana))
