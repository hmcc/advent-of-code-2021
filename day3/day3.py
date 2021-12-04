from collections import Counter

def read_input(filename):
    numbers = []
    with open(filename) as file:
        for line in file:
            numbers += [tuple(int(c) for c in line.strip())]
    return numbers


def transpose(numbers):
    return tuple(map(tuple, zip(*numbers)))



def count(number_list, idx, default):
    next_idx = idx + 1 if idx >= 0 else idx - 1
    counts = Counter(number_list).most_common()
    if len(counts) == 1:
        return counts[0][0]
    if default is not None and counts[idx][1] == counts[next_idx][1]:
        return default
    return counts[-idx][0]


def least_common(number_list, default=None):
    return count(number_list, -1, default)



def most_common(number_list, default=None):
    return count(number_list, 0, default)


def epsilon(transposed_numbers):
    counts = tuple(least_common(n) for n in transposed_numbers)
    return binary_digits_to_decimal(counts)


def gamma(transposed_numbers):
    counts = tuple(most_common(n) for n in transposed_numbers)
    return binary_digits_to_decimal(counts)


def binary_digits_to_decimal(digits):
    return int(''.join(str(d) for d in digits), 2)


def o2_generator_rating(numbers):
    for i in range(len(numbers[0])):
        most_common_in_ith_bit = most_common(transpose(numbers)[i], 1)
        numbers = [n for n in numbers if n[i] == most_common_in_ith_bit]
    return binary_digits_to_decimal(numbers[0])


def co2_scrubber_rating(numbers):
    for i in range(len(numbers[0])):
        least_common_in_ith_bit = least_common(transpose(numbers)[i], 0)
        numbers = [n for n in numbers if n[i] == least_common_in_ith_bit]
    return binary_digits_to_decimal(numbers[0])



def part_one(filename):
    numbers = read_input(filename)
    transposed = transpose(numbers)
    g = gamma(transposed)
    e = epsilon(transposed)
    return g * e


def part_two(filename):
    numbers = read_input(filename)
    o2 = o2_generator_rating(numbers)
    co2 = co2_scrubber_rating(numbers)
    return o2 * co2



print(part_two('day3/input'))
