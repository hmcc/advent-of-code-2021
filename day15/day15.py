from itertools import product
from math import inf
import time
from heapdict import heapdict


def read_file(filename):
    risk_levels = []
    with open(filename) as file:
        for line in file:
            risk_levels.append([int(n) for n in line.strip()])
    return {(x, y): value for y, row in enumerate(risk_levels) for x, value in enumerate(row)}


def expand(cavern, factor, max_x, max_y):
    expanded_cavern = {}
    for (a, b) in product(range(factor), range(factor)):
        for (x, y), value in cavern.items():
            new_value = (value + a + b) % 9
            if new_value == 0:
                new_value = 9
            new_x = a * max_x + x
            new_y = b * max_y + y
            expanded_cavern[(new_x, new_y)] = new_value
    return expanded_cavern



def dimensions(cavern):
    max_x = max(x for x, _ in cavern)
    max_y = max(y for _, y in cavern)
    return (max_x + 1, max_y + 1)


def neighbours(x, y, max_x, max_y, queue):
    possibilities = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return [(x1, y1) for (x1, y1) in possibilities
            if 0 <= x1 < max_x
            and 0 <= y1 < max_y
            and (x1, y1) in queue]


def initialise_queue(cavern):
    return heapdict(cavern)


def initialise_risks(cavern):
    risks = {location: inf for location in cavern}
    risks[(0, 0)] = 0
    return risks


def next_visit(queue):
    return queue.popitem()[0]


def visit(coordinates, cavern, cavern_dimensions, risks, queue):
    for adjacent in neighbours(*coordinates, *cavern_dimensions, queue):
        new_risk = risks[coordinates] + cavern[adjacent]
        if new_risk < risks[adjacent]:
            risks[adjacent] = new_risk
            queue[adjacent] = new_risk


def answer(max_x, max_y, risks):
    return risks[(max_x - 1, max_y - 1)]


def explore(cavern):
    risks = initialise_risks(cavern)
    queue = initialise_queue(risks)
    max_x, max_y = dimensions(cavern)

    while queue:
        coordinates = next_visit(queue)
        visit(coordinates, cavern, (max_x, max_y), risks, queue)

    return answer(max_x, max_y, risks)


def part_one(filename):
    cavern = read_file(filename)
    return explore(cavern)


def part_two(filename):
    cavern = read_file(filename)
    max_x, max_y = dimensions(cavern)
    cavern = expand(cavern, 5, max_x, max_y)
    return explore(cavern)


def pretty_print(cavern, max_x, max_y):
    grid = [[0] * max_x for i in range(max_y)]
    for (x, y), value in cavern.items():
        grid[y][x] = value
    for row in grid:
        print(''.join([str(item).ljust(2) for item in row]))



start_time = time.time()
print(part_two('day15/input'))
print(f'{time.time() - start_time:0.2f} s')
