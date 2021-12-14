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


def insertion_indices(polymer, key):
    key1, key2 = list(key)
    return [idx + 1 for idx, (a, b) in enumerate(zip(polymer[:-1], polymer[1:])) if a == key1 and b == key2]


def all_insertions(polymer, pairs):
    insertions = {}
    for key, value in pairs.items():
        indices = insertion_indices(polymer, key)
        for idx in indices:
            insertions[idx] = value
    return insertions


def insert(polymer, insertions):
    indices = sorted(insertions)
    parts = [polymer[i:j] for i,j in zip([0] + indices, indices + [None])]
    result = ''.join((''.join((part, insertions[key])) for part, key in zip(parts, indices)))
    result += parts[-1]
    return result


def process_once(polymer, pairs):
    insertions = all_insertions(polymer, pairs)
    return insert(polymer, insertions)


def part_one(filename):
    polymer, pairs = parse_file(filename)
    for i in range(10):
        polymer = process_once(polymer, pairs)
    counted = Counter(polymer).most_common()
    return counted[0][1] - counted[-1][1]


print(part_one('day14/input'))
