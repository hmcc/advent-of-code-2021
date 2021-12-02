def process(filename):
    position = 0
    depth = 0
    with open(filename) as file:
        for line in file:
            position, depth = move(*parse(line), position, depth)
    return (position, depth)


def parse(command):
    return command.strip().split()[0], int(command.split()[1])


def move(direction, amount, position=0, depth=0):
    if direction == 'forward':
        position += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount
    else:
        print(f'invalid instruction at {direction}: {amount}')
    return (position, depth)


def part_one(filename):
    position, depth = process(filename)
    return position * depth


print(part_one('day2/input'))

