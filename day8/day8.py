from collections import Counter
from itertools import permutations

letters_to_numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


letter_count_to_decoded = {
    4: 'e',
    6: 'b',
    9: 'f'
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


def difference(str1, str2):
    as_list = list(set(str1) - set(str2))
    as_list.sort()
    return ''.join(as_list)


def decode_by_lookup(signal_pattern, decoder):
    try:
        return decoder[signal_pattern]
    except KeyError:
        return ''.join(decoder[letter] for letter in signal_pattern)


def decode_by_letter_count(signal_pattern):
    """
    From part one, some letter combinations have a unique length.
    The one with only 2 letters is 1, 3 letters is 7, 4 letters is 4,
    all 7 letters is 8."""
    letter_count = len(signal_pattern)
    if letter_count in (2, 3, 4, 7):
        return next(x for x in letters_to_numbers if len(x) == letter_count)
    raise KeyError


def decode_singles(signal_pattern):
    """
    Count up all the letters in the pattern.
    The letter that appears 9 times is f, the letter that appears 6 times is b,
    and the letter that appears 4 times is e"""
    counts = Counter(list(''.join(signal_pattern)))
    decoder = {}
    for k, v in counts.items():
        try:
            decoder[k] = letter_count_to_decoded[v]
        except KeyError:
            pass
    return decoder


def infer(decoder):
    """
    If we know 'abc' = 'def', and we know 'ab' = 'de', we know 'c' = 'f'.
    """
    for key1, key2 in permutations(decoder.keys(), 2):
        try:
            decoder[difference(key1, key2)] = difference(decoder[key1], decoder[key2])
        except KeyError:
            pass


def decode_pattern(signal_pattern, decoder):
    try:
        return decode_by_lookup(signal_pattern, decoder)
    except KeyError:
        return decode_by_letter_count(signal_pattern)


def decode_output(output, decoder):
    as_numbers = [letters_to_numbers[decoder[output_pattern]] for output_pattern in output]
    return int(''.join([str(n) for n in as_numbers]))


def is_complete(signal, decoder):
    return all(signal_pattern in decoder for signal_pattern in signal)


def part_one(filename):
    outputs = all_output(read_file(filename))
    decoded = []
    for pattern in outputs:
        try:
            decoded.append(letters_to_numbers[decode_by_letter_count(pattern)])
        except KeyError:
            pass
    return len(decoded)


def part_two(filename):
    signals_and_outputs = read_file(filename)
    total = 0
    for signal, output in signals_and_outputs:
        decoder = decode_singles(signal)
        while not is_complete(output, decoder):
            for signal_pattern in signal:
                try:
                    decoder[signal_pattern] = decode_pattern(signal_pattern, decoder)
                except KeyError:
                    pass
            infer(decoder)
        total += decode_output(output, decoder)
    return total


print(part_one('day8/input_sample'))
