def differences(filename):
    diffs = []
    current = 0
    with open(filename) as file:
        for line in file:
            prev = current
            current = int(line.strip())
            diffs.append(current - prev)
    return diffs[1:]

def count_positive(diffs):
    positive_diffs = [item for item in diffs if item > 0]
    return len(positive_diffs)

def part_one(input):
    diffs = differences(input)
    print(count_positive(diffs))


part_one('day1/input')
