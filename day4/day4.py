MARKER = '*'


def read_input(filename):
    with open(filename) as file:
        draw = [int(n) for n in file.readline().strip().split(',')]
        grids = read_grids(file)
    return draw, grids


def read_grids(file):
    grids = [[]]
    for line in file:
        if line.strip():
            grids[-1].append([int(n) for n in line.strip().split()])
        elif len(grids[-1]) > 0:
            grids.append([])
    return grids


def mark_grid(grid, number):
    return [[n if n != number else MARKER for n in row] for row in grid]


def transpose(grid):
    return tuple(map(tuple, zip(*grid)))


def grid_wins(grid):
    return any([all(item == MARKER for item in row) for row in grid]) or \
        any([all(item == MARKER for item in row) for row in transpose(grid)])


def score(grid, number):
    grid = [[n for n in row if n != '*'] for row in grid]
    return sum(map(sum, grid)) * number


def play(filename, let_squid_win=False):
    drawn, grids = read_input(filename)
    for number in drawn:
        winning_grids = []
        for idx, grid in enumerate(grids):
            grids[idx] = mark_grid(grid, number)
            if grid_wins(grids[idx]):
                if not let_squid_win or len(grids) <= 1:
                    return score(grids[idx], number)
                winning_grids.append(idx)
        grids = [grid for idx, grid in enumerate(grids) if idx not in winning_grids]
    return 0


def part_one(filename):
    return play(filename)


def part_two(filename):
    return play(filename, True)


print(part_two('day4/input'))
