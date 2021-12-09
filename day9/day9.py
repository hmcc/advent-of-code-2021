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
    adjacent = []
    for y in (row - 1, row, row + 1):
        if y < 0 or y >= len(heightmap):
            continue
        for x in (column - 1, column, column + 1):
            if x < 0 or x >= len(heightmap[0]):
                continue
            if x == column and y == row:
                continue
            adjacent.append((x, y))
    return adjacent


def low_point(coordinate, heightmap):
    base = heightmap[coordinate[1]][coordinate[0]]
    return all(heightmap[y][x] > base for x, y in adjacent(coordinate, heightmap))


def risk_level(value):
    return value + 1


def part_one(filename):
    heightmap = read_file(filename)
    return sum([
        risk_level(value)
        for y, row in enumerate(heightmap)
        for x, value in enumerate(row) 
        if low_point((x, y), heightmap)
    ])


print(part_one('day9/input'))