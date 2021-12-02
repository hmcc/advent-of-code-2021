def process(filename, move_fn):
    location = {
        'position': 0,
        'depth': 0,
        'aim': 0
    }

    with open(filename) as file:
        for line in file:
            location = move_fn(*parse(line), location)
    return location['position'] * location['depth']


def parse(command):
    return command.strip().split()[0], int(command.split()[1])


def move_one(direction, amount, location):
    if direction == 'forward':
        location['position'] += amount
    elif direction == 'down':
        location['depth'] += amount
    elif direction == 'up':
        location['depth'] -= amount
    else:
        print(f'invalid instruction: {direction}: {amount}')
    return location


def move_two(direction, amount, location):
    if direction == 'forward':
        location['position'] += amount
        location['depth'] += location['aim'] * amount
    elif direction == 'down':
        location['aim'] += amount
    elif direction == 'up':
        location['aim'] -= amount
    else:
        print(f'invalid instruction: {direction}: {amount}')
    return location


#print(process('day2/input', move_one))
print(process('day2/input', move_two))
