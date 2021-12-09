from functools import reduce
from operator import mul


def read_file(filename):
    rows = []
    with open(filename) as file:
        for line in file:
            row = line.rstrip()
            if row:
                rows.append([int(c) for c in row])
    return rows


def adjacent(coordinate, heightmap):
    column, row = coordinate
    possible_y = tuple(y for y in (row - 1, row, row + 1) if 0 <= y < len(heightmap))
    possible_x = tuple(x for x in (column - 1, column, column + 1) if 0 <= x < len(heightmap[0]))
    for y in possible_y:
        for x in possible_x:
            if x == column and y == row:
                continue
            yield (x, y)


def flow(coordinate, heightmap, visited):
    column, row = coordinate
    possible_y = tuple(y for y in (row - 1, row, row + 1) if 0 <= y < len(heightmap))
    possible_x = tuple(x for x in (column - 1, column, column + 1) if 0 <= x < len(heightmap[0]))
    for y in possible_y:
        for x in possible_x:
            if (x, y) in visited:
                continue
            if heightmap[y][x] == 9:
                continue
            # can't flow diagonally if the adjacent values are 9, e.g.
            # 8 9
            # 9 6
            # the 6 won't flow to the 8 or vice versa
            if x != column and y != row and heightmap[y][column] == 9 and heightmap[row][x] == 9:
                continue
            visited.add((x, y))
            yield (x, y)
            for new_coordinate in flow((x, y), heightmap, visited):
                yield new_coordinate


def low_point(coordinate, heightmap):
    base = heightmap[coordinate[1]][coordinate[0]]
    return all(heightmap[y][x] > base for x, y in adjacent(coordinate, heightmap))


def risk_level(value):
    return value + 1


def basin_size(coordinates, heightmap):
    return sum(1 for _ in flow(coordinates, heightmap, set()))


def part_one(filename):
    heightmap = read_file(filename)
    return sum([
        risk_level(value)
        for y, row in enumerate(heightmap)
        for x, value in enumerate(row)
        if low_point((x, y), heightmap)
    ])


def part_two(filename):
    heightmap = read_file(filename)
    basin_sizes = [
        basin_size((x, y), heightmap)
        for y, row in enumerate(heightmap)
        for x, _ in enumerate(row)
        if low_point((x, y), heightmap)
    ]
    basin_sizes.sort()
    return reduce(mul, basin_sizes[-3:])


print(part_two('day9/input'))
