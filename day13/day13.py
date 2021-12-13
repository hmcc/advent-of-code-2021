import re
from operator import itemgetter

p = re.compile('fold along ([xy])=([0-9]+)')


def parse_file(filename):
    plots = []
    folds = []
    with open(filename) as file:
        for line in file:
            try:
                plots.append(parse_plot(line))
            except ValueError:
                try:
                    folds.append(parse_fold(line))
                except ValueError:
                    pass

    return to_grid(plots), folds


def parse_plot(line):
    x, y = line.strip().split(',')
    return (int(x), int(y))


def parse_fold(line):
    matcher = p.match(line)
    if matcher:
        return matcher.group(1), int(matcher.group(2))
    raise ValueError


def to_grid(plots):
    width = max(plots)[0] + 1
    height = max(plots, key=itemgetter(1))[1] + 1
    grid = [[0 for x in range(width)] for y in range(height)]
    for x, y in plots:
        grid[y][x] = 1
    return grid


def combine(l1, l2):
    return [e1 or e2 for e1, e2 in zip(l1, l2)]


def fold_y(grid, location):
    bottom = grid[:location]
    top = grid[location+1:]
    top.reverse()
    return list(map(combine, top, bottom))


def fold_row(row, location):
    left = row[:location]
    right = row[location+1:]
    right.reverse()
    return combine(left, right)


def fold_x(grid, location):
    return [fold_row(row, location) for row in grid]


def fold(grid, direction, location):
    if direction == 'x':
        return fold_x(grid, location)
    if direction == 'y':
        return fold_y(grid, location)
    raise ValueError


def count(grid):
    return sum([sum(x) for x in grid])


def part_one(filename):
    grid, folds = parse_file(filename)
    direction, location = folds[0]
    grid = fold(grid, direction, location)
    return count(grid)


def part_two(filename):
    grid, folds = parse_file(filename)
    for direction, location in folds:
        grid = fold(grid, direction, location)
    return grid


def pretty_print(grid):
    for row in grid:
        print(''.join(['#' if item > 0 else '.' for item in row]))
    print()


pretty_print(part_two('day13/input'))
