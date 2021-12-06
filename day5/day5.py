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


def fill_x(coordinates):
    y = coordinates[0][1]
    x1 = coordinates[0][0]
    x2 = coordinates[1][0]
    if x2 < x1:
        x1, x2 = x2, x1
    return [(x, y) for x in range(x1, x2 + 1)]


def fill_y(coordinates):
    x = coordinates[0][0]
    y1 = coordinates[0][1]
    y2 = coordinates[1][1]
    if y2 < y1:
        y1, y2 = y2, y1
    return [(x, y) for y in range(y1, y2 + 1)]


def fill_all(coordinates):
    all_coordinates = []
    for start, end in coordinates:
        if start[0] == end[0]:
            all_coordinates.extend(fill_y((start, end)))
        elif start[1] == end[1]:
            all_coordinates.extend(fill_x((start, end)))
        else:
            pass   # skip all but horizontal or vertical lines
    return all_coordinates


def initialise_grid(coordinates):
    cols = max(coord[0] for coord in coordinates) + 1
    rows = max(coord[1] for coord in coordinates) + 1
    return [ [0]*cols for i in range(rows)]


def update_grid(grid, fills):
    for x, y in fills:
        grid[y][x] += 1
    return grid


def part_one(filename, debug=False):
    coordinates = fill_all(read_input(filename))
    grid = initialise_grid(coordinates)
    grid = update_grid(grid, coordinates)
    if debug:
        pretty_print(grid)
    just_two_and_above = [j for i in grid for j in i if j >= 2]
    return len(just_two_and_above)



def pretty_print(grid):
    for row in grid:
        print(''.join([str(item) if item > 0 else '.' for item in row]))
    print()


print(part_one('day5/input'))
