import re

p = re.compile(r'(\d+,\d+) -> (\d+,\d+)')


def read_input(filename):
    coordinates = []
    with open(filename) as file:
        for line in file:
            matcher = p.match(line.strip())
            if matcher:
                coordinates.append((
                    tuple(int(n) for n in matcher.group(1).split(',')),
                    tuple(int(n) for n in matcher.group(2).split(','))
                ))
    return coordinates


def fill_x(start, end):
    if not start[1] == end[1]:
        return []
    y = start[1]
    x1 = start[0]
    x2 = end[0]
    step = 1 if x2 > x1 else -1
    return [(x, y) for x in range(x1, x2 + step, step)]


def fill_y(start, end):
    if not start[0] == end[0]:
        return []
    x = start[0]
    y1 = start[1]
    y2 = end[1]
    step = 1 if y2 > y1 else -1
    return [(x, y) for y in range(y1, y2 + step, step)]


def fill_diagonal(start, end):
    if not abs(start[0] - end[0]) == abs(start[1] - end[1]):
        return []
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    return list(zip(range(x1, x2 + xstep, xstep), range(y1, y2 + ystep, ystep)))


def fill_all(coordinates, *fill_fns):
    all_coordinates = []
    for start, end in coordinates:
        for fill_fn in fill_fns:
            all_coordinates.extend(fill_fn(start, end))
    return all_coordinates


def initialise_grid(coordinates):
    cols = max(coord[0] for coord in coordinates) + 1
    rows = max(coord[1] for coord in coordinates) + 1
    return [[0]*cols for i in range(rows)]


def update_grid(grid, fills):
    for x, y in fills:
        grid[y][x] += 1
    return grid


def count_two_or_more_occurrences(coordinates, debug=False):
    grid = initialise_grid(coordinates)
    grid = update_grid(grid, coordinates)
    if debug:
        pretty_print(grid)
    just_two_and_above = [j for i in grid for j in i if j >= 2]
    return len(just_two_and_above)


def part_one_coordinates(filename, debug=False):
    coordinates = fill_all(read_input(filename), fill_x, fill_y)
    return count_two_or_more_occurrences(coordinates, debug)


def part_two(filename, debug=False):
    coordinates = fill_all(read_input(filename), fill_x, fill_y, fill_diagonal)
    return count_two_or_more_occurrences(coordinates, debug)


def pretty_print(grid):
    for row in grid:
        print(''.join([str(item) if item > 0 else '.' for item in row]))
    print()


print(part_two('day5/input'))
