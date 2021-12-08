letters_to_numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdfeg': 8,
    'abcdfg': 9
}


def read_file(filename):
    content = []
    with open(filename) as file:
        for line in file:
            content.append(parse_line(line))
    return content


def all_output(content):
    return [item for sublist in content for item in sublist[1]]


def parse_line(line):
    split_line = line.strip().split(' | ')
    signal = [''.join(sorted(s)) for s in split_line[0].split()]
    output = [''.join(sorted(o)) for o in split_line[1].split()]
    return signal, output


def decode(letters):
    letter_count = len(letters)
    if letter_count in (2, 3, 4, 7):
        key = next(x for x in letters_to_numbers if len(x) == letter_count)
        return letters_to_numbers[key]
    return None


def day_one(filename):
    outputs = all_output(read_file(filename))
    decoded_to_number = [decode(letters) for letters in outputs]
    return len([n for n in decoded_to_number if n])


print(day_one('day8/input'))