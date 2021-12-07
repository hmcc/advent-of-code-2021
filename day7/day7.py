from collections import Counter, defaultdict


def read_input(filename):
    with open(filename) as file:
        positions = [int(n) for n in file.readline().strip().split(',')]
    return positions


def fuel_cost(positions, position):
    return sum(abs(x - position) for x in positions)


def solve(positions):
    costs = [fuel_cost(positions, idx) for idx, _ in enumerate(positions)]
    return min(costs)


print(solve(read_input('day7/input')))


