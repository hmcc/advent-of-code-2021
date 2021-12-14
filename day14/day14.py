from collections import Counter, defaultdict


def parse_file(filename):
    polymer = {}
    pairs = {}
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


def to_pairs(polymer):
    polymer_pairs = defaultdict(int, {})
    for ch1, ch2 in zip(polymer[:-1], polymer[1:]):
        polymer_pairs[ch1 + ch2] += 1
    return polymer_pairs


def parse_pair(line):
    return line.strip().split(' -> ')


def process_once(polymer, pairs):
    new_polymer = defaultdict(int)
    for pair, count in polymer.items():
        try:
            new_letter = pairs[pair]
            new_polymer[pair[0] + new_letter] += count
            new_polymer[new_letter + pair[1]] += count
        except ValueError:
            new_polymer[pair] = count
    return new_polymer


def process_n(polymer, pairs, n):
    for _ in range(n):
        polymer = process_once(polymer, pairs)
    return polymer


def letter_counts(polymer, last_letter):
    counts = defaultdict(int)
    for pair, count in polymer.items():
        counts[pair[0]] += count
    counts[last_letter] += 1
    return Counter(counts).most_common()


def process_file(filename, n):
    polymer, pairs = parse_file(filename)
    result = process_n(to_pairs(polymer), pairs, n)
    counted = letter_counts(result, polymer[-1])
    return counted[0][1] - counted[-1][1]


def part_one(filename):
    return process_file(filename, 10)


def part_two(filename):
    return process_file(filename, 40)


print(part_two('day14/input'))
