from collections import Counter, defaultdict


def read_input(filename):
    with open(filename) as file:
        positions = [int(n) for n in file.readline().strip().split(',')]
    return positions


def triangle(n):
    return sum(range(n+1))


def cost_one(positions, position):
    return sum(abs(x - position) for x in positions)


def cost_two(positions, position):
    return sum(triangle(abs(x - position)) for x in positions)


def solve(positions, cost_fn):
    costs = [cost_fn(positions, idx) for idx, _ in enumerate(positions)]
    return min(costs)


def part_one(filename):
    return solve(read_input('day7/input'), cost_one)


def part_two(filename):
    return solve(read_input('day7/input'), cost_two)


print(part_two('day7/input'))


