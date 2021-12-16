from collections import Counter
from math import inf
import time

def read_file(filename):
    risk_levels = []
    with open(filename) as file:
        for line in file:
            risk_levels.append([int(n) for n in line.strip()])
    return {(x, y): value for y, row in enumerate(risk_levels) for x, value in enumerate(row)}


def dimensions(cavern):
    max_x = max(x for x, _ in cavern)
    max_y = max(y for _, y in cavern)
    return (max_x + 1, max_y + 1)


def neighbours(x, y, max_x, max_y, visited):
    possibilities = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return [(x1, y1) for (x1, y1) in possibilities \
        if 0 <= x1 < max_x \
        and 0 <= y1 < max_y \
        and (x1, y1) not in visited]


def initialise_risks(cavern):
    risks = {location: inf for location in cavern}
    risks[(0, 0)] = 0
    return risks


def next_visit(risks, visited):
    todos = {location: risk for location, risk in risks.items() if location not in visited}
    counted = Counter(todos).most_common()
    return counted[-1][0]


def visit(x, y, cavern, risks, visited):
    visited.add((x, y))
    for adjacent in neighbours(x, y, *(dimensions(cavern)), visited):
        new_risk = risks[(x, y)] + cavern[adjacent]
        if new_risk < risks[adjacent]:
            risks[adjacent] = new_risk


def answer(cavern, risks):
    return risks[tuple(d - 1 for d in dimensions(cavern))]


def part_one(filename):
    cavern = read_file(filename)
    risks = initialise_risks(cavern)
    visited = set()

    while len(visited) < len(cavern):
        todo = next_visit(risks, visited)
        visit(*todo, cavern, risks, visited)
    
    return answer(cavern, risks)


def pretty_print(risks):
    max_x, max_y = dimensions(risks)
    grid = [[0] * max_x for i in range(max_y)]
    for (x, y), value in risks.items():
        grid[y][x] = value
    for row in grid:
        print(''.join([str(item).ljust(5) for item in row]))


start_time = time.time()
print(part_one('day15/input'))
print(f'{time.time() - start_time:0.2f} s')