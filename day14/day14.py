from collections import Counter


def parse_file(filename):
    polymer = []
    pairs = {}
    folds = []
    with open(filename) as file:
        polymer = parse_polymer(file.readline())
        for line in file:
            try:
                key, value = parse_pair(line)
                pairs[key] = value
            except ValueError:
                pass
            
    return polymer, pairs


def parse_polymer(line):
    return line.strip()


def parse_pair(line):
    return line.strip().split(' -> ')


def process_once(polymer, pairs):
    new_polymer = ''
    for ch1, ch2 in zip(polymer[:-1], polymer[1:]):
        new_polymer += ch1
        try:
            new_polymer += pairs[''.join((ch1, ch2))]
        except KeyError:
            pass
    new_polymer += polymer[-1]
    return new_polymer


def process_n(polymer, pairs, n):
    for i in range(n):
        polymer = process_once(polymer, pairs)
    counted = Counter(polymer).most_common()
    return counted[0][1] - counted[-1][1]


def part_one(filename):
    polymer, pairs = parse_file(filename)
    return process_n(polymer, pairs, 10)


def part_two(filename):
    polymer, pairs = parse_file(filename)
    return process_n(polymer, pairs, 40)


print(part_one('day14/input'))
