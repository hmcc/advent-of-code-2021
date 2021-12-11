class DumboOctopus:
    def __init__(self, value):
        self.value = value
        self.flashed = False

    def update(self) -> int:
        if not self.flashed:
            self.value = (self.value + 1) % 10
            self.flashed = self.value == 0
            return self.flashed
        return False


def read_input(filename):
    octos = []
    with open(filename) as file:
        for line in file:
            octos += [[DumboOctopus(int(n)) for n in line.strip()]]
    return octos


def get(x, y, octos):
    return octos[y][x]


def reset(octos):
    for row in octos:
        for octo in row:
            octo.flashed = False


def neighbours(x, y, octos):
    possible_y = tuple(y1 for y1 in (y - 1, y, y + 1) if 0 <= y1 < len(octos))
    possible_x = tuple(x1 for x1 in (x - 1, x, x + 1) if 0 <= x1 < len(octos[0]))
    found = []
    for y1 in possible_y:
        for x1 in possible_x:
            if x1 == x and y1 == y:
                continue
            found += [(x1, y1)]
    return found


def process(octos):
    flash_count = 0
    reset(octos)
    to_process = [(x, y) for y, row in enumerate(octos) for x, _ in enumerate(row)]
    while len(to_process) > 0:
        affected = []
        for coordinates in to_process:
            did_flash = get(*coordinates, octos).update()
            if did_flash:
                flash_count += 1
                affected += neighbours(*coordinates, octos)
        to_process = affected
    return flash_count


def part_one(filename, iterations):
    octos = read_input(filename)
    flash_count = 0
    for _ in range(iterations):
        flash_count += process(octos)
    return flash_count


def part_two(filename):
    octos = read_input(filename)
    target = len(octos) * len(octos[0])
    for iteration in range(999999):
        flash_count = process(octos)
        if flash_count == target:
            return iteration + 1
    return flash_count


print(part_two('day11/input'))
