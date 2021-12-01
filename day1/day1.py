def differences(filename, window_size):
    diffs = []
    window = [0] * window_size
    with open(filename) as file:
        for line in file:
            window.append(int(line.strip()))
            diffs.append(window[-1] - window[0])
            window.pop(0)
    return diffs[window_size:]


def count_positive(items):
    positive = [item for item in items if item > 0]
    return len(positive)


def count_positive_differences(filename, window_size):
    diffs = differences(filename, window_size)
    return count_positive(diffs)


def part_one(input):
    print(count_positive_differences(input, 1))


def part_two(input):
    print(count_positive_differences(input, 3))


part_two('day1/input')
