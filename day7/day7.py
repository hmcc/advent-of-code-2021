def read_input(filename):
    with open(filename) as file:
        positions = [int(n) for n in file.readline().strip().split(',')]
    return positions


def triangle(n):
    return int(n * (n + 1) / 2)


def cost_one(positions, position):
    return sum(abs(x - position) for x in positions)


def cost_two(positions, position):
    return sum(triangle(abs(x - position)) for x in positions)


def solve(positions, cost_fn):
    costs = [cost_fn(positions, idx) for idx, _ in enumerate(positions)]
    return min(costs)


def part_one(filename):
    return solve(read_input(filename), cost_one)


def part_two(filename):
    return solve(read_input(filename), cost_two)


print(part_two('day7/input'))
